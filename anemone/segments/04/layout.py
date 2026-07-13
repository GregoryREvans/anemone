import pathlib

import evans

import anemone

breaks = evans.Breaks(
    evans.Page(
        evans.System(measures=2, lbsd=(3, "(12 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(12 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=2, lbsd=(3, "(12 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(12 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=2, lbsd=(3, "(12 16 16 16 16 16 16)"), x_offset=4),
    ),
    time_signatures=anemone.reduced_signatures_04,
    default_spacing=(1, 26),  # 42
    spacing=[
        # (2, (1, 15)),
    ],
    bar_number=1,
)

output_path = pathlib.Path(__file__).parent

breaks.make_document_layout(path=output_path)
