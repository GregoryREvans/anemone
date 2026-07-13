import pathlib
from fractions import Fraction
from random import choice, seed

import abjad
import baca
import evans
from abjadext import rmakers

import anemone


def swells(selections, group_size=1, dyns=["p", "mf", "p", "f"], hairpins=["<", ">"]):
    ties = abjad.select.logical_ties(selections, pitched=True)
    leaves = [tie[0] for tie in ties]
    groups = abjad.select.partition_by_counts(
        leaves, [group_size], cyclic=True, overhang=True
    )
    cyc_dynamics = evans.CyclicList(dyns, forget=False)
    cyc_hairpins = evans.CyclicList(hairpins, forget=False)
    for group in groups:
        dynamic = abjad.Dynamic(cyc_dynamics(r=1)[0])
        abjad.attach(dynamic, group[0])
    for group in groups[:-1]:
        hairpin = abjad.StartHairpin(cyc_hairpins(r=1)[0])
        abjad.attach(hairpin, group[0])


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
    fermata_measures=anemone.fermata_measures_05,
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
        evans.MusicCommand( # provisional, mix with other materials
            ("viola 1 voice", (0, 7)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[4, 4, 3, 4, 3, 3, 4, 3, 2, 3, 3, 2, 3]),
            ),
            evans.loop(
                [-8],
                [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]
            ),
            evans.BendHandler([-3]),
            lambda _: swells(_, group_size=5, dyns=["ff", "mf", "f", "mp"], hairpins=[">", "<"]),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (7, 9)),
            evans.talea([1, 2, 3, 4, 2], 8),
            evans.PitchHandler([
                [-11, -11+11],
                [-11+6, -11+11+6],
                [-11+6+5, -11+11+6+5],
                [-11+6+5+4, -11+11+6+5+4],
                [-11+6+5+4+3, -11+11+6+5+4+3],
                [-11+6+5+4+3+2, -11+11+6+5+4+3+2],
                [-11+6+5+4+3+2+1, -11+11+6+5+4+3+2+1],
                [-11+6+5+4+3+2+1+0.5, -11+11+6+5+4+3+2+1+0.5],
            ]),
            abjad.glissando,
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.leaf(_, len(abjad.select.leaves(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(_, len(abjad.select.leaves(_))//2),
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", (9, 11)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=[4, 4, 3, 4, 3, 3, 4, 3, 2, 3, 3, 2, 3]),
            ),
            evans.loop(
                [-8],
                [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]
            ),
            evans.BendHandler([-3]),
            lambda _: swells(_, group_size=5, dyns=["mf", "f", "mp", "ff", "mf", "fff"]),
        ),
        ## Viola 2
        evans.MusicCommand(
            ("viola 2 voice", (0, 6)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=evans.Sequence([4, 4, 3, 4, 3, 3, 4, 3, 2, 3, 3, 2, 3]).rotate(-1)),
                pre_commands=[lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0])))]
            ),
            evans.loop(
                [-8],
                evans.Sequence([0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]).rotate(2)
            ),
            evans.BendHandler([-3]),
            lambda _: swells(_, group_size=6, dyns=["ff", "mf", "f", "mp"], hairpins=[">", "<"]),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (6, 8)),
            evans.talea([2, 3, 4, 2, 1], 8),
            evans.PitchHandler([
                [-11, -11+10],
                [-11+6, -11+10+6],
                [-11+6+5, -11+10+6+5],
                [-11+6+5+4, -11+10+6+5+4],
                [-11+6+5+4+3, -11+10+6+5+4+3],
                [-11+6+5+4+3+2, -11+10+6+5+4+3+2],
                [-11+6+5+4+3+2+1, -11+10+6+5+4+3+2+1],
                [-11+6+5+4+3+2+1+0.5, -11+10+6+5+4+3+2+1+0.5],
            ]),
            abjad.glissando,
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.leaf(_, len(abjad.select.leaves(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(_, len(abjad.select.leaves(_))//2),
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", (8, 11)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=evans.Sequence([4, 4, 3, 4, 3, 3, 4, 3, 2, 3, 3, 2, 3]).rotate(-1)),
            ),
            evans.loop(
                [-8],
                evans.Sequence([0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]).rotate(2)
            ),
            evans.BendHandler([-3]),
            lambda _: swells(_, group_size=6, dyns=["mf", "f", "mp", "ff", "mf", "fff"], hairpins=["<", ">"]),
        ),
        ## Viola 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 4)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=evans.Sequence([4, 4, 3, 4, 3, 3, 4, 3, 2, 3, 3, 2, 3]).rotate(-3)),
                pre_commands=[lambda _: rmakers.force_rest(abjad.select.get(abjad.select.tuplets(_), abjad.index([0, 1])))]
            ),
            evans.loop(
                [-8],
                evans.Sequence([0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]).rotate(4)
            ),
            evans.BendHandler([-3]),
            lambda _: swells(_, group_size=4, dyns=["ff", "mf", "f", "mp"], hairpins=[">", "<"]),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (4, 6)),
            evans.talea([3, 4, 2, 1, 2], 8),
            evans.PitchHandler([
                [-11, -11+9],
                [-11+6, -11+9+6],
                [-11+6+5, -11+9+6+5],
                [-11+6+5+4, -11+9+6+5+4],
                [-11+6+5+4+3, -11+9+6+5+4+3],
                [-11+6+5+4+3+2, -11+9+6+5+4+3+2],
                [-11+6+5+4+3+2+1, -11+9+6+5+4+3+2+1],
                [-11+6+5+4+3+2+1+0.5, -11+9+6+5+4+3+2+1+0.5],
            ]),
            abjad.glissando,
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.leaf(_, len(abjad.select.leaves(_))//2),
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(_, len(abjad.select.leaves(_))//2),
            ),
            evans.Attachment(
                abjad.StopHairpin(),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", (6, 11)),
            evans.accelerando(
                [(1, 2), (1, 15), (1, 16)],
                [(1, 16), (1, 3), (1, 16)],
                preprocessor=evans.make_preprocessor(quarters=True, fuse_counts=evans.Sequence([4, 4, 3, 4, 3, 3, 4, 3, 2, 3, 3, 2, 3]).rotate(-3)),
            ),
            evans.loop(
                [-8],
                evans.Sequence([0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]).rotate(4)
            ),
            evans.BendHandler([-3]),
            lambda _: swells(_, group_size=4, dyns=["mf", "f", "mp", "ff", "mf", "fff"], hairpins=["<", ">"]),
        ),
        ####
        # evans.call(
        #     "score",
        #     lambda _: evans.SegmentMaker.beam_score_without_splitting(_, better_tuplets=True),
        #     lambda _: abjad.select.components(_, abjad.Score),
        # ),
        # evans.attach(
        #     "Global Context",
        #     anemone.lib.mark_67,
        #     lambda _: abjad.select.leaf(_, 0),
        # ),
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
    time_signatures=anemone.signatures_05,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="05",
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
