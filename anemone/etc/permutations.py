import abjad
import evans

for rotation in range(5):

    seq = evans.Sequence([0, 1, 2, 3, 4]).permutational_parsimony(
        cycles=[[(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)], [(0, 1, 3, 2, 4)]],
        accumulate=True,
    ).rotate(rotation)

    flattened_seq = seq.flatten(depth=-1)

    flattened_seq = flattened_seq.transpose(1)

    stacked_intervals = flattened_seq.stack_intervals()

    stacked_intervals = [0] + stacked_intervals

    base_pitch = -11

    semitonal_chord = [base_pitch + interval for interval in stacked_intervals]

    staff_1 = abjad.Staff()

    for pitch in semitonal_chord:
        staff_1.append(abjad.Note(abjad.NumberedPitch(pitch), abjad.Duration(1, 4)))

    abjad.attach(abjad.Clef("alto"), staff_1[0])

    quartertonal_chord = [base_pitch + (interval / 2) for interval in stacked_intervals]

    staff_2 = abjad.Staff()

    for pitch in quartertonal_chord:
        staff_2.append(abjad.Note(abjad.NumberedPitch(pitch), abjad.Duration(1, 4)))

    abjad.attach(abjad.Clef("alto"), staff_2[0])

    score = abjad.Score([staff_1, staff_2])

    abjad.show(score)
