import pathlib

import evans

import anemone

breaks = evans.Breaks(
    evans.Page(
        evans.System(measures=5, lbsd=(0, "(12 18 14 14 14 14 14)"), x_offset=4),
        evans.System(measures=5, lbsd=(70, "(12 15 15 15 15 15 15)"), x_offset=4),
    ),
    time_signatures=anemone.reduced_signatures_18,
    default_spacing=(1, 10),  # 42
    spacing=[
        (2, (1, 30)),
    ],
    bar_number=1,
)

output_path = pathlib.Path(__file__).parent

breaks.make_document_layout(path=output_path)
