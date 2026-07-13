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
    fermata_measures=anemone.fermata_measures_10,
    commands=[
        ## PREAMBLE
        # evans.call(
        #     "Global Context",
        #     anemone.lib.add_time_marks,
        #     selector=lambda _: _,
        # ),
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
        evans.MusicCommand(
            ("string 1 voice", (0, 8)),
            evans.talea([1, 1, 1, 3, 7, 4, 6, 5, 1, 1, 1, 1, 8, 2, 7, 3, 6, 4, 5, 1, 1, 1, 9, 10], 16),
            evans.PitchHandler([-6, 6, -6, -5, -4, -1, 0, 4, 6, -6, 6, -6, 6, 5, 6, 4, 5, 4, 5, 6, -6, 6, 5, 4], staff_positions=True),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.Dots.transparent = ##t", site="before"
            ),
            evans.zero_padding_glissando,
        ),
        evans.MusicCommand(
            ("viola 1 voice", (0, 8)),
            evans.talea(
                evans.Sequence([4, 1, 5, 1, 1, 2, 3, 1, 6, 1, 1, 1, 1, 4, 1, 1, 1]).rotate(0),
                8,
            ),
            evans.PitchHandler(evans.Sequence.range(-9, 21, 0.5).mirror(sequential_duplicates=False).rotate(5).random_walk(200, [1], 0)),
            abjad.glissando,
            evans.ArticulationHandler(["accent"], articulation_boolean_vector=[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0]),
            abjad.Dynamic("pp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StopTrillSpan(),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("string 2 voice", (0, 8)),
            evans.talea([8, 10, 1, 1, 1, 3, 7, 4, 6, 5, 1, 1, 1, 1, 8, 2, 7, 3, 6, 4, 5, 1, 1, 1], 16),
            evans.PitchHandler([5, 4, -6, 6, -6, 5, 4, 6, 5, 7, 6, -6, 6, -6, 6, 4, 5, 4, 3, 6, 7, 6, -6, 6], staff_positions=True),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.Dots.transparent = ##t", site="before"
            ),
            evans.zero_padding_glissando,
        ),
        evans.MusicCommand(
            ("viola 2 voice", (0, 8)),
            evans.talea(
                evans.Sequence([4, 1, 5, 1, 1, 2, 3, 1, 6, 1, 1, 1, 1, 4, 1, 1, 1]).rotate(-1),
                8,
            ),
            evans.PitchHandler(evans.Sequence.range(-9, 21, 0.5).mirror(sequential_duplicates=False).rotate(7).random_walk(200, [1], 1)),
            abjad.glissando,
            evans.ArticulationHandler(["accent"], articulation_boolean_vector=[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0]),
            abjad.Dynamic("pp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StopTrillSpan(),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("string 3 voice", (0, 8)),
            evans.talea(evans.Sequence([8, 10, 1, 1, 1, 3, 7, 4, 6, 5, 1, 1, 1, 1, 8, 2, 7, 3, 6, 4, 5, 1, 1, 1]).reverse(), 16),
            evans.PitchHandler([int(_) for _ in evans.PitchSegment([5, 4, -6, 6, -6, 5, 4, 6, 5, 7, 6, -6, 6, -6, 6, 4, 5, 4, 3, 6, 7, 6, -6, 6]).transpose(1).retrograde()], staff_positions=True),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.Dots.transparent = ##t", site="before"
            ),
            evans.zero_padding_glissando,
        ),
        evans.MusicCommand(
            ("viola 3 voice", (0, 8)),
            evans.talea(
                evans.Sequence([4, 1, 5, 1, 1, 2, 3, 1, 6, 1, 1, 1, 1, 4, 1, 1, 1]).rotate(-2),
                8,
            ),
            evans.PitchHandler(evans.Sequence.range(-9, 21, 0.5).mirror(sequential_duplicates=False).rotate(3).random_walk(200, [1], 2)),
            abjad.glissando,
            evans.ArticulationHandler(["accent"], articulation_boolean_vector=[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0]),
            abjad.Dynamic("pp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StopTrillSpan(),
        ),
        ####
        evans.call(
            "score",
            lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
            lambda _: abjad.select.components(_, abjad.Score),
        ),
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
    time_signatures=anemone.signatures_10,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="10",
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
