import pathlib

import evans

import anemone

breaks = evans.Breaks(
    evans.Page(
        evans.System(measures=4, lbsd=(53, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(53+30, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(53+30+30, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(53+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(53+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(53+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(53+30+30+30+30+30+30, "(10)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=4, lbsd=(8, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(8+30, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(8+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30+30+30, "(10)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=3, lbsd=(8, "(10)"), x_offset=4),
        evans.System(measures=3, lbsd=(8+30, "(10)"), x_offset=4),
        evans.System(measures=3, lbsd=(8+30+30, "(10)"), x_offset=4),
        evans.System(measures=3, lbsd=(8+30+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30+30, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(8+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30+30+30, "(10)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=4, lbsd=(8, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(8+30, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(8+30+30, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(8+30+30+30, "(10)"), x_offset=4),
        evans.System(measures=4, lbsd=(8+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30+30, "(10)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=4, lbsd=(8, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30+30, "(10)"), x_offset=4),
    ),
    evans.Page(
        evans.System(measures=5, lbsd=(8, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30, "(10)"), x_offset=4),
        evans.System(measures=5, lbsd=(8+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30, "(10)"), x_offset=4),
        # evans.System(measures=0, lbsd=(8+30+30+30+30+30+30+30, "(10)"), x_offset=4),
    ),
    time_signatures=anemone.all_signatures,
    default_spacing=(1, 40),
    # spacing=[
    #     (193, (1, 30)),
    #     (194, (7, 144)),  #
    #     (195, (1, 30)),
    #     (196, (1, 30)),
    #     (197, (1, 30)),
    #     (198, (7, 144)),  #
    #     (199, (1, 30)),
    #     (200, (1, 30)),
    #     (201, (1, 30)),
    #     (202, (1, 30)),
    # ],
    bar_number=1,
)

output_path = pathlib.Path(__file__).parent

breaks.make_document_layout(path=output_path)
