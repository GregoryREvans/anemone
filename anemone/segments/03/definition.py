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
    fermata_measures=anemone.fermata_measures_03,
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
            evans.even_division(
                [16],
                beam_meter=True,
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([1], 3))],
                ],
            ),
            evans.PitchHandler(["d''", "a''", "e'''", "a''"]),
            evans.slur([2]),
            abjad.Dynamic("f"),
            abjad.StartHairpin(">o"),
            abjad.Clef("alto"),
            evans.Attachment(
                abjad.Markup(r"\markup {clt.}"),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [1]),
            evans.note(),
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Markup(r"\markup o.b."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [2]),
            evans.even_division(
                [16],
                extra_counts=[1],
                preprocessor=evans.make_preprocessor(quarters=True),
                beam_meter=True,
            ),
            evans.PitchHandler(["d''", "a''", "e'''", "a''"]),
            evans.slur([2]),
            abjad.Dynamic("mf"),
            abjad.StartHairpin(">o"),
            evans.Attachment(
                abjad.Markup(r"\markup {cordes + clt.}"),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [3]),
            evans.note(),
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Markup(r"\markup o.b."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [4]),
            evans.even_division(
                [16],
                beam_meter=True,
            ),
            evans.PitchHandler(["d''", "a''", "e'''", "a''"]),
            evans.slur([2]),
            abjad.Dynamic("mp"),
            abjad.StartHairpin(">o"),
            evans.Attachment(
                abjad.Markup(r"\markup {cordes + clt.}"),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [5]),
            evans.note(),
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.get.leaf(abjad.select.leaf(_, -1), 1),
            ),
            evans.Attachment(
                abjad.Markup(r"\markup o.b."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [6, 7, 8]),
            evans.tuplet(
                [
                    (1, -4, 1),
                    (1, 1, -6),
                    (-2, 1),
                    (-3, 1, 1),
                    (1, -3),
                ],
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([2], 3) ^ abjad.index([0, -1]))]
                ],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[2, 1, 1, 2, 1], split_at_measure_boundaries=True),
                rewrite=-1,
                beam_meter=True,
            ),
            evans.Attachment(
                abjad.Markup(r"\markup pizz."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.note(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [9, 10, 11]),
            evans.tuplet(
                [
                    (1, 1, -6),
                    (-2, 1),
                    (-3, 1, 1),
                    (1, -3),
                    (1, -4, 1),
                ],
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([2], 3) ^ abjad.index([0, -1]))]
                ],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[1, 1, 2, 1, 2], split_at_measure_boundaries=True),
                rewrite=-1,
                beam_meter=True,
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [12, 13]),
            evans.talea([2, 1, 3], 4),
            evans.loop([-2], [-1]),
            abjad.glissando,
            abjad.Dynamic("p"),
            evans.ArticulationHandler(["tremolo"]),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", [0, 1]),
            evans.make_tied_notes(),
            evans.PitchHandler([["cs", "gs"]]),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("string 2 voice", [0, 1]),
            # evans.accelerando(
            #     [(1, 12), (1, 2), (1, 16)],
            #     preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            #     pre_commands=[
            #         lambda _: rmakers.force_rest(_),
            #         lambda _: [rmakers.force_note(x) for x in abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))],
            #         lambda _: [rmakers.force_note(x) for x in abjad.select.get(abjad.select.rests(_), abjad.index([1], 2))],
            #     ],
            #     treat_tuplets=False,
            # ),
            evans.accelerando(
                [(1, 5), (9, 16), (1, 16)],
                preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            ),
            evans.PitchHandler(
                [0, 3, 6, 2, -2, -4, -3, -1],
                staff_positions=True,
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin(">"),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            # lambda _: rmakers.unbeam(_),
            # abjad.StartBeam(),
            # evans.Attachment(
            #     abjad.StopBeam(),
            #     selector=lambda _: abjad.select.leaf(_, -1),
            # ),
            evans.Attachment(
                abjad.Markup(r"\markup clb."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                [
                    r"\override Staff.Stem.stencil = ##t",
                    r"\override Staff.Beam.stencil = ##t",
                    r"\override Staff.Dots.stencil = ##t",
                    r"\override Staff.Flag.stencil = ##t",
                    r"\override Staff.Rest.stencil = ##t",
                    r"\override Staff.NoteHead.transparent = ##f",
                ],
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    [
                        r"\override Staff.Stem.stencil = ##f",
                        r"\override Staff.Beam.stencil = ##f",
                        r"\override Staff.Dots.stencil = ##f",
                        r"\override Staff.Flag.stencil = ##f",
                        r"\override Staff.Rest.stencil = ##f",
                        r"\override Staff.NoteHead.transparent = ##t",
                    ],
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [2, 3]),
            evans.note(),
            evans.PitchHandler([
                ["cs", "gs"],
                ["d", "a"],
            ]),
            abjad.glissando,
        ),
        evans.MusicCommand(
            ("string 2 voice", [2, 3]),
            evans.accelerando(
                [(1, 5), (9, 16), (1, 16)],
                preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            ),
            evans.PitchHandler(
                [0, 3, 6, 2, -2, -4, -3, -1],
                staff_positions=True,
            ),
            abjad.Dynamic("ff"),
            abjad.StartHairpin(">"),
            evans.Attachment(
                abjad.Dynamic("pp"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                [
                    r"\override Staff.Stem.stencil = ##t",
                    r"\override Staff.Beam.stencil = ##t",
                    r"\override Staff.Dots.stencil = ##t",
                    r"\override Staff.Flag.stencil = ##t",
                    r"\override Staff.Rest.stencil = ##t",
                    r"\override Staff.NoteHead.transparent = ##f",
                ],
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    [
                        r"\override Staff.Stem.stencil = ##f",
                        r"\override Staff.Beam.stencil = ##f",
                        r"\override Staff.Dots.stencil = ##f",
                        r"\override Staff.Flag.stencil = ##f",
                        r"\override Staff.Rest.stencil = ##f",
                        r"\override Staff.NoteHead.transparent = ##t",
                    ],
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [4, 5]),
            evans.talea([1], 4),
            evans.PitchHandler([
                ["cs", "gs"],
                ["d", "a"],
                ["ds", "as"],
                ["e", "b"],
                ["f", "c'"],
                ["fs", "cs'"],
                ["g", "d'"],
                ["gs", "ds'"],
                ["a", "e'"],
            ]),
            abjad.glissando,
        ),
        evans.MusicCommand(
            ("string 2 voice", [4, 5]),
            evans.accelerando(
                [(9, 16), (1, 5), (1, 16)],
                [(1, 7), (1, 2), (1, 16)],
            ),
            evans.PitchHandler(
                [0, 3, 6, 2, -2, -4, -3, -1],
                staff_positions=True,
            ),
            abjad.Dynamic("p"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                [
                    r"\override Staff.Stem.stencil = ##t",
                    r"\override Staff.Beam.stencil = ##t",
                    r"\override Staff.Dots.stencil = ##t",
                    r"\override Staff.Flag.stencil = ##t",
                    r"\override Staff.Rest.stencil = ##t",
                    r"\override Staff.NoteHead.transparent = ##f",
                ],
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    [
                        r"\override Staff.Stem.stencil = ##f",
                        r"\override Staff.Beam.stencil = ##f",
                        r"\override Staff.Dots.stencil = ##f",
                        r"\override Staff.Flag.stencil = ##f",
                        r"\override Staff.Rest.stencil = ##f",
                        r"\override Staff.NoteHead.transparent = ##t",
                    ],
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [6, 7, 8]),
            evans.tuplet(
                [
                    (1, -3),
                    (1, -4, 1),
                    (1, 1, -6),
                    (-2, 1),
                    (-3, 1, 1),
                ],
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([1], 3) ^ abjad.index([0, -1]))]
                ],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[1, 2, 1, 1, 2], split_at_measure_boundaries=True),
                rewrite=-1,
                beam_meter=True,
            ),
            evans.Attachment(
                abjad.Markup(r"\markup pizz."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.note(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [9, 10, 11]),
            evans.make_tied_notes(),
            evans.PitchHandler([6], staff_positions=True),
            evans.ArticulationHandler(["tremolo"]),
            abjad.LilyPondLiteral(r"\highest", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\revert-noteheads", site="after"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
            abjad.Dynamic("pp"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [12, 13]),
            evans.make_tied_notes(),
            evans.PitchHandler([["cs", "gs"]]),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("string 2 voice", [12, 13]),
            # evans.accelerando(
            #     [(1, 12), (1, 2), (1, 16)],
            #     preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            #     pre_commands=[
            #         lambda _: rmakers.force_rest(_),
            #         lambda _: [rmakers.force_note(x) for x in abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))],
            #         lambda _: [rmakers.force_note(x) for x in abjad.select.get(abjad.select.rests(_), abjad.index([1], 2))],
            #     ],
            #     treat_tuplets=False,
            # ),
            evans.accelerando(
                [(1, 5), (9, 16), (1, 16)],
                preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            ),
            evans.PitchHandler(
                [0, 3, 6, 2, -2, -4, -3, -1],
                staff_positions=True,
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin(">"),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            # lambda _: rmakers.unbeam(_),
            # abjad.StartBeam(),
            # evans.Attachment(
            #     abjad.StopBeam(),
            #     selector=lambda _: abjad.select.leaf(_, -1),
            # ),
            evans.Attachment(
                abjad.Markup(r"\markup clb."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                [
                    r"\override Staff.Stem.stencil = ##t",
                    r"\override Staff.Beam.stencil = ##t",
                    r"\override Staff.Dots.stencil = ##t",
                    r"\override Staff.Flag.stencil = ##t",
                    r"\override Staff.Rest.stencil = ##t",
                    r"\override Staff.NoteHead.transparent = ##f",
                ],
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    [
                        r"\override Staff.Stem.stencil = ##f",
                        r"\override Staff.Beam.stencil = ##f",
                        r"\override Staff.Dots.stencil = ##f",
                        r"\override Staff.Flag.stencil = ##f",
                        r"\override Staff.Rest.stencil = ##f",
                        r"\override Staff.NoteHead.transparent = ##t",
                    ],
                    site="after",
                ),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", [0, 1]),
            evans.talea(
                [1, -14, 1, 1, -12, 1],
                16,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(["e'''"]),
            evans.Attachment(
                abjad.Markup(r"\pizz-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 0),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Markup(r"\flick-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 1),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Articulation("snappizzicato"),
                selector=lambda _: abjad.select.note(_, 2),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Markup(r"\flick-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 3),
                direction=abjad.UP,
            ),
            abjad.Clef("treble"),
            abjad.Dynamic("mp"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, 2),
            ),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, 3),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [2, 3]),
            evans.talea(
                [1, -14, 1, 1, -10, 1],
                16,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(["eqf'''", "ef'''", "etqf'''", "d'''"]),
            evans.Attachment(
                abjad.Markup(r"\pizz-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 0),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Markup(r"\flick-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 1),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Articulation("snappizzicato"),
                selector=lambda _: abjad.select.note(_, 2),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Markup(r"\flick-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 3),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, 2),
            ),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, 3),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [4, 5]),
            evans.talea(
                [1, -16, 1, 1, -10, 1],
                16,
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(["d'''", "cs'''", "c'''", "b''"]),
            evans.Attachment(
                abjad.Markup(r"\pizz-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 0),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Markup(r"\flick-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 1),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Articulation("snappizzicato"),
                selector=lambda _: abjad.select.note(_, 2),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Markup(r"\flick-with-nail-markup"),
                selector=lambda _: abjad.select.note(_, 3),
                direction=abjad.UP,
            ),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.note(_, 2),
            ),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, 3),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [6, 7, 8]),
            evans.make_tied_notes(),
            evans.PitchHandler([6], staff_positions=True, clef="treble"),
            evans.ArticulationHandler(["tremolo"]),
            abjad.LilyPondLiteral(r"\highest", site="before"),
            abjad.Dynamic("pp"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [9, 10, 11]),
            evans.tuplet(
                [
                    (-2, 1),
                    (-3, 1, 1),
                    (1, -3),
                    (1, -4, 1),
                    (1, 1, -6),
                ],
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.tuplets(_), abjad.index([1], 3) ^ abjad.index([0, -1]))]
                ],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[1, 2, 1, 2, 1], split_at_measure_boundaries=True),
                rewrite=-1,
                beam_meter=True,
            ),
            evans.Attachment(
                abjad.Markup(r"\markup pizz."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.note(_, 0),
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\revert-noteheads", site="before"),
                selector=lambda _: abjad.select.note(_, 0),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [12, 13]),
            evans.make_tied_notes(),
            evans.PitchHandler([["d", "a"]]),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("string 3 voice", [12, 13]),
            # evans.accelerando(
            #     [(1, 12), (1, 2), (1, 16)],
            #     preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            #     pre_commands=[
            #         lambda _: rmakers.force_rest(_),
            #         lambda _: [rmakers.force_note(x) for x in abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))],
            #         lambda _: [rmakers.force_note(x) for x in abjad.select.get(abjad.select.rests(_), abjad.index([1], 2))],
            #     ],
            #     treat_tuplets=False,
            # ),
            evans.accelerando(
                [(1, 4), (5, 8), (1, 16)],
                preprocessor=evans.make_preprocessor(fuse_counts=[2]),
            ),
            evans.PitchHandler(
                [0, 3, 6, 2, -2, -4, -3, -1],
                staff_positions=True,
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin(">"),
            evans.Attachment(
                abjad.Dynamic("p"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            # lambda _: rmakers.unbeam(_),
            # abjad.StartBeam(),
            # evans.Attachment(
            #     abjad.StopBeam(),
            #     selector=lambda _: abjad.select.leaf(_, -1),
            # ),
            evans.Attachment(
                abjad.Markup(r"\markup clb."),
                direction=abjad.UP,
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
            abjad.LilyPondLiteral(r"\stopStaff", site="before"),
            abjad.LilyPondLiteral(
                r"\override Staff.StaffSymbol.transparent = ##f", site="before"
            ),
            abjad.LilyPondLiteral(r"\startStaff", site="before"),
            abjad.LilyPondLiteral(
                [
                    r"\override Staff.Stem.stencil = ##t",
                    r"\override Staff.Beam.stencil = ##t",
                    r"\override Staff.Dots.stencil = ##t",
                    r"\override Staff.Flag.stencil = ##t",
                    r"\override Staff.Rest.stencil = ##t",
                    r"\override Staff.NoteHead.transparent = ##f",
                ],
                site="before",
            ),
            evans.Attachment(
                abjad.LilyPondLiteral(
                    [
                        r"\override Staff.Stem.stencil = ##f",
                        r"\override Staff.Beam.stencil = ##f",
                        r"\override Staff.Dots.stencil = ##f",
                        r"\override Staff.Flag.stencil = ##f",
                        r"\override Staff.Rest.stencil = ##f",
                        r"\override Staff.NoteHead.transparent = ##t",
                    ],
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
            anemone.lib.mark_80,
            lambda _: abjad.select.leaf(_, 0),
        ),
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
    time_signatures=anemone.signatures_03,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="03",
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
