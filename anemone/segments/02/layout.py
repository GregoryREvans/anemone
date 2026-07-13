import pathlib

import evans

import anemone

breaks = evans.Breaks(
    evans.Page(
        evans.System(measures=4, lbsd=(3, "(14 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=4, lbsd=(69, "(13 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=3, lbsd=(5, "(13 14 14 14 14 14 14)"), x_offset=4),
        evans.System(measures=3, lbsd=(60, "(13 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=3, lbsd=(5, "(13 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=2, lbsd=(60, "(13 19 19 19 19 19 19)"), x_offset=4),
    ),
    time_signatures=anemone.reduced_signatures_02,
    default_spacing=(1, 26),  # 42
    spacing=[
        # (2, (1, 15)),
    ],
    bar_number=1,
)

output_path = pathlib.Path(__file__).parent

breaks.make_document_layout(path=output_path)
