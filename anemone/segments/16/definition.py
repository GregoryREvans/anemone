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
    fermata_measures=anemone.fermata_measures_16,
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
            ("change 1 voice", [0, 1]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                anemone.pitch.string_crossing_modules(first_state=1, random_seed=0, length=600),
                staff_positions=True,
            ),
            evans.slur(
                anemone.pitch.string_crossing_modules(
                    first_state=1, random_seed=0, length=600, return_lengths_only=True
                )
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [0, 1]),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(0).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(0)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+9, -4+9+9, -4+9+9+9],
                    -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                ]
            ),
            evans.zero_padding_glissando,
            abjad.LilyPondLiteral(
                r"\override Dots.extra-offset = #'(0 . 0.75)",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    r"\revert Dots.stencil.extra-offset",
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.Clef("alto"),
            abjad.Dynamic("mp"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [2, 3]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([0, 1, 2, 3, 2, 1]).rotate(0),
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(
                        abjad.select.get(abjad.select.leaves(_), [0, 1, 2])
                    ),
                ],
            ),
            evans.loop(
                [-10],
                [
                    1,
                ],
            ),
            lambda _: evans.upward_gliss(_, zero_padding=False),
            evans.ArticulationHandler(["staccato"], forget=False),
            abjad.Dynamic("fff"),
            abjad.StartHairpin(">"),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("change 1 voice", [4, 5]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                anemone.pitch.string_crossing_modules(first_state=2, random_seed=1, length=600),
                staff_positions=True,
            ),
            evans.slur(
                anemone.pitch.string_crossing_modules(
                    first_state=2, random_seed=1, length=600, return_lengths_only=True
                )
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [4, 5]),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(-1).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-2)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+9, -4+9+9, -4+9+9+9],
                    -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                ]
            ),
            evans.zero_padding_glissando,
            abjad.LilyPondLiteral(
                r"\override Dots.extra-offset = #'(0 . 0.75)",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    r"\revert Dots.stencil.extra-offset",
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.Dynamic("f"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [6, 7]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([0, 1, 2, 3, 2, 1]).rotate(1),
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(
                        abjad.select.get(abjad.select.leaves(_), [0, 1, 2])
                    ),
                ],
            ),
            evans.loop(
                [-9],
                [
                    1,
                ],
            ),
            lambda _: evans.upward_gliss(_, zero_padding=False),
            evans.ArticulationHandler(["staccato"], forget=False),
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("fff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("change 2 voice", [0, 1, 2]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                anemone.pitch.string_crossing_modules(first_state=3, random_seed=2, length=600),
                staff_positions=True,
            ),
            evans.slur(
                anemone.pitch.string_crossing_modules(
                    first_state=3, random_seed=2, length=600, return_lengths_only=True
                )
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [0, 1, 2]),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(-3).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-4)).helianthate(2, -2).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+9, -4+9+9, -4+9+9+9],
                    -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                ]
            ),
            evans.zero_padding_glissando,
            abjad.LilyPondLiteral(
                r"\override Dots.extra-offset = #'(0 . 0.75)",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    r"\revert Dots.stencil.extra-offset",
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.Clef("alto"),
            abjad.Dynamic("mp"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [3, 4]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([0, 1, 2, 3, 2, 1]).rotate(2),
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(
                        abjad.select.get(abjad.select.leaves(_), [0, 1, 2])
                    ),
                ],
            ),
            evans.loop(
                [-8],
                [
                    1,
                ],
            ),
            lambda _: evans.upward_gliss(_, zero_padding=False),
            evans.ArticulationHandler(["staccato"], forget=False),
            abjad.Dynamic("fff"),
            abjad.StartHairpin(">"),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("change 2 voice", [5, 6]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                anemone.pitch.string_crossing_modules(first_state=4, random_seed=3, length=600),
                staff_positions=True,
            ),
            evans.slur(
                anemone.pitch.string_crossing_modules(
                    first_state=4, random_seed=3, length=600, return_lengths_only=True
                )
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [5, 6]),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(-4).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-5)).helianthate(2, -2).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+9, -4+9+9, -4+9+9+9],
                    -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                ]
            ),
            evans.zero_padding_glissando,
            abjad.LilyPondLiteral(
                r"\override Dots.extra-offset = #'(0 . 0.75)",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    r"\revert Dots.stencil.extra-offset",
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.Dynamic("f"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [7]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([0, 1, 2, 3, 2, 1]).rotate(3),
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(
                        abjad.select.get(abjad.select.leaves(_), [0, 1, 2])
                    ),
                ],
            ),
            evans.loop(
                [-7],
                [
                    1.5,
                ],
            ),
            lambda _: evans.upward_gliss(_, zero_padding=False),
            evans.ArticulationHandler(["staccato"], forget=False),
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("fff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("change 3 voice", [0, 1, 2, 3]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                anemone.pitch.string_crossing_modules(first_state=5, random_seed=4, length=600),
                staff_positions=True,
            ),
            evans.slur(
                anemone.pitch.string_crossing_modules(
                    first_state=5, random_seed=4, length=600, return_lengths_only=True
                )
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [0, 1, 2, 3]),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(-5).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-6)).helianthate(3, -3).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+9, -4+9+9, -4+9+9+9],
                    -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                ]
            ),
            evans.zero_padding_glissando,
            abjad.LilyPondLiteral(
                r"\override Dots.extra-offset = #'(0 . 0.75)",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    r"\revert Dots.stencil.extra-offset",
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.Clef("alto"),
            abjad.Dynamic("mp"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [4, 5]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([0, 1, 2, 3, 2, 1]).rotate(4),
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-1,
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(
                        abjad.select.get(abjad.select.leaves(_), [0, 1, 2])
                    ),
                ],
            ),
            evans.loop(
                [-6],
                [
                    0.5,
                ],
            ),
            lambda _: evans.upward_gliss(_, zero_padding=False),
            evans.ArticulationHandler(["staccato"], forget=False),
            abjad.Dynamic("fff"),
            abjad.StartHairpin(">"),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("change 3 voice", [6, 7]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                anemone.pitch.string_crossing_modules(first_state=6, random_seed=5, length=600),
                staff_positions=True,
            ),
            evans.slur(
                anemone.pitch.string_crossing_modules(
                    first_state=6, random_seed=5, length=600, return_lengths_only=True
                )
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [6, 7]),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(-6).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-7)).helianthate(3, -3).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+9, -4+9+9, -4+9+9+9],
                    -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                ]
            ),
            evans.zero_padding_glissando,
            abjad.LilyPondLiteral(
                r"\override Dots.extra-offset = #'(0 . 0.75)",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    r"\revert Dots.stencil.extra-offset",
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.Dynamic("f"),
        ),
        ####
        # evans.call(
        #     "score",
        #     lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
        #     lambda _: abjad.select.components(_, abjad.Score),
        # ),
        # evans.attach(
        #     "Global Context",
        #     anemone.lib.mark_100,
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
    time_signatures=anemone.signatures_16,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="16",
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
