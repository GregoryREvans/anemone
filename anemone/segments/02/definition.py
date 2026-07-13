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
    fermata_measures=anemone.fermata_measures_02,
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
            ("viola 1 voice", [0, 1]),
            evans.talea(
                [1, 2, 3, 4, 5, 2, 4, 5, 3, 1, 4, 3, 1, 5, 2, 3, 5, 2, 1, 4, 5, 1, 4, 2, 3],
                8
            ),
            evans.PitchHandler(["b", "bqf", "b", "bf", "b", "bqs", "c"]),
            # abjad.glissando,
            evans.NoteheadHandler(
                notehead_list=["harmonic", "default"],
                transition=True,
                head_boolean_vector=[1],
                head_vector_forget=False,
                transition_boolean_vector=[0, 1, 1, 1, 1, 1, 1, 1],
                transition_vector_forget=False,
                forget=True,
            ),
            evans.Attachment(
                abjad.Glissando(),
                selector=lambda _: abjad.select.note(_, 0),
            ),
            abjad.Dynamic("ppp"),
            abjad.StartHairpin("<|"),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin("|>"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["gr.", "->", "ord.", "->", "flaut.", "->", "½gr.", "->"],
                abjad.Tweak(r"\tweak staff-padding #3"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [2, 1, 3], cyclic=True, overhang=True),
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["P", "->", "N"],
                abjad.Tweak(r"\tweak staff-padding #5"),
                lilypond_id=2,
            ),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [2, 3, 4]),
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
            ("viola 1 voice", [6, 7]),
            evans.make_tied_notes(),
            evans.PitchHandler(["c'"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 1, 5, 1, 1, 3, 1],
                wavelengths=[1.5],
                thickness=0.2,
                divisions=[11],
                counts=[1],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            evans.Attachment(
                abjad.Markup(r"\markup ord."),
                selector=lambda _: abjad.select.note(_, 0),
                direction=abjad.UP,
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (8, 19)),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True, split_at_measure_boundaries=True),
                beam_meter=True,
            ),
            evans.loop(
                [-9, -9+8, -9+8+8, -9+8+8+8, -9+8+8+8, -9+8+8, -9+8, -9],
                [0, 1, 0, 0, 1, 0, 1, 0.5, 0.5, 0.5, 0.5, 1, 0],
            ),
            evans.slur([4]),
            abjad.Dynamic("f"),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", [0, 1, 2]),
            evans.talea(
                [4, 5, 2, 4, 5, 3, 1, 4, 3, 1, 5, 2, 3, 5, 2, 1, 4, 5, 1, 4, 2, 3, 1, 2, 3],
                8
            ),
            evans.PitchHandler(["a", "aqs", "as", "b", "bqs", "c'", "cqs'"]),
            # abjad.glissando,
            evans.NoteheadHandler(
                notehead_list=["harmonic", "default"],
                transition=True,
                head_boolean_vector=[1],
                head_vector_forget=False,
                transition_boolean_vector=[1],
                transition_vector_forget=False,
                forget=True,
            ),
            abjad.Dynamic("ppp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("mf"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["gr.", "->", "ord.", "->", "flaut.", "->", "½gr.", "->"],
                abjad.Tweak(r"\tweak staff-padding #3"),
                lilypond_id=1,
                pieces=lambda x: abjad.select.partition_by_counts(abjad.select.logical_ties(x), [2, 1, 3], cyclic=True, overhang=True),
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["P", "->", "N"],
                abjad.Tweak(r"\tweak staff-padding #5"),
                lilypond_id=2,
            ),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [3, 4]),
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
            ("viola 2 voice", [6, 7]),
            evans.make_tied_notes(),
            evans.PitchHandler("b"),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 1, 5, 1, 1, 3, 1],
                wavelengths=[1.5],
                thickness=0.2,
                divisions=[17],
                counts=[1],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            evans.Attachment(
                abjad.Markup(r"\markup ord."),
                selector=lambda _: abjad.select.note(_, 0),
                direction=abjad.UP,
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (8, 15)),
            evans.talea(
                evans.Sequence([1, 1, 2, 3, 5, 8]).zipped_bifurcation(),
                8,
                preprocessor=evans.make_preprocessor(quarters=True, split_at_measure_boundaries=True),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.logical_ties(_), abjad.index([0, 2, 5], 6))],
                ],
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(
                [
                    ["cs", "g", "fs'"],
                    ["d''", "ef''"],
                    ["d", "c'", "fs'", "ds'"],
                    "g''",
                    ["d'", "b'"],
                    ["fs'", "b'"],
                ]
            ),
            abjad.Dynamic("f"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (15, 19)),
            evans.even_division(
                [16],
                extra_counts=[1,],
                preprocessor=evans.make_preprocessor(quarters=True, split_at_measure_boundaries=True),
                beam_meter=True,
            ),
            evans.loop(
                [-9, -9+8.5, -9+8.5+8.5, -9+8.5+8.5+8.5, -9+8.5+8.5+8.5, -9+8.5+8.5, -9+8.5, -9],
                [0.5, 1, 1.5, 1],
            ),
            evans.slur([4]),
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", [0]),
            evans.talea(
                [4, 5, 3, 1, 4, 3, 1, 5, 2, 3, 5, 2, 1, 4, 5, 1, 4, 2, 3, 1, 2, 3, 4, 5, 2],
                8
            ),
            evans.PitchHandler(["as", "b", "bqf", "b", "cs'", "ctqs'", "c'"]),
            # abjad.glissando,
            evans.NoteheadHandler(
                notehead_list=["harmonic", "default"],
                transition=True,
                head_boolean_vector=[1],
                head_vector_forget=False,
                transition_boolean_vector=[1],
                transition_vector_forget=False,
                forget=True,
            ),
            abjad.Dynamic("ppp"),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["gr.", "->", "ord."],
                abjad.Tweak(r"\tweak staff-padding #3"),
                lilypond_id=1,
            ),
            lambda _: baca.text_spanner(
                abjad.select.leaves(_),
                ["P", "->", "N"],
                abjad.Tweak(r"\tweak staff-padding #5"),
                lilypond_id=2,
            ),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [1, 2, 3]),
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
            ("viola 3 voice", [4, 5, 6, 7]),
            evans.make_tied_notes(),
            evans.PitchHandler(["a"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 1, 5, 1, 1, 3, 1],
                wavelengths=[1.5],
                thickness=0.2,
                divisions=[23],
                counts=[1],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            evans.Attachment(
                abjad.Markup(r"\markup ord."),
                selector=lambda _: abjad.select.note(_, 0),
                direction=abjad.UP,
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (8, 11)),
            evans.talea(
                evans.Sequence([2, 3, 5, 8, 1, 1]).zipped_bifurcation(),
                8,
                extra_counts=[0, 1, 0, 0, 1],
                preprocessor=evans.make_preprocessor(quarters=True, split_at_measure_boundaries=True),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.logical_ties(_), ~abjad.index([0, 2, 5], 6))],
                ],
                rewrite=-2,
                # beam_meter=True,
            ),
            evans.PitchHandler(
                [
                    [-5, -5+0.5],
                    [0, 0+1],
                    [2, 2+1.5],
                    [6, 6+2],
                    [11, 11+1.5],
                    [14, 14+1],
                    [15, 15+0.5],
                ]
            ),
            abjad.Dynamic("f"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (11, 19)),
            evans.even_division(
                [16],
                extra_counts=[2,],
                preprocessor=evans.make_preprocessor(quarters=True, split_at_measure_boundaries=True),
                beam_meter=True,
            ),
            evans.loop(
                [-9, -9+9, -9+9+9, -9+9+9+9, -9+9+9+9, -9+9+9, -9+9, -9],
                [1, 0.5, 1, 1.5],
            ),
            evans.slur([4]),
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1)
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

        evans.attach(
            "Global Context",
            anemone.lib.met_90,
            selector=lambda _: abjad.select.leaf(_, 6)
        ),
        evans.attach(
            "Global Context",
            abjad.Markup(r"""\markup {\translate #'(0 . 1.5) \tiny \bold "rall."}"""),
            selector=lambda _: abjad.select.leaf(_, 6),
            direction=abjad.UP,
        ),
        evans.attach(
            "Global Context",
            abjad.LilyPondLiteral(r"\rallArrow #3", site="after"),
            selector=lambda _: abjad.select.leaf(_, 6),
        ),
        evans.attach(
            "Global Context",
            abjad.StopTextSpan(),
            selector=lambda _: abjad.select.leaf(_, 8)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_80_small,
            selector=lambda _: abjad.select.leaf(_, 8)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_80,
            selector=lambda _: abjad.select.leaf(_, 8)
        ),

        evans.attach(
            "Global Context",
            anemone.lib.met_90,
            selector=lambda _: abjad.select.leaf(_, 11)
        ),
        evans.attach(
            "Global Context",
            abjad.Markup(r"""\markup {\translate #'(0 . 2) \tiny \bold "accel."}"""),
            selector=lambda _: abjad.select.leaf(_, 11),
            direction=abjad.UP,
        ),
        evans.attach(
            "Global Context",
            abjad.LilyPondLiteral(r"\accelArrow #3", site="after"),
            selector=lambda _: abjad.select.leaf(_, 11),
        ),
        evans.attach(
            "Global Context",
            abjad.StopTextSpan(),
            selector=lambda _: abjad.select.leaf(_, 12)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_100_small,
            selector=lambda _: abjad.select.leaf(_, 12)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_100,
            selector=lambda _: abjad.select.leaf(_, 12)
        ),

        evans.attach(
            "Global Context",
            anemone.lib.met_90,
            selector=lambda _: abjad.select.leaf(_, 13)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_80_small,
            selector=lambda _: abjad.select.leaf(_, 13)
        ),
        # evans.attach(
        #     "Global Context",
        #     abjad.Markup(r"""\markup {\translate #'(0 . 2) \tiny \bold "accel."}"""),
        #     selector=lambda _: abjad.select.leaf(_, 13),
        #     direction=abjad.UP,
        # ),
        evans.attach(
            "Global Context",
            abjad.LilyPondLiteral(r"\accelArrow #3", site="after"),
            selector=lambda _: abjad.select.leaf(_, 13),
        ),
        evans.attach(
            "Global Context",
            abjad.StopTextSpan(),
            selector=lambda _: abjad.select.leaf(_, 14)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_100_small,
            selector=lambda _: abjad.select.leaf(_, 14)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_100,
            selector=lambda _: abjad.select.leaf(_, 14)
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
    time_signatures=anemone.signatures_02,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="02",
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
