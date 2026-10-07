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
                \time 7/8
                s1 * 7/8
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
                  %! scaling time signatures
                \time 4/4
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
                \time 3/4
                s1 * 3/4

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 5]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 6]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 7]
                  %! scaling time signatures
                \time 2/4
                s1 * 1/2

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
                \time 2/4
                s1 * 1/2

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
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 12]
                  %! scaling time signatures
                \time 5/8
                s1 * 5/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 13]
                  %! scaling time signatures
                \time 3/4
                s1 * 3/4

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 14]
                  %! scaling time signatures
                \time 7/8
                s1 * 7/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 15]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 16]
                  %! scaling time signatures
                \time 2/4
                s1 * 1/2

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 17]
                  %! scaling time signatures
                \time 5/8
                s1 * 5/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 18]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 19]
                s1 * 1

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
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 22]
                  %! scaling time signatures
                \time 2/4
                s1 * 1/2

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 23]
                  %! scaling time signatures
                \time 7/8
                s1 * 7/8

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 24]
                  %! scaling time signatures
                \time 4/4
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 25]
                  %! scaling time signatures
                \time 5/8
                s1 * 5/8

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
                                        r2..

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
                                        r2.

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
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 8]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 9]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 10]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 11]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 12]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 13]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 14]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 15]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 16]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 17]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 18]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 19]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 20]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 21]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 22]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 23]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 24]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 25]
                                        r2

                                        r8
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
                                        r2..

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
                                        r2.

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
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 8]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 9]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 10]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 11]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 12]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 13]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 14]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 15]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 16]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 17]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 18]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 19]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 20]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 21]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 22]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 23]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 24]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 25]
                                        r2

                                        r8
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
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \clef "alto"
                                        \afterGrace
                                        g2..
                                        \p
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            c'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 2]
                                        g1
                                        \f
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 3]
                                        g4.
                                        ~

                                        g4
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 4]
                                        g2.
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 5]
                                        g1
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 6]
                                        g1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 7]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        d16
                                        :32
                                        \stopTrillSpan
                                        [
                                        - \tweak circled-tip ##t
                                        \<

                                        ds16
                                        :32

                                        e16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        d16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        e16
                                        :32
                                        \ff
                                        [
                                        - \tweak circled-tip ##t
                                        \>

                                        ds16
                                        :32

                                        e16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        f16
                                        :32
                                        \!
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 8]
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        a4.
                                        \p
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


                                        a4
                                        \f
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 9]
                                        a2
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 10]
                                        a2.
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 11]
                                        a1

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 12]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            ds16
                                            :32
                                            \stopTrillSpan
                                            [
                                            - \tweak circled-tip ##t
                                            \<

                                            e16
                                            :32

                                            f16
                                            :32

                                            ds16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            f16
                                            :32
                                            ]

                                        }

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            e16
                                            :32
                                            [

                                            f16
                                            :32
                                            \ff
                                            - \tweak circled-tip ##t
                                            \>

                                            fs16
                                            :32

                                            f16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            e16
                                            :32
                                            ]

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            f16
                                            :32
                                            [

                                            fs16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            e16
                                            :32
                                            \!
                                            ]

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 13]
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        b2.
                                        \p
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            ds'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 14]
                                        b2..
                                        \f

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 15]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        e16
                                        :32
                                        \stopTrillSpan
                                        [
                                        - \tweak circled-tip ##t
                                        \<

                                        f16
                                        :32

                                        fs16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        e16
                                        :32
                                        ]

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            fs16
                                            :32
                                            [

                                            f16
                                            :32

                                            fs16
                                            :32

                                            g16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            fs16
                                            :32
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        fs16
                                        :32
                                        [

                                        g16
                                        :32

                                        gs16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        fs16
                                        :32
                                        ]

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            gs16
                                            :32
                                            [

                                            g16
                                            :32

                                            gs16
                                            :32

                                            a16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            gs16
                                            :32
                                            ]

                                        }

                                        \times 4/5
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 16]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            gs16
                                            :32
                                            [

                                            a16
                                            :32

                                            as16
                                            :32

                                            gs16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            as16
                                            :32
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        a16
                                        :32
                                        [

                                        as16
                                        :32

                                        b16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        as16
                                        :32
                                        \f
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 17]
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        c'4.
                                        \p
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 3
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            d'4

                                            \tweak NoteHead.style #'harmonic
                                            ef'4

                                            \tweak NoteHead.style #'harmonic
                                            e'4
                                            \revert Stem.stencil

                                        }


                                        c'4
                                        \f

                                        \times 2/3
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 18]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            f16
                                            :32
                                            \stopTrillSpan
                                            [
                                            - \tweak circled-tip ##t
                                            \<

                                            fs16
                                            :32

                                            g16
                                            :32

                                            f16
                                            :32

                                            g16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            fs16
                                            :32
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        g16
                                        :32
                                        [

                                        gs16
                                        :32

                                        g16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        g16
                                        :32
                                        ]

                                        \times 4/5
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            gs16
                                            :32
                                            [

                                            a16
                                            :32

                                            g16
                                            :32

                                            a16
                                            :32

                                            \revert Staff.Stem.stemlet-length
                                            gs16
                                            :32
                                            ]

                                        }

                                        \override Staff.Stem.stemlet-length = 0.75
                                        a16
                                        :32
                                        [

                                        as16
                                        :32

                                        a16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        a16
                                        :32
                                        \ff
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 19]
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        d'1
                                        \p
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            g'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 20]
                                        d'2.
                                        \f
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 21]
                                        d'1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 22]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        fs16
                                        :32
                                        \stopTrillSpan
                                        [
                                        - \tweak circled-tip ##t
                                        \<

                                        g16
                                        :32

                                        gs16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        fs16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        gs16
                                        :32
                                        [

                                        g16
                                        :32

                                        gs16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        a16
                                        :32
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 23]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        gs16
                                        :32
                                        [

                                        a16
                                        :32

                                        as16
                                        :32

                                        b16
                                        :32

                                        a16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        b16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        as16
                                        :32
                                        [

                                        b16
                                        :32

                                        c'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        b16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        c'16
                                        :32
                                        [

                                        cs'16
                                        :32

                                        d'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        c'16
                                        :32
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 24]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        d'16
                                        :32
                                        [

                                        cs'16
                                        :32

                                        d'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        ds'16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        d'16
                                        :32
                                        [

                                        ds'16
                                        :32

                                        e'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        f'16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        ds'16
                                        :32
                                        [

                                        f'16
                                        :32

                                        e'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        f'16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        fs'16
                                        :32
                                        [

                                        f'16
                                        :32

                                        fs'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        g'16
                                        :32
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 25]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        gs'16
                                        :32
                                        [

                                        fs'16
                                        :32

                                        gs'16
                                        :32

                                        g'16
                                        :32

                                        gs'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        a'16
                                        :32
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        gs'16
                                        :32
                                        [

                                        a'16
                                        :32

                                        as'16
                                        :32

                                        \revert Staff.Stem.stemlet-length
                                        b'16
                                        :32
                                        \fff
                                        ]
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
                                        r2..

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
                                        r2.

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
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 8]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 9]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 10]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 11]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 12]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 13]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 14]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 15]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 16]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 17]
                                        r2

                                        r8

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 18]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 19]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 20]
                                        r2.

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 21]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 22]
                                        r2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 23]
                                        r2..

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 24]
                                        r1

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 25]
                                        r2

                                        r8
                                        \bar "||"

                                    }

                                }

                            }

                        >>

                    }

                >>

            }

        >>
