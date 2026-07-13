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
    fermata_measures=anemone.fermata_measures_18,
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
            ("viola 1 voice", (0, 8)),
            evans.talea(
                evans.Sequence([[3, 3], [3], [3, 3, 3], [3], [3, 1], [3], [1, 3]]).rotate(-2).flatten(depth=-1).multiply(4),
                16,
                extra_counts=[0, 1, 0, 0, 1],
                end_counts=[1],
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
            ),
            evans.PitchHandler(
                ["af", "aqf", "af", "atqf"],
            ),
            abjad.glissando,
            evans.ArticulationHandler(
                ["tremolo"],
                articulation_boolean_vector=[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            ),
            abjad.Dynamic("mp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["XP", "->", "MSP", "->", "P", "->", "N", "->", "½T", "->", "N", "->", "½P", "->", "P", "->", "MSP", "->", "XP", "->"],
                abjad.Tweak(r"\tweak staff-padding #4"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [3, 2, 4], cyclic=True, overhang=True),
            ),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", 8),
            evans.note(),
            evans.PitchHandler(["atqf"]),
            evans.Attachment(
                abjad.Dynamic("fff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", (0, 8)),
            evans.talea(
                evans.Sequence([[3, 3], [3], [3, 3, 3], [3], [3, 1], [3], [1, 3]]).rotate(-1).flatten(depth=-1).multiply(2),
                8,
                extra_counts=[0, 1, 0, 0, 1],
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
            ),
            evans.PitchHandler(
                ["g", "gqs", "g", "gqs", "gs", "gtqs", "gs"],
            ),
            abjad.glissando,
            evans.ArticulationHandler(
                ["tremolo"],
                articulation_boolean_vector=[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            ),
            abjad.Dynamic("mp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["XP", "->", "MSP", "->", "P", "->", "N", "->", "½T", "->", "N", "->", "½P", "->", "P", "->", "MSP", "->", "XP", "->"],
                abjad.Tweak(r"\tweak staff-padding #4"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [3, 2, 4], cyclic=True, overhang=True),
            ),
            abjad.Clef("alto"),
            abjad.StopTrillSpan(),
        ),
        evans.MusicCommand(
            ("viola 2 voice", 8),
            evans.note(),
            evans.PitchHandler(["g"]),
            evans.Attachment(
                abjad.Dynamic("fff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 8)),
            evans.talea(
                evans.Sequence([[3, 3], [3], [3, 3, 3], [3], [3, 1], [3], [1, 3]]).rotate(0).flatten(depth=-1).multiply(1),
                4,
                extra_counts=[0],
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
            ),
            evans.PitchHandler(
                ["fs", "ftqs", "g", "gqs", "g", "ftqs", "fs", "fqs"],
            ),
            abjad.glissando,
            evans.ArticulationHandler(
                ["tremolo"],
                articulation_boolean_vector=[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            ),
            abjad.Dynamic("mp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["XP", "->", "MSP", "->", "P", "->", "N", "->", "½T", "->", "N", "->", "½P", "->", "P", "->", "MSP", "->", "XP", "->"],
                abjad.Tweak(r"\tweak staff-padding #4"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [3, 2, 4], cyclic=True, overhang=True),
            ),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", 8),
            evans.note(),
            evans.PitchHandler(["ftqs"]),
            evans.Attachment(
                abjad.Dynamic("fff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        ####
        evans.call(
            "score",
            lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
            lambda _: abjad.select.components(_, abjad.Score),
        ),
        # evans.attach(
        #     "Global Context",
        #     anemone.lib.mark_120,
        #     lambda _: abjad.select.leaf(_, 0),
        # ),
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
        evans.attach(
            "viola 3 voice",
            abjad.Markup(r"\colophon"),
            lambda _: abjad.select.leaf(_, -3),
            direction=abjad.DOWN,
        ),
        evans.attach(
            "Global Context",
            abjad.BarLine("|."),
            evans.select_measures([9], leaf=1),
        ),
        evans.attach(
            "Global Context",
            abjad.Markup(
                r'\markup \lower #9 \with-dimensions-from \null \musicglyph #"scripts.uverylongfermata"',
            ),
            evans.select_measures([9], leaf=1),
            direction=abjad.UP,
        ),
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
    time_signatures=anemone.signatures_18,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="18",
    current_directory=pathlib.Path(__file__).parent,
    cutaway=False,
    beam_pattern="meter",
    beam_rests=True,
    barline="|.",
    rehearsal_mark="",
    fermata="scripts.ufermata",
    with_layout=True,
    mm_rests=False,
    extra_rewrite=False,  # should default to false but defaults to true
    print_clock_time=True,
    color_out_of_range=False,
)

maker.build_segment()
