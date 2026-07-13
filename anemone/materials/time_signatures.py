import abjad
import evans


##
## 01 ##
##

signatures_01 = [abjad.TimeSignature((4, 4)) for _ in range(7)]

signatures_01.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_01 = []

reduced_signatures_01 = evans.reduce_fermata_measures(
    signatures_01, fermata_measures_01
)

##
## 02 ##
##

signatures_02 = [abjad.TimeSignature(_) for _ in [(3, 4), (4, 4), (7, 8), (4, 4), (5, 4), (5, 8), (5, 8)]]

signatures_02 = signatures_02 + [abjad.TimeSignature((4, 4)) for _ in range(12)]

signatures_02.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_02 = []

reduced_signatures_02 = evans.reduce_fermata_measures(
    signatures_02, fermata_measures_02
)

##
## 03 ##
##

signatures_03 = [abjad.TimeSignature(_) for _ in [
    (4, 4), (7, 8),
    (4, 4), (3, 4),
    (9, 8), (3, 4),
    (4, 4), (4, 4), (5, 8),
    (4, 4), (3, 4), (2, 4),
    (4, 4), (7, 8),
]] # 14 total

signatures_03.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_03 = []

reduced_signatures_03 = evans.reduce_fermata_measures(
    signatures_03, fermata_measures_03
)

##
## 04 ##
##

signatures_04 = [abjad.TimeSignature((4, 4)) for _ in range(10)]

signatures_04.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_04 = []

reduced_signatures_04 = evans.reduce_fermata_measures(
    signatures_04, fermata_measures_04
)

##
## 05 ##
##

signatures_05 = [abjad.TimeSignature((4, 4)) for _ in range(11)]

signatures_05.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_05 = []

reduced_signatures_05 = evans.reduce_fermata_measures(
    signatures_05, fermata_measures_05
)

##
## 06 ##
##

signatures_06 = [abjad.TimeSignature((4, 4)) for _ in range(9)]

signatures_06.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_06 = []

reduced_signatures_06 = evans.reduce_fermata_measures(
    signatures_06, fermata_measures_06
)

##
## 07 ##
##

signatures_07 = [abjad.TimeSignature((4, 4)) for _ in range(7)]

signatures_07.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_07 = []

reduced_signatures_07 = evans.reduce_fermata_measures(
    signatures_07, fermata_measures_07
)

##
## 08 ##
##

signatures_08 = [abjad.TimeSignature((4, 4)) for _ in range(8)]

signatures_08.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_08 = []

reduced_signatures_08 = evans.reduce_fermata_measures(
    signatures_08, fermata_measures_08
)

##
## 09 ##
##

signatures_09 = [abjad.TimeSignature((4, 4)) for _ in range(23)]

signatures_09.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_09 = []

reduced_signatures_09 = evans.reduce_fermata_measures(
    signatures_09, fermata_measures_09
)

##
## 10 ##
##

signatures_10 = [abjad.TimeSignature((4, 4)) for _ in range(8)]

signatures_10.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_10 = []

reduced_signatures_10 = evans.reduce_fermata_measures(
    signatures_10, fermata_measures_10
)

##
## 11 ##
##

numerators_11 = evans.Sequence([[8, 8, 5, 4], [8, 7, 6, 5], [8, 6, 4]]).helianthate(2, -1).rotate(1).flatten(depth=-1)

proposed_meter_sequence_11 = evans.Sequence([abjad.TimeSignature((_, 8)) for _ in numerators_11]).reduce_time_signatures_in_list().reverse()

signatures_11 = [proposed_meter_sequence_11[_] for _ in range(9)]

signatures_11.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_11 = []

reduced_signatures_11 = evans.reduce_fermata_measures(
    signatures_11, fermata_measures_11
)

##
## 12 ##
##

signatures_12 = [abjad.TimeSignature((4, 4)) for _ in range(11)]

signatures_12.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_12 = []

reduced_signatures_12 = evans.reduce_fermata_measures(
    signatures_12, fermata_measures_12
)

##
## 13 ##
##

numerators_13 = evans.Sequence([[8, 8, 5, 4], [8, 7, 6, 5], [8, 6, 4]]).helianthate(-1, 2).rotate(3).flatten(depth=-1)

proposed_meter_sequence_13 = evans.Sequence([abjad.TimeSignature((_, 8)) for _ in numerators_13]).reduce_time_signatures_in_list()

signatures_13 = [proposed_meter_sequence_13[_] for _ in range(14)]

signatures_13.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_13 = []

reduced_signatures_13 = evans.reduce_fermata_measures(
    signatures_13, fermata_measures_13
)

##
## 14 ##
##

signatures_14 = [abjad.TimeSignature((4, 4)) for _ in range(25)]

signatures_14.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_14 = []

reduced_signatures_14 = evans.reduce_fermata_measures(
    signatures_14, fermata_measures_14
)

##
## 15 ##
##

signatures_15 = [abjad.TimeSignature((4, 4)) for _ in range(7)]

signatures_15.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_15 = []

reduced_signatures_15 = evans.reduce_fermata_measures(
    signatures_15, fermata_measures_15
)

##
## 16 ##
##

numerators_16 = evans.Sequence([[8, 8, 5, 4], [8, 7, 6, 5], [8, 6, 4]]).helianthate(-1, 2).rotate(3).flatten(depth=-1)

proposed_meter_sequence_16 = evans.Sequence([abjad.TimeSignature((_, 8)) for _ in numerators_16]).reduce_time_signatures_in_list().reverse()

signatures_16 = [proposed_meter_sequence_16[_] for _ in range(8)]

signatures_16.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_16 = []

reduced_signatures_16 = evans.reduce_fermata_measures(
    signatures_16, fermata_measures_16
)

##
## 17 ##
##

numerators = evans.Sequence([[8, 8, 5, 4], [8, 7, 6, 5], [8, 6, 4]]).helianthate(-1, 1).flatten(depth=-1)

proposed_meter_sequence = evans.Sequence([abjad.TimeSignature((_, 8)) for _ in numerators]).reduce_time_signatures_in_list()

signatures_17 = [proposed_meter_sequence[_] for _ in range(22)]

signatures_17.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_17 = []

reduced_signatures_17 = evans.reduce_fermata_measures(
    signatures_17, fermata_measures_17
)

##
## 18 ##
##

signatures_18 = [abjad.TimeSignature((4, 4)) for _ in range(8)] #and 10 for final fermata...

signatures_18.append(abjad.TimeSignature((1, 4))) # for final stab

signatures_18.append(abjad.TimeSignature((1, 4)))  # for ending skip

signatures_18.append(abjad.TimeSignature((1, 4)))  # for ending skip

fermata_measures_18 = [9]

reduced_signatures_18 = evans.reduce_fermata_measures(
    signatures_18, fermata_measures_18
)



##
## total ##
##

all_signatures = evans.join_time_signature_lists(
    [
        reduced_signatures_01,
        reduced_signatures_02,
        reduced_signatures_03,
        reduced_signatures_04,
        reduced_signatures_05,
        reduced_signatures_06,
        reduced_signatures_07,
        reduced_signatures_08,
        reduced_signatures_09,
        reduced_signatures_10,
        reduced_signatures_11,
        reduced_signatures_12,
        reduced_signatures_13,
        reduced_signatures_14,
        reduced_signatures_15,
        reduced_signatures_16,
        reduced_signatures_17,
        reduced_signatures_18,
    ]
)
