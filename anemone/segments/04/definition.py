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
    cyc_swell_peaks = evans.CyclicList(["p", "p", "mp", "mp", "mf", "mf", "f", "f", "ff", "ff", "fff", "fff"], forget=False)
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
    possible_gliss_pitches = [step - 6 for step in range(23)]
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
            replacement_leaves = evans.tuplet([(4, 1)])([group_duration])
            abjad.attach(abjad.Glissando(), abjad.select.leaf(replacement_leaves, 0))
            indicators = abjad.get.indicators(abjad.select.leaf(group, 0))
            for indicator in indicators:
                abjad.detach(indicator, abjad.select.leaf(group, 0))
                abjad.attach(indicator, abjad.select.leaf(replacement_leaves, 0))
            seed(i*glissando_seed_modifier%30)
            start_pitch = choice(possible_gliss_pitches)
            stop_pitch = choice(possible_gliss_pitches)
            while stop_pitch == start_pitch:
                stop_pitch = choice(possible_gliss_pitches)
            handler = evans.PitchHandler([[abjad.NamedPitch(start_pitch).name, abjad.NamedInterval("+P4").transpose(abjad.NamedPitch(start_pitch)).name], [abjad.NamedPitch(stop_pitch).name, abjad.NamedInterval("+P4").transpose(abjad.NamedPitch(stop_pitch)).name]])
            handler(replacement_leaves)
            for chord in abjad.select.leaves(replacement_leaves):
                abjad.tweak(chord.note_heads[1], r"\tweak style #'harmonic")
            if i % 4 != 0:
                evans.ArticulationHandler(["tremolo"])(replacement_leaves)
                abjad.attach(abjad.Dynamic("sfp"), abjad.select.leaf(replacement_leaves, 0))
                abjad.attach(abjad.StartHairpin("<|"), abjad.select.leaf(replacement_leaves, 0))
                abjad.attach(abjad.Dynamic("ff"), abjad.select.leaf(replacement_leaves, -1))
            else:
                abjad.attach(abjad.Dynamic("mf"), abjad.select.leaf(replacement_leaves, 0))
                abjad.attach(abjad.StartHairpin(">"), abjad.select.leaf(replacement_leaves, 0))
                abjad.attach(abjad.Dynamic("p"), abjad.select.leaf(replacement_leaves, -1))
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
    fermata_measures=anemone.fermata_measures_04,
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
        evans.attach(
            "viola 1 voice",
            abjad.Clef("alto"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "viola 2 voice",
            abjad.Clef("alto"),
            selector=lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "viola 3 voice",
            abjad.Clef("alto"),
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
        ########## HARMONIC TRILLS AND GLISSANDI AND STUFF!!!!
        evans.MusicCommand(
            ("viola 1 voice", (0, 10)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(0),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(0),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(0),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 7 for _ in [0, 1, 2, 3, 5, 4, 3, 1]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=2),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", (0, 10)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(1),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-2),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(3),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 6 for _ in [0, 2, 1, 3, 4, 6, 7, 5, 4, 3, 1, 2, 1]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=3),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 10)),
            evans.even_division(
                evans.Sequence([32, 32, 16, 32, 16, 16, 16, 8, 16, 16]).rotate(4),
                extra_counts=evans.Sequence([0, 1, 0, 2, 1, 3, 2, 4]).zipped_bifurcation().rotate(-5),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 2, 5, 8], 9))],
                    rests_in_runs,
                ],
                preprocessor=evans.make_preprocessor(
                    quarters=True,
                    fuse_counts=evans.Sequence([1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1]).rotate(6),
                    split_at_measure_boundaries=True,
                ),
                # beam_meter=True,
            ),
            evans.PitchHandler(viola_1_run_pitches([_ - 5 for _ in [3, 2, 1, 0, 1, 2, 3, 5, 4, 5, 6, 4, 2]])),
            lambda _: [abjad.slur(x) for x in abjad.select.runs(_) if 1 < len(x)],
            lambda _: trill_runs(_, intervals=["+P4", "+P5", "+M3", "+P4", "+M2", "+P4", "+m3"]),
            conditional_swells,
            lambda _: replace_alternating_rests_with_glissandi(_, glissando_seed_modifier=5),
        ),
        ####
        evans.call(
            "score",
            lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
            lambda _: abjad.select.components(_, abjad.Score),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_91,
            lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_91,
            lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_79,
            selector=lambda _: abjad.select.leaf(_, 7)
        ),
        evans.attach(
            "Global Context",
            abjad.Markup(r"""\markup {\translate #'(-2 . 1.5) \tiny \bold "rall."}"""),
            selector=lambda _: abjad.select.leaf(_, 7),
            direction=abjad.UP,
        ),
        evans.attach(
            "Global Context",
            abjad.LilyPondLiteral(r"\rallArrow #3", site="after"),
            selector=lambda _: abjad.select.leaf(_, 7),
        ),
        evans.attach(
            "Global Context",
            abjad.StopTextSpan(),
            selector=lambda _: abjad.select.leaf(_, 9)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_67_small,
            selector=lambda _: abjad.select.leaf(_, 9)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_67,
            selector=lambda _: abjad.select.leaf(_, 9)
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
        ###
        ###
        ###
    ],
    score_template=anemone.score,
    transpose_from_sounding_pitch=False,
    time_signatures=anemone.signatures_04,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="04",
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
