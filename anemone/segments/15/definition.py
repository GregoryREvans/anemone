import pathlib
from fractions import Fraction
from random import choice, seed

import abjad
import baca
import evans
from abjadext import rmakers

import anemone


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
    fermata_measures=anemone.fermata_measures_15,
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
            evans.talea(
                evans.Sequence([3, 2, 5, 4, 6, 1, 2]).rotate(0),
                4,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(9).random_walk(random_seed=5, length=90, step_list=[2, 2, 2, 1, 2, 2]).remove_repeats().stutter(counts=[2, 3], indices=[0, 1], period=1, cyclic=False)
            ),
            abjad.iterpitches.respell_with_sharps,
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("mf"),
                selector=lambda _: abjad.select.logical_tie(_, len(abjad.select.logical_ties(_))//2)[0]
            ),
            evans.Attachment(
                abjad.StartHairpin(">"),
                selector=lambda _: abjad.select.logical_tie(_, len(abjad.select.logical_ties(_))//2)[0]
            ),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            lambda _: baca.text_spanner(
                _,
                ["P", "->", "T", "->", "XP", "->",],
                abjad.Tweak(r"\tweak staff-padding #2"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [7, 11, 5], cyclic=True, overhang=True),
            ),
            abjad.Clef("alto"),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", (0, 7)),
            evans.talea(
                evans.Sequence([3, 2, 5, 4, 6, 1, 2]).rotate(-3),
                4,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(8).random_walk(random_seed=7, length=90, step_list=[2, 2, 2, 1, 2, 2]).remove_repeats().stutter(counts=[2, 2], indices=[0, 1], period=1, cyclic=False)
            ),
            abjad.iterpitches.respell_with_sharps,
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("mf"),
                selector=lambda _: abjad.select.logical_tie(_, len(abjad.select.logical_ties(_))//2)[0]
            ),
            evans.Attachment(
                abjad.StartHairpin(">"),
                selector=lambda _: abjad.select.logical_tie(_, len(abjad.select.logical_ties(_))//2)[0]
            ),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            lambda _: baca.text_spanner(
                _,
                ["P", "->", "T", "->", "XP", "->",],
                abjad.Tweak(r"\tweak staff-padding #2"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [7, 11, 5], cyclic=True, overhang=True),
            ),
            abjad.Clef("alto"),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 7)),
            evans.talea(
                evans.Sequence([3, 2, 5, 4, 6, 1, 2]).rotate(3),
                4,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(
                evans.Sequence.range(-12, 24, 0.5).mirror(sequential_duplicates=False).rotate(7).random_walk(random_seed=6, length=90, step_list=[2, 2, 2, 1, 2, 2]).remove_repeats().stutter(counts=[3, 2], indices=[0, 1], period=1, cyclic=False)
            ),
            abjad.iterpitches.respell_with_sharps,
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("mf"),
                selector=lambda _: abjad.select.logical_tie(_, len(abjad.select.logical_ties(_))//2)[0]
            ),
            evans.Attachment(
                abjad.StartHairpin(">"),
                selector=lambda _: abjad.select.logical_tie(_, len(abjad.select.logical_ties(_))//2)[0]
            ),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            lambda _: baca.text_spanner(
                _,
                ["P", "->", "T", "->", "XP", "->",],
                abjad.Tweak(r"\tweak staff-padding #2"),
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [7, 11, 5], cyclic=True, overhang=True),
            ),
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
            anemone.lib.mark_120,
            lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_120,
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
    time_signatures=anemone.signatures_15,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="15",
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
