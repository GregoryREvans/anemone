        \context Score = "Score"
        <<
            \context TimeSignatureContext = "Global Context"
            {

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 1]
                \tempo 4=100
                \mark \markup \bold {  }
                  %! scaling time signatures
                \time 4/4
                s1 * 1
                ^ \markup {
                  \raise #6 \with-dimensions-from \null
                  \override #'(font-size . 3)
                  \override #'(font-name . "Helvetica Bold")
                  \concat {
                      \abjad-metronome-mark-markup #2 #0 #1 #"100"
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
                \tempo 4=90
                s1 * 1
                ^ \markup {\translate #'(-2 . 1.5) \tiny \bold "rall."}
                \rallArrow #3

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 6]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 7]
                \tempo 4=80
                s1 * 1
                \stopTextSpan
                ^ \markup {
                  \with-dimensions-from \null
                  \override #'(font-size . 1)
                  \override #'(font-name . "Helvetica Bold")
                  \concat {
                      \abjad-metronome-mark-markup #2 #0 #1 #"80"
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
                                        \harmonicsOn
                                        \clef "alto"
                                        \override Staff.Stem.stemlet-length = 0.75
                                        cs32
                                        - \accent
                                        - \staccato
                                        \sfp
                                        [
                                        (
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \tweak bound-details.right.padding 0.5
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \tweak bound-details.right.stencil-align-dir-y #center
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \tweak staff-padding 6
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-markup \diamond-notehead-markup
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-right-markup \default-notehead-markup
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne
                                        \<

                                        a32
                                        - \staccato

                                        f'32
                                        - \staccato

                                        cs''32
                                        - \staccato
                                        )

                                        cs''32
                                        - \staccato
                                        (

                                        f'32
                                        - \staccato

                                        a32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        cs32
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        cs32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        a32
                                        - \staccato

                                        f'32
                                        - \staccato

                                        cs''32
                                        - \staccato
                                        )

                                        cs''32
                                        - \staccato
                                        (

                                        f'32
                                        - \staccato

                                        a32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        cs32
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        d32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        bf32
                                        - \staccato

                                        fs'32
                                        - \staccato

                                        d''32
                                        - \staccato
                                        )

                                        d''32
                                        - \accent
                                        - \staccato
                                        (

                                        fs'32
                                        - \staccato

                                        bf32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        d32
                                        - \accent
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        ef32
                                        - \staccato
                                        [
                                        (

                                        b32
                                        - \staccato

                                        g'32
                                        - \staccato

                                        ef''32
                                        - \staccato
                                        )

                                        ef''32
                                        - \accent
                                        - \staccato
                                        (

                                        g'32
                                        - \staccato

                                        b32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        ef32
                                        - \staccato
                                        )
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 2]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        f32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        cs'32
                                        - \accent
                                        - \staccato

                                        a'32
                                        - \staccato

                                        f''32
                                        - \accent
                                        - \staccato
                                        )

                                        f''32
                                        - \staccato
                                        (

                                        a'32
                                        - \staccato

                                        cs'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        f32
                                        - \accent
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        fs32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        d'32
                                        - \staccato

                                        bf'32
                                        - \staccato

                                        fs''32
                                        - \staccato
                                        )

                                        fs''32
                                        - \staccato
                                        (

                                        bf'32
                                        - \staccato

                                        d'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        fs32
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        g32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        ef'32
                                        - \staccato

                                        b'32
                                        - \staccato

                                        g''32
                                        - \staccato
                                        )

                                        g''32
                                        - \staccato
                                        (

                                        b'32
                                        - \staccato

                                        ef'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        g32
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        a32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        f'32
                                        - \staccato

                                        cs''32
                                        - \staccato

                                        a''32
                                        - \staccato
                                        )

                                        a''32
                                        - \accent
                                        - \staccato
                                        (

                                        cs''32
                                        - \staccato

                                        f'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        a32
                                        - \accent
                                        - \staccato
                                        \ff
                                        )
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                        ]
                                        \harmonicsOff

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 3]
                                        <bf b>1
                                        - \accent
                                        \sfp
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \tweak bound-details.right.padding 0.5
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \tweak bound-details.right.stencil-align-dir-y #center
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \tweak staff-padding 1
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-markup \diamond-notehead-markup
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-right-markup \default-notehead-markup
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne
                                          %! abjad.glissando(7)
                                        \glissando

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 4]
                                        <aqs bqf>1
                                        - \accent
                                          %! abjad.glissando(7)
                                        \glissando

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 5]
                                        <aqf aqs>1
                                        - \accent
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 6]
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        a1
                                        - \tweak circled-tip ##t
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 2
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            d'4

                                            \tweak NoteHead.style #'harmonic
                                            e'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 7]
                                        a2..
                                        \ff

                                        <cs' b'>8
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
                                        \bar "||"

                                    }

                                }

                            }

                        >>

                    }

                >>

            }

        >>
