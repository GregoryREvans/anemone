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
    fermata_measures=anemone.fermata_measures_14,
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
        ##########
        ## Viola 1
        evans.MusicCommand(
            ("change 1 voice", (0, 9)),
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
            ("viola 1 voice", (0, 9)),
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
                    -3, -2, -1, -3, -1, 0, 1, -3, 1, -3, 1, 2, 3, 4, -3, 4, -3, 4, -3, 4, 5, 6, 7, -3, 7, 8, 9, -3, 9, -3, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 19, 20,
                ]
            ),
            evans.zero_padding_glissando,
            abjad.Clef("alto"),
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
        ),
        evans.MusicCommand(
            ("change 1 voice", (9, 13)),
            evans.even_division(
                [16],
                extra_counts=[0, 0, 1, 0, 0, 0, 1],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -2, -1]))),
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
            ("viola 1 voice", (9, 13)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(3).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-3)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+8, -4+8+8, -4+8+8+8],
                    10, 5, 10, 9, 4, 9, 8, 3, 8, 7, 2, 7, 6, 1, 6, 5, 0, 5, 4, -1, 4, 3, -2, 3, 2, -3, 2, 1, -4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
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
            abjad.LilyPondLiteral(
                r"\harmonicsOn",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("change 1 voice", (13, 19)),
            evans.even_division(
                [16],
                extra_counts=[0, 2, 1, 2, 0, 0, 1],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 1, -1]))),
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
            ("viola 1 voice", (13, 19)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(6).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-6)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 1, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [-4, -4+8, -4+8+8, -4+8+8+8],
                    10, 5, 10, 9, 4, 9, 8, 3, 8, 7, 2, 7, 6, 1, 6, 5, 0, 5, 4, -1, 4, 3, -2, 3, 2, -3, 2, 1, -4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
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
        ),
        evans.MusicCommand(
            ("change 1 voice", (19, 25)),
            evans.even_division(
                [32],
                extra_counts=[1],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
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
            ("viola 1 voice", (19, 25)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(9).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-9)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [3, 3+7, 3+7+7, 3+7+7+7],
                    10,
                    -3,
                    12, 11, 12, 10, 13, 9, 13, 14, 13, 14, 15, 12, 11, 12, 10, 13, 9, 13, 14, 13, 14, 15
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
        ),
        ## Viola 2
        evans.MusicCommand(
            ("change 2 voice", (2, 7)),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
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
            ("viola 2 voice", (2, 7)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(1).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-1)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [-5, 5]
            ),
            evans.zero_padding_glissando,
            abjad.Clef("alto"),
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
        ),
        evans.MusicCommand(
            ("change 2 voice", (7, 14)),
            evans.even_division(
                [16],
                extra_counts=[1, 1, 0, 1, 0, 1, 0, 1],
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
            ("viola 2 voice", (7, 14)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(4).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-4)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([-2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [-5, 5]
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
            abjad.LilyPondLiteral(
                r"\harmonicsOn",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("change 2 voice", (14, 19)),
            evans.even_division(
                [16],
                extra_counts=[2, 1, 2, 1, 0, 0, 2, 1],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0]))),
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
            ("viola 2 voice", (14, 19)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(7).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-7)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [-5, 5]
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
        ),
        evans.MusicCommand(
            ("change 2 voice", (19, 25)),
            evans.even_division(
                [32],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
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
            ("viola 2 voice", (19, 25)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(10).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-10)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [3, 3+7, 3+7+7, 3+7+7+7],
                    10,
                    -3,
                    9, 13, 14, 13, 14, 15, 12, 11, 12, 10, 13, 9, 13, 14, 13, 14, 15, 12, 11, 12, 10, 13,
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
        ),
        ## Viola 3
        evans.MusicCommand(
            ("change 3 voice", (1, 5)),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 1, 2, -2, -1]))),
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
            ("viola 3 voice", (1, 5)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(2).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-2)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 1, 2, -2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [-5, 5]
            ),
            evans.zero_padding_glissando,
            abjad.Clef("alto"),
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
        ),
        evans.MusicCommand(
            ("change 3 voice", (5, 12)),
            evans.even_division(
                [16],
                extra_counts=[1, 1, 1, 0, 0, 1, 1, 0, 0],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 1, -1]))),
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
            ("viola 3 voice", (5, 12)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(5).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-5)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 1, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [-5, 5]
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
            abjad.LilyPondLiteral(
                r"\harmonicsOn",
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("change 3 voice", (12, 20)),
            evans.even_division(
                [16],
                extra_counts=[2, 1, 1, 0, 2, 2, 1, 0, 0],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -2, -1]))),
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
            ("viola 3 voice", (12, 20)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(8).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-8)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -2, -1]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [-5, 5]
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
        ),
        evans.MusicCommand(
            ("change 3 voice", (20, 25)),
            evans.even_division(
                [32],
                extra_counts=[-1],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0]))),
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
            ("viola 3 voice", (20, 25)),
            evans.talea(
                evans.Sequence([8, 6, 5, 4, 1, 1, 1]).rotate(11).zipped_bifurcation().partition_by_counts(evans.Sequence([4, 3, 2]).rotate(-11)).helianthate(1, -1).flatten(depth=-1),
                16,
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0]))),
                ],
                rewrite=-2,
            ),
            evans.PitchHandler(
                [
                    [3, 3+7, 3+7+7, 3+7+7+7],
                    10,
                    -3,
                    15, 12, 11, 12, 10, 13, 9, 13, 14, 13, 14, 15, 12, 11, 12, 10, 13, 9, 13, 14, 13, 14,
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
        ),
        ####
        # evans.call(
        #     "score",
        #     lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
        #     lambda _: abjad.select.components(_, abjad.Score),
        # ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_100,
            lambda _: abjad.select.leaf(_, 0),
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_100,
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
    time_signatures=anemone.signatures_14,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="14",
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
