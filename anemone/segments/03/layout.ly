\context Score = "Score"
\with
{
    currentBarNumber = 1
}
<<
    \context TimeSignatureContext = "Global Context"
    {
        \context LayoutContext = "Layout"
        {
            \autoPageBreaksOff
            \evans-lbsd #3 #'(10 13 12 13 13 13 13)
            \evans-new-spacing-section #1 #26
            \evans-system-X-offset #4
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #26
            s1 * 7/8
            \noBreak
            \evans-new-spacing-section #1 #26
            s1 * 1
            \noBreak
            \evans-new-spacing-section #35 #624
            s1 * 3/4
            \break
            \evans-lbsd #65 #'(10 13 12 13 13 13 13)
            \evans-system-X-offset #4
            \evans-new-spacing-section #1 #26
            s1 * 9/8
            \noBreak
            \evans-new-spacing-section #1 #26
            s1 * 3/4
            \noBreak
            \evans-new-spacing-section #1 #26
            s1 * 1
            \noBreak
            \evans-new-spacing-section #35 #624
            s1 * 1
            \break
            \evans-lbsd #3 #'(10 11 11 11 11 11 11)
            \evans-system-X-offset #4
            \pageBreak
            \evans-new-spacing-section #1 #26
            s1 * 5/8
            \noBreak
            \evans-new-spacing-section #1 #26
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #26
            s1 * 3/4
            \noBreak
            \evans-new-spacing-section #35 #624
            s1 * 1/2
            \break
            \evans-lbsd #65 #'(10 11 11 11 11 11 11)
            \evans-system-X-offset #4
            \evans-new-spacing-section #1 #26
            s1 * 1
            \noBreak
            \evans-new-spacing-section #35 #624
            s1 * 7/8
            \break
            \evans-lbsd #3 #'(10 13 12 13 13 13 13)
            \evans-system-X-offset #4
            \pageBreak
        }
    }
>>