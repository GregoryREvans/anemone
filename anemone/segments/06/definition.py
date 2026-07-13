import pathlib
from fractions import Fraction
from random import choice, seed

import abjad
import baca
import evans
from abjadext import rmakers

import anemone


def occasional_trill(selections):
    ties = abjad.select.logical_ties(selections)
    gotten_ties = abjad.select.get(ties, abjad.index([5, 11, 13, 17, 18], 20))
    for tie in gotten_ties:
        tie_and_terminator = [tie, abjad.get.leaf(tie[-1], 1)]
        baca.trill_spanner(tie_and_terminator, alteration=abjad.NamedInterval("+P1"), harmonic=True)

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
    fermata_measures=anemone.fermata_measures_06,
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
            ("viola 1 voice", (0, 9)),
            evans.talea(
                evans.Sequence([8, 6, 9, 10, 12, 11, 14, 9]).rotate(0),
                16,
                extra_counts=evans.Sequence([0, 1, 0, 1, 2, 1, 2, 3, 0, 2]).rotate(0),
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                rewrite=-2,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(5).random_walk(length=100, random_seed=70120261, step_list=[1, 1, 1, 1, 2, 2, 2, 3, 3, 4]).stutter(counts=[5], indices=[0], cyclic=False)
            ),
            lambda _: anemone.swells(_, group_size=3, dyns=["p", "mf", "p", "f"]),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["N", "->", "P", "->", "N", "->", "½P", "->", "T", "->", "XP", "->", "N", "->", "P", "->", "½T", "->"],
                abjad.Tweak(r"\tweak staff-padding #5.5"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [2, 1, 3], cyclic=True, overhang=True),
            ),
            occasional_trill,
            lambda _: evans.ArticulationHandler(["accent"])(abjad.select.get(abjad.select.logical_ties(_), abjad.index([_ for _ in range(6)]))),
            abjad.Clef("alto"),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", (0, 9)),
            evans.talea(
                evans.Sequence([8, 6, 9, 10, 12, 11, 14, 9]).rotate(1),
                16,
                extra_counts=evans.Sequence([0, 1, 0, 1, 2, 1, 2, 3, 0, 2]).rotate(-2),
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                rewrite=-2,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(4).random_walk(length=100, random_seed=70120262, step_list=[1, 1, 1, 1, 2, 2, 2, 3, 3, 4]).stutter(counts=[7], indices=[0], cyclic=False)
            ),
            lambda _: anemone.swells(_, group_size=4, dyns=["mp", "mf", "p", "f", "pp", "mf"]),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["N", "->", "P", "->", "N", "->", "½P", "->", "T", "->", "XP", "->", "N", "->", "P", "->", "½T", "->"],
                abjad.Tweak(r"\tweak staff-padding #5.5"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [2, 1, 3], cyclic=True, overhang=True),
            ),
            occasional_trill,
            lambda _: evans.ArticulationHandler(["accent"])(abjad.select.get(abjad.select.logical_ties(_), abjad.index([_ for _ in range(8)]))),
            abjad.Clef("alto"),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 9)),
            evans.talea(
                evans.Sequence([8, 6, 9, 10, 12, 11, 14, 9]).rotate(2),
                16,
                extra_counts=evans.Sequence([0, 1, 0, 1, 2, 1, 2, 3, 0, 2]).rotate(-4),
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                rewrite=-2,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(3).random_walk(length=100, random_seed=70120263, step_list=[1, 1, 1, 1, 2, 2, 2, 3, 3, 4]).stutter(counts=[8], indices=[0], cyclic=False)
            ),
            lambda _: anemone.swells(_, group_size=2, dyns=["mp", "mf", "p", "f", "pp", "mf", "p", "mf"]),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["N", "->", "P", "->", "N", "->", "½P", "->", "T", "->", "XP", "->", "N", "->", "P", "->", "½T", "->"],
                abjad.Tweak(r"\tweak staff-padding #5.5"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [2, 1, 3], cyclic=True, overhang=True),
            ),
            occasional_trill,
            lambda _: evans.ArticulationHandler(["accent"])(abjad.select.get(abjad.select.logical_ties(_), abjad.index([_ for _ in range(9)]))),
            abjad.Clef("alto"),
        ),
        ####
        # evans.call(
        #     "score",
        #     lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
        #     lambda _: abjad.select.components(_, abjad.Score),
        # ),
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
    time_signatures=anemone.signatures_06,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="06",
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
