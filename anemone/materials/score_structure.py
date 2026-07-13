import abjad


score = abjad.Score(
    [
        abjad.Staff(lilypond_type="TimeSignatureContext", name="Global Context"),
        abjad.StaffGroup(
            [
                abjad.StaffGroup(
                    [
                        abjad.Staff(
                            [abjad.Voice(name="string 1 voice")],
                            name="string 1 staff",
                            lilypond_type="VanishingStringStaff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="bow 1 voice")],
                            name="bow 1 staff",
                            lilypond_type="VanishingBowStaff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="viola 1 voice")],
                            name="viola 1 staff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="change 1 voice")],
                            name="change 1 staff",
                            lilypond_type="VanishingChangeStaff",
                        ),
                    ],
                    name="sub group 1",
                    lilypond_type="RemoveableStaffGroup",
                ),
                abjad.StaffGroup(
                    [
                        abjad.Staff(
                            [abjad.Voice(name="string 2 voice")],
                            name="string 2 staff",
                            lilypond_type="VanishingStringStaff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="bow 2 voice")],
                            name="bow 2 staff",
                            lilypond_type="VanishingBowStaff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="viola 2 voice")],
                            name="viola 2 staff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="change 2 voice")],
                            name="change 2 staff",
                            lilypond_type="VanishingChangeStaff",
                        ),
                    ],
                    name="sub group 2",
                    lilypond_type="RemoveableStaffGroup",
                ),
                abjad.StaffGroup(
                    [
                        abjad.Staff(
                            [abjad.Voice(name="string 3 voice")],
                            name="string 3 staff",
                            lilypond_type="VanishingStringStaff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="bow 3 voice")],
                            name="bow 3 staff",
                            lilypond_type="VanishingBowStaff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="viola 3 voice")],
                            name="viola 3 staff",
                        ),
                        abjad.Staff(
                            [abjad.Voice(name="change 3 voice")],
                            name="change 3 staff",
                            lilypond_type="VanishingChangeStaff",
                        ),
                    ],
                    name="sub group 3",
                    lilypond_type="RemoveableStaffGroup",
                ),
            ],
            name="Staff Group",
        ),
    ],
    name="Score",
)


abjad.setting(
    score["sub group 1"]
).instrumentName = r'\markup { \hcenter-in #14 "Viola I" }'
abjad.setting(
    score["sub group 1"]
).shortInstrumentName = r'\markup { \hcenter-in #12 "va. I" }'

abjad.setting(
    score["sub group 2"]
).instrumentName = r'\markup { \hcenter-in #14 "Viola II" }'
abjad.setting(
    score["sub group 2"]
).shortInstrumentName = r'\markup { \hcenter-in #12 "va. II" }'

abjad.setting(
    score["sub group 3"]
).instrumentName = r'\markup { \hcenter-in #14 "Viola III" }'
abjad.setting(
    score["sub group 3"]
).shortInstrumentName = r'\markup { \hcenter-in #12 "va. III" }'
