import pathlib

import evans

import anemone

breaks = evans.Breaks(
    evans.Page(
        evans.System(measures=4, lbsd=(3, "(10 13 12 13 13 13 13)"), x_offset=4),
        evans.System(measures=4, lbsd=(65, "(10 13 12 13 13 13 13)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=4, lbsd=(3, "(10 11 11 11 11 11 11)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(10 11 11 11 11 11 11)"), x_offset=4),
    ),
    time_signatures=anemone.reduced_signatures_03,
    default_spacing=(1, 26),  # 42
    spacing=[
        # (2, (1, 15)),
    ],
    bar_number=1,
)

output_path = pathlib.Path(__file__).parent

breaks.make_document_layout(path=output_path)
