import pathlib
from fractions import Fraction
from random import choice, seed

import abjad
import baca
import evans
from abjadext import rmakers

import anemone


def trill(selections):
    ties = abjad.select.logical_ties(selections, pitched=True)
    for tie in ties:
        start = tie[0]
        end = abjad.get.leaf(tie[-1], 1)
        abjad.attach(abjad.StartTrillSpan(), start)
        abjad.attach(abjad.StopTrillSpan(), end)


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
    fermata_measures=anemone.fermata_measures_01,
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
        ## VIOLA 1
        # [2, 4, 5, 5, 4, 3, 5, 4, 6, 6, 5, 6, 6, 6, 6, 3, 1, 1, 5, 6, 6, 6, 6, 5, 6, 4, 5, 2, 6, 6, 5, 3, 5, 4, 5, 1, 4, 5, 5, 6, 6]
        evans.MusicCommand(
            ("viola 1 voice", (0, 2)),
            evans.even_division(
                [32],
                preprocessor=evans.make_preprocessor(
                    eighths=True,
                    fuse_counts=[2, 4, 5, 5, 4, 3, 5, 4, 6, 6, 5, 6, 6, 6, 6, 3, 1, 1, 5, 6, 6, 6, 6, 5, 6, 4, 5, 2, 6, 6, 5, 3, 5, 4, 5, 1, 4, 5, 5, 6, 6],
                ),
                rewrite=-2,
                beam_meter=True,
            ),
            evans.loop(
                [-11, -11+8, -11+8+8, -11+8+8+8, -11+8+8+8, -11+8+8, -11+8, -11],
                [0, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]
            ),
            evans.ArticulationHandler(["staccato"]),
            evans.ArticulationHandler(["accent"], articulation_boolean_vector=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]),
            evans.slur([4]),
            abjad.LilyPondLiteral(r"\harmonicsOn", site="before"),
            evans.Attachment(
                abjad.LilyPondLiteral(r"\harmonicsOff", site="after"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            evans.text_span(
                [
                    r"\diamond-notehead-markup",
                    r"\default-notehead-markup",
                ],
                "->",
                padding=6,
                id=1,
                # font="Helvetica Bold"
            ),
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [2, 3, 4]),
            evans.note(),
            evans.PitchHandler([[-1, -2], [-1.5, -2.5], [-2.5, -3.5],]),
            evans.ArticulationHandler(["accent"]),
            abjad.glissando,
            abjad.Dynamic("sfp"),
            evans.text_span(
                [
                    r"\diamond-notehead-markup",
                    r"\default-notehead-markup",
                ],
                "->",
                padding=1,
                id=1,
                # font="Helvetica Bold"
            ),
        ),
        evans.MusicCommand(
            ("viola 1 voice", [5, 6]),
            evans.talea([60], 8, end_counts=[1]),
            evans.PitchHandler(["a", [evans.JIPitch("a,,", "5/1", with_quarter_tones=True), evans.JIPitch("a,,", "9/1", with_quarter_tones=True)]]),
            abjad.LilyPondLiteral(
                r"\once \override TrillSpanner.stencil = #line-spanner-multiple-lines",
                site="before",
            ),
            abjad.bundle(
                abjad.StartTrillSpan(),
                r"- \tweak details.n-copies 2",
                r"- \tweak details.pad-copies 0.3",
                r"- \tweak bound-details.left.stencil-offset #'(0 . -1.4)",
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -2),
            ),
            evans.Attachment(
                evans.AfterGraceContainer(
                    [abjad.Note("d'4"), abjad.Note("e'4")],
                    as_trill_heads=True,
                    harmonics=True,
                ),
                selector=lambda _: abjad.select.note(_, 0),
            ),
        ),
        ## VIOLA 2
        # [4, 3, 5, 1, 2, 1, 2, 2, 3, 4, 5, 4, 5, 3, 6, 2, 4, 3, 4, 2, 2, 5, 6, 5, 6, 6, 6, 3, 1, 2, 6, 3, 4, 6, 6, 6, 5, 6, 6, 2, 5]
        evans.MusicCommand(
            ("viola 2 voice", (0, 2)),
            evans.note(
                preprocessor=evans.make_preprocessor(
                    eighths=True,
                    fuse_counts=[4, 3, 5, 1, 2, 1, 2, 2, 3, 4, 5, 4, 5, 3, 6, 2, 4, 3, 4, 2, 2, 5, 6, 5, 6, 6, 6, 3, 1, 2, 6, 3, 4, 6, 6, 6, 5, 6, 6, 2, 5],
                ),
                rewrite=-2,
                beam_meter=True,
            ),
            evans.PitchHandler(
                evans.Sequence([3, 4, 5, 4, 6, 3, 6, 7, 3, 2, 7, 8]).transpose(-6).rotate(0)
            ),
            evans.trill(
                counts=[1],
                cyclic=True,
                alteration="P4",
                harmonic=True,
                padding=2,
                right_padding=0,
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.leaf(
                    _, len(abjad.select.leaves(_)) // 2
                ),
            ),
            evans.Attachment(
                abjad.StartHairpin(">o"),
                selector=lambda _: abjad.select.leaf(
                    _, len(abjad.select.leaves(_)) // 2
                ),
            ),
            evans.Attachment(
                abjad.StopHairpin(), selector=lambda _: abjad.select.leaf(_, -1)
            ),
            abjad.Clef("alto"),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [2, 3]),
            evans.talea(
                [8, 4],
                8,
                # extra_counts=[0, 1, 0, 1, -1],
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-2,
            ),
            evans.PitchHandler([[0, -3], [-1, -4], [-3, -6],]),
            evans.ArticulationHandler(["accent"]),
            abjad.glissando,
            abjad.Dynamic("sfp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("mf"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            evans.text_span(
                [
                    r"\diamond-notehead-markup",
                    r"\default-notehead-markup",
                ],
                "->",
                padding=1.5,
                id=1,
                # font="Helvetica Bold"
            ),
        ),
        evans.MusicCommand(
            ("viola 2 voice", [4, 5, 6]),
            evans.talea([60], 8, end_counts=[1]),
            evans.PitchHandler([-6, [evans.JIPitch("a,,", "7/1", with_quarter_tones=True), evans.JIPitch("a,,", "13/1", with_quarter_tones=True)]]),
            abjad.LilyPondLiteral(
                r"\once \override TrillSpanner.stencil = #line-spanner-multiple-lines",
                site="before",
            ),
            abjad.bundle(
                abjad.StartTrillSpan(),
                r"- \tweak details.n-copies 3",
                r"- \tweak details.pad-copies 0.3",
                r"- \tweak bound-details.left.stencil-offset #'(0 . -1.4)",
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -2),
            ),
            evans.Attachment(
                evans.AfterGraceContainer(
                    [abjad.Note("gs4"), abjad.Note("a4"), abjad.Note("as4")],
                    as_trill_heads=True,
                    harmonics=True,
                ),
                selector=lambda _: abjad.select.note(_, 0),
            ),
        ),
        ## VIOLA 3
        evans.MusicCommand(
            ("viola 3 voice", (0, 2)),
            evans.note(
                preprocessor=evans.make_preprocessor(
                    eighths=True,
                    fuse_counts=[1, 3, 1, 3, 4, 3, 3, 2, 4, 3, 2, 4, 5, 2, 4, 2, 5, 6, 6, 6, 3, 4, 1, 3, 1, 2, 4, 2, 1, 2, 3, 4, 2, 4, 5, 4, 3, 5, 4, 2, 5],
                ),
                pre_commands=[
                    lambda _: [rmakers.force_rest(x) for x in abjad.select.get(abjad.select.leaves(_), abjad.index([0, 2, 4], 7))]
                ],
                rewrite=-2,
            ),
            evans.PitchHandler([_ + 2 for _ in [-9, -10, -9, -11, -8]]),
            evans.BendHandler([-2, -2, 1, -3]),
            abjad.Dynamic("f"),
            evans.Attachment(
                abjad.Clef("alto"),
                selector=lambda _: abjad.select.leaf(_, 0),
            ),
            trill,
        ),
        evans.MusicCommand(
            ("viola 3 voice", [2, 3, 4, 5]),
            evans.talea(
                [7, 3],
                8,
                extra_counts=[0, 1, 0, 1, -1],
                preprocessor=evans.make_preprocessor(quarters=True),
                rewrite=-2,
            ),
            evans.PitchHandler([
                [-5+.5, -5],
                [-4+1, -4],
                [-3+1.5, -3],
                [-2+2, -2],
                [-1+2.5, -1],
                [0+3, 0],
                [1+3.5, 1],
            ]),
            evans.ArticulationHandler(["accent"]),
            abjad.glissando,
            abjad.Dynamic("mp"),
            abjad.StartHairpin("<"),
            evans.Attachment(
                abjad.Dynamic("f"),
                selector=lambda _: abjad.select.leaf(_, 2),
            ),
            evans.Attachment(
                abjad.StartHairpin(">"),
                selector=lambda _: abjad.select.leaf(_, 2),
            ),
            evans.Attachment(
                abjad.Dynamic("mp"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            evans.text_span(
                [
                    r"\diamond-notehead-markup",
                    r"\default-notehead-markup",
                ],
                "->",
                [3, 4],
                padding=2,
                id=1,
                # font="Helvetica Bold"
            ),
        ),
        evans.MusicCommand(
            ("viola 3 voice", 6),
            evans.talea([60], 8, end_counts=[1]),
            evans.PitchHandler(["cs'", [evans.JIPitch("a,,", "11/1", with_quarter_tones=True), evans.JIPitch("a,,", "15/1", with_quarter_tones=True)]]),
            abjad.LilyPondLiteral(
                r"\once \override TrillSpanner.stencil = #line-spanner-multiple-lines",
                site="before",
            ),
            abjad.bundle(
                abjad.StartTrillSpan(),
                r"- \tweak details.n-copies 1",
                r"- \tweak details.pad-copies 0.3",
                r"- \tweak bound-details.left.stencil-offset #'(0 . -1.4)",
            ),
            evans.Attachment(
                abjad.StopTrillSpan(),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            abjad.StartHairpin("o<"),
            evans.Attachment(
                abjad.Dynamic("ff"),
                selector=lambda _: abjad.select.leaf(_, -1),
            ),
            evans.Attachment(
                evans.AfterGraceContainer(
                    [abjad.Note("fs'4")],
                    as_trill_heads=True,
                    harmonics=True,
                ),
                selector=lambda _: abjad.select.note(_, 0),
            ),
        ),
        ## GLOBAL CONTEXT
        # evans.attach(
        #     "Global Context",
        #     abjad.Markup(r'''\markup \override #'(font-name . "Helvetica Bold") { \raise #1.5 \left-brace #1 \with-color #(rgb-color 0.6 0.6 1) A \with-color #(rgb-color 0.961 0.961 0.406) B \with-color #(rgb-color 1 0.2 0.2) D \with-color #(rgb-color 0.2 1 0.592) C \raise #1.5 \right-brace #2 }'''),
        #     selector=lambda _: abjad.select.leaf(_, 0),
        #     direction=abjad.UP
        # ),
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
            selector=lambda _: abjad.select.leaf(_, 4)
        ),
        evans.attach(
            "Global Context",
            abjad.Markup(r"""\markup {\translate #'(-2 . 1.5) \tiny \bold "rall."}"""),
            selector=lambda _: abjad.select.leaf(_, 4),
            direction=abjad.UP,
        ),
        evans.attach(
            "Global Context",
            abjad.LilyPondLiteral(r"\rallArrow #3", site="after"),
            selector=lambda _: abjad.select.leaf(_, 4),
        ),
        evans.attach(
            "Global Context",
            abjad.StopTextSpan(),
            selector=lambda _: abjad.select.leaf(_, 6)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.mark_80_small,
            selector=lambda _: abjad.select.leaf(_, 6)
        ),
        evans.attach(
            "Global Context",
            anemone.lib.met_80,
            selector=lambda _: abjad.select.leaf(_, 6)
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
    time_signatures=anemone.signatures_01,
    clef_handlers=None,
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "abjad.ily",
        "../../build/segment_stylesheet.ily",
    ],
    segment_name="01",
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
