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
            \evans-lbsd #3 #'(11 12 12 12 12 12 12)
            \evans-new-spacing-section #1 #20
            \evans-system-X-offset #4
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #20
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #20
            s1 * 1
            \noBreak
            \evans-new-spacing-section #7 #96
            s1 * 1
            \break
            \evans-lbsd #65 #'(11 12 12 12 12 12 12)
            \evans-system-X-offset #4
            \evans-new-spacing-section #1 #20
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #20
            s1 * 1
            \noBreak
            \evans-new-spacing-section #7 #96
            s1 * 1
            \break
            \evans-lbsd #3 #'(11 12 12 12 12 12 12)
            \evans-system-X-offset #4
            \pageBreak
        }
    }
>>