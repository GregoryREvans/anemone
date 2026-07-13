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
            \evans-lbsd #0 #'(12 18 14 14 14 14 14)
            \evans-new-spacing-section #1 #10
            \evans-system-X-offset #4
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #30
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #10
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #10
            s1 * 1
            \noBreak
            \evans-new-spacing-section #7 #48
            s1 * 1
            \break
            \evans-lbsd #70 #'(12 15 15 15 15 15 15)
            \evans-system-X-offset #4
            \evans-new-spacing-section #1 #10
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #10
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #10
            s1 * 1
            \noBreak
            \evans-new-spacing-section #1 #10
            s1 * 1/4
            \noBreak
            \evans-new-spacing-section #7 #48
            s1 * 1/4
            \break
            \evans-lbsd #0 #'(12 18 14 14 14 14 14)
            \evans-system-X-offset #4
            \pageBreak
        }
    }
>>