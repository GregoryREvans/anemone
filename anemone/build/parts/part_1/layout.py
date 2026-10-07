import pathlib

import evans

import anemone
# 220 measures total
breaks = evans.Breaks(
    evans.Page( # 1
        evans.System(measures=1, lbsd=(53, "(10 18 14 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=1, lbsd=(53+30, "(10 18 14 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(53+30+30, "(10 15 15 15 15 15 15)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(53+30+30+30, "(10 15 15 15 15 15 15)"), x_offset=4.5),
    ),
    evans.Page( # 2
        evans.System(measures=4, lbsd=(6, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30, "(10 14 14 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30+30, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30+30+30, "(10 21 21 21 21 21 21)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30+30+30+20, "(10 21 21 21 21 21 21)"), x_offset=4.5),
    ),
    evans.Page( # 3
        evans.System(measures=3, lbsd=(6, "(10 14 12 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30, "(10 14 12 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30+30, "(10 12 12 12 12 12 12)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30, "(10 13 12 13 12 11 11)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30+29, "(4 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30+29+20, "(10 16 16 16 16 16 16)"), x_offset=4.5),
    ),
    evans.Page( # 4
        evans.System(measures=2, lbsd=(6, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30, "(10 17 17 17 17 17 17)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30+30+20, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30+30+20+25, "(10 15 15 15 15 15 15)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30+20+25+30, "(4 16 16 16 16 16 16)"), x_offset=4.5),
    ),
    evans.Page( # 5
        evans.System(measures=4, lbsd=(9, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30+30, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30+30+28, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30+30+28+35, "(4 15 15 15 15 15 15)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30+30+28+35+20, "(10 15 15 15 15 15 15)"), x_offset=4.5),
    ),
    evans.Page( # 6
        evans.System(measures=2, lbsd=(6, "(10 17 17 17 17 17 17)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30, "(10 17 17 17 17 17 17)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30, "(10 17 17 17 17 17 17)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30, "(10 17 17 17 17 17 17)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30+30, "(10 19 19 19 19 19 19)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(66+30+30+30+30+30, "(10 19 19 19 19 19 19)"), x_offset=4.5),
    ),
    evans.Page( # 7
        evans.System(measures=2, lbsd=(6, "(10 23 23 23 23 23 23)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30, "(10 23 23 23 23 23 23)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30, "(10 19 19 19 19 19 19)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30+30, "(10 19 19 19 19 19 19)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30+30, "(10 19 19 19 19 19 19)"), x_offset=4.5),
    ),
    evans.Page( # 8
        evans.System(measures=3, lbsd=(9, "(10 11 16 11 16 11 16)"), x_offset=4.5),
        evans.System(measures=5, lbsd=(9+30, "(10 11 16 11 16 11 16)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(9+30+30, "(11 14 14 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=5, lbsd=(9+30+30+30, "(11 14 14 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=5, lbsd=(9+30+30+30+30, "(10 14 14 14 14 14 14)"), x_offset=4.5),
    ),
    evans.Page( # 9
        evans.System(measures=2, lbsd=(6, "(10 17 17 17 17 17 17)"), x_offset=4.5),
        evans.System(measures=1, lbsd=(6+30, "(10 22 20 20 20 20 20)"), x_offset=4.5),
        evans.System(measures=1, lbsd=(6+30+30, "(10 22 20 20 20 20 20)"), x_offset=4.5),
        evans.System(measures=1, lbsd=(6+30+30+30, "(10 20 20 20 20 20 20)"), x_offset=4.5),
        evans.System(measures=1, lbsd=(6+30+30+30+30, "(10 20 20 20 20 20 20)"), x_offset=4.5),
    ),
    evans.Page( # 10
        evans.System(measures=2, lbsd=(6, "(10 19 19 19 19 19 19)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+27, "(10 19 19 19 19 19 19)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+27+27, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+27+27+27, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=1, lbsd=(6+27+27+27+27, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=1, lbsd=(6+27+27+27+27+27, "(10 18 18 18 18 18 18)"), x_offset=4.5),
    ),
    evans.Page( # 11
        evans.System(measures=2, lbsd=(6, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+32, "(4 13 13 13 13 13 13)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+27+27, "(10 13 13 13 13 13 13)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+27+27+27, "(10 13 13 13 13 13 13)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+27+27+27+27, "(10 13 13 13 13 13 13)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+27+27+27+27+27, "(10 16 16 16 16 16 16)"), x_offset=4.5),
    ),
    evans.Page( # 12
        evans.System(measures=2, lbsd=(6, "(10 14 14 14 14 14 14)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30, "(10 16 16 16 16 16 16)"), x_offset=4.5),
        evans.System(measures=5, lbsd=(6+30+30+30, "(10 15 15 15 15 15 15)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30+30, "(10 12 15 12 15 12 15)"), x_offset=4.5),
    ),
    evans.Page( # 13
        evans.System(measures=4, lbsd=(6, "(10 12 15 12 15 12 15)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30, "(10 12 15 12 15 12 15)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30+30, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30+30+30, "(10 16 16 16 16 16 16)"), x_offset=4.5),
    ),
    evans.Page( # 14
        evans.System(measures=3, lbsd=(6, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=4, lbsd=(6+30, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30, "(10 18 18 18 18 18 18)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30, "(10 17 17 17 17 17 17)"), x_offset=4.5),
        evans.System(measures=2, lbsd=(6+30+30+30+30, "(10 17 17 17 17 17 17)"), x_offset=4.5),
    ),
    evans.Page( # 15
        evans.System(measures=4, lbsd=(6, "(10 15 15 15 15 15 15)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30, "(10 15 15 15 15 15 15)"), x_offset=4.5),
        evans.System(measures=3, lbsd=(6+30+30, "(10 15 15 15 15 15 15)"), x_offset=4.5),
    ),
    time_signatures=anemone.all_signatures,
    default_spacing=(1, 20),
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
