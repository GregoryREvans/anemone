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
        ########## Long trill
        ## Viola 1
        evans.MusicCommand(
            ("viola 1 voice", [0, 1, 2, 3, 4, 5]),
            evans.make_tied_notes(),
            evans.PitchHandler(["g"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(0)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [6]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[0],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 10 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [1]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [7, 8, 9, 10]),
            evans.make_tied_notes(),
            evans.PitchHandler(["a"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(1)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [11]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[1],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 9 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [1]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [12, 13]),
            evans.make_tied_notes(),
            evans.PitchHandler(["b"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(2)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [14, 15]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[0, 1, 0, 1, 1, 0, 2],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 8 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [2]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [16]),
            evans.make_tied_notes(),
            evans.PitchHandler(["c'"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(3)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [17]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=evans.Sequence([0, 1, 0, 1, 1, 0, 2]).rotate(-1),
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 7 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [2]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [18, 19, 20]),
            evans.make_tied_notes(),
            evans.PitchHandler(["d'"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(4)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [21, 22, 23, 24]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[0],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 6 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [3]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("fff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", [0, 1, 2, 3, 4, 5, 6, 7]),
            evans.make_tied_notes(),
            evans.PitchHandler(["g"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(0)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [8]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[1],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 9 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [1]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [9, 10, 11, 12]),
            evans.make_tied_notes(),
            evans.PitchHandler(["gs"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(1)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [13, 14]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[0, 1],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 8 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [1]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [15]),
            evans.make_tied_notes(),
            evans.PitchHandler(["a"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(2)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [16, 17, 18]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=evans.Sequence([0, 1, 0, 1, 1, 0, 2]).rotate(-2),
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 7 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [2]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [19, 20]),
            evans.make_tied_notes(),
            evans.PitchHandler(["as"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(3)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [21, 22, 23, 24]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=evans.Sequence([0, 1, 0, 1, 1, 0, 2]).rotate(-3),
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 5 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [2]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
            evans.make_tied_notes(),
            evans.PitchHandler(["g"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(0)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [10]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[0],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 8 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [1]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [11, 12, 13]),
            evans.make_tied_notes(),
            evans.PitchHandler(["gqs"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(1)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [14]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[1],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 7 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [2]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), len(abjad.select.leaves(_))//2)
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [15, 16]),
            evans.make_tied_notes(),
            evans.PitchHandler(["gs"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(2)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [17, 18]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=[1, 0],
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 6 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [2]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [19, 20]),
            evans.make_tied_notes(),
            evans.PitchHandler(["gtqs"]),
            lambda _: anemone.lib.integrate_multi_trills(
                _,
                intervals=[evans.PitchSegment(_).to_intervals() for _ in evans.Sequence([[0, 5], [0, 5, 7], [0, 4], [0, 2, 3, 4]]).rotate(3)],
                harmonics_boolean_vector=[1],
            ),
            lambda _: anemone.swells(abjad.select.logical_ties(_, grace=False), group_size=1, dyns=["p", "f"]),
        ),
        evans.MusicCommand(
            ("viola 3 voice", [21, 22, 23, 24]),
            evans.even_division(
                [16],
                preprocessor=evans.make_preprocessor(quarters=True),
                extra_counts=evans.Sequence([0, 1, 0, 1, 1, 0, 2]).rotate(-4),
                rewrite=-1,
                beam_meter=True,
            ),
            evans.loop([_ - 4 for _ in [0, 1, 2, 0, 2, 1, 2, 3, 2]], [3]),
            abjad.iterpitches.respell_with_sharps,
            evans.ArticulationHandler(["tremolo"]),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("fff"),
                selector=lambda _: abjad.select.leaf(abjad.select.leaves(_), -1)
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
