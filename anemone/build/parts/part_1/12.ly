        \context Score = "Score"
        <<
            \context TimeSignatureContext = "Global Context"
            {

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 1]
                \tempo 4=80
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
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 9]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 10]
                s1 * 1

                  %! COMMENT_MEASURE_NUMBERS
                  %! evans.SegmentMaker.comment_measure_numbers()
                % [Global Context measure 11]
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

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [string 1 voice measure 11]
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

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [bow 1 voice measure 11]
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

                                        \times 2/3
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 1]
                                            \clef "alto"
                                            aqs2
                                            \sfp
                                            ^ \markup crine
                                            \<
                                              %! abjad.glissando(7)
                                            \glissando

                                            \highest
                                            b'2
                                            \f
                                            \>

                                            b'2
                                            \p

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 2]
                                        b'2

                                        b'4.

                                        \vibrato #'(1 5 1 2 3 4) #3 #0.2
                                        b'8
                                        :32
                                        - \accent
                                        \mf
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
                                        % [viola 1 voice measure 3]
                                        b'4.
                                        :32

                                        b'8
                                        \p
                                          %! SPANNER_STOP
                                          %! baca._do_spanner_indicator_command(2)
                                          %! baca.trill_spanner()
                                        \stopTrillSpan
                                        ~

                                        b'2

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 4]
                                        b'4.

                                        b'8
                                        ~

                                        b'2
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 5]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        b'8
                                        [

                                        \vibrato #'(1 5 1 2 3 4) #3 #0.2
                                        \revert Staff.Stem.stemlet-length
                                        b'8
                                        :32
                                        - \accent
                                        \mf
                                        ]
                                        ~
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        - \tweak staff-padding 4.5
                                          %! SPANNER_START
                                          %! baca._do_spanner_indicator_command(1)
                                          %! baca.trill_spanner()
                                        \startTrillSpan

                                        b'2
                                        :32

                                        b'4
                                        \p
                                          %! SPANNER_STOP
                                          %! baca._do_spanner_indicator_command(2)
                                          %! baca.trill_spanner()
                                        \stopTrillSpan

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 6]
                                        \revert-noteheads
                                        \override Staff.Stem.stemlet-length = 0.75
                                        f16
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \f
                                        [
                                        (
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \>
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #6.5
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "P"
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpan

                                        fqs16

                                        gqf16
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \mp
                                        )
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \<

                                        \revert Staff.Stem.stemlet-length
                                        fqs16
                                        ]
                                        (

                                        \override Staff.Stem.stemlet-length = 0.75
                                        eqs16
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \ff
                                        [
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \>

                                        f16
                                        )

                                        e16
                                        (

                                        \revert Staff.Stem.stemlet-length
                                        f16
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \pp
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpan
                                        ]
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.hairpin()
                                        \<
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #6.5
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "T"
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpan

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 4/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            e16
                                            [

                                            ef16
                                            )

                                            \revert Staff.Stem.stemlet-length
                                            e16
                                            ]
                                            (

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            eqs32
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \f
                                            [
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            - \tweak stencil #abjad-flared-hairpin
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \>

                                            fqs32

                                            eqs32

                                            fqs32
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \p
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \<

                                            gqf32
                                            )

                                            fqs32
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \ff
                                            (
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            - \tweak stencil #abjad-flared-hairpin
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \>

                                            \revert Staff.Stem.stemlet-length
                                            fs32
                                            ]

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 4/3
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 7]
                                            \override Staff.Stem.stemlet-length = 0.75
                                            g16
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \stopTextSpan
                                            [
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \tweak staff-padding #6.5
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            - \abjad-solid-line-with-arrow
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            - \baca-text-spanner-left-text "N"
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \startTextSpan

                                            af16

                                            \revert Staff.Stem.stemlet-length
                                            a16
                                            )
                                            ]

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 8/7
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            af32
                                            [
                                            (

                                            a32

                                            aqs32
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \stopTextSpan
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \tweak staff-padding #6.5
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            - \abjad-solid-line-with-arrow
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            - \baca-text-spanner-left-text "P"
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \startTextSpan

                                            bqf32

                                            aqs32

                                            aqf32
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \mf
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \<

                                            \revert Staff.Stem.stemlet-length
                                            gqs32
                                            )
                                            ]

                                        }

                                        \tweak text #tuplet-number::calc-fraction-text
                                        \times 4/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            aqf16
                                            [
                                            (

                                            a16

                                            \revert Staff.Stem.stemlet-length
                                            bf16
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \stopTextSpan
                                            ]
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
                                            \tweak staff-padding #6.5
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            - \abjad-solid-line-with-arrow
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            - \baca-text-spanner-left-text "N"
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            - \baca-text-spanner-right-text "P"
                                              %! SPANNER_START
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.text_spanner()
                                            \startTextSpan

                                        }

                                        \times 2/3
                                        {

                                            \override Staff.Stem.stemlet-length = 0.75
                                            a16
                                            [

                                            bf16
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(2)
                                              %! baca.hairpin()
                                            \f
                                            )

                                            a16
                                            (

                                            bf16

                                            bqf16

                                            \revert Staff.Stem.stemlet-length
                                            aqs16
                                            )
                                              %! SPANNER_STOP
                                              %! baca.PiecewiseCommand._call(3)
                                              %! baca.text_spanner()
                                            \stopTextSpan
                                            ]

                                        }

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 8]
                                        \harmonicsOn
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
                                        % [viola 1 voice measure 9]
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
                                        )
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 10]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        bf32
                                        - \staccato
                                        [
                                        (

                                        fs'32
                                        - \staccato

                                        d''32
                                        - \staccato

                                        bf''32
                                        - \staccato
                                        )

                                        bf''32
                                        - \accent
                                        - \staccato
                                        (

                                        d''32
                                        - \staccato

                                        fs'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        bf32
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        b32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        g'32
                                        - \accent
                                        - \staccato

                                        ef''32
                                        - \staccato

                                        b''32
                                        - \accent
                                        - \staccato
                                        )

                                        b''32
                                        - \staccato
                                        (

                                        ef''32
                                        - \staccato

                                        g'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        b32
                                        - \accent
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        cs'32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        a'32
                                        - \staccato

                                        f''32
                                        - \staccato

                                        cs'''32
                                        - \staccato
                                        )

                                        cs'''32
                                        - \staccato
                                        (

                                        f''32
                                        - \staccato

                                        a'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        cs'32
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        d'32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        bf'32
                                        - \staccato

                                        fs''32
                                        - \staccato

                                        d'''32
                                        - \staccato
                                        )

                                        d'''32
                                        - \staccato
                                        (

                                        fs''32
                                        - \staccato

                                        bf'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        d'32
                                        - \staccato
                                        )
                                        ]

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 11]
                                        \override Staff.Stem.stemlet-length = 0.75
                                        ef'32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        b'32
                                        - \staccato

                                        g''32
                                        - \staccato

                                        ef'''32
                                        - \staccato
                                        )

                                        ef'''32
                                        - \accent
                                        - \staccato
                                        (

                                        g''32
                                        - \staccato

                                        b'32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        ef'32
                                        - \accent
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        f'32
                                        - \staccato
                                        [
                                        (

                                        cs''32
                                        - \staccato

                                        a''32
                                        - \staccato

                                        f'''32
                                        - \staccato
                                        )

                                        f'''32
                                        - \accent
                                        - \staccato
                                        (

                                        a''32
                                        - \staccato

                                        cs''32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        f'32
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        f'32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        cs''32
                                        - \accent
                                        - \staccato

                                        a''32
                                        - \staccato

                                        f'''32
                                        - \accent
                                        - \staccato
                                        )

                                        f'''32
                                        - \staccato
                                        (

                                        a''32
                                        - \staccato

                                        cs''32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        f'32
                                        - \accent
                                        - \staccato
                                        )
                                        ]

                                        \override Staff.Stem.stemlet-length = 0.75
                                        fs'32
                                        - \accent
                                        - \staccato
                                        [
                                        (

                                        d''32
                                        - \staccato

                                        bf''32
                                        - \staccato

                                        fs'''32
                                        - \staccato
                                        )

                                        fs'''32
                                        - \staccato
                                        (

                                        bf''32
                                        - \staccato

                                        d''32
                                        - \staccato

                                        \revert Staff.Stem.stemlet-length
                                        fs'32
                                        - \staccato
                                        \ff
                                        )
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                        ]
                                        \bar "||"
                                        \harmonicsOff

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

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 11]
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
