"""
All the pixel art for my Pixel Agent Desk characters: heads, outfits, legs,
arms, glasses and colors. draw_character.py does the assembling.

Everything is drawn as rows of letters, one letter per pixel, "." for
see-through. Heads are 20 wide and 13 tall. Body pieces are 16 wide.
Only front, left and back are drawn; facing right is the left drawing flipped.

Letters that mean the same thing for everyone:
  o outline   e eyes   h hair   H lighter hair pixels (curls, braids, locs)
  s skin      S skin in shadow  c blush   m lips   L lip gloss
  g gold      y sparkle         x the "!" in the alert jump

Letters each outfit fills in with its own colors:
  p P  main top color and its shadow     t  second top color
  u U  color-block color and shadow      n  small accent (buttons, trim, choker)
  j J  bottoms and their shadow          f  shoes      q  sock
  a r  upper sleeve and forearm          A R  the same two, seen from the side
  d D  whatever is on her head (bow, hair ties, bandana, hat)
"""

PALETTE = {
    "e": "#1a1113",
    "h": "#30272c",
    "H": "#62525b",
    "M": "#4b3d44",  # a quieter hair highlight, for finger waves and the fade
    "g": "#e8b84a",
    "y": "#ffd97a",
    "x": "#f2857d",
    "G": "#5a372a",  # brown glasses frames. Not black, so her eyes stay the darkest thing on her face
    "T": "#7fa3d9",  # the blue tint in the 90s shades
}

# Everything that touches skin changes with the skin tone. Blush is terracotta
# rather than pink (pink goes chalky on brown skin) and gets deeper and redder
# as the skin does. The outline is a warm near-black that gets darker on the
# deeper tones, so there's always a clear edge around the face. The two
# deepest tones also get blacker eyes, because the usual ones got lost.
SKIN = {
    "#5C3A21": {"s": "#5C3A21", "S": "#4a2d18", "c": "#8a3f33", "m": "#3a1a1c", "L": "#a3564f", "o": "#1f1518", "e": "#0b0607"},
    "#6F4527": {"s": "#6F4527", "S": "#5a361d", "c": "#9a4638", "m": "#47211f", "L": "#b0605a", "o": "#21161a", "e": "#0b0607"},
    "#8D5A3B": {"s": "#8D5A3B", "S": "#74472D", "c": "#A94A3F", "m": "#602a28", "L": "#c9756c", "o": "#261a1e"},
    "#A0673F": {"s": "#A0673F", "S": "#875332", "c": "#BD5646", "m": "#7a3530", "L": "#d98a80", "o": "#2a1d21"},
    "#B97A4F": {"s": "#B97A4F", "S": "#A06640", "c": "#CF6654", "m": "#8a3d38", "L": "#d98a80", "o": "#33242a"},
    "#C68A5E": {"s": "#C68A5E", "S": "#ad7449", "c": "#d9705f", "m": "#96453f", "L": "#e39a90", "o": "#35262b"},
}

# ---------------------------------------------------------------------------
# Heads. The edge of curly hair steps in and out on purpose: that bumpy
# silhouette is what makes it read as curls at this size.
# ---------------------------------------------------------------------------

HEADS = {
    # One big round cloud of curls.
    "bow": {
        "front": [
            "......ooo..ooo......",
            "...ooohhhoohhhooo...",
            "..ohhhhhhhhHhhhhho..",
            ".ohhhhHhhhhhhhhhhho.",
            "ohhhhhhhhhhhhHhhhhho",
            "ohhHhhhhhhhhhhhhHhho",
            ".ohhhhhhSSSShhhhhho.",
            ".ohhhSssssssssShhho.",
            "ohhhhssessssesshhhho",
            "ohhhhssessssesshhhho",
            ".ohhgcsssmLssscghho.",
            "..ohgossssssssogho..",
            "...oo.oooooooo.oo...",
        ],
        "left": [
            "......ooo..ooo......",
            "...ooohhhoohhhooo...",
            "..ohhhhhhhhhhhhhho..",
            ".ohhhhHhhhhhhhhhhho.",
            "ohhhhhhhhhhhhHhhhhho",
            "ohhHhhhhhhhhhhhhhhho",
            "..ohSSSSShhhhhhhhho.",
            "..osssssshhhhhhhHho.",
            "..osesssshhhhhhhhhho",
            "..osesssshhhhhhhhhho",
            "..omscssshghhhhhhho.",
            "...osssssoghhhhhho..",
            "....ooooo.oooooooo..",
        ],
        "back": [
            "......ooo..ooo......",
            "...ooohhhoohhhooo...",
            "..ohhhhhhhhhhhhhho..",
            ".ohhhhHhhhhhhhhhhho.",
            "ohhhhhhhhhhhhHhhhhho",
            "ohhHhhhhhhhhhhhhhhho",
            ".ohhhhhhhhhhhhhhhho.",
            ".ohhhhhhHhhhhhhhhho.",
            "ohhhhhhhhhhhhhhhhhho",
            "ohhhHhhhhhhhhhhhhhho",
            ".ohhhhhhhhhhhhHhhho.",
            "..ohhhhhhhhhhhhhho..",
            "...ooo.oooooo.ooo...",
        ],
    },
    # Two round puffs. Their tops poke above the drawing, so they're in TOPPERS.
    "puffs": {
        "front": [
            "ohhHhhho....ohhhHhho",
            "ohhhhhhoooooohhhhhho",
            "ohhhhhdhhhhhhdhhhhho",
            ".ohhhdhhhhhhhhdhhho.",
            "..ooohhhhhhhhhhooo..",
            "...ohhhhhhhhhhhho...",
            "...ohhhSSSSSShhho...",
            "...ohSssssssssSho...",
            "...ohsessssssesho...",
            "...ohsessssssesho...",
            "...ogcsssmLssscgo...",
            "....gossssssssog....",
            "......oooooooo......",
        ],
        "left": [
            "....ohhHhhhhho......",
            "....ohhhhhhhho......",
            "....ohhhhhhHho......",
            "...oohhhddhhhooo....",
            "..ohhhhhhhhhhhhho...",
            "..ohhhhhhhhhhhhho...",
            "..ohSSSSShhhhhhho...",
            "..osssssshhhhhhho...",
            "..osesssshhhhhhho...",
            "..osesssshhhhhhho...",
            "..omscssshghhhhho...",
            "...osssssoghhhho....",
            "....ooooo.ooooo.....",
        ],
        "back": [
            "ohhHhhho....ohhhHhho",
            "ohhhhhhoooooohhhhhho",
            "ohhhhhdhhhhhhdhhhhho",
            ".ohhhdhhhhhhhhdhhho.",
            "..ooohhhhhhhhhhooo..",
            "...ohhhhhhhhhhhho...",
            "...ohhhhHhhhhhhho...",
            "...ohhhhhhhhhhhho...",
            "...ohhhhhhhhhhhho...",
            "...ohhhhhhhhhHhho...",
            "...ohhhhhhhhhhhho...",
            "....oohhhhhhhhoo....",
            "......oooooooo......",
        ],
    },
    # Long box braids with a bandana tied across the forehead. The braids
    # carry on below the head in TAILS. The lighter pixels are the gaps
    # between braids.
    "braids": {
        "front": [
            "......oooooooo......",
            "....oohhhhhhhhoo....",
            "...ohhHhhhhhhHhho...",
            "...ohhhhhhhhhhhho...",
            "...oddddddddddddo...",
            "...odDddddddddDdo...",
            "...ohhSSSSSSSShho...",
            "...ohSssssssssSho...",
            "...ohssessssessho...",
            "...ohssessssessho...",
            "...ohcsssmLssscho...",
            "...ohossssssssoho...",
            "...oho.oooooo.oho...",
        ],
        "left": [
            "......oooooooo......",
            "....oohhhhhhhhoo....",
            "...ohhHhhhhhhHhho...",
            "...ohhhhhhhhhhhho...",
            "..odddddddddddddo...",
            "..odddDdddddddDdo...",
            "..ohSSSSShhHhhHho...",
            "..osssssshhHhhHho...",
            "..osesssshhHhhHho...",
            "..osesssshhHhhHho...",
            "..omscssshhHhhHho...",
            "...osssssohHhhHho...",
            "....ooooo.oHhhHho...",
        ],
        "back": [
            "......oooooooo......",
            "....oohhhhhhhhoo....",
            "...ohhHhhhhhhHhho...",
            "...ohhhhhhhhhhhho...",
            "...oddddddDDddddo...",
            "...odDdddDddDdDdo...",
            "...ohHhhHhhHhhHho...",
            "...ohHhhHhhHhhHho...",
            "...ohHhhHhhHhhHho...",
            "...ohHhhHhhHhhHho...",
            "...ohHhhHhhHhhHho...",
            "...ohHhhHhhHhhHho...",
            "...ohHhhHhhHhhHho...",
        ],
    },
    # Finger waves: hair sculpted flat to the head in S-shaped ridges (the
    # zig-zag of lighter pixels), with laid edges, the little curls of baby
    # hair swooped onto the forehead at each temple.
    "waves": {
        "front": [
            "......oooooooo......",
            "....oohhhhhhhhoo....",
            "...ohMMhhhMMhhhho...",
            "...ohhhMMhhhMMhho...",
            "...ohMMhhhMMhhhho...",
            "...ohhhMMhhhMMhho...",
            "...ohhhSSSSSShhho...",
            "...ohshsssssshsho...",
            "...oSssessssessSo...",
            "...oSssessssessSo...",
            "...oScsssmLssscSo...",
            "....osssssssssso....",
            ".....oooooooooo.....",
        ],
        "left": [
            "......oooooooo......",
            "....oohhhhhhhhoo....",
            "...ohMMhhhMMhhhho...",
            "..ohhhhMMhhhMMhho...",
            "..ohhMMhhhMMhhhho...",
            "..ohhhhMMhhhMMhho...",
            "..ohSSSSShMMhhhho...",
            "..oshsssshhhMMhho...",
            "..osesssshMMhhhho...",
            "..osesssshhhMMhho...",
            "..omscssshhhhhhho...",
            "...osssssohhhhho....",
            "....ooooo.ooooo.....",
        ],
        "back": [
            "......oooooooo......",
            "....oohhhhhhhhoo....",
            "...ohMMhhhMMhhhho...",
            "...ohhhMMhhhMMhho...",
            "...ohMMhhhMMhhhho...",
            "...ohhhMMhhhMMhho...",
            "...ohMMhhhMMhhhho...",
            "...ohhhMMhhhMMhho...",
            "...ohMMhhhMMhhhho...",
            "...ohhhMMhhhMMhho...",
            "...ohhhhhhhhhhhho...",
            "....oohhhhhhhhoo....",
            "......oooooooo......",
        ],
    },
    # Short hair under a bucket hat. The brim is the wide row.
    "bucket": {
        "front": [
            ".....oooooooooo.....",
            "....odddddddddDo....",
            "....odddddddddDo....",
            "....odddddddddDo....",
            "..odddddddddddddDo..",
            ".oDDDDDDDDDDDDDDDDo.",
            "..oohSSSSSSSSSShoo..",
            "...ohSssssssssSho...",
            "...ohssessssessho...",
            "...ohssessssessho...",
            "...oScsssmLssscSo...",
            "....osssssssssso....",
            ".....oooooooooo.....",
        ],
        "left": [
            ".....oooooooooo.....",
            "....odddddddddDo....",
            "....odddddddddDo....",
            "....odddddddddDo....",
            "..odddddddddddddDo..",
            ".oDDDDDDDDDDDDDDDDo.",
            "..ooSSSSShhhhhhoo...",
            "..osssssshhhhhho....",
            "..osesssshhhhhho....",
            "..osesssshhhhhho....",
            "..omscssshhhhhho....",
            "...osssssoooooo.....",
            "....ooooo...........",
        ],
        "back": [
            ".....oooooooooo.....",
            "....odddddddddDo....",
            "....odddddddddDo....",
            "....odddddddddDo....",
            "..odddddddddddddDo..",
            ".oDDDDDDDDDDDDDDDDo.",
            "..oohhhhhhhhhhhhoo..",
            "...ohhhhhhhhhhhho...",
            "...ohhhhHhhhhhhho...",
            "...ohhhhhhhhhhhho...",
            "...ohhhhhhhhhHhho...",
            "....oohhhhhhhhoo....",
            "......oooooooo......",
        ],
    },
    # Shoulder-length locs. The stripes of lighter pixels are the gaps
    # between locs; the last two rows hang onto the shoulders (in TAILS).
    "locs": {
        "front": [
            "......oooooooo......",
            "....oohhHhhHhhoo....",
            "...ohhHhhHhhHhhho...",
            "..ohHhhHhhhhHhhHho..",
            "..ohHhhhhhhhhhhHho..",
            "..ohHhhSSSSSShhHho..",
            "..ohHhSssssssShHho..",
            "..ohHhsssssssshHho..",
            "..ohHhsesssseshHho..",
            "..ohHhsesssseshHho..",
            "..ohHhsssmmssshHho..",
            "..ohHhossssssohHho..",
            "..ohHho.oooo.ohHho..",
        ],
        "left": [
            "......oooooooo......",
            "....oohhHhhHhhoo....",
            "...ohhHhhHhhHhhho...",
            "..ohHhhHhhhhHhhHho..",
            "..ohhhhhhHhhHhhHho..",
            "..ohSSSSShHhhHhhho..",
            "..osssssshHhhHhhho..",
            "..osssssshHhhHhhho..",
            "..osesssshHhhHhhho..",
            "..osesssshHhhHhhho..",
            "..omssssshHhhHhhho..",
            "...osssssohHhhHhho..",
            "....ooooo.ohhHhhho..",
        ],
        "back": [
            "......oooooooo......",
            "....oohhHhhHhhoo....",
            "...ohhHhhHhhHhhho...",
            "..ohHhhHhhhhHhhHho..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
            "..ohHhhHhhHhhHhhHo..",
        ],
    },
    # High-top fade: a tall flat box on top (the flat lid is in TOPPERS),
    # fading from black through grey to skin down the sides and back.
    "hightop": {
        "front": [
            "....ohhhhhhhhhho....",
            "....ohhhhhhhhhho....",
            "....ohhhhhhhhhho....",
            "....ohhhhhhhhhho....",
            "....oMhhhhhhhhMo....",
            "....oMMhhhhhhMMo....",
            "....oMSSSSSSSSMo....",
            "....oSssssssssSo....",
            "....ossessssesso....",
            "....ossessssesso....",
            "....ossssmmsssso....",
            "....oossssssssoo....",
            "......oooooooo......",
        ],
        "left": [
            "...ohhhhhhhhhho.....",
            "...ohhhhhhhhhho.....",
            "...ohhhhhhhhhho.....",
            "...ohhhhhhhhhho.....",
            "...ohhhhhhhhMMo.....",
            "...ohhhhhhMMMMo.....",
            "..oSSSSSSMMMMMo.....",
            "..osssssssMMMMo.....",
            "..osessssssMMSo.....",
            "..osessssssSSSo.....",
            "..omssssssssSo......",
            "...osssssssso.......",
            "....oooooooo........",
        ],
        "back": [
            "....ohhhhhhhhhho....",
            "....ohhhhhhhhhho....",
            "....ohhhhhhhhhho....",
            "....ohhhhhhhhhho....",
            "....oMhhhhhhhhMo....",
            "....oMMhhhhhhMMo....",
            "....oMMMhhhhMMMo....",
            "....oSMMMMMMMMSo....",
            "....oSSMMMMMMSSo....",
            "....osSSSSSSSSso....",
            "....osssssssssso....",
            "....oossssssssoo....",
            "......oooooooo......",
        ],
    },
    # Short pixie cut swept to one side, with laid edges at the temples.
    # Her hoops are separate, in EARRINGS, so they can swing.
    "pixie": {
        "front": [
            "......oooooooo......",
            "....oohhhhHhhhoo....",
            "...ohhhhhHhhhhhho...",
            "...ohhhhHhhhhhhho...",
            "...ohhhHhhhhhhhho...",
            "...ohhhhhhhhSSSho...",
            "...ohhhhhSSsssSho...",
            "...ohshsssssshsho...",
            "...oSssessssessSo...",
            "...oSssessssessSo...",
            "...oScsssmLssscSo...",
            "....osssssssssso....",
            ".....oooooooooo.....",
        ],
        "left": [
            "......oooooooo......",
            "....oohhhHhhhhoo....",
            "...ohhhHhhhhhhhho...",
            "..ohhhHhhhhhhhhho...",
            "..ohhhhhhhhhhhhho...",
            "..ohhhhSShhhhhhho...",
            "..ohhSSSShhhhhhho...",
            "..oshsssshhhhhhho...",
            "..osesssshhhhhhho...",
            "..osesssshhhhhhho...",
            "..omscsssshhhhho....",
            "...osssssssoooo.....",
            "....ooooooo.........",
        ],
        "back": [
            "......oooooooo......",
            "....oohhhhhhhhoo....",
            "...ohhhhhhHhhhhho...",
            "...ohhhhhhhhhhhho...",
            "...ohhHhhhhhhhhho...",
            "...ohhhhhhhhhhhho...",
            "...ohhhhhhhhHhhho...",
            "...ohhhhhhhhhhhho...",
            "...ohhhhhhhhhhhho...",
            "...oShhhhhhhhhhSo...",
            "...oSShhhhhhhhSSo...",
            "....osssssssssso....",
            ".....oooooooooo.....",
        ],
    },
}

# Which columns the eyes are in on each front head.
EYES = {"puffs": (6, 13)}
DEFAULT_EYES = (7, 12)

# What sits above the head drawing, as (column, row, pixels) measured from
# the head's top-left corner. A negative row is above the hair.
TOPPERS = {
    "bow": {
        # The middle of the bottom row is hair, because the bow sits on a dip
        # in the curls and you'd see straight through it otherwise.
        "front": (6, -2, [".dd..dd.", "dDDddDDd", ".ddhhdd."]),
        # From the side you only see one loop of the bow.
        "left": (8, -2, [".dd.", "dDDd", ".dd."]),
    },
    "puffs": {
        "front": (0, -2, ["..ooo..........ooo..", ".ohhhoo......oohhho."]),
        "left": (5, -2, ["..oooo..", "oohhhhoo"]),
    },
    "hightop": {
        "front": (4, -2, ["oooooooooooo", "ohhhhhhhhhho"]),
        "left": (3, -2, ["oooooooooooo", "ohhhhhhhhhho"]),
    },
}

# Hair that hangs below the head, over the shoulders or down the back.
# Same (column, row, pixels) idea; row 13 is the first row under the head.
TAILS = {
    "braids": {
        "front": (3, 13, ["oho........oho", "oHo........oHo", "oho........oho",
                          "oHo........oHo", "ooo........ooo"]),
        "left": (10, 13, ["oHhhHho", "oHhhHho", "oHhhHho", "oHhhHho", "ooooooo"]),
        "back": (5, 13, ["oHhhHhhHho", "oHhhHhhHho", "oHhhHhhHho", "oHhhHhhHho", "oooooooooo"]),
    },
    "locs": {
        "front": (2, 13, ["ohHho......ohHho", ".ooo........ooo."]),
        "left": (10, 13, ["ohhHhhho", "oooooooo"]),
        "back": (2, 13, ["ohHhhHhhHhhHhhHo", "oooooooooooooooo"]),
    },
}

# Earrings that hang free of the head, so they can swing in the dance.
# Each hoop is a solid ring three wide and four tall. With the corners cut
# off the pixels only touched diagonally, and it read as a sparkle instead
# of a ring. From the front and back the inner edge of each hoop sits right
# on the edge of her face, so the gold touches skin with no gap. From the
# side there's one hoop below the ear.
HOOP = ["ggg", "g.g", "g.g", "ggg"]
# Facing front, the two corners furthest from her head are rounded off.
# The side nearest her head stays solid, so the ring still holds together.
HOOP_LEFT_EAR = [".gg", "g.g", "g.g", ".gg"]
HOOP_RIGHT_EAR = [row[::-1] for row in HOOP_LEFT_EAR]
EARRINGS = {
    "pixie": {
        "front": [(2, 10, HOOP_LEFT_EAR), (15, 10, HOOP_RIGHT_EAR)],
        "left": [(8, 10, HOOP)],
    },
}


# Glasses for puffs. "front" and "left" are the frames, measured from the
# head's corner like the toppers.
#
# The round ones (her soft look) are only three rows tall, so each lens shows
# the top pixel of her eye with skin either side, and the bottom of the frame
# covers the lower pixel. There's no room for a ^ in there, so "happy" is a
# closed-eye dash. Bigger frames took over her whole face.
#
# The shades (her 90s look) have no frame around the lens at all, just a thin
# gold wire across the nose and back to the ear. "lenses" lists boxes
# (column, row, width, height) to color in behind her eyes with the "fill"
# letter, which is what makes them look tinted.
GLASSES = {
    "round": {
        "front": (4, 7, [".GGG....GGG.", "G...G..G...G", ".GGG....GGG."]),
        "left": (3, 7, ["GGG...", "...GGG", "GGG..."]),
        "happy": "dash",
    },
    "shades": {
        "front": (8, 8, ["gggg"]),
        "left": (6, 8, ["ggg"]),
        "lenses": {"front": [(5, 8, 3, 2), (12, 8, 3, 2)], "left": [(3, 8, 3, 2)]},
        "fill": "T",
    },
}

# ---------------------------------------------------------------------------
# Tops. Six rows each, sitting between the head and the hips.
# ---------------------------------------------------------------------------

TOPS = {
    # Cropped cardigan, open over a top, two buttons.
    "cardigan": {
        "front": ["....opttttpo....", "....oppttnpo....", "....oppttppo....",
                  "....oPPttnPo....", "....otttttto....", "....otttttto...."],
        "left": [".....otpppo.....", ".....otpppo.....", ".....otpppo.....",
                 ".....otPPPo.....", ".....otttto.....", ".....otttto....."],
        "back": ["....oppppppo....", "....oppppppo....", "....oppppppo....",
                 "....oPPPPPPo....", "....otttttto....", "....otttttto...."],
    },
    # Crop top: three rows of top, two of bare midriff, then the waistband.
    "crop": {
        "front": ["....oppppppo....", "....oppppppo....", "....oPPPPPPo....",
                  "....osssssso....", "....osssssso....", "....oJJJJJJo...."],
        "left": [".....oppppo.....", ".....oppppo.....", ".....oPPPPo.....",
                 ".....osssso.....", ".....osssso.....", ".....oJJJJo....."],
    },
    # Satin slip dress: thin straps, a streak of shine, and a choker.
    "slip": {
        "front": ["....ossnnsso....", "....opsssspo....", "....oppppppo....",
                  "....opptpppo....", "....oppppppo....", "....oppptppo...."],
        "left": [".....osnsso.....", ".....opssso.....", ".....oppppo.....",
                 ".....optppo.....", ".....oppppo.....", ".....oppppo....."],
        "back": ["....ossnnsso....", "....opsssspo....", "....opsssspo....",
                 "....oppppppo....", "....opptpppo....", "....oppppppo...."],
    },
    # Overalls over a crop top. One strap is done up; on the other side the
    # bib corner is folded down, with a bit of midriff showing beside it.
    "overalls": {
        "front": ["....opjppppo....", "....opjppppo....", "....ojjjjppo....",
                  "....ojjjjjso....", "....ojjnjjJo....", "....ojjjjjjo...."],
        "left": [".....opjppo.....", ".....opjppo.....", ".....ojjjpo.....",
                 ".....ojjjso.....", ".....ojjjjo.....", ".....ojjjjo....."],
        "back": ["....opjppjpo....", "....oppjjppo....", "....opjjjjpo....",
                 "....osjjjjso....", "....ojjjjjjo....", "....ojjjjjjo...."],
    },
    # Oversized jersey: trim at the neck, a stripe across the shoulders, a two-digit number.
    "jersey": {
        "front": ["....opnnnnpo....", "....ouuuuuuo....", "....oppppppo....",
                  "....opnpnnpo....", "....opnpnnpo....", "....oppppppo...."],
        "left": [".....onpppo.....", ".....ouuuuo.....", ".....oppppo.....",
                 ".....oppppo.....", ".....oppppo.....", ".....oppppo....."],
        "back": ["....oppppppo....", "....ouuuuuuo....", "....oppppppo....",
                 "....opnpnnpo....", "....opnpnnpo....", "....oppppppo...."],
    },
    # Color-block windbreaker: one color across the shoulders, a white band,
    # another color below, and a zip at the collar.
    "windbreaker": {
        "front": ["....ouuttuuo....", "....ouutuuuo....", "....otttttto....",
                  "....oppppppo....", "....oppppppo....", "....oPPPPPPo...."],
        "left": [".....otuuuo.....", ".....ouuuuo.....", ".....otttto.....",
                 ".....oppppo.....", ".....oppppo.....", ".....oPPPPo....."],
        "back": ["....ouuuuuuo....", "....ouuuuuuo....", "....otttttto....",
                 "....oppppppo....", "....oppppppo....", "....oPPPPPPo...."],
    },
    # Cropped color-block jacket: two colors split down the middle over a
    # white band, then midriff and a high waistband.
    "blockjacket": {
        "front": ["....opppuuuo....", "....opppuuuo....", "....otttttto....",
                  "....oPPPUUUo....", "....osssssso....", "....oJJJJJJo...."],
        "left": [".....oppppo.....", ".....oppppo.....", ".....otttto.....",
                 ".....oPPPPo.....", ".....osssso.....", ".....oJJJJo....."],
        "back": ["....ouuupppo....", "....ouuupppo....", "....otttttto....",
                 "....oUUUPPPo....", "....osssssso....", "....oJJJJJJo...."],
    },
}

# ---------------------------------------------------------------------------
# Legs. Every set has the same poses so the animations work for all of them.
# "short" is one row shorter than standing, which is what makes a character
# sink down a little when sitting or crouching.
# ---------------------------------------------------------------------------

# Bare legs with a strap shoe: mary janes with a sock, or heels if the
# outfit sets the sock color to skin.
BARE_LEGS = {
    "front": {
        "stand": ["....ossoosso....", "....ofqooqfo....", "....offooffo...."],
        "left_up": ["....ofqoosso....", "....offooqfo....", "........offo...."],
        "right_up": ["....ossooqfo....", "....ofqooffo....", "....offo........"],
        "short": ["....ofqooqfo....", "....offooffo...."],
    },
    "left": {
        "stand": ["......osso......", "......ofqo......", ".....offo......."],
        "stride": ["......osso......", ".....oqo.oqo....", "....offo.offo..."],
        "short": ["...oqssssso.....", "...offo........."],
    },
}

# Baggy pants: each leg is a pixel wider than a bare leg and sits further
# out, with a chunky shoe underneath.
BAGGY_LEGS = {
    "front": {
        "stand": ["...ojjjoojjjo...", "...ojjjoojjjo...", "...offfoofffo..."],
        "left_up": ["...ojjjoojjjo...", "...offfoojjjo...", "........offfo..."],
        "right_up": ["...ojjjoojjjo...", "...ojjjoofffo...", "...offfo........"],
        "short": ["...ojjjoojjjo...", "...offfoofffo..."],
    },
    "left": {
        "stand": [".....ojjjjo.....", ".....ojjjjo.....", "....offffo......"],
        "stride": [".....ojjjjo.....", "....ojjoojjo....", "...offo.offo...."],
        "short": ["...ojjjjjjo.....", "...offo........."],
    },
}

# Wide-leg pants: they flare out toward the hem and cover the shoes.
WIDE_LEGS = {
    "front": {
        "stand": ["...ojjjoojjjo...", "..ojjjjoojjjjo..", "..oJJJJooJJJJo.."],
        "left_up": ["...ojjjoojjjo...", "..oJJJJoojjjjo..", "........oJJJJo.."],
        "right_up": ["...ojjjoojjjo...", "..ojjjjooJJJJo..", "..oJJJJo........"],
        "short": ["..ojjjjoojjjjo..", "..oJJJJooJJJJo.."],
    },
    "left": {
        "stand": [".....ojjjjo.....", "....ojjjjjjo....", "....oJJJJJJo...."],
        "stride": ["....ojjjjjjo....", "...ojjjoojjjo...", "...oJJJo.oJJJo.."],
        "short": ["...ojjjjjjo.....", "...oJJo........."],
    },
}

# Bottoms: three rows of hips, plus which legs go underneath.
BOTTOMS = {
    # Pleats are just light and dark stripes taking turns.
    "pleats": {
        "hips": {"front": ["...ojJjJjJjJo..."] * 3, "left": ["....ojJjJjJo...."] * 3},
        "legs": BARE_LEGS,
    },
    # The skirt of the slip dress, flaring a little, with the shine carried on.
    "dress": {
        "hips": {"front": ["....oppppppo....", "...opptpppppo...", "...oPPPPPPPPo..."],
                 "left": ["....oppppppo....", "....opptpppo....", "....oPPPPPPo...."]},
        "legs": BARE_LEGS,
    },
    "baggy": {
        "hips": {"front": ["...ojjjjjjjjo...", "...ojjjJJjjjo...", "...ojjjJJjjjo..."],
                 "left": ["....ojjjjjjo...."] * 3},
        "legs": BAGGY_LEGS,
    },
    # Baggy jeans with the long hem of the jersey hanging over them.
    "jersey_baggy": {
        "hips": {"front": ["...oppppppppo...", "...oPPPPPPPPo...", "...ojjjJJjjjo..."],
                 "left": ["....oppppppo....", "....oPPPPPPo....", "....ojjjjjjo...."]},
        "legs": BAGGY_LEGS,
    },
    "wide": {
        "hips": {"front": ["....ojjjjjjo....", "...ojjjjjjjjo...", "...ojjjJJjjjo..."],
                 "left": ["....ojjjjjjo...."] * 3},
        "legs": WIDE_LEGS,
    },
}

# ---------------------------------------------------------------------------
# Arms. Poses for the LEFT side of the drawing, as (column, row, pixels)
# pieces. Rows count down from the top of the top, so a negative row reaches
# up beside the head. The right arm is the same pieces mirrored.
# "a" is the upper sleeve and "r" the forearm, so short sleeves and bare
# arms are just a matter of which colors an outfit gives them.
# ---------------------------------------------------------------------------

FRONT_ARMS = {
    "down": [(2, 0, ["oo", "oa", "oa", "or", "os", "oo"])],
    "out": [(0, 0, ["oooo", "osra", "oooo"])],
    "up": [(0, -3, ["oo..", "oso.", "oro.", ".oao", "..oo"])],
    # Typing: a short upper arm, plus a hand resting on the tummy that taps
    # one row up or down.
    "type_hi": [(2, 0, ["oo", "oa", "oa", "oo"]), (5, 3, ["ss"])],
    "type_lo": [(2, 0, ["oo", "oa", "oa", "oo"]), (5, 4, ["ss"])],
}

# From the side you only see one arm, drawn over the middle of the top.
SIDE_ARMS = {
    "down": [(7, 1, ["AA", "AA", "RR", "ss"])],
    "forward": [(7, 1, ["AA", "AA"]), (6, 3, ["RR", "ss"])],
    "back": [(7, 1, ["AA", "AA"]), (8, 3, ["RR", "ss"])],
    "type_hi": [(7, 1, ["AA", "AA"]), (5, 3, ["RRRR"]), (3, 2, ["ss"])],
    "type_lo": [(7, 1, ["AA", "AA"]), (5, 3, ["RRRR"]), (3, 3, ["ss"])],
}

# Little extras that float next to the character, in whole-frame coordinates.
SPARKLE_BIG = [".y.", "yyy", ".y."]
SPARKLE_SMALL = ["y"]
BANG = ["xx", "xx", "..", "xx"]

# ---------------------------------------------------------------------------
# Outfit colors. A one-letter value means "same as that letter", which is
# how bare arms work: a sleeve colored "s" is just skin.
# Anything an outfit leaves out falls back to OUTFIT_DEFAULTS.
# ---------------------------------------------------------------------------

OUTFIT_DEFAULTS = {"a": "p", "r": "a", "A": "P", "R": "A", "U": "u", "D": "d", "q": "f",
                   "t": "p", "n": "p", "u": "p", "d": "p", "j": "p", "J": "P", "f": "P"}

WHITE, WHITE_SHADE = "#f5f1ea", "#d8d0c4"
BLACK, BLACK_SHADE = "#3d353a", "#2b2428"
DENIM, DENIM_SHADE = "#5f86b8", "#47699a"
INDIGO, INDIGO_SHADE = "#3f5f8f", "#2f4a73"
BURGUNDY, BURGUNDY_SHADE, BURGUNDY_SHINE = "#8c2f3f", "#6d2130", "#b85566"
FOREST, FOREST_SHADE = "#2f6b4a", "#24543a"
MUSTARD, MUSTARD_SHADE = "#e0b040", "#bf9230"
TAN = "#c79a5b"
BARE_ARMS = {"a": "s", "A": "S"}

OUTFITS = {
    # The two soft outfits.
    "soft_pink": {"top": "cardigan", "bottoms": "pleats", "colors": {
        "p": "#f6bfcd", "P": "#e4a1b4", "t": "#fffaf5", "n": "#fffaf5",
        "j": "#f7ecd9", "J": "#e3d2b6", "d": "#f6bfcd", "D": "#fde0e8",
        "f": "#5a3a3f", "q": "#fffaf5"}},
    "soft_lavender": {"top": "cardigan", "bottoms": "pleats", "colors": {
        "p": "#d2c3f2", "P": "#b8a6e0", "t": "#fffaf5", "n": "#fffaf5",
        "j": "#c2dbba", "J": "#a6c49d", "d": "#c2dbba", "D": "#dcecd6",
        "f": "#5a3a3f", "q": "#fffaf5"}},

    # 90s versions of the same two.
    "bow_90s": {"top": "windbreaker", "bottoms": "baggy", "colors": {
        "u": BURGUNDY, "U": BURGUNDY_SHADE, "t": WHITE, "p": FOREST, "P": FOREST_SHADE,
        "a": "u", "r": "p", "A": "U", "R": "P",
        "j": DENIM, "J": DENIM_SHADE, "f": WHITE, "d": MUSTARD, "D": "#f0cc70"}},
    "puffs_90s": {"top": "crop", "bottoms": "wide", "colors": {
        "p": BURGUNDY, "P": BURGUNDY_SHADE, **BARE_ARMS,
        "j": DENIM, "J": DENIM_SHADE, "f": WHITE, "d": MUSTARD}},

    # The rest of the 90s crew.
    "braids": {"top": "crop", "bottoms": "baggy", "colors": {
        "p": WHITE, "P": WHITE_SHADE, **BARE_ARMS,
        "j": DENIM, "J": DENIM_SHADE, "f": WHITE, "d": BURGUNDY, "D": BURGUNDY_SHINE}},
    "waves": {"top": "slip", "bottoms": "dress", "colors": {
        "p": BURGUNDY, "P": BURGUNDY_SHADE, "t": BURGUNDY_SHINE, "n": BLACK_SHADE, **BARE_ARMS,
        "f": BLACK_SHADE, "q": "s"}},
    "bucket": {"top": "overalls", "bottoms": "baggy", "colors": {
        "p": MUSTARD, "P": MUSTARD_SHADE, "n": MUSTARD, **BARE_ARMS,
        "j": INDIGO, "J": INDIGO_SHADE, "f": WHITE, "d": FOREST, "D": FOREST_SHADE}},
    "locs": {"top": "jersey", "bottoms": "jersey_baggy", "colors": {
        "p": FOREST, "P": FOREST_SHADE, "u": MUSTARD, "n": WHITE,
        "r": "s", "R": "S",
        "j": DENIM, "J": DENIM_SHADE, "f": TAN}},
    "hightop": {"top": "windbreaker", "bottoms": "baggy", "colors": {
        "u": INDIGO, "U": INDIGO_SHADE, "t": WHITE, "p": MUSTARD, "P": MUSTARD_SHADE,
        "a": "u", "r": "p", "A": "U", "R": "P",
        "j": BLACK, "J": BLACK_SHADE, "f": WHITE}},
    "pixie": {"top": "blockjacket", "bottoms": "wide", "colors": {
        "p": BLACK, "P": BLACK_SHADE, "u": BURGUNDY, "U": BURGUNDY_SHADE, "t": WHITE,
        "j": WHITE, "J": WHITE_SHADE, "f": BLACK_SHADE}},
}

# ---------------------------------------------------------------------------
# Every sheet that gets saved: file name -> who's on it.
# ---------------------------------------------------------------------------

BOW = {"hair": "bow", "skin": "#A0673F"}
PUFFS = {"hair": "puffs", "skin": "#B97A4F"}

SHEETS = {
    "bow_soft": {**BOW, "outfit": "soft_pink"},
    "puffs_soft": {**PUFFS, "outfit": "soft_lavender", "glasses": "round"},
    "bow_90s": {**BOW, "outfit": "bow_90s"},
    "puffs_90s": {**PUFFS, "outfit": "puffs_90s", "glasses": "shades"},
    "braids": {"hair": "braids", "skin": "#5C3A21", "outfit": "braids"},
    "waves": {"hair": "waves", "skin": "#6F4527", "outfit": "waves"},
    "bucket": {"hair": "bucket", "skin": "#8D5A3B", "outfit": "bucket"},
    "locs": {"hair": "locs", "skin": "#A0673F", "outfit": "locs"},
    "hightop": {"hair": "hightop", "skin": "#B97A4F", "outfit": "hightop"},
    "pixie": {"hair": "pixie", "skin": "#C68A5E", "outfit": "pixie"},
}
