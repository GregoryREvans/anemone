import evans

concordance = {
    "rhythm": [ # done
        "even division",
        "sustains",
        "tuplets",
        "common denominator talea",
        "excavated accel / rall",
    ],
    "pitch": [
        "double/triple stops",
        "clusters",
        "cannibalized sequence",
        "scale",
        "pc sets",
    ],
    "articulations": [ # articulations bleed to adjacent blocks
        "accent pattern",
        "trill",
        "finger pressure",
        "scratch",
        "vib",
    ],
    "dynamics": [
        "--",
        ">< or |><|",
        "< or <|",
        "> or |>",
        "<> or <|>",
    ],
    "dynamic change density": [
        "no change",
        "sparse",
        "moderate",
        "dense",
    ],
    "specialized scenarios": ["barriolage", "", "", "", "tremolo", ""],
    "glissando": ["glissando", "", ""],
    # "transition types?"
}
grand_matrix = {}

commands = { # we need 54 total (double check with the chart we made)
    "rhythm": [[(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 2, 3), (1,), (4,)], [(0, 2, 3), (1,), (4,)], [(0, 4, 2, 3), (1,)], [(0, 4, 2, 3), (1,)], [(0, 4, 2, 1, 3)], [(0, 4, 2, 1, 3)]], #needs 10 transformations
    "pitch": [[(0, 2, 1, 4, 3)], [(0, 2, 1, 4, 3)], [(0, 2, 1, 4, 3)], [(0, 2, 1, 3, 4)], [(0, 4, 2, 1, 3)], [(0, 4, 2, 1, 3)], [(0, 4, 1, 3, 2)], [(0, 4, 1, 3, 2)], [(0, 4, 1, 3, 2)], [(0, 4, 3, 1, 2)]],
    "articulations": [[(0,), (1, 4, 2, 3)], [(0,), (1, 4, 2, 3)], [(0,), (1, 4, 2, 3)], [(0, 4, 3, 1, 2)], [(0, 4, 3, 1, 2)], [(0, 4, 3, 1, 2)], [(0, 1, 3, 2), (4,)], [(0, 1, 3, 2), (4,)], [(0, 1, 3, 2), (4,)], [(0, 1, 3, 2), (4,)]],
    "dynamics": [[(0, 1, 3), (2,), (4,)], [(0, 1, 3), (2,), (4,)], [(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 1, 4), (2,), (3,)], [(0, 1, 4), (2,), (3,)], [(0, 1, 4), (2,), (3,)], [(0, 4, 1, 2, 3)]],
    "dynamic change density": [[(0, 3, 1, 2)],  [(0, 3, 1, 2)],  [(0, 3, 1, 2)], [(0, 2, 1, 3)], [(0, 2, 1, 3)], [(0, 2, 1, 3)], [(0, 1, 3), (2,)], [(0, 1, 3), (2,)], [(0, 3), (1, 2)], [(0, 1), (2, 3)], [(0, 3), (1,), (2,)], [(1, 3), (0,), (2,)], [(0, 2), (1, 3)]], # needs 13 transformations
    "specialized scenarios": [[(0,), (1, 2, 5), (3, 4)], [(0,), (1, 2, 5), (3, 4)], [(0,), (1, 2, 5), (3, 4)], [(0,), (1, 2, 5), (3, 4)], [(0,), (1, 2, 5), (3, 4)], [(0,), (1, 3, 2), (4, 5)], [(0,), (1, 3), (2, 4, 5)], [(0, 1), (2, 3, 5), (4,)]], # needs 8 transformations
    "glissando": [[(0, 1, 2)], [(0,), (1, 2)], [(0, 1, 2)], [(0, 1), (2,)], [(0, 1, 2)], [(0, 2), (1,)], [(0, 2, 1)], [(0, 2, 1)], [(0, 1, 2)], [(0,), (1, 2)], [(0, 1, 2)], [(0, 1), (2,)], [(0, 1, 2)], [(0, 2), (1,)], [(0, 2, 1)], [(0, 2, 1)], [(0, 1, 2)], [(0,), (1, 2)]],
}

for name, thread in commands.items():
    grand_matrix[name] = []
    if name == "dynamic change density":
        result = evans.Sequence([0, 1, 2, 3]).permutational_parsimony(thread, accumulate=True).flatten(depth=-1).items[:54]
    elif name == "specialized scenarios":
        result = evans.Sequence([0, 1, 2, 3, 4, 5]).permutational_parsimony(thread, accumulate=True).flatten(depth=-1).items[:54]
    elif name == "glissando":
        result = evans.Sequence([0, 1, 2]).permutational_parsimony(thread, accumulate=True).flatten(depth=-1).items[:54]
    else:
        result = evans.Sequence([0, 1, 2, 3, 4]).permutational_parsimony(thread, accumulate=True).flatten(depth=-1).items[:54]
    grand_matrix[name].extend(result)

pre_s = [[str(e) for e in row] for name, row in grand_matrix.items()]
s = pre_s
for i, pair in enumerate(grand_matrix.items()):
    s[i] = [pair[0] + ":"] + s[i]

lens = [max(map(len, col)) for col in zip(*s)]
fmt = "\t".join("{{:{}}}".format(x) for x in lens)
table = [fmt.format(*row) for row in s]

with open("permutation_matrix.txt", "w") as text_file:
    text_file.write("\n".join(table))

explicit = []
for row, lookup_pair in zip(pre_s, concordance.items()):
    temp = []
    for _ in row[1:]:
        looked_up_value = lookup_pair[1][int(_)]
        temp.append(looked_up_value)
    explicit.append(temp)

for i, pair in enumerate(grand_matrix.items()):
    explicit[i] = [pair[0] + ":"] + explicit[i]

lens = [max(map(len, col)) for col in zip(*explicit)]
fmt = "\t".join("{{:{}}}".format(x) for x in lens)
table_ = [fmt.format(*row) for row in explicit]

with open("explicit_matrix.txt", "w") as text_file:
    text_file.write("\n".join(table_))
