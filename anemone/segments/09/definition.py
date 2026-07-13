import pathlib
from fractions import Fraction
from random import choice, seed

import abjad
import baca
import evans
from abjadext import rmakers

import anemone


def rests_in_runs(selections):
    for i, tuplet in enumerate(abjad.select.tuplets(selections)):
        if i % 3 == 0:
            relevant_leaves = abjad.select.get(abjad.select.leaves(tuplet), abjad.index([0, 1, -1]))
        else:
            relevant_leaves = abjad.select.get(abjad.select.leaves(tuplet), abjad.index([0, -2, -1]))
        rmakers.force_rest(relevant_leaves)


def trill_runs(selections, intervals=["+P4"]):
    cyc_intervals = evans.CyclicList(intervals, forget=False)
    for run in abjad.select.runs(selections):
        abjad.attach(
            abjad.bundle(
                abjad.StartTrillSpan(interval=abjad.NamedInterval(cyc_intervals(r=1)[0])),
                r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))""",
            ),
            run[0]
        )
        abjad.attach(abjad.StopTrillSpan(), abjad.get.leaf(run[-1], 1))


def conditional_swells(selections):
    cyc_swell_peaks = evans.CyclicList(["mf", "f", "f", "ff", "ff", "fff", "ff", "f"], forget=False)
    cyc_individual_dynamics = evans.CyclicList(["p", "f", "mp", "mf"], forget=False)
    runs = abjad.select.runs(selections)
    for run in runs:
        if 2 < len(run):
            abjad.attach(abjad.StartHairpin("o<"), run[0])
            abjad.attach(abjad.Dynamic(cyc_swell_peaks(r=1)[0]), run[len(run)//2])
            abjad.attach(abjad.StartHairpin(">o"), run[len(run)//2])
            abjad.attach(abjad.StopHairpin(), run[-1])
        elif len(run) == 2:
            abjad.attach(abjad.Dynamic("sfp"), run[0])
            abjad.attach(abjad.StartHairpin("--"), run[0])
            abjad.attach(abjad.StopHairpin(), abjad.get.leaf(run[-1], 1))
        else:
            abjad.attach(abjad.Dynamic(cyc_individual_dynamics(r=1)[0]), run[0])


def replace_alternating_rests_with_glissandi(selections, glissando_seed_modifier=0):
    possible_gliss_pitches = [step for step in range(-5, 5)]
    rests = abjad.select.rests(selections)
    larger_rests = [rest for rest in rests if abjad.Duration(1, 4) <= rest.written_duration]
    non_tuplet_rests = []
    for rest in larger_rests:
        if type(abjad.get.parentage(rest).parent) is not abjad.Tuplet:
            non_tuplet_rests.append(rest)
    grouped_rests = abjad.select.group_by_contiguity(non_tuplet_rests)
    for i, group in enumerate(grouped_rests):
        if i == 0 or i % 2 != 0:
            group_duration = abjad.get.duration(group)
            if i % 4 != 0:
                replacement_leaves = evans.accelerando(
                    [(1, 13), (1, 6), (1, 16)],
                    [(1, 7), (1, 15), (1, 16)],
                    [(1, 17), (1, 8), (1, 16)],
                    preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[2, 3]),
                )([group_duration])
                indicators = abjad.get.indicators(abjad.select.leaf(group, 0))
                for indicator in indicators:
                    abjad.detach(indicator, abjad.select.leaf(group, 0))
                    abjad.attach(indicator, abjad.select.leaf(replacement_leaves, 0))
                seed(i*glissando_seed_modifier%30)
                start_pitch = choice(possible_gliss_pitches)
                stop_pitch = choice(possible_gliss_pitches)
                while stop_pitch == start_pitch:
                    stop_pitch = choice(possible_gliss_pitches)
                handler = evans.PitchHandler([start_pitch, stop_pitch], staff_positions=True)
                handler(replacement_leaves)
                evans.ArticulationHandler(["tremolo"])(replacement_leaves)
                evans.zero_padding_glissando(replacement_leaves)
                abjad.attach(abjad.Dynamic("ff"), abjad.select.leaf(replacement_leaves, 0))
                abjad.attach(abjad.Markup(r"\markup gridato"), abjad.select.note(replacement_leaves, 0), direction=abjad.UP)
                abjad.attach(abjad.Markup(r"\markup normale"), abjad.get.leaf(abjad.select.leaf(group, -1), 1), direction=abjad.UP)
            else:
                replacement_leaves = evans.tuplet(
                    [choice([(1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1)]) for quarter in range(5)],
                    preprocessor=evans.make_preprocessor(quarters=True),
                    pre_commands=[
                        lambda selections: [rmakers.force_rest(note) for note in abjad.select.get(abjad.select.notes(selections), abjad.index([0, 2, 5, 6, 11], 13))],
                    ]
                )([group_duration])
                indicators = abjad.get.indicators(abjad.select.leaf(group, 0))
                for indicator in indicators:
                    abjad.detach(indicator, abjad.select.leaf(group, 0))
                    abjad.attach(indicator, abjad.select.leaf(replacement_leaves, 0))
                seed(i*glissando_seed_modifier*2%30)
                pitches = [choice(["c", "g", "d'", "a'"]) for note in range(len(abjad.select.notes(replacement_leaves)))]
                for note, pitch in zip(abjad.select.notes(replacement_leaves), pitches):
                    note.written_pitch = abjad.NamedPitch(pitch)
                abjad.attach(abjad.Dynamic("p"), abjad.select.note(replacement_leaves, 0))
                abjad.attach(abjad.StartHairpin("<"), abjad.select.note(replacement_leaves, 0))
                abjad.attach(abjad.Dynamic("ff"), abjad.select.note(replacement_leaves, -1))
                abjad.attach(abjad.Markup(r"\markup {b.b.}"), abjad.select.note(replacement_leaves, 0), direction=abjad.UP)
                abjad.attach(abjad.Markup(r"\markup normale"), abjad.get.leaf(abjad.select.leaf(group, -1), 1), direction=abjad.UP)
            abjad.mutate.replace(group, replacement_leaves)
        elif i % 3 == 0:
            group_durations = [abjad.get.duration(term) for term in group]
            replacement_tie = evans.make_tied_notes()(group_durations)
            seed(i*glissando_seed_modifier%30)
            random_pitch = choice(possible_gliss_pitches)
            handler = evans.PitchHandler([
                [
                    abjad.NamedPitch(random_pitch).name,
                    abjad.NamedInterval("+P4").transpose(abjad.NamedPitch(random_pitch)).name,
                ]
            ])
            temp_container = abjad.Container([replacement_tie])
            handler(temp_container)
            replacement_tie = abjad.mutate.eject_contents(temp_container)
            for chord in abjad.select.leaves(replacement_tie):
                abjad.tweak(chord.note_heads[1], r"\tweak style #'harmonic")
            indicators = abjad.get.indicators(abjad.select.leaf(group, 0))
            for indicator in indicators:
                abjad.detach(indicator, abjad.select.leaf(group, 0))
                abjad.attach(indicator, abjad.select.leaf(replacement_tie, 0))
            if 1 < len(replacement_tie):
                abjad.attach(abjad.Dynamic("mp"), replacement_tie[0])
                abjad.attach(abjad.StartHairpin("<"), replacement_tie[0])
                abjad.attach(abjad.Dynamic("f"), replacement_tie[-1])
            else:
                abjad.attach(abjad.Dynamic("sfz"), replacement_tie[0])
            abjad.mutate.replace(group, replacement_tie)
        else:
            group_durations = [abjad.get.duration(term) for term in group]
            replacement_tie = evans.make_tied_notes()(group_durations)
            seed(i*glissando_seed_modifier%30)
            random_pitch = choice(possible_gliss_pitches)
            random_interval = choice(["+m2", "+M2", "+P5", "+m7", "+M7"])
            handler = evans.PitchHandler([
                [
                    abjad.NamedPitch(random_pitch).name,
                    abjad.NamedInterval(random_interval).transpose(abjad.NamedPitch(random_pitch)).name,
                ]
            ])
            temp_container = abjad.Container([replacement_tie])
            handler(temp_container)
            replacement_tie = abjad.mutate.eject_contents(temp_container)
            indicators = abjad.get.indicators(abjad.select.leaf(group, 0))
            for indicator in indicators:
                abjad.detach(indicator, abjad.select.leaf(group, 0))
                abjad.attach(indicator, abjad.select.leaf(replacement_tie, 0))
            if 1 < len(replacement_tie):
                abjad.attach(abjad.Dynamic("p"), replacement_tie[0])
                abjad.attach(abjad.StartHairpin("<"), replacement_tie[0])
                abjad.attach(abjad.Dynamic("ff"), replacement_tie[-1])
            else:
                abjad.attach(abjad.Dynamic("f"), replacement_tie[0])
            abjad.mutate.replace(group, replacement_tie)


def viola_1_run_pitches(seq=[0, 1, 2, 3, 5, 4, 3, 1]):
    pitch_segment = evans.PitchSegment(seq)
    out = pitch_segment
    out += pitch_segment.invert(1).transpose(-10)
    out += pitch_segment.alpha(1).transpose(3)
    out += pitch_segment.alpha(1).invert().transpose(5+12)
    out += pitch_segment.relative()
    out += pitch_segment.relative().invert(pitch_segment.relative()[0])
    out += pitch_segment.rotate(3).invert(2).transpose(-1)
    out += pitch_segment.rotate(5).transpose(6)
    out += pitch_segment.transpose(4)
    out += pitch_segment.transpose(2)
    out += pitch_segment
    out += pitch_segment
    out += pitch_segment
    out = evans.Sequence(out).remove_repeats()
    return out


def emergency_beam_last_run(selections, target_run=-1):
    run = abjad.select.run(selections, target_run)
    rmakers.unbeam(run)
    abjad.beam(run)

maker = evans.SegmentMaker(
    instruments=anemone.instruments,
    names=[
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
    ],
    abbreviations=[
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
        '" "',
    ],
    name_staves=False,
    fermata_measures=anemone.fermata_measures_09,
    commands=[
        ## PREAMBLE
        # evans.call(
        #     "Global Context",
        #     anemone.lib.add_time_marks,
        #     selector=lambda _: _,
        # ),
        evans.attach(
            "string 1 voice",
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 1 voice",
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##t", site="before"
            ),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 1 voice",
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 2 voice",
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 2 voice",
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##t", site="before"
            ),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 2 voice",
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 3 voice",
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 3 voice",
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##t", site="before"
            ),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "string 3 voice",
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        ## GLOBAL CONTEXT
        # evans.attach(
        #     "Global Context",
        #     abjad.Markup(r'''\markup \override #'(font-name . "Helvetica Bold") { \raise #1.5 \left-brace #1 \with-color #(rgb-color 0.6 0.6 1) A \with-color #(rgb-color 0.961 0.961 0.406) B \with-color #(rgb-color 1 0.2 0.2) D \with-color #(rgb-color 0.2 1 0.592) C \raise #1.5 \right-brace #2 }'''),
        #     selector=lambda _: abjad.select.leaf(_, 0),
        #     direction=abjad.UP
        # ),
        ## Viola 1
        evans.MusicCommand(
            ("viola 1 voice", (0, 7)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(7),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-8),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(9),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 7 for _ in [0, 1, 2, 3, 5, 4, 3, 1]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=7),
            abjad.Clef("alto"),
            lambda _: emergency_beam_last_run(_, target_run=-3),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (7, 10)),
            evans.accelerando(
                [(1, 13), (1, 6), (1, 16)],
                [(1, 7), (1, 15), (1, 16)],
                [(1, 17), (1, 8), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[2, 3], split_at_measure_boundaries=True),
            ),
            evans.PitchHandler(
                [-3, 3, -2, 2, -1, 1, 0, 4, -4, 4, -3, 4, -2, 4, -1, 3, 0, 2, 1],
                staff_positions=True,
            ),
            evans.zero_padding_glissando,
            abjad.Dynamic("f"),
            evans.ArticulationHandler(
                ["accent"],
                articulation_boolean_vector=[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["¼gr.", "->", "½gr.", "->", "¾gr.", "->", "molto gr."],
                abjad.Tweak(r"\tweak staff-padding #5.5"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [10, 10, 15], cyclic=True, overhang=True),
                lilypond_id=1,
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                [r"\trem-four-markup", "->", r"\trem-two-markup", "->", r"\trem-three-markup", "->", r"\trem-four-markup", "->", r"\trem-three-markup", "->"],
                abjad.Tweak(r"\tweak staff-padding #8"),
                lilypond_id=2,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [5, 4, 6, 3], cyclic=True, overhang=True),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (10, 14)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(16),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-17),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(18),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 7 for _ in [0, 1, 2, 3, 5, 4, 3, 1]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=7),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (14, 23)),
            evans.talea(
                evans.Sequence([4, 3, 2, 1]).random_sequence(
                    random_seed=1502265, total_length=40
                ),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
            ),
            evans.PitchHandler([17]),
            evans.zero_padding_glissando,
            abjad.Dynamic("mp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1)
            ),
            evans.ArticulationHandler(
                ["tremolo"],
                articulation_boolean_vector=evans.Sequence(
                    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                ).zipped_bifurcation(),
            ),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[4, 4, 4, 4, 4, 4],
                thickness=0.2,
                divisions=[5, 4, 6, 4],
                counts=[2+5],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", (0, 9)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(10),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-11),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(12),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 6 for _ in [0, 2, 1, 3, 4, 6, 7, 5, 4, 3, 1, 2, 1]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=11),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (9, 13)),
            evans.accelerando(
                [(1, 13), (1, 6), (1, 16)],
                [(1, 7), (1, 15), (1, 16)],
                [(1, 17), (1, 8), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[2, 3], split_at_measure_boundaries=True),
            ),
            evans.PitchHandler(
                [-3, 3, -2, 2, -1, 1, 0, 4, -4, 4, -3, 4, -2, 4, -1, 3, 0, 2, 1],
                staff_positions=True,
            ),
            evans.zero_padding_glissando,
            abjad.Dynamic("f"),
            evans.ArticulationHandler(
                ["accent"],
                articulation_boolean_vector=[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["¼gr.", "->", "½gr.", "->", "¾gr.", "->", "molto gr."],
                abjad.Tweak(r"\tweak staff-padding #5.5"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [10, 10, 11], cyclic=True, overhang=True),
                lilypond_id=1,
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                [r"\trem-four-markup", "->", r"\trem-two-markup", "->", r"\trem-three-markup", "->", r"\trem-four-markup", "->", r"\trem-three-markup", "->"],
                abjad.Tweak(r"\tweak staff-padding #8"),
                lilypond_id=2,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [5, 4, 6, 3], cyclic=True, overhang=True),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (13, 17)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(19),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-20),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(21),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 6 for _ in [0, 2, 1, 3, 4, 6, 7, 5, 4, 3, 1, 2, 1]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=11),
            emergency_beam_last_run,
        ),
        evans.MusicCommand(
            ("viola 2 voice", (17, 23)),
            evans.talea(
                evans.Sequence([4, 3, 2, 1]).random_sequence(
                    random_seed=1502264, total_length=40
                ),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
            ),
            evans.PitchHandler([16]),
            evans.zero_padding_glissando,
            abjad.Dynamic("mp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            evans.ArticulationHandler(
                ["tremolo"],
                articulation_boolean_vector=evans.Sequence(
                    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                ).zipped_bifurcation(),
            ),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[3, 4, 4, 4, 4, 4],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2+4],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 11)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(13),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-14),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(15),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 5 for _ in [3, 2, 1, 0, 1, 2, 3, 5, 4, 5, 6, 4, 2]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=13),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (11, 16)),
            evans.accelerando(
                [(1, 13), (1, 6), (1, 16)],
                [(1, 7), (1, 15), (1, 16)],
                [(1, 17), (1, 8), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[2, 3], split_at_measure_boundaries=True),
            ),
            evans.PitchHandler(
                [-3, 3, -2, 2, -1, 1, 0, 4, -4, 4, -3, 4, -2, 4, -1, 3, 0, 2, 1],
                staff_positions=True,
            ),
            evans.zero_padding_glissando,
            abjad.Dynamic("f"),
            evans.ArticulationHandler(
                ["accent"],
                articulation_boolean_vector=[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["¼gr.", "->", "½gr.", "->", "¾gr.", "->", "molto gr."],
                abjad.Tweak(r"\tweak staff-padding #5.5"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [10, 10, 11], cyclic=True, overhang=True),
                lilypond_id=1,
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                [r"\trem-four-markup", "->", r"\trem-two-markup", "->", r"\trem-three-markup", "->", r"\trem-four-markup", "->", r"\trem-three-markup", "->"],
                abjad.Tweak(r"\tweak staff-padding #8"),
                lilypond_id=2,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [5, 4, 6, 3], cyclic=True, overhang=True),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (16, 20)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(22),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-23),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(24),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 5 for _ in [3, 2, 1, 0, 1, 2, 3, 5, 4, 5, 6, 4, 2]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=13),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (20, 23)),
            evans.talea(
                evans.Sequence([4, 3, 2, 1]).random_sequence(
                    random_seed=1502263, total_length=40
                ),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
            ),
            evans.PitchHandler([15]),
            evans.zero_padding_glissando,
            abjad.Dynamic("mp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1)
            ),
            evans.ArticulationHandler(
                ["tremolo"],
                articulation_boolean_vector=evans.Sequence(
                    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                ).zipped_bifurcation(),
            ),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[3, 2, 3, 4, 3, 4],
                thickness=0.2,
                divisions=[6, 4, 5, 4],
                counts=[2+3],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        ####
        evans.call(
            "score",
            lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
            lambda _: abjad.select.components(_, abjad.Score),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_80,
            lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_80,
            lambda _: abjad.select.leaf(_, 0),
        ),
        evans.call(
            "Global Context",
            evans.hide_duplicate_time_signatures,
            lambda _: _,
        ),
        ####
        # evans.attach(
        #     "Global Context",
        #     abjad.LilyPondLiteral(r"\once \set Timing.beatStructure = 3,1", site="before"),
        #     selector=lambda _: abjad.select.leaf(_, 37)
        # ),
        # evans.attach(
        #     "Global Context",
        #     abjad.LilyPondLiteral(r"\once \set Timing.beatStructure = 3", site="before"),
        #     selector=lambda _: abjad.select.leaf(_, 38)
        # ),
        # evans.call(
        #     "score",
        #     evans.decorate_artificial_harmonic_chords,
        #     selector=lambda _: _,
        # ),
        ####
        # evans.attach(
        #     "cello voice",
        #     abjad.Markup(r"\colophon"),
        #     lambda _: abjad.select.leaf(_, -3),
        #     direction=abjad.DOWN,
        # ),
        # evans.attach(
        #     "Global Context",
        #     abjad.BarLine("|."),
        #     evans.select_measures([122], leaf=1),
        # ),
        ###
        ###
        ###
        # evans.attach(
        #     "Global Context",
        #     abjad.Markup(
        #         r'\markup \lower #9 \with-dimensions-from \null \musicglyph #"scripts.ulongfermata"',
        #     ),
        #     evans.select_measures([2], leaf=1),
        #     direction=abjad.UP,
        # ),
        # evans.attach(
        #     "Global Context",
        #     abjad.Markup(
        #         r'\markup \lower #9 \with-dimensions-from \null \musicglyph #"scripts.ufermata"',
        #     ),
        #     evans.select_measures([7], leaf=1),
        #     direction=abjad.UP,
        # ),
    ],
    score_template=anemone.score,
    transpose_from_sounding_pitch=False,
    time_signatures=anemone.signatures_09,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="09",
    current_directory=pathlib.Path(__file__).parent,
    cutaway=False,
    beam_pattern="meter",
    beam_rests=True,
    barline="||",
    rehearsal_mark="",
    fermata="scripts.ufermata",
    with_layout=True,
    mm_rests=False,
    extra_rewrite=False,  # should default to false but defaults to true
    print_clock_time=True,
    color_out_of_range=False,
)

maker.build_segment()
