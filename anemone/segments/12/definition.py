import pathlib
from fractions import Fraction
from random import choice, seed

import abjad
import baca
import evans
from abjadext import rmakers

import anemone


def stabs(selections, pattern, dynamic):
    targets = abjad.select.get(abjad.select.logical_ties(selections), pattern)
    for target in targets:
        evans.ArticulationHandler(["tremolo"])(target)
        evans.vibrato_spanner(
            peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
            wavelengths=[3],
            thickness=0.2,
            divisions=[6],
            counts=[1],
            cyclic=True,
            padding=4.5,
            forget=False,
        )(target)
        abjad.attach(abjad.Articulation('accent'), target[0])
        abjad.attach(abjad.Dynamic(dynamic), target[0])
        abjad.attach(abjad.Dynamic("p"), abjad.get.leaf(target[-1], 1))

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
    fermata_measures=anemone.fermata_measures_12,
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
            ("viola 1 voice", [0]),
            evans.tuplet(
                [(1, 1, 1)],
            ),
            evans.PitchHandler(["aqs", "b'", "b'", "b'"]),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            evans.Attachment(
                abjad.StartHairpin(">"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.note(_, 2),
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\highest", site="before"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            abjad.glissando,
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [1, 2, 3, 4]),
            evans.talea(
                evans.Sequence([4, 3, 4, 5, 3, 6, 5]).rotate(0),
                8,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(["b'"]),
            lambda _: stabs(_, abjad.index([2, 6], 8), "mf")
        ),
        evans.MusicCommand(
            ("viola 1 voice", [5, 6]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([-4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4]).zipped_bifurcation(),
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(10).random_walk(random_seed=0, length=700, step_list=[2, 2, 2, 1, 2, 2]).remove_repeats()
            ),
            abjad.LilyPondLiteral(r"\revert-noteheads", site="before"),
            evans.slur([3, 3, 4, 6, 5, 7, 5, 9, 10, 6, 3, 8, 3, 6]),
            evans.hairpin("f > mp < ff > pp < f |> p < ff |> mf < f > p <", [3, 3, 4, 5, 4, 3, 11, 7, 14, 6, 4, 8, 5]),
            lambda _: baca.text_spanner(
                _,
                ["P", "->", "T", "->", "N", "->", "P", "->", "N", "->"],
                abjad.Tweak(r"\tweak staff-padding #6.5"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [7, 11, 5], cyclic=True, overhang=True),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (7, 11)),
            evans.even_division(
                [32],
                preprocessor=evans.make_preprocessor(
                    eighths=True,
                    fuse_counts=[2, 4, 5, 5, 4, 3, 5, 4, 6, 6, 5, 6, 6, 6, 6, 3, 1, 1, 5, 6, 6, 6, 6, 5, 6, 4, 5, 2, 6, 6, 5, 3, 5, 4, 5, 1, 4, 5, 5, 6, 6],
                ),
                rewrite=-2,
                beam_meter=True,
            ),
            evans.loop(
                [-11, -11+8, -11+8+8, -11+8+8+8, -11+8+8+8, -11+8+8, -11+8, -11],
                [0, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]
            ),
            evans.ArticulationHandler(["staccato"]),
            evans.ArticulationHandler(["accent"], articulation_boolean_vector=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]),
            evans.slur([4]),
            abjad.LilyPondLiteral(r"\harmonicsOn", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            evans.text_span(
                [
                    r"\diamond-notehead-markup",
                    r"\default-notehead-markup",
                ],
                "->",
                padding=6,
                id=1,
                # font="Helvetica Bold"
            ),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", [0]),
            evans.tuplet(
                [(1, 1, 1)],
            ),
            evans.PitchHandler(["eqf", "b'", "b'", "b'"]),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            evans.Attachment(
                abjad.StartHairpin(">"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.note(_, 2),
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\highest", site="before"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            abjad.glissando,
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [1, 2, 3, 4, 5]),
            evans.talea(
                evans.Sequence([4, 3, 4, 5, 3, 6, 5]).rotate(1),
                8,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(["b'"]),
            lambda _: stabs(_, abjad.index([-2, -6], 8), "mf")
        ),
        evans.MusicCommand(
            ("viola 2 voice", [6, 7, 8]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([-4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4]).zipped_bifurcation().rotate(-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(11).random_walk(random_seed=1, length=700, step_list=[2, 2, 2, 1, 2, 2]).remove_repeats()
            ),
            abjad.LilyPondLiteral(r"\revert-noteheads", site="before"),
            evans.slur([3, 3, 4, 6, 5, 7, 5, 9, 10, 6, 3, 8, 3, 6]),
            evans.hairpin("f > mp < ff > pp < f |> p < ff |> mf < f > p <", [3, 3, 4, 5, 4, 3, 11, 7, 14, 6, 4, 8, 5]),
            lambda _: baca.text_spanner(
                _,
                ["P", "->", "T", "->", "N", "->", "P", "->", "N", "->"],
                abjad.Tweak(r"\tweak staff-padding #6.5"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [7, 11, 5], cyclic=True, overhang=True),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (9, 11)),
            evans.even_division(
                [32],
                preprocessor=evans.make_preprocessor(
                    eighths=True,
                    fuse_counts=[2, 4, 5, 5, 4, 3, 5, 4, 6, 6, 5, 6, 6, 6, 6, 3, 1, 1, 5, 6, 6, 6, 6, 5, 6, 4, 5, 2, 6, 6, 5, 3, 5, 4, 5, 1, 4, 5, 5, 6, 6],
                ),
                rewrite=-2,
                beam_meter=True,
            ),
            evans.loop(
                [-11, -11+8, -11+8+8, -11+8+8+8, -11+8+8+8, -11+8+8, -11+8, -11],
                [0, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]
            ),
            evans.ArticulationHandler(["staccato"]),
            evans.ArticulationHandler(["accent"], articulation_boolean_vector=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]),
            evans.slur([4]),
            abjad.LilyPondLiteral(r"\harmonicsOn", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            evans.text_span(
                [
                    r"\diamond-notehead-markup",
                    r"\default-notehead-markup",
                ],
                "->",
                padding=6,
                id=1,
                # font="Helvetica Bold"
            ),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", [0]),
            evans.tuplet(
                [(1, 1, 1)],
            ),
            evans.PitchHandler(["eqs", "b'", "b'", "b'"]),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            evans.Attachment(
                abjad.StartHairpin(">"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.note(_, 2),
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\highest", site="before"),
                selector=lambda _: abjad.select.note(_, 1),
            ),
            abjad.glissando,
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [1, 2, 3, 4, 5, 6]),
            evans.talea(
                evans.Sequence([4, 3, 4, 5, 3, 6, 5]).rotate(-1),
                8,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(["b'"]),
            lambda _: stabs(_, abjad.index([3, 7], 8), "mf")
        ),
        evans.MusicCommand(
            ("viola 3 voice", [7, 8]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([-4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4]).zipped_bifurcation().rotate(1),
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(12).random_walk(random_seed=2, length=700, step_list=[2, 2, 2, 1, 2, 2]).remove_repeats()
            ),
            abjad.LilyPondLiteral(r"\revert-noteheads", site="before"),
            evans.slur([3, 3, 4, 6, 5, 7, 5, 9, 10, 6, 3, 8, 3, 6]),
            evans.hairpin("f > mp < ff > pp < f |> p < ff |> mf < f > p <", [3, 3, 4, 5, 4, 3, 11, 7, 14, 6, 4, 8, 5]),
            lambda _: baca.text_spanner(
                _,
                ["P", "->", "T", "->", "N", "->", "P", "->", "N", "->"],
                abjad.Tweak(r"\tweak staff-padding #6.5"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [7, 11, 5], cyclic=True, overhang=True),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (9, 11)),
            evans.talea(
                evans.Sequence([4, 3, 4, 5, 3, 6, 5]).rotate(-1),
                8,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(["b'"]),
            lambda _: stabs(_, abjad.index([1, 5, 6], 8), "ff"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\highest", site="before"),
                selector=lambda _: abjad.select.note(_, 0),
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\revert-noteheads", site="after"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        ####
        # evans.call(
        #     "score",
        #     lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
        #     lambda _: abjad.select.components(_, abjad.Score),
        # ),
        # evans.attach(
        #     "Global Context",
        #     anemone.lib.mark_80,
        #     lambda _: abjad.select.leaf(_, 0),
        # ),
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
    time_signatures=anemone.signatures_12,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="12",
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
