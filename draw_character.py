"""
Draws my character sheets for Pixel Agent Desk.

The app wants one 384x576 image per character: a grid of 48x64 frames,
8 across and 9 down. I draw everything on a tiny 24x32 grid and double it,
because the app's own characters use 2x2 "chunky" pixels and I want mine to
sit at the same size next to the office furniture.

The pixel art itself lives in parts.py. This file stacks those pieces into
frames, turns the frames into the 18 animations, and saves one sheet for
every entry in parts.SHEETS, plus the two preview pictures for the README.

Run it with:  python3 draw_character.py   (needs Pillow: pip install pillow)
"""

from pathlib import Path

from PIL import Image

from parts import (
    BANG, BOTTOMS, DEFAULT_EYES, EARRINGS, EYES, FRONT_ARMS, GLASSES, HEADS, OUTFIT_DEFAULTS,
    OUTFITS, PALETTE, SHEETS, SIDE_ARMS, SKIN, SPARKLE_BIG, SPARKLE_SMALL, TAILS,
    TOPPERS, TOPS,
)

HERE = Path(__file__).parent

SCALE = 2
GRID_W, GRID_H = 24, 32   # one frame, before doubling
LEFT = 4                  # the 16-wide body drawings start 4 columns in, so they're centered
HAIR_LEFT = LEFT - 2      # the head drawings are 20 wide, so the hair sticks out past the body
FLOOR = 30                # row the shoes stand on (matches where the app's own characters stand)

# Where each animation sits on the sheet. Pixel Agent Desk reads the sheet
# left to right, top to bottom, four frames per animation, in this order.
# (It's the same order as the app's public/shared/sprite-frames.json. If the
# app ever changes that file, this list has to change with it.)
SHEET_COLS = 8
SHEET_ORDER = [
    "front_idle", "front_walk", "front_sit_idle", "front_sit_work",
    "left_idle", "left_walk", "left_sit_idle", "left_sit_work",
    "right_idle", "right_walk", "right_sit_idle", "right_sit_work",
    "back_idle", "back_walk", "back_sit_idle", "back_sit_work",
    "front_done_dance", "front_alert_jump",
]


def check_art():
    """
    Make sure every drawing is the width it's supposed to be. A row that's
    one letter short doesn't crash anything, it just quietly shifts half a
    face sideways, so it's worth catching before saving.
    """
    problems = []

    def rows_are(what, rows, width):
        if any(len(row) != width for row in rows):
            problems.append(f"{what}: rows should be {width} wide, got {[len(r) for r in rows]}")

    for hair, views in HEADS.items():
        for view, rows in views.items():
            rows_are(f"head {hair}/{view}", rows, 20)
            if len(rows) != 13:
                problems.append(f"head {hair}/{view}: should be 13 rows, got {len(rows)}")
    for top, views in TOPS.items():
        for view, rows in views.items():
            rows_are(f"top {top}/{view}", rows, 16)
    for name, bottoms in BOTTOMS.items():
        for view, rows in bottoms["hips"].items():
            rows_are(f"hips {name}/{view}", rows, 16)
        for view, poses in bottoms["legs"].items():
            for pose, rows in poses.items():
                rows_are(f"legs {name}/{view}/{pose}", rows, 16)
    for name, views in EARRINGS.items():
        for view, hoops in views.items():
            for col, row, rows in hoops:
                rows_are(f"earrings {name}/{view}", rows, len(rows[0]))
    for group_name, group in (("topper", TOPPERS), ("tail", TAILS), ("glasses", GLASSES)):
        for name, views in group.items():
            for view in ("front", "left", "back"):
                if view in views:
                    rows_are(f"{group_name} {name}/{view}", views[view][2], len(views[view][2][0]))

    if problems:
        raise SystemExit("Some drawings in parts.py are the wrong size:\n  " + "\n  ".join(problems))


def stamp(grid, rows, col, row):
    """Paint a small drawing onto the frame, skipping the see-through dots."""
    for dy, line in enumerate(rows):
        for dx, letter in enumerate(line):
            x, y = col + dx, row + dy
            if letter != "." and 0 <= x < GRID_W and 0 <= y < GRID_H:
                grid[y][x] = letter


def mirrored(pieces):
    """Flip left-arm pieces over to the right side of the 16-wide drawing."""
    return [(16 - col - len(rows[0]), row, [line[::-1] for line in rows])
            for col, row, rows in pieces]


def for_view(drawings, view):
    """Pick the drawing for a view. Anything without its own back uses the front."""
    return drawings.get(view, drawings["front"])


def head_for(look, view, face):
    """The head drawing for one frame, with the expression and lenses put in."""
    head = [list(line) for line in HEADS[look["hair"]][view]]
    style = GLASSES.get(look.get("glasses"), {})

    if view == "front":
        if face == "happy":
            for eye in EYES.get(look["hair"], DEFAULT_EYES):
                if style.get("happy") == "dash":
                    # Closed, smiling eyes: a little dash across the lens.
                    head[8][eye - 1] = head[8][eye + 1] = "e"
                else:
                    # Eyes become little ^ ^ shapes.
                    head[9][eye] = "s"
                    head[9][eye - 1] = head[9][eye + 1] = "e"
        elif face == "surprised":
            # Mouth drops open. Just one dark row: two rows read as a beard.
            head[10][9] = head[10][10] = "o"

    # Color in the lenses last, and only where there's skin, so whatever
    # shape her eyes are in stays dark on top.
    for col, row, width, height in style.get("lenses", {}).get(view, []):
        for r in range(row, row + height):
            for c in range(col, col + width):
                if head[r][c] in "sSc":
                    head[r][c] = style["fill"]
    return ["".join(line) for line in head]


def draw(direction, look, x=0, y=0, head_y=0, legs="stand", arms=("down", "down"),
         arm_y=(0, 0), swing=0, face="normal", extras=()):
    """
    Build one 24x32 frame by stacking legs, hips, top and head upward from
    the floor. Everything else in this file is just calling this with small
    nudges:

      look      who to draw: one of the entries in parts.SHEETS
      x, y      slide the whole character (y=-3 is a jump, 3 rows up)
      head_y    nudge only the head, which is the idle "breathing" bob
      legs      which leg pose to use
      arms      (left, right) arm poses; the side view only uses the first
      arm_y     nudge each arm up or down a row
      swing     nudge hanging earrings sideways
      face      "normal", "happy" or "surprised" (front view only)
      extras    floating bits like sparkles, as (col, row, pixels)
    """
    view = "left" if direction == "right" else direction
    grid = [["."] * GRID_W for _ in range(GRID_H)]
    outfit = OUTFITS[look["outfit"]]
    bottoms = BOTTOMS[outfit["bottoms"]]
    hair = look["hair"]

    leg_rows = for_view(bottoms["legs"], view)[legs]
    hip_rows = for_view(bottoms["hips"], view)
    top_rows = for_view(TOPS[outfit["top"]], view)
    head = head_for(look, view, face)

    legs_top = FLOOR + y - len(leg_rows) + 1
    hips_top = legs_top - len(hip_rows)
    body_top = hips_top - len(top_rows)
    head_top = body_top - len(head) + head_y

    stamp(grid, leg_rows, LEFT + x, legs_top)
    stamp(grid, hip_rows, LEFT + x, hips_top)
    stamp(grid, top_rows, LEFT + x, body_top)
    stamp(grid, head, HAIR_LEFT + x, head_top)

    on_head = []
    if hair in TOPPERS:
        on_head.append(for_view(TOPPERS[hair], view))
    if look.get("glasses") and view != "back":   # you can't see glasses from behind
        on_head.append(GLASSES[look["glasses"]][view])
    for col, row, rows in on_head:
        stamp(grid, rows, HAIR_LEFT + x + col, head_top + row)

    # Arms go on after the head so a raised hand shows in front of the hair.
    if view == "left":
        for col, row, rows in SIDE_ARMS[arms[0]]:
            stamp(grid, rows, LEFT + x + col, body_top + row + arm_y[0])
    else:
        for col, row, rows in FRONT_ARMS[arms[0]]:
            stamp(grid, rows, LEFT + x + col, body_top + row + arm_y[0])
        for col, row, rows in mirrored(FRONT_ARMS[arms[1]]):
            stamp(grid, rows, LEFT + x + col, body_top + row + arm_y[1])

    # Hanging earrings go over the edge of the face and the top of the arm,
    # so the whole ring shows.
    if hair in EARRINGS:
        for col, row, rows in for_view(EARRINGS[hair], view):
            stamp(grid, rows, HAIR_LEFT + x + col + swing, head_top + row)

    # Long hair goes on very last, so braids and locs fall over the
    # shoulders instead of hiding behind the arms.
    if hair in TAILS:
        col, row, rows = for_view(TAILS[hair], view)
        stamp(grid, rows, HAIR_LEFT + x + col, head_top + row)

    if direction == "right":
        grid = [line[::-1] for line in grid]

    for col, row, rows in extras:
        stamp(grid, rows, col, row)
    return grid


# ---------------------------------------------------------------------------
# The animations. Each one is 4 frames, and the names match the app's
# sprite-frames.json so the frames land in the right squares.
# ---------------------------------------------------------------------------

def animations(look):
    def frame(direction, **nudges):
        return draw(direction, look, **nudges)

    anims = {}

    for d in ("front", "left", "right", "back"):
        side = d in ("left", "right")

        # Idle: the head dips one row and comes back, like breathing.
        anims[f"{d}_idle"] = [frame(d, head_y=bob) for bob in (0, 0, 1, 1)]
        anims[f"{d}_sit_idle"] = [frame(d, legs="short", head_y=bob) for bob in (0, 0, 1, 1)]

        if side:
            # Walk: legs open into a stride, close again, and the arm swings.
            anims[f"{d}_walk"] = [
                frame(d, legs="stride", arms=("forward", "")),
                frame(d, y=-1),
                frame(d, legs="stride", arms=("back", "")),
                frame(d, y=-1),
            ]
            # Typing: one hand reaching forward, tapping up and down.
            anims[f"{d}_sit_work"] = [
                frame(d, legs="short", arms=(pose, ""))
                for pose in ("type_hi", "type_lo", "type_hi", "type_lo")
            ]
        else:
            # Walk: lift one foot, then the other, with a tiny hop between.
            anims[f"{d}_walk"] = [
                frame(d),
                frame(d, y=-1, legs="left_up"),
                frame(d),
                frame(d, y=-1, legs="right_up"),
            ]

    # Typing from the front: the two hands take turns tapping.
    taps = [("type_hi", "type_lo"), ("type_lo", "type_hi")] * 2
    anims["front_sit_work"] = [
        frame("front", legs="short", arms=pair, head_y=nod)
        for pair, nod in zip(taps, (0, 0, 0, 1))
    ]
    # Typing from behind: you can't see the hands, so the elbows take turns
    # lifting instead.
    anims["back_sit_work"] = [
        frame("back", legs="short", arm_y=lift)
        for lift in ((-1, 0), (0, -1), (-1, 0), (0, -1))
    ]

    # Happy dance: sway left, hands up, sway right, arms wide, with sparkles.
    # Hanging earrings swing the opposite way to the sway, like they're
    # trailing a beat behind.
    anims["front_done_dance"] = [
        frame("front", x=-1, swing=1, legs="left_up", arms=("up", "out"), face="happy",
              extras=[(22, 3, SPARKLE_SMALL)]),
        frame("front", y=-1, arms=("up", "up"), face="happy",
              extras=[(0, 1, SPARKLE_BIG), (21, 0, SPARKLE_BIG)]),
        frame("front", x=1, swing=-1, legs="right_up", arms=("out", "up"), face="happy",
              extras=[(1, 3, SPARKLE_SMALL)]),
        frame("front", arms=("out", "out"), face="happy",
              extras=[(0, 2, SPARKLE_BIG), (21, 1, SPARKLE_BIG)]),
    ]

    # Alert jump: notice something (!), crouch, spring up, tuck at the top.
    anims["front_alert_jump"] = [
        frame("front", legs="short", face="surprised", extras=[(11, 0, BANG)]),
        frame("front", legs="short", head_y=1, arms=("out", "out"), face="surprised",
              extras=[(11, 0, BANG)]),
        frame("front", y=-3, arms=("up", "up"), face="surprised"),
        frame("front", y=-4, legs="short", arms=("up", "up"), face="surprised"),
    ]
    return anims


def colors_for(look):
    """One letter -> hex table for a character: shared colors, her skin, her outfit."""
    colors = PALETTE | SKIN[look["skin"]] | OUTFIT_DEFAULTS | OUTFITS[look["outfit"]]["colors"]
    # A one-letter value points at another letter ("a": "s" means sleeves are
    # skin). Keep following until we land on a real color.
    for letter in colors:
        while len(colors[letter]) == 1:
            colors[letter] = colors[colors[letter]]
    return colors


def to_image(grid, colors):
    """Turn one grid of letters into a real 48x64 picture."""
    small = Image.new("RGBA", (GRID_W, GRID_H), (0, 0, 0, 0))
    for y, line in enumerate(grid):
        for x, letter in enumerate(line):
            if letter != ".":
                small.putpixel((x, y), tuple(bytes.fromhex(colors[letter][1:])) + (255,))
    # NEAREST keeps the pixels as hard squares. Any other setting blurs them.
    return small.resize((GRID_W * SCALE, GRID_H * SCALE), Image.NEAREST)


def lineup(frames, zoom=3, per_row=5, gap=8, background="#f4efe8"):
    """
    Lay character frames out in rows on a plain background, for the README.
    zoom stays a whole number so the pixels stay square, and five per row at
    3x fits GitHub's page width without it shrinking (and blurring) the image.
    """
    w, h = GRID_W * SCALE * zoom, GRID_H * SCALE * zoom
    rows = -(-len(frames) // per_row)   # divide, rounding up
    picture = Image.new("RGBA", (gap + per_row * (w + gap), gap + rows * (h + gap)), background)
    for i, frame in enumerate(frames):
        big = frame.resize((w, h), Image.NEAREST)
        picture.alpha_composite(big, (gap + (i % per_row) * (w + gap), gap + (i // per_row) * (h + gap)))
    return picture


def main():
    check_art()
    (HERE / "sprites").mkdir(exist_ok=True)
    frame_w, frame_h = GRID_W * SCALE, GRID_H * SCALE
    sheet_rows = -(-len(SHEET_ORDER) * 4 // SHEET_COLS)

    standing, dancing = [], [[], [], [], []]
    for name, look in SHEETS.items():
        anims = animations(look)
        missing = set(SHEET_ORDER) - set(anims)
        if missing:
            raise SystemExit(f"These animations are in SHEET_ORDER but not drawn: {sorted(missing)}")

        colors = colors_for(look)
        sheet = Image.new("RGBA", (SHEET_COLS * frame_w, sheet_rows * frame_h), (0, 0, 0, 0))
        for slot, anim in enumerate(SHEET_ORDER):
            for step, grid in enumerate(anims[anim]):
                square = slot * 4 + step
                sheet.paste(to_image(grid, colors),
                            ((square % SHEET_COLS) * frame_w, (square // SHEET_COLS) * frame_h))

        # Lossless, otherwise WebP smudges the flat colors and the edges go fuzzy.
        sheet.save(HERE / "sprites" / f"{name}.webp", "WEBP", lossless=True)
        print(f"Saved sprites/{name}.webp")

        standing.append(to_image(anims["front_idle"][0], colors))
        for step in range(4):
            dancing[step].append(to_image(anims["front_done_dance"][step], colors))

    # The two pictures the README shows: everyone standing, and everyone dancing.
    lineup(standing).convert("RGB").save(HERE / "preview.png")
    dance = [lineup(frames).convert("RGB") for frames in dancing]
    dance[0].save(HERE / "dance.gif", save_all=True, append_images=dance[1:], duration=125, loop=0)
    print("Saved preview.png and dance.gif")


if __name__ == "__main__":
    main()
