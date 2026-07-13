\version "2.25.16"
\language "english" %! LilyPondFile

\include "abjad.ily"
\include "../../parts_stylesheet.ily"
\include "../../../lib.ily"
\include "evans.ily"                                   %! LilyPondFile
%{ \include "abjad.ily" %! LilyPondFile %}
%{ \include "baca-spanners.ily"
\include "../../../lib.ily"
\include "evans.ily"
\include "evans-accidentals-markups.ily"
\include "evans-chart-markups.ily"
\include "evans-spanners.ily" %}

\header { %! LilyPondFile
    tagline = ##f
} %! LilyPondFile

\score{
    \removeWithTag #'(formatting voice1 voice2 voice3 voice4 voice5 voice6 voice7 voice8 voice9 voice11 voice12 voice13)
    <<
        { \include "layout.ly" }
    	{
            \include "../../score/01.ly"
            \include "../../score/02.ly"
            \include "../../score/03.ly"
            \include "../../score/04.ly"
            \include "../../score/05.ly"
            \include "../../score/06.ly"
            \include "../../score/07.ly"
            \include "../../score/08.ly"
            \include "../../score/09.ly"
            \include "../../score/10.ly"
            \include "../../score/11.ly"
            \include "../../score/12.ly"
    	}
    >>
%{ \midi{} %}
}
