  %! abjad.LilyPondFile._get_format_pieces()
\version "2.26.0"
  %! abjad.LilyPondFile._get_format_pieces()
\language "english"
\include "abjad.ily"
\include "../../build/segment_stylesheet.ily"
  %! abjad.LilyPondFile._get_format_pieces()
\score
  %! abjad.LilyPondFile._get_format_pieces()
{
    <<

        \context Score = "Score"
        <<
      { \include "layout.ly" }
            \context TimeSignatureContext = "Global Context"
            {

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 1]
                \tempo 4=91
                \mark \markup \bold {  }
                  %! scaling time signatures
                \time 4/4
                s1 * 1
                ^ \markup {
                  \raise #6 \with-dimensions-from \null
                  \override #'(font-size . 3)
                  \override #'(font-name . "Helvetica Bold")
                  \concat {
                      \abjad-metronome-mark-markup #2 #0 #1 #"91"
                  }
                }

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 2]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 3]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 4]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 5]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 6]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 7]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 8]
                \tempo 4=79
                s1 * 1
                ^ \markup {\translate #'(-2 . 1.5) \tiny \bold "rall."}
                \rallArrow #3

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 9]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 10]
                \tempo 4=67
                s1 * 1
                \stopTextSpan
                ^ \markup {
                  \with-dimensions-from \null
                  \override #'(font-size . 1)
                  \override #'(font-name . "Helvetica Bold")
                  \concat {
                      \abjad-metronome-mark-markup #2 #0 #1 #"67"
                  }
                }

            }

            \tag #'group1
            {

                \context StaffGroup = "Staff Group"
                <<

                    \tag #'group2
                    {

                        \context RemoveableStaffGroup = "sub group 1"
                        \with
                        {
                            instrumentName = \markup { \hcenter-in #14 "Viola I" }
                            shortInstrumentName = \markup { \hcenter-in #12 "va. I" }
                        }
                        <<

                            \tag #'voice1
                            {

                                \context VanishingStringStaff = "string 1 staff"
                                {

                                    \context Voice = "string 1 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 1]
                                        \override Staff.StaffSymbol.transparent = ##t
                                        \startStaff
                                        \stopStaff
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                            \tag #'voice2
                            {

                                \context VanishingBowStaff = "bow 1 staff"
                                {

                                    \context Voice = "bow 1 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 1]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                            \tag #'voice3
                            {

                                \context Staff = "viola 1 staff"
                                {

                                    \context Voice = "viola 1 voice"
                                    {

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 1]
                                            \clef "alto"
                                            <
                                                fs'
                                                \tweak style #'harmonic
                                                b'
                                            >4
                                            \mf
                                            \>
                                            \glissando

                                            <
                                                g'
                                                \tweak style #'harmonic
                                                c''
                                            >16
                                            \p

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            f32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan bf

                                            fs32

                                            g32

                                            af32

                                            bf32
                                            \p
                                            - \tweak circled-tip ##t
                                            \>

                                            a32

                                            af32

                                            fs32

                                            b32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                g
                                                \tweak style #'harmonic
                                                c'
                                            >2
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                af
                                                \tweak style #'harmonic
                                                df'
                                            >8
                                            :32
                                            \ff

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 2]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            bf32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan f'

                                            a32

                                            af32

                                            fs32
                                            \p
                                            - \tweak circled-tip ##t
                                            \>

                                            g32

                                            af32

                                            bf32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r32
                                            \stopTrillSpan
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        \pitchedTrill
                                        a'16
                                        (
                                        - \tweak circled-tip ##t
                                        \<
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan cs''

                                        bf'16

                                        \revert Staff.Stem.stemlet-length
                                        g'16
                                        \mp
                                        ]
                                        - \tweak circled-tip ##t
                                        \>

                                        \override Staff.Stem.stemlet-length = 0.75
                                        af'16
                                        [

                                        fs'16
                                        \!
                                        )

                                        r16
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        ]

                                        <cs' gs'>4
                                        \f

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 3]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            f'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan bf'

                                            af'16

                                            bf'16

                                            b'16
                                            \mp
                                            - \tweak circled-tip ##t
                                            \>

                                            bf'16

                                            cs''16

                                            c''16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                c''
                                                \tweak style #'harmonic
                                                f''
                                            >1
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                af
                                                \tweak style #'harmonic
                                                df'
                                            >4
                                            :32
                                            \ff

                                        }

                                        \times 16/17
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            d''32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan e''

                                            ef''32

                                            c''32

                                            bf'32

                                            b'32

                                            bf'32

                                            a'32

                                            af'32
                                            \mf
                                            - \tweak circled-tip ##t
                                            \>

                                            fs'32

                                            g'32

                                            af'32

                                            bf'32

                                            b'32

                                            c''32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 5]
                                        <cs' gs'>4
                                        \f

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        r16

                                        \pitchedTrill
                                        cs''16
                                        \p
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan fs''

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        \stopTrillSpan
                                        ]

                                        \times 8/11
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            d''32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan f''

                                            e''32

                                            ef''32

                                            d''32

                                            c''32
                                            \mf
                                            - \tweak circled-tip ##t
                                            \>

                                            g'32

                                            f'32

                                            fs'32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                c''
                                                \tweak style #'harmonic
                                                f''
                                            >4
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                g
                                                \tweak style #'harmonic
                                                c'
                                            >16
                                            :32
                                            \ff

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 6]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            g'16
                                            \sfp
                                            (
                                            - \tweak stencil #constante-hairpin
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan c''

                                            a'16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \!
                                            \stopTrillSpan
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        \pitchedTrill
                                        bf'16
                                        \f
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan f''

                                        r16
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        ]

                                        <
                                            a'
                                            \tweak style #'harmonic
                                            d''
                                        >2
                                        \mp
                                        \<
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 7]
                                        <
                                            a'
                                            \tweak style #'harmonic
                                            d''
                                        >4
                                        \f

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            a'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan cs''

                                            af'16

                                            ef'16

                                            d'16
                                            \f
                                            - \tweak circled-tip ##t
                                            \>

                                            c'16

                                            b16

                                            c'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                a
                                                \tweak style #'harmonic
                                                d'
                                            >4
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                cs''
                                                \tweak style #'harmonic
                                                fs''
                                            >16
                                            :32
                                            \ff

                                        }

                                        \times 8/11
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 8]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            cs'32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan fs'

                                            d'32

                                            e'32

                                            a32

                                            bf32
                                            \f
                                            - \tweak circled-tip ##t
                                            \>

                                            b32

                                            c'32

                                            d'32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r32
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            cs'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan ds'

                                            c'16

                                            bf16

                                            g16
                                            \ff
                                            - \tweak circled-tip ##t
                                            \>

                                            af16

                                            a16

                                            bf16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        <f' ef''>4
                                        \f

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 9]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        r16

                                        \pitchedTrill
                                        c'16
                                        \mp
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan f'

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        \stopTrillSpan
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        \pitchedTrill
                                        b16
                                        \mf
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan d'

                                        r16
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        ]

                                        \times 4/5
                                        {

                                            <
                                                b
                                                \tweak style #'harmonic
                                                e'
                                            >2
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                a
                                                \tweak style #'harmonic
                                                d'
                                            >8
                                            :32
                                            \ff

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 10]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        \pitchedTrill
                                        bf16
                                        (
                                        - \tweak circled-tip ##t
                                        \<
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan ef'

                                        af16

                                        \revert Staff.Stem.stemlet-length
                                        f16
                                        \ff
                                        ]
                                        - \tweak circled-tip ##t
                                        \>

                                        \override Staff.Stem.stemlet-length = 0.75
                                        fs16
                                        [

                                        g16
                                        \!
                                        )

                                        r16
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        ]

                                        <ef'' f''>4
                                        \f

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            af32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan ef'

                                            bf32

                                            a32

                                            af32
                                            \fff
                                            - \tweak circled-tip ##t
                                            \>

                                            fs32

                                            f32

                                            fs32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r32
                                            \stopTrillSpan
                                            ]
                                            \bar "||"

                                        }

                                    }

                                }

                            }

                            \tag #'voice4
                            {

                                \context VanishingChangeStaff = "change 1 staff"
                                {

                                    \context Voice = "change 1 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 1]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                        >>

                    }

                    \tag #'group3
                    {

                        \context RemoveableStaffGroup = "sub group 2"
                        \with
                        {
                            instrumentName = \markup { \hcenter-in #14 "Viola II" }
                            shortInstrumentName = \markup { \hcenter-in #12 "va. II" }
                        }
                        <<

                            \tag #'voice5
                            {

                                \context VanishingStringStaff = "string 2 staff"
                                {

                                    \context Voice = "string 2 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 1]
                                        \override Staff.StaffSymbol.transparent = ##t
                                        \startStaff
                                        \stopStaff
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 2 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                            \tag #'voice6
                            {

                                \context VanishingBowStaff = "bow 2 staff"
                                {

                                    \context Voice = "bow 2 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 1]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 2 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                            \tag #'voice7
                            {

                                \context Staff = "viola 2 staff"
                                {

                                    \context Voice = "viola 2 voice"
                                    {

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 1]
                                            \clef "alto"
                                            <
                                                fs'
                                                \tweak style #'harmonic
                                                b'
                                            >4
                                            \mf
                                            \>
                                            \glissando

                                            <
                                                g'
                                                \tweak style #'harmonic
                                                c''
                                            >16
                                            \p

                                        }

                                        \times 8/9
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            fs16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan b

                                            af16

                                            g16

                                            a16
                                            \p
                                            - \tweak circled-tip ##t
                                            \>

                                            bf16

                                            c'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                cs'
                                                \tweak style #'harmonic
                                                fs'
                                            >4
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                c''
                                                \tweak style #'harmonic
                                                f''
                                            >16
                                            :32
                                            \ff

                                        }

                                        \times 2/3
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 2]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            cs'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan gs'

                                            b16

                                            bf16

                                            a16

                                            g16
                                            \p
                                            - \tweak circled-tip ##t
                                            \>

                                            af16

                                            g16

                                            bf16

                                            af16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            a16
                                            \sfp
                                            (
                                            - \tweak stencil #constante-hairpin
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan cs'

                                            g16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \!
                                            \stopTrillSpan
                                            ]

                                        }

                                        <c'' df''>4
                                        \f

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 3]
                                        r8

                                        r8

                                        \override Staff.Stem.stemlet-length = 0.75
                                        \pitchedTrill
                                        fs8
                                        \p
                                        [
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan b

                                        \revert Staff.Stem.stemlet-length
                                        r8
                                        \stopTrillSpan
                                        ]

                                        \times 8/11
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            e16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan fs

                                            ef16

                                            f16

                                            fs16

                                            g16
                                            \mp
                                            - \tweak circled-tip ##t
                                            \>

                                            a16

                                            af16

                                            a16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 4]
                                            <
                                                af'
                                                \tweak style #'harmonic
                                                df''
                                            >2
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                cs''
                                                \tweak style #'harmonic
                                                fs''
                                            >8
                                            :32
                                            \ff

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r32
                                        [

                                        \pitchedTrill
                                        bf'32
                                        (
                                        - \tweak circled-tip ##t
                                        \<
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan ef''

                                        af'32

                                        g'32
                                        \mp
                                        - \tweak circled-tip ##t
                                        \>

                                        f'32

                                        fs'32
                                        \!
                                        )

                                        r32
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r32
                                        ]

                                        <a' e''>4
                                        \f

                                        \times 8/9
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 5]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            e'32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan g'

                                            ef'32

                                            fs'32

                                            f'32
                                            \mf
                                            - \tweak circled-tip ##t
                                            \>

                                            g'32

                                            af'32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r32
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            g'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan c''

                                            bf'16
                                            \mf
                                            - \tweak circled-tip ##t
                                            \>

                                            c''16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                c'
                                                \tweak style #'harmonic
                                                f'
                                            >2
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                fs
                                                \tweak style #'harmonic
                                                b
                                            >8
                                            :32
                                            \ff

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 6]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            cs''32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan gs''

                                            ef''32

                                            d''32
                                            \f
                                            - \tweak circled-tip ##t
                                            \>

                                            e''32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r32
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            f''8
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan a''

                                            d''8
                                            \f
                                            - \tweak circled-tip ##t
                                            \>

                                            \revert Staff.Stem.stemlet-length
                                            ef''8
                                            \!
                                            )
                                            ]

                                            \revert Staff.Stem.stemlet-length
                                            r4
                                            \stopTrillSpan

                                        }

                                        <
                                            b
                                            \tweak style #'harmonic
                                            e'
                                        >4
                                        \mp
                                        \<
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 7]
                                        <
                                            b
                                            \tweak style #'harmonic
                                            e'
                                        >4
                                        \f

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            cs''32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan fs''

                                            c''32

                                            cs''32

                                            bf'32

                                            af'32

                                            a'32

                                            g'32

                                            fs'32

                                            e'32
                                            \ff
                                            - \tweak circled-tip ##t
                                            \>

                                            ef'32

                                            f'32

                                            fs'32

                                            g'32

                                            a'32

                                            af'32

                                            a'32

                                            bf'32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                b
                                                \tweak style #'harmonic
                                                e'
                                            >4
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                g'
                                                \tweak style #'harmonic
                                                c''
                                            >16
                                            :32
                                            \ff

                                        }

                                        \times 2/3
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 8]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            c''16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan d''

                                            b'16
                                            \ff
                                            - \tweak circled-tip ##t
                                            \>

                                            cs''16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r32
                                        [

                                        \pitchedTrill
                                        d''32
                                        (
                                        - \tweak circled-tip ##t
                                        \<
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan g''

                                        e''32

                                        f''32
                                        \fff
                                        - \tweak circled-tip ##t
                                        \>

                                        ef''32

                                        d''32
                                        \!
                                        )

                                        r32
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r32
                                        ]

                                        <e'' d'''>4
                                        \f

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            cs''16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan e''

                                            b'16
                                            \fff
                                            - \tweak circled-tip ##t
                                            \>

                                            c''16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 8/9
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 9]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            b'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan e''

                                            fs'16

                                            f'16

                                            ef'16
                                            \p
                                            - \tweak circled-tip ##t
                                            \>

                                            d'16

                                            e'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                d''
                                                \tweak style #'harmonic
                                                g''
                                            >2
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                a'
                                                \tweak style #'harmonic
                                                d''
                                            >8
                                            :32
                                            \ff

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 10]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            f'16
                                            \sfp
                                            (
                                            - \tweak stencil #constante-hairpin
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan c''

                                            fs'16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \!
                                            \stopTrillSpan
                                            ]

                                        }

                                        <fs' e''>4
                                        \f

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r32
                                        [

                                        r32

                                        \pitchedTrill
                                        af'32
                                        (
                                        - \tweak circled-tip ##t
                                        \<
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan c''

                                        g'32

                                        af'32

                                        a'32

                                        g'32

                                        \revert Staff.Stem.stemlet-length
                                        af'32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        fs'32
                                        \p
                                        [
                                        - \tweak circled-tip ##t
                                        \>

                                        g'32

                                        f'32

                                        e'32

                                        ef'32

                                        cs'32

                                        d'32
                                        \!
                                        )

                                        \revert Staff.Stem.stemlet-length
                                        r32
                                        \stopTrillSpan
                                        ]
                                        \bar "||"

                                    }

                                }

                            }

                            \tag #'voice8
                            {

                                \context VanishingChangeStaff = "change 2 staff"
                                {

                                    \context Voice = "change 2 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 1]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 2 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                        >>

                    }

                    \tag #'group4
                    {

                        \context RemoveableStaffGroup = "sub group 3"
                        \with
                        {
                            instrumentName = \markup { \hcenter-in #14 "Viola III" }
                            shortInstrumentName = \markup { \hcenter-in #12 "va. III" }
                        }
                        <<

                            \tag #'voice9
                            {

                                \context VanishingStringStaff = "string 3 staff"
                                {

                                    \context Voice = "string 3 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 1]
                                        \override Staff.StaffSymbol.transparent = ##t
                                        \startStaff
                                        \stopStaff
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 3 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                            \tag #'voice10
                            {

                                \context VanishingBowStaff = "bow 3 staff"
                                {

                                    \context Voice = "bow 3 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 1]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 3 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                            \tag #'voice11
                            {

                                \context Staff = "viola 3 staff"
                                {

                                    \context Voice = "viola 3 voice"
                                    {

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 3 voice measure 1]
                                            \clef "alto"
                                            <
                                                fs'
                                                \tweak style #'harmonic
                                                b'
                                            >2
                                            \mf
                                            \>
                                            \glissando

                                            <
                                                g'
                                                \tweak style #'harmonic
                                                c''
                                            >8
                                            \p

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        \pitchedTrill
                                        bf16
                                        \p
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan ef'

                                        r16
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        ]

                                        \times 4/5
                                        {

                                            <
                                                cs''
                                                \tweak style #'harmonic
                                                fs''
                                            >4
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                d'
                                                \tweak style #'harmonic
                                                g'
                                            >16
                                            :32
                                            \ff

                                        }

                                        \times 2/3
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 3 voice measure 2]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r4

                                            \override Staff.Stem.stemlet-length = 0.75
                                            \pitchedTrill
                                            a8
                                            [
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan e'

                                            af8
                                            \p
                                            - \tweak circled-tip ##t
                                            \>

                                            g8
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 8/9
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            af16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan c'

                                            a16

                                            bf16

                                            c'16
                                            \p
                                            - \tweak circled-tip ##t
                                            \>

                                            b16

                                            c'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 3]
                                        <c'' df''>4
                                        \f

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            cs'32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan fs'

                                            b32

                                            a32

                                            fs32

                                            g32
                                            \mp
                                            - \tweak circled-tip ##t
                                            \>

                                            af32

                                            a32

                                            af32

                                            g32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r32
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 8/9
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            fs32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan gs

                                            e32

                                            f32

                                            e32
                                            \mp
                                            - \tweak circled-tip ##t
                                            \>

                                            ef32

                                            f32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                c'
                                                \tweak style #'harmonic
                                                f'
                                            >2
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                fs
                                                \tweak style #'harmonic
                                                b
                                            >8
                                            :32
                                            \ff

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            g32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan c'

                                            fs'32

                                            f'32
                                            \mf
                                            - \tweak circled-tip ##t
                                            \>

                                            af'32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        <ef'' f''>2
                                        \f

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 3 voice measure 5]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            g'16
                                            \sfp
                                            (
                                            - \tweak stencil #constante-hairpin
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan bf'

                                            af'16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \!
                                            \stopTrillSpan
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r8
                                        [

                                        \revert Staff.Stem.stemlet-length
                                        \pitchedTrill
                                        f'8
                                        \f
                                        ]
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan bf'

                                        r8
                                        \stopTrillSpan

                                        r8

                                        \times 4/5
                                        {

                                            <
                                                fs'
                                                \tweak style #'harmonic
                                                b'
                                            >4
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                fs
                                                \tweak style #'harmonic
                                                b
                                            >16
                                            :32
                                            \ff

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 3 voice measure 6]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            fs'16
                                            \sfp
                                            (
                                            - \tweak stencil #constante-hairpin
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan cs''

                                            e'16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \!
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 8/9
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            ef'32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan g'

                                            e'32

                                            ef'32

                                            f'32

                                            d''32

                                            ef''32

                                            c''32

                                            cs''32
                                            \mf
                                            - \tweak circled-tip ##t
                                            \>

                                            c''32

                                            ef''32

                                            d''32

                                            e''32

                                            f''32

                                            e''32

                                            f''32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        <
                                            fs'
                                            \tweak style #'harmonic
                                            b'
                                        >4
                                        \mp
                                        \<
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 7]
                                        <
                                            fs'
                                            \tweak style #'harmonic
                                            b'
                                        >4
                                        \f

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r32
                                            [

                                            \pitchedTrill
                                            ef''32
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan af''

                                            fs'32

                                            g'32

                                            af'32
                                            \f
                                            - \tweak circled-tip ##t
                                            \>

                                            a'32

                                            af'32

                                            g'32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            <
                                                cs''
                                                \tweak style #'harmonic
                                                fs''
                                            >4
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                d'
                                                \tweak style #'harmonic
                                                g'
                                            >16
                                            :32
                                            \ff

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        r16

                                        \pitchedTrill
                                        fs'16
                                        \mp
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan gs'

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        \stopTrillSpan
                                        ]

                                        \times 2/3
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 3 voice measure 8]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            e'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan a'

                                            f'16

                                            e'16

                                            ef'16

                                            f'16
                                            \f
                                            - \tweak circled-tip ##t
                                            \>

                                            g'16

                                            fs'16

                                            f'16

                                            e'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \stopTrillSpan
                                            ]

                                        }

                                        <c'' df''>4
                                        \f

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            ef'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan gf'

                                            e'16
                                            \ff
                                            - \tweak circled-tip ##t
                                            \>

                                            f'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 9]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        \pitchedTrill
                                        fs'16
                                        \mf
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan b'

                                        r16
                                        \stopTrillSpan

                                        \revert Staff.Stem.stemlet-length
                                        r16
                                        ]

                                        \times 4/5
                                        {

                                            <
                                                c'
                                                \tweak style #'harmonic
                                                f'
                                            >2.
                                            :32
                                            \sfp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<
                                            \glissando

                                            <
                                                fs
                                                \tweak style #'harmonic
                                                b
                                            >8.
                                            :32
                                            \ff

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 3 voice measure 10]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            \pitchedTrill
                                            af'16
                                            \sfp
                                            (
                                            - \tweak stencil #constante-hairpin
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan ef''

                                            g'16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r8
                                            \!
                                            \stopTrillSpan
                                            ]

                                        }

                                        <ef'' f''>4
                                        \f

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r8
                                            [

                                            \pitchedTrill
                                            af'16
                                            (
                                            - \tweak circled-tip ##t
                                            \<
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan c''

                                            a'16

                                            g'16

                                            f'16

                                            af'16
                                            \ff
                                            - \tweak circled-tip ##t
                                            \>

                                            g'16

                                            fs'16

                                            f'16

                                            ef'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            \stopTrillSpan
                                            ]
                                            \bar "||"

                                        }

                                    }

                                }

                            }

                            \tag #'voice12
                            {

                                \context VanishingChangeStaff = "change 3 staff"
                                {

                                    \context Voice = "change 3 voice"
                                    {

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 1]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 2]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 3]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 4]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 6]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 7]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 8]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 3 voice measure 10]
                                        r1
                                        \bar "||"

                                    }

                                }

                            }

                        >>

                    }

                >>

            }

        >>
    >>
  %! abjad.LilyPondFile._get_format_pieces()
}