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
    fermata_measures=anemone.fermata_measures_07,
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
            ("viola 1 voice", (0, 3)),
            evans.talea(
                [6, 3, 6, 4, 2, 8],
                8,
            ),
            evans.PitchHandler([4, -1, 4, -1, 5, 3, 4, -3]),
            abjad.Clef("alto"),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in [[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (3, 7)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
            ),
            evans.PitchHandler(
                evans.Sequence([-3, 3, -2, 2, -1, 1, 0, 4, -4, 4, -3, 4, -2, 4, -1, 3, 0, 2, 1]).derive_intervals([1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2]),
                staff_positions=True,
            ),
            evans.zero_padding_glissando,
            lambda _: [
                abjad.attach(
                    abjad.LilyPondLiteral(r"\scrape-circular-clockwise", site="after"),
                    x[0],
                )
                for x in abjad.select.logical_ties(_, pitched=True)
            ],
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1, pitched=True),
            ),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", (0, 4)),
            evans.talea(
                [6, 3, 6, 4, 2, 8],
                8,
            ),
            evans.PitchHandler(evans.PitchSegment([4, -1, 4, -1, 5, 3, 4, -3]).hexpole().transpose(-7)),
            abjad.Clef("alto"),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).hexpole().transpose(-7).to_intervals() for _ in [[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (4, 7)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
            ),
            evans.PitchHandler(
                evans.Sequence([-3, 3, -2, 2, -1, 1, 0, 4, -4, 4, -3, 4, -2, 4, -1, 3, 0, 2, 1]).derive_intervals([1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2]),
                staff_positions=True,
            ),
            evans.zero_padding_glissando,
            lambda _: [
                abjad.attach(
                    abjad.LilyPondLiteral(r"\scrape-circular-clockwise", site="after"),
                    x[0],
                )
                for x in abjad.select.logical_ties(_, pitched=True)
            ],
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1, pitched=True),
            ),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 5)),
            evans.talea(
                [6, 3, 6, 4, 2, 8],
                8,
            ),
            evans.PitchHandler(evans.PitchSegment([4, -1, 4, -1, 5, 3, 4, -3]).hexpole().alpha(1).invert(0).transpose(7)),
            abjad.StopTrillSpan(),
            abjad.Clef("alto"),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).hexpole().alpha(1).invert(0).transpose(7).to_intervals() for _ in [[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (5, 7)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
                preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            ),
            evans.PitchHandler(
                evans.Sequence([-3, 3, -2, 2, -1, 1, 0, 4, -4, 4, -3, 4, -2, 4, -1, 3, 0, 2, 1]).derive_intervals([1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2]),
                staff_positions=True,
            ),
            evans.zero_padding_glissando,
            lambda _: [
                abjad.attach(
                    abjad.LilyPondLiteral(r"\scrape-circular-clockwise", site="after"),
                    x[0],
                )
                for x in abjad.select.logical_ties(_, pitched=True)
            ],
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1, pitched=True),
            ),
        ),
        ####
        # evans.call(
        #     "score",
        #     lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
        #     lambda _: abjad.select.components(_, abjad.Score),
        # ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_67,
            lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_67,
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
    time_signatures=anemone.signatures_07,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="07",
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
    global_barline_only=True,
)

maker.build_segment()
