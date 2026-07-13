import pathlib
from fractions import Fraction
from random import choice, seed

import abjad
import baca
import evans
from abjadext import rmakers

import anemone


def make_polyrhythm(selections, tuplets=[(1, 1, 1, 1, 1)], pitches=[-1, -2, -3, -2]):
    new_tuplet = evans.tuplet(tuplets, beam_meter=True)(selections)
    evans.PitchHandler(pitches)(new_tuplet)
    return new_tuplet

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
    fermata_measures=anemone.fermata_measures_17,
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
            ("viola 1 voice", [0, 1, 2]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(0)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ - 6 for _ in [0, 1, 2, 3, 4, 7, 5, 6, 7, 9]], [1, 2, -1, 3, -1]
            ),
            evans.slur([10]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [3]),
            evans.make_tied_notes(),
            evans.PitchHandler(["ef''"]),
            abjad.Dynamic("ff"),
            # evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [4]),
            evans.talea(
                [1],
                8,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(-1)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([-3, -2, -1, -0.5, -2, -4], [0.5]),
            abjad.bundle(
                abjad.StartTrillSpan(interval=abjad.NamedInterval("+P4")),
                r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))"""
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin("|>"),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin("<|"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [5, 6, 7]),
            evans.make_tied_notes(),
            evans.PitchHandler(["ef''"]),
            abjad.Dynamic("ff"),
            evans.ArticulationHandler(["tremolo"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[2, 3, 2, 4, 2, 1],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [8, 9, 10]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(4)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ - 2 for _ in [0, 1, 2, 3, 4, 7, 5, 6, 7]], [1, 2, -1, 3, -1]
            ),
            evans.slur([9]),
            abjad.LilyPondLiteral(r"\harmonicsOn", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [11]),
            evans.make_tied_notes(),
            evans.PitchHandler(["eqf''"]),
            abjad.Dynamic("ff"),
            # evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [12]),
            evans.tuplet([(1, 1, 1, 1)], beam_meter=True),
            evans.PitchHandler([1, -1, 2, 0, -2, 0, 1, -1]),
            abjad.Dynamic("ff"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [13]),
            evans.make_tied_notes(),
            evans.PitchHandler(["e''"]),
            abjad.Dynamic("ff"),
            evans.ArticulationHandler(["tremolo"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[2, 3, 2, 4, 2, 1],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [14, 15]),
            evans.talea(
                [1],
                8,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(-3)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ + 1 for _ in [-3, -2, -1, -0.5, -2, -4]], [1]),
            abjad.bundle(
                abjad.StartTrillSpan(interval=abjad.NamedInterval("+P4")),
                r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))"""
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin("|>"),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin("<|"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [16, 17, 18]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(8)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ + 2 for _ in [0, 1, 2, 3, 4, 7, 5]], [1, 2, -1, 3, -1]
            ),
            evans.slur([7]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
            evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [19]),
            evans.make_tied_notes(),
            evans.PitchHandler(["eqs''"]),
            abjad.Dynamic("ff"),
            # evans.ArticulationHandler(["tremolo"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[2, 3, 2, 4, 2, 1],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [20, 21]),
            evans.talea(
                [1],
                8,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(-4)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ + 2 for _ in [-3, -2, -1, -0.5, -2, -4]], [1.5]),
            abjad.bundle(
                abjad.StartTrillSpan(interval=abjad.NamedInterval("+P4")),
                r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))"""
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin("|>"),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin("<|"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", [0]),
            evans.make_tied_notes(),
            evans.PitchHandler(["ef''"]),
            abjad.Dynamic("ff"),
            evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [1]),
            evans.tuplet([(1, 1, 1, 1, 1, 1)], beam_meter=True),
            evans.PitchHandler([1, 2, 3, 2.5, 2, 1, 1.5]),
            abjad.Dynamic("ff"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [2, 3]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(1)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ - 5 for _ in [0, 1, 2, 3, 4, 7, 5, 6, 7, 9]], [1, 2, -1, 3, -1]
            ),
            evans.slur([10]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [4]),
            evans.make_tied_notes(),
            evans.PitchHandler(["ef''"]),
            abjad.Dynamic("ff"),
            # abjad.bundle(
            #     abjad.StartTrillSpan(interval=abjad.NamedInterval("+P4")),
            #     r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))"""
            # ),
            # evans.Attachment(
            #     abjad.StopTrillSpan(),
            #     selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            # ),
            # evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [5, 6, 7, 8]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(3)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ - 3 for _ in [0, 1, 2, 3, 4, 7, 5, 6, 7]], [1, 2, -1, 3, -1]
            ),
            evans.slur([9]),
            abjad.LilyPondLiteral(r"\harmonicsOn", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [9]),
            evans.talea(
                [1],
                8,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(-5)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([-3, -2, -1, -0.5, -2, -4], [0.5]),
            abjad.bundle(
                abjad.StartTrillSpan(interval=abjad.NamedInterval("+P4")),
                r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))"""
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin("|>"),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin("<|"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [10, 11]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(5)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ - 1 for _ in [0, 1, 2, 3, 4, 7, 5, 6]], [1, 2, -1, 3, -1]
            ),
            evans.slur([8]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
            evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [12]),
            evans.make_tied_notes(),
            evans.PitchHandler(["eqf''"]),
            abjad.Dynamic("ff"),
            evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [13, 14, 15, 16]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(7)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ + 1 for _ in [0, 1, 2, 3, 4, 7, 5]], [1, 2, -1, 3, -1]
            ),
            evans.slur([7]),
            abjad.LilyPondLiteral(r"\harmonicsOn", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [17]),
            evans.make_tied_notes(),
            evans.PitchHandler(["e''"]),
            abjad.Dynamic("ff"),
            # evans.ArticulationHandler(["tremolo"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[2, 3, 2, 4, 2, 1],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [18, 19]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(9)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ + 3 for _ in [0, 1, 2, 3, 4, 7]], [1, 2, -1, 3, -1]
            ),
            evans.slur([6]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
            evans.ArticulationHandler(["tremolo"]),
            # abjad.bundle(
            #     abjad.StartTrillSpan(interval=abjad.NamedInterval("+P4")),
            #     r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))"""
            # ),
            # evans.Attachment(
            #     abjad.StopTrillSpan(),
            #     selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            # ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [20, 21]),
            evans.make_tied_notes(),
            evans.PitchHandler(["f''"]),
            abjad.Dynamic("ff"),
            evans.ArticulationHandler(["tremolo"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[2, 3, 2, 4, 2, 1],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", [0]),
            evans.tuplet(
                [(1, 1, 1, 1)],
                beam_meter=True,
            ),
            evans.PitchHandler([0, 0.5, 0, -0.5, 0, 1, 0, -1, 0, 1.5, 0, -1.5, 0, 1, 0, -1]),
            abjad.Dynamic("ff"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [1, 2]),
            evans.make_tied_notes(),
            evans.PitchHandler(["ef''"]),
            abjad.Dynamic("ff"),
            # evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [3, 4, 5]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(2)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ - 4 for _ in [0, 1, 2, 3, 4, 7, 5, 6, 7, 9]], [1, 2, -1, 3, -1]
            ),
            evans.slur([10]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [6, 7]),
            evans.tuplet([(1, 1, 1, 1), (1, 1, 1, 1, 1)], beam_meter=True),
            evans.PitchHandler([-1, -2, -4, -3, -0.5, -2, -3.5, -4]),
            abjad.Dynamic("ff"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [8, 9, 10]),
            evans.make_tied_notes(),
            evans.PitchHandler(["eqf''"]),
            abjad.Dynamic("ff"),
            evans.ArticulationHandler(["tremolo"]),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [11, 12, 13]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(6)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ - 0 for _ in [0, 1, 2, 3, 4, 7, 5, 6]], [1, 2, -1, 3, -1]
            ),
            evans.slur([8]),
            abjad.LilyPondLiteral(r"\harmonicsOn", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [14, 15, 16]),
            evans.make_tied_notes(),
            evans.PitchHandler(["e''"]),
            abjad.Dynamic("ff"),
            # evans.ArticulationHandler(["tremolo"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[2, 3, 2, 4, 2, 1],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [17]),
            evans.talea(
                [1],
                8,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(-6)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.leaves(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([-3, -2, -1, -0.5, -2, -4], [0.5]),
            abjad.bundle(
                abjad.StartTrillSpan(interval=abjad.NamedInterval("+P4")),
                r"""- \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))"""
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.get.leaf(abjad.select.note(_, -1), 1)
            ),
            abjad.Dynamic("f"),
            abjad.StartHairpin("|>"),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin("<|"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_))//2),
            ),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [18]),
            evans.make_tied_notes(),
            evans.PitchHandler(["eqs''"]),
            abjad.Dynamic("ff"),
            evans.ArticulationHandler(["tremolo"]),
            lambda _: evans.vibrato_spanner(
                peaks=[1, 5, 1, 2, 3, 4, 2, 1, 5, 4, 3, 2, 3],
                wavelengths=[2, 3, 2, 4, 2, 1],
                thickness=0.2,
                divisions=[4, 5, 4, 6],
                counts=[2],
                cyclic=True,
                padding=4.5,
                forget=False,
            )(abjad.select.leaves(_)),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [19, 20, 21]),
            evans.talea(
                [1],
                16,
                extra_counts=evans.Sequence([3, 1, 2, 0])
                .permutations().rotate(10)
                .flatten(depth=-1),
                preprocessor=evans.make_preprocessor(quarters=True),
                pre_commands=[
                    lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, -1]))),
                    lambda _: rmakers.force_rest([abjad.select.get(abjad.select.notes(_), abjad.index([0, -1]))])
                    # lambda _: rmakers.force_rest(abjad.select.get(abjad.select.logical_ties(_, pitched=True), abjad.index([23]))),
                ],
                # rewrite=-1,
                beam_meter=True,
            ),
            evans.loop(
                [_ + 4 for _ in [0, 1, 2, 3, 4, 7]], [1, 2, -1, 3, -1]
            ),
            evans.slur([6]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.note(_, len(abjad.select.notes(_)) // 2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.note(_, -1)
            ),
            evans.ArticulationHandler(["tremolo"]),
        ),
        ####
        evans.call(
            "viola 3 voice",
            evans.IntermittentVoiceHandler(
                lambda _: make_polyrhythm(_, [(1, 1, 1, 1, 1)], [13, -4, 11, -6, 10, -3, 9, -5, 8, -8]),
                direction=abjad.UP,
            ),
            selector=lambda _: evans.select_measures([0])(_)[0],
        ),
        evans.call(
            "viola 2 voice",
            evans.IntermittentVoiceHandler(
                lambda _: make_polyrhythm(_, [(1, 1, 1, 1, 1)], [13, -4, 11, -6, 10, -3, 9, -5, 8, -8]),
                direction=abjad.UP,
            ),
            selector=lambda _: evans.select_measures([1])(_)[0],
        ),
        evans.call(
            "viola 3 voice",
            evans.IntermittentVoiceHandler(
                lambda _: make_polyrhythm(_, [(1, 1, 1, 1, 1)], [13, -4, 11, -6, 10, -3, 9, -5, 8, -8]),
                direction=abjad.UP,
            ),
            selector=lambda _: evans.select_measures([6])(_)[0],
        ),
        evans.call(
            "viola 3 voice",
            evans.IntermittentVoiceHandler(
                lambda _: make_polyrhythm(_, [(1, 1, 1, 1, 1, 1)], [13, -4, 11, -6, 10, -3, 9, -5, 8, -8]),
                direction=abjad.UP,
            ),
            selector=lambda _: evans.select_measures([7])(_)[0],
        ),
        evans.call(
            "viola 1 voice",
            evans.IntermittentVoiceHandler(
                lambda _: make_polyrhythm(_, [(1, 1, 1, 1, 1)], [13, -4, 11, -6, 10, -3, 9, -5, 8, -8]),
                direction=abjad.UP,
            ),
            selector=lambda _: evans.select_measures([12])(_)[0],
        ),
        ####
        # evans.call(
        #     "score",
        #     lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
        #     lambda _: abjad.select.components(_, abjad.Score),
        # ),
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
    time_signatures=anemone.signatures_17,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="17",
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
