import pathlib

import evans

import anemone

breaks = evans.Breaks(
    evans.Page(
        evans.System(measures=3, lbsd=(3, "(13 16 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=3, lbsd=(65, "(13 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=3, lbsd=(3, "(13 16 15 15 15 15 15)"), x_offset=4),
    ),
    time_signatures=anemone.reduced_signatures_06,
    default_spacing=(1, 20),  # 42
    spacing=[
        # (2, (1, 15)),
    ],
    bar_number=1,
)

output_path = pathlib.Path(__file__).parent

breaks.make_document_layout(path=output_path)
