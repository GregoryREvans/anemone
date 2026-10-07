        \context Score = "Score"
        <<
            \context TimeSignatureContext = "Global Context"
            {

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 1]
                \tempo 4=120
                \mark \markup \bold {  }
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 2]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 3]
                  %! scaling time signatures
                \time 5/8
                s1 * 5/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 4]
                  %! scaling time signatures
                \time 2/4
                s1 * 1/2

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 5]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 6]
                  %! scaling time signatures
                \time 7/8
                s1 * 7/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 7]
                  %! scaling time signatures
                \time 3/4
                s1 * 3/4

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 8]
                  %! scaling time signatures
                \time 5/8
                s1 * 5/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 9]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 10]
                  %! scaling time signatures
                \time 3/4
                s1 * 3/4

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 11]
                  %! scaling time signatures
                \time 2/4
                s1 * 1/2

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 12]
                  %! scaling time signatures
                \time 3/4
                s1 * 3/4

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 13]
                  %! scaling time signatures
                \time 2/4
                s1 * 1/2

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 14]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 15]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 16]
                  %! scaling time signatures
                \time 5/8
                s1 * 5/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 17]
                  %! scaling time signatures
                \time 2/4
                s1 * 1/2

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 18]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 19]
                  %! scaling time signatures
                \time 7/8
                s1 * 7/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 20]
                  %! scaling time signatures
                \time 3/4
                s1 * 3/4

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 21]
                  %! scaling time signatures
                \time 5/8
                s1 * 5/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 22]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

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
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 4]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 6]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 7]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 8]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 10]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 11]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 12]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 13]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 14]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 15]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 16]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 17]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 18]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 19]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 20]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 21]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 22]
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
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 4]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 6]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 7]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 8]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 10]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 11]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 12]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 13]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 14]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 15]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 16]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 17]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 18]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 19]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 20]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 21]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 22]
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

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 1]
                                        \clef "alto"
                                        r4

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            fs16
                                            [
                                            (
                                            - \tweak circled-tip ##t
                                            \<

                                            g16

                                            af16

                                            a16

                                            \revert Staff.Stem.stemlet-length
                                            bf16
                                            ]

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            cs'16
                                            [

                                            b16

                                            c'16

                                            cs'16

                                            ef'16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            g16
                                            ]
                                            (

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        af16
                                        [

                                        a16

                                        bf16

                                        \revert Staff.Stem.stemlet-length
                                        b16
                                        ]

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 2]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            d'32
                                            [

                                            c'32

                                            cs'32

                                            d'32

                                            e'32
                                            )

                                            a32
                                            (

                                            \revert Staff.Stem.stemlet-length
                                            bf32
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            b16
                                            [

                                            c'16

                                            cs'16

                                            e'16
                                            \ff
                                            - \tweak circled-tip ##t
                                            \>

                                            \revert Staff.Stem.stemlet-length
                                            d'16
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        ef'16
                                        [

                                        e'16

                                        fs'16
                                        )

                                        \revert Staff.Stem.stemlet-length
                                        af16
                                        ]
                                        (

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            a16
                                            [

                                            bf16

                                            b16

                                            c'16

                                            ef'16

                                            \revert Staff.Stem.stemlet-length
                                            cs'16
                                            ]

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 3]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            d'32
                                            [

                                            ef'32

                                            f'32
                                            )

                                            b32
                                            (

                                            c'32

                                            cs'32

                                            \revert Staff.Stem.stemlet-length
                                            d'32
                                            ]

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            ef'16
                                            [

                                            fs'16

                                            e'16

                                            f'16

                                            fs'16

                                            \revert Staff.Stem.stemlet-length
                                            af'16
                                            \!
                                            )
                                            ]

                                        }

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 4]
                                        ef''2
                                        \ff

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 5]
                                        r4

                                        \override Staff.Stem.stemlet-length = 0.75
                                        \pitchedTrill
                                        a8
                                        \f
                                        [
                                        - \tweak stencil #abjad-flared-hairpin
                                        \>
                                        - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                        \startTrillSpan d'

                                        \revert Staff.Stem.stemlet-length
                                        bf8
                                        ]

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            b8
                                            \mp
                                            [
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<

                                            bqs8

                                            \revert Staff.Stem.stemlet-length
                                            bf8
                                            \ff
                                            ]

                                        }

                                        r4
                                        \stopTrillSpan

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 6]
                                        \vibrato #'(1 5 1 2) #2 #0.2
                                        ef''2..
                                        :32
                                        \ff
                                        ~
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        - \tweak staff-padding 4.5
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        \startTrillSpan

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 7]
                                        ef''2.
                                        :32
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 8]
                                        ef''4.
                                        :32
                                        ~

                                        ef''4
                                        :32

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 9]
                                        r4
                                        \stopTrillSpan

                                        \override Staff.Stem.stemlet-length = 0.75
                                        r16
                                        [

                                        \harmonicsOn
                                        bf16
                                        (
                                        - \tweak circled-tip ##t
                                        \<

                                        b16

                                        \revert Staff.Stem.stemlet-length
                                        c'16
                                        ]

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            cs'16
                                            [

                                            d'16

                                            f'16

                                            ef'16

                                            \revert Staff.Stem.stemlet-length
                                            e'16
                                            ]

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            f'16
                                            )
                                            [

                                            b16
                                            (

                                            c'16

                                            cs'16

                                            d'16

                                            \revert Staff.Stem.stemlet-length
                                            ef'16
                                            ]

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 10]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            fs'32
                                            [

                                            e'32

                                            f'32

                                            fs'32
                                            \ff
                                            )
                                            - \tweak circled-tip ##t
                                            \>

                                            cs'32
                                            (

                                            d'32

                                            \revert Staff.Stem.stemlet-length
                                            ef'32
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        e'16
                                        [

                                        f'16

                                        af'16

                                        \revert Staff.Stem.stemlet-length
                                        fs'16
                                        ]

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            g'16
                                            [

                                            af'16
                                            )

                                            c'16
                                            (

                                            cs'16

                                            d'16

                                            \revert Staff.Stem.stemlet-length
                                            ef'16
                                            ]

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 11]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            e'16
                                            [

                                            g'16

                                            f'16

                                            fs'16
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            ]

                                        }

                                        r4
                                        \harmonicsOff

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 12]
                                        eqf''2.
                                        \ff

                                        <<

                                            \context Voice = "viola 1 voice temp"
                                            {

                                                  %! COMMENT_MEASURE_NUMBERS
                                                  %! evans.SegmentMaker.comment_measure_numbers()
                                                % [viola 1 voice temp measure 13]
                                                \override Staff.Stem.stemlet-length = 0.75
                                                \voiceTwo
                                                cs'8
                                                \ff
                                                [

                                                \revert Staff.Stem.stemlet-length
                                                b8
                                                ]

                                                \override Staff.Stem.stemlet-length = 0.75
                                                d'8
                                                [

                                                \revert Staff.Stem.stemlet-length
                                                c'8
                                                ]

                                            }

                                            \context Voice = "intermittent_voice"
                                            {

                                                \times 4/5
                                                {

                                                      %! COMMENT_MEASURE_NUMBERS
                                                      %! evans.SegmentMaker.comment_measure_numbers()
                                                    % [intermittent_voice measure 13]
                                                    \override Staff.Stem.stemlet-length = 0.75
                                                    \voiceOne
                                                    cs''8
                                                    [

                                                    af8

                                                    b'8

                                                    fs8

                                                    \revert Staff.Stem.stemlet-length
                                                    bf'8
                                                    ]

                                                }

                                            }

                                        >>
                                        \oneVoice

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 14]
                                        \vibrato #'(1 5 1 2) #2 #0.2
                                        e''1
                                        :32
                                        \ff
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        - \tweak staff-padding 4.5
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        \startTrillSpan

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 15]
                                        r4
                                        \stopTrillSpan

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            \pitchedTrill
                                            bf8
                                            \f
                                            [
                                            - \tweak stencil #abjad-flared-hairpin
                                            \>
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan ef'

                                            b8

                                            \revert Staff.Stem.stemlet-length
                                            c'8
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        cqs'8
                                        [

                                        \revert Staff.Stem.stemlet-length
                                        b8
                                        ]

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            a8
                                            [

                                            b8
                                            \mp
                                            - \tweak stencil #abjad-flared-hairpin
                                            \<

                                            \revert Staff.Stem.stemlet-length
                                            c'8
                                            ]

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 16]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        cs'8
                                        [

                                        dqf'8

                                        \revert Staff.Stem.stemlet-length
                                        c'8
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        bf8
                                        \ff
                                        [

                                        \revert Staff.Stem.stemlet-length
                                        r8
                                        \stopTrillSpan
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 17]
                                        r4

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            r16
                                            [

                                            d'16
                                            :32
                                            (
                                            - \tweak circled-tip ##t
                                            \<

                                            ef'16
                                            :32

                                            e'16
                                            :32

                                            f'16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            fs'16
                                            :32
                                            ]

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 18]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            a'32
                                            :32
                                            [

                                            g'32
                                            :32
                                            )

                                            ef'32
                                            :32
                                            (

                                            e'32
                                            :32

                                            f'32
                                            :32

                                            fs'32
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            g'32
                                            :32
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        bf'16
                                        :32
                                        [

                                        af'16
                                        :32
                                        )

                                        f'16
                                        :32
                                        (

                                        \revert Staff.Stem.stemlet-length
                                        fs'16
                                        :32
                                        ]

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            g'16
                                            :32
                                            [

                                            af'16
                                            :32

                                            a'16
                                            :32

                                            c''16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            bf'16
                                            :32
                                            )
                                            ]

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            e'16
                                            :32
                                            \ff
                                            [
                                            (
                                            - \tweak circled-tip ##t
                                            \>

                                            f'16
                                            :32

                                            fs'16
                                            :32

                                            g'16
                                            :32

                                            af'16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            b'16
                                            :32
                                            ]

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 19]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        a'16
                                        :32
                                        )
                                        [

                                        g'16
                                        :32
                                        (

                                        af'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        a'16
                                        :32
                                        ]

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            bf'32
                                            :32
                                            [

                                            b'32
                                            :32

                                            d''32
                                            :32

                                            c''32
                                            :32
                                            )

                                            fs'32
                                            :32
                                            (

                                            g'32
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            af'32
                                            :32
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            a'16
                                            :32
                                            [

                                            bf'16
                                            :32

                                            cs''16
                                            :32

                                            b'16
                                            :32
                                            \!
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            r16
                                            ]

                                        }

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 20]
                                        \vibrato #'(1 5 1 2) #2 #0.2
                                        eqs''2.
                                        \ff
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        - \tweak staff-padding 4.5
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        \startTrillSpan

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 21]
                                        r4
                                        \stopTrillSpan

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            \pitchedTrill
                                            b8
                                            \f
                                            [
                                            - \tweak stencil #abjad-flared-hairpin
                                            \>
                                            - \tweak TrillPitchHead.stencil #(lambda (grob) (grob-interpret-markup grob #{ \markup \musicglyph #"noteheads.s0harmonic" #}))
                                            \startTrillSpan e'

                                            c'8

                                            \revert Staff.Stem.stemlet-length
                                            cs'8
                                            ]

                                        }

                                        dqf'8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 22]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        c'8
                                        [

                                        \revert Staff.Stem.stemlet-length
                                        bf8
                                        \mp
                                        ]
                                        - \tweak stencil #abjad-flared-hairpin
                                        \<

                                        \override Staff.Stem.stemlet-length = 0.75
                                        cqs'8
                                        [

                                        \revert Staff.Stem.stemlet-length
                                        dqf'8
                                        ]

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            dqs'8
                                            [

                                            ef'8

                                            \revert Staff.Stem.stemlet-length
                                            dqf'8
                                            \ff
                                            ]

                                        }

                                        r4
                                        \stopTrillSpan
                                        \bar "||"

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
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 4]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 5]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 6]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 7]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 8]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 9]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 10]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 11]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 12]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 13]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 14]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 15]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 16]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 17]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 18]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 19]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 20]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 21]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 22]
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
