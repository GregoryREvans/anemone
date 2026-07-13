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
                                        \tweak NoteHead.style #'harmonic
                                        <gs a>8
                                        \ppp
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
                                        \tweak staff-padding #5
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
                                        - \baca-text-spanner-right-text "N"
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanTwo
                                        - \tweak stencil #abjad-flared-hairpin
                                        \<
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gtqs atqs>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gqs gtqs>4.
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "ord."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <g as>4
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "flaut."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 2]
                                        \tweak NoteHead.style #'default
                                        <g as>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <fs gs>2
                                        ~

                                        \tweak NoteHead.style #'harmonic
                                        <fs gs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <g b>8
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 3]
                                        \tweak NoteHead.style #'default
                                        <g b>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <ftqs aqs>2
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "½gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <fqs atqs>4.
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 4]
                                        \tweak NoteHead.style #'default
                                        <fqs atqs>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <eqs gtqs>4.
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <e as>8
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "ord."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <ds gs>4
                                        \mp
                                        - \tweak stencil #abjad-flared-hairpin
                                        \>
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 5]
                                        \tweak NoteHead.style #'harmonic
                                        <ds gs>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <e gs>4.

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <dtqs ftqs>8
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "flaut."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <eqs ftqs>4
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 6]
                                        \tweak NoteHead.style #'default
                                        <eqs ftqs>4.

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <fqs ftqs>4
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "½gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <f g>4.
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 7]
                                        \tweak NoteHead.style #'harmonic
                                        <fs g>2
                                        ~

                                        \tweak NoteHead.style #'harmonic
                                        <fs g>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <f gs>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <eqs ftqs>8
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
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
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "ord."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-right-text "flaut."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 8]
                                        \tweak NoteHead.style #'default
                                        <fqs aqs>2

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <eqs gqs>2
                                        \p
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanTwo
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

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [change 1 voice measure 8]
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

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 1]
                                        \clef "alto"
                                        \tweak NoteHead.style #'harmonic
                                        <g gs>2
                                        \ppp
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
                                        \tweak staff-padding #5
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
                                        - \baca-text-spanner-right-text "N"
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanTwo
                                        \<
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <ftqs gtqs>2
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "ord."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 2]
                                        \tweak NoteHead.style #'default
                                        <ftqs gtqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gqs gtqs>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <ftqs aqs>2
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "flaut."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <fs gs>8
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 3]
                                        \tweak NoteHead.style #'harmonic
                                        <fs gs>2

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gqs bqs>4.
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "½gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gtqs bqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 4]
                                        \tweak NoteHead.style #'default
                                        <gqs cqs'>2

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <g b>4.
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gtqs dqs'>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 5]
                                        \tweak NoteHead.style #'harmonic
                                        <gqs cqs'>2
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "ord."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne
                                        ~

                                        \tweak NoteHead.style #'harmonic
                                        <gqs cqs'>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gtqs cqs'>4
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "flaut."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gs b>8
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 6]
                                        \tweak NoteHead.style #'harmonic
                                        <gs b>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <ftqs gtqs>2
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "½gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne
                                        ~

                                        \tweak NoteHead.style #'default
                                        <ftqs gtqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <fqs ftqs>8
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 7]
                                        \tweak NoteHead.style #'harmonic
                                        <fqs ftqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <ftqs gtqs>8
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <g gs>2

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <fqs gtqs>4
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 8]
                                        \tweak NoteHead.style #'default
                                        <fqs gtqs>4.

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <eqs ftqs>8
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
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
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "ord."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-right-text "flaut."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <fqs aqs>2
                                        \mf
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanTwo
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

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 1]
                                        \clef "alto"
                                        \tweak NoteHead.style #'harmonic
                                        <fs g>2
                                        \ppp
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
                                        \tweak staff-padding #3
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \abjad-solid-line-with-arrow
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-left-text "gr."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        - \baca-text-spanner-right-text "ord."
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanOne
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
                                        \tweak staff-padding #5
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
                                        - \baca-text-spanner-right-text "N"
                                          %! SPANNER_START
                                          %! baca.PiecewiseCommand._call(2)
                                          %! baca.text_spanner()
                                        \startTextSpanTwo

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <ftqs gtqs>2
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 2]
                                        \tweak NoteHead.style #'default
                                        <ftqs gtqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <g gs>4.

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gs b>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gtqs atqs>4.
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 3]
                                        \tweak NoteHead.style #'harmonic
                                        <gtqs atqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <as d'>4.

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <aqs cqs'>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gtqs ctqs'>4.
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 4]
                                        \tweak NoteHead.style #'default
                                        <gtqs ctqs'>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gs c'>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <ftqs cqs'>4.

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <g c'>8
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 5]
                                        \tweak NoteHead.style #'harmonic
                                        <g c'>2

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gs c'>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gtqs bqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <g a>8
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 6]
                                        \tweak NoteHead.style #'default
                                        <g a>4.

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <ftqs gqs>2
                                        ~

                                        \tweak NoteHead.style #'harmonic
                                        <ftqs gqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 7]
                                        \tweak NoteHead.style #'default
                                        <fqs gqs>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <fs g>2

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <gqs atqs>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gs as>8
                                        ~

                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 8]
                                        \tweak NoteHead.style #'harmonic
                                        <gs as>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <g b>8

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'harmonic
                                        <gqs atqs>4

                                                        - \tweak arrow-length #2
                                                        - \tweak arrow-width #0.5
                                                        - \tweak bound-details.right.arrow ##t
                                                        - \tweak thickness #2.5
                                                        \glissando


                                        \tweak NoteHead.style #'default
                                        <fs b>4.
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanOne
                                          %! SPANNER_STOP
                                          %! baca.PiecewiseCommand._call(3)
                                          %! baca.text_spanner()
                                        \stopTextSpanTwo
                                        \bar "||"

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