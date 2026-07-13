import evans

probs_1 = evans.Sequence([1, 6, 5, 4, 3, 2]).normalize_to_sum(desired_sum=1)
probs_2 = evans.Sequence([4, 1, 6, 5, 4, 3]).normalize_to_sum(desired_sum=1)
probs_3 = evans.Sequence([3, 4, 1, 6, 5, 4]).normalize_to_sum(desired_sum=1)
probs_4 = evans.Sequence([2, 3, 4, 1, 6, 5]).normalize_to_sum(desired_sum=1)
probs_5 = evans.Sequence([1, 2, 3, 4, 1, 6]).normalize_to_sum(desired_sum=1)
probs_6 = evans.Sequence([1, 2, 4, 8, 16, 32]).normalize_to_sum(desired_sum=1)

probs = {
    "1": {
        "1": probs_1[0],
        "2": probs_1[1],
        "3": probs_1[2],
        "4": probs_1[3],
        "5": probs_1[4],
        "6": probs_1[5],
    },
    "2": {
        "1": probs_2[0],
        "2": probs_2[1],
        "3": probs_2[2],
        "4": probs_2[3],
        "5": probs_2[4],
        "6": probs_2[5],
    },
    "3": {
        "1": probs_3[0],
        "2": probs_3[1],
        "3": probs_3[2],
        "4": probs_3[3],
        "5": probs_3[4],
        "6": probs_3[5],
    },
    "4": {
        "1": probs_4[0],
        "2": probs_4[1],
        "3": probs_4[2],
        "4": probs_4[3],
        "5": probs_4[4],
        "6": probs_4[5],
    },
    "5": {
        "1": probs_5[0],
        "2": probs_5[1],
        "3": probs_5[2],
        "4": probs_5[3],
        "5": probs_5[4],
        "6": probs_5[5],
    },
    "6": {
        "1": probs_6[0],
        "2": probs_6[1],
        "3": probs_6[2],
        "4": probs_6[3],
        "5": probs_6[4],
        "6": probs_6[5],
    },
}


viola_1_sequence = ["2"] + evans.Sequence.markov(
    transition_prob=probs,
    first_state="2",
    length=40,
    seed=0,
)

viola_2_sequence = ["4"] + evans.Sequence.markov(
    transition_prob=probs,
    first_state="4",
    length=40,
    seed=1,
)

viola_3_sequence = ["1"] + evans.Sequence.markov(
    transition_prob=probs,
    first_state="1",
    length=40,
    seed=2,
)


print([int(_) for _ in viola_1_sequence])
print("")
print([int(_) for _ in viola_2_sequence])
print("")
print([int(_) for _ in viola_3_sequence])
print("")
