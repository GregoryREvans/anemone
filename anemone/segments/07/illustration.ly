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
                \tempo 4=67
                \mark \markup \bold {  }
                  %! scaling time signatures
                \time 4/4
                s1 * 1
                ^ \markup {
                  \raise #6 \with-dimensions-from \null
                  \override #'(font-size . 3)
                  \override #'(font-name . "Helvetica Bold")
                  \concat {
                      \abjad-metronome-mark-markup #2 #0 #1 #"67"
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
                \bar "||"

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
                                        e'2.
                                        \p
                                        \<
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            a'4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        b4
                                        \f
                                        \stopTrillSpan
                                        \>
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 2
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            e'4

                                            \tweak NoteHead.style #'harmonic
                                            fs'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 2]
                                        b8
                                        \p
                                        \<

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        e'2.
                                        \f
                                        \stopTrillSpan
                                        \>
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            gs'4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        b8
                                        \p
                                        \stopTrillSpan
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 3
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            cs'4

                                            \tweak NoteHead.style #'harmonic
                                            d'4

                                            \tweak NoteHead.style #'harmonic
                                            ds'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 1 voice measure 3]
                                        b4.
                                        \f
                                        \>

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        f'4
                                        \p
                                        \stopTrillSpan
                                        \<
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            bf'4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        ef'4.
                                        \f
                                        \stopTrillSpan
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 2
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            af'4

                                            \tweak NoteHead.style #'harmonic
                                            bf'4
                                            \revert Stem.stencil

                                        }


                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'1
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 4]
                                            \once \override Beam.grow-direction = #right
                                            <g a>16 * 491/64
                                            \p
                                            \stopTrillSpan
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \<
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 139/32
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                a
                                                \tweak X-extent #'(0 . 0)
                                                b
                                            >16 * 113/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                e'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 19/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                b
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 33/32
                                            ]
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'1
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 5]
                                            \once \override Accidental.stencil = ##f
                                            \once \override Beam.grow-direction = #left
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 59/64
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                            >16 * 61/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                e''
                                            >16 * 69/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                            >16 * 83/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                f''
                                            >16 * 27/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g
                                                \tweak X-extent #'(0 . 0)
                                                e'
                                            >16 * 37/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                d''
                                            >16 * 211/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                a
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 285/64
                                            ]
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'1
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 6]
                                            \once \override Accidental.stencil = ##f
                                            \once \override Beam.grow-direction = #right
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                b'
                                            >16 * 491/64
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                b
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                            >16 * 139/32
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 113/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 19/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                e'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 33/32
                                            ]
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'1
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 1 voice measure 7]
                                            \once \override Accidental.stencil = ##f
                                            \once \override Beam.grow-direction = #left
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                            >16 * 59/64
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g
                                                \tweak X-extent #'(0 . 0)
                                                a
                                            >16 * 61/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 69/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                a
                                                \tweak X-extent #'(0 . 0)
                                                b
                                            >16 * 83/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                e'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 27/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                b
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 37/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 211/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            <c' f'>16 * 285/64
                                            \ff
                                            ]
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

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
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \clef "alto"
                                        \afterGrace
                                        e'2.
                                        \p
                                        \<
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            b'4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        a'4
                                        \f
                                        \stopTrillSpan
                                        \>
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 2
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            e''4

                                            \tweak NoteHead.style #'harmonic
                                            d''4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 2]
                                        a'8
                                        \p
                                        \<

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        e'2.
                                        \f
                                        \stopTrillSpan
                                        \>
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            c''4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        a'8
                                        \p
                                        \stopTrillSpan
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 3
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            g''4

                                            \tweak NoteHead.style #'harmonic
                                            fs''4

                                            \tweak NoteHead.style #'harmonic
                                            f''4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 3]
                                        a'4.
                                        \f
                                        \>

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        ef'4
                                        \p
                                        \stopTrillSpan
                                        \<
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            bf'4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        f'4.
                                        \f
                                        \stopTrillSpan
                                        \>
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 2
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            c''4

                                            \tweak NoteHead.style #'harmonic
                                            bf'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 2 voice measure 4]
                                        f'2
                                        \p
                                        \<
                                        ~

                                        f'8

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        e'4.
                                        \f
                                        \stopTrillSpan
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            c''4
                                            \revert Stem.stencil

                                        }


                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'1
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 5]
                                            \once \override Beam.grow-direction = #right
                                            <g a>16 * 491/64
                                            \p
                                            \stopTrillSpan
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \<
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 139/32
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                a
                                                \tweak X-extent #'(0 . 0)
                                                b
                                            >16 * 113/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                e'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 19/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                b
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 33/32
                                            ]
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'1
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 6]
                                            \once \override Accidental.stencil = ##f
                                            \once \override Beam.grow-direction = #left
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 59/64
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                            >16 * 61/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                e''
                                            >16 * 69/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                            >16 * 83/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                f''
                                            >16 * 27/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g
                                                \tweak X-extent #'(0 . 0)
                                                e'
                                            >16 * 37/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                d''
                                            >16 * 211/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                a
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 285/64
                                            ]
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'1
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 2 voice measure 7]
                                            \once \override Accidental.stencil = ##f
                                            \once \override Beam.grow-direction = #right
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                b'
                                            >16 * 491/64
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                b
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                            >16 * 139/32
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 113/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 19/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            <e' a'>16 * 33/32
                                            \ff
                                            ]
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

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
                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \clef "alto"
                                        \afterGrace
                                        a2.
                                        \p
                                        \stopTrillSpan
                                        \<
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


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        d4
                                        \f
                                        \stopTrillSpan
                                        \>
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 2
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            f4

                                            \tweak NoteHead.style #'harmonic
                                            g4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 2]
                                        d8
                                        \p
                                        \<

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        a2.
                                        \f
                                        \stopTrillSpan
                                        \>
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            cs'4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        d8
                                        \p
                                        \stopTrillSpan
                                        \<
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 3
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            e4

                                            \tweak NoteHead.style #'harmonic
                                            ef4

                                            \tweak NoteHead.style #'harmonic
                                            fs4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 3]
                                        d4.
                                        \f
                                        \>

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        af4
                                        \p
                                        \stopTrillSpan
                                        \<
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            cf'4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        fs4.
                                        \f
                                        \stopTrillSpan
                                        \>
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 2
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            a4

                                            \tweak NoteHead.style #'harmonic
                                            b4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 4]
                                        fs2
                                        \p
                                        \<
                                        ~

                                        fs8

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        a4.
                                        \f
                                        \stopTrillSpan
                                        \>
                                        ~
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 1
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            cs'4
                                            \revert Stem.stencil

                                        }


                                          %! COMMENT_MEASURE_NUMBERS
                                          %! evans.SegmentMaker.comment_measure_numbers()
                                        % [viola 3 voice measure 5]
                                        a4.
                                        \p
                                        \<

                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        c4.
                                        \f
                                        \stopTrillSpan
                                        \>
                                        - \tweak bound-details.left.stencil-offset #'(0 . -1.4)
                                        - \tweak details.n-copies 3
                                        - \tweak details.pad-copies 0.3
                                        \startTrillSpan
                                        {

                                            \override Stem.stencil = ##f
                                            \tweak NoteHead.style #'harmonic
                                            d4

                                            \tweak NoteHead.style #'harmonic
                                            df4

                                            \tweak NoteHead.style #'harmonic
                                            e4
                                            \revert Stem.stencil

                                        }


                                        \once \override TrillSpanner.stencil = #line-spanner-multiple-lines
                                        \afterGrace
                                        a4
                                        \p
                                        \stopTrillSpan
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


                                        \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \score
                                            {
                                                \context Score = "Score"
                                                \with
                                                {
                                                    \override SpacingSpanner.spacing-increment = 0.5
                                                    proportionalNotationDuration = ##f
                                                }
                                                <<
                                                    \context RhythmicStaff = "Rhythmic_Staff"
                                                    \with
                                                    {
                                                        \remove Time_signature_engraver
                                                        \remove Staff_symbol_engraver
                                                        \override Stem.direction = #up
                                                        \override Stem.length = 5
                                                        \override TupletBracket.bracket-visibility = ##t
                                                        \override TupletBracket.direction = #up
                                                        \override TupletBracket.minimum-length = 4
                                                        \override TupletBracket.padding = 1.25
                                                        \override TupletBracket.shorten-pair = #'(-1 . -1.5)
                                                        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
                                                        \override TupletNumber.font-size = 0
                                                        \override TupletNumber.text = #tuplet-number::calc-fraction-text
                                                        tupletFullLength = ##t
                                                    }
                                                    {
                                                        c'\breve
                                                    }
                                                >>
                                                \layout
                                                {
                                                    indent = 0
                                                    ragged-right = ##t
                                                }
                                            }
                                        \times 2/2
                                        {

                                              %! COMMENT_MEASURE_NUMBERS
                                              %! evans.SegmentMaker.comment_measure_numbers()
                                            % [viola 3 voice measure 6]
                                            \once \override Beam.grow-direction = #right
                                            <g a>16 * 255/32
                                            \p
                                            \stopTrillSpan
                                            [
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \<
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 223/32
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                a
                                                \tweak X-extent #'(0 . 0)
                                                b
                                            >16 * 311/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                e'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 207/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                b
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                            >16 * 147/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                d'
                                                \tweak X-extent #'(0 . 0)
                                                a'
                                            >16 * 113/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                                \tweak X-extent #'(0 . 0)
                                                f'
                                            >16 * 23/16
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                g'
                                                \tweak X-extent #'(0 . 0)
                                                e''
                                            >16 * 5/4
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            \once \override Accidental.stencil = ##f
                                            \once \override NoteHead.X-extent = #'(0 . 0)
                                            \once \override NoteHead.transparent = ##t
                                            <
                                                \tweak X-extent #'(0 . 0)
                                                f
                                                \tweak X-extent #'(0 . 0)
                                                c'
                                            >16 * 73/64
                                              %! abjad.glissando(7)
                                            - \abjad-zero-padding-glissando
                                              %! abjad.glissando(7)
                                            \glissando
                                            \scrape-circular-clockwise

                                            <g' f''>16 * 69/64
                                            \ff
                                            ]
                                            \scrape-circular-clockwise

                                        }
                                        \revert TupletNumber.text

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