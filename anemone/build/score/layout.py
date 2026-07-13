import pathlib

import evans

import anemone
# 220 measures total
breaks = evans.Breaks(
    evans.Page( # 1
        evans.System(measures=2, lbsd=(53, "(12 18 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 2
        evans.System(measures=3, lbsd=(6, "(12 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=2, lbsd=(75, "(12 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 3
        evans.System(measures=4, lbsd=(3, "(14 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=4, lbsd=(69, "(13 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 4
        evans.System(measures=3, lbsd=(5, "(13 14 14 14 14 14 14)"), x_offset=4),
        evans.System(measures=3, lbsd=(60, "(13 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 5
        evans.System(measures=3, lbsd=(5, "(13 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=2, lbsd=(60, "(13 19 19 19 19 19 19)"), x_offset=4),
    ),
    evans.Page( # 6
        evans.System(measures=4, lbsd=(3, "(10 13 12 13 13 13 13)"), x_offset=4),
        evans.System(measures=4, lbsd=(65, "(10 13 12 13 13 13 13)"), x_offset=4),
    ),
    evans.Page( # 7
        evans.System(measures=4, lbsd=(6, "(10 12 12 12 12 12 12)"), x_offset=4),
        evans.System(measures=2, lbsd=(60, "(10 13 12 13 12 11 11)"), x_offset=4),
    ),
    evans.Page( # 8
        evans.System(measures=2, lbsd=(4, "(12 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(12 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page( # 9
        evans.System(measures=2, lbsd=(3, "(12 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=2, lbsd=(69, "(12 17 17 17 17 17 17)"), x_offset=4),
    ),
    evans.Page( # 10
        evans.System(measures=2, lbsd=(6, "(12 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=4, lbsd=(65, "(12 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 11
        evans.System(measures=4, lbsd=(3, "(12 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=4, lbsd=(64, "(12 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page( # 12
        evans.System(measures=3, lbsd=(3, "(12 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=4, lbsd=(64, "(12 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page( # 13
        evans.System(measures=4, lbsd=(5, "(12 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=4, lbsd=(65, "(12 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page( # 14
        evans.System(measures=4, lbsd=(8, "(11 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=4, lbsd=(65, "(12 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 15
        evans.System(measures=2, lbsd=(4, "(10 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(10 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page( # 16
        evans.System(measures=2, lbsd=(3, "(10 16 16 16 16 16 16)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(10 16 16 16 16 16 16)"), x_offset=4),
    ),
    evans.Page( # 17
        evans.System(measures=2, lbsd=(3, "(10 19 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=2, lbsd=(64, "(10 19 19 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 18
        evans.System(measures=2, lbsd=(3, "(11 19 19 18 18 18 18)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(11 18 19 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 19
        evans.System(measures=2, lbsd=(3, "(10 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=3, lbsd=(65, "(10 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 20
        evans.System(measures=5, lbsd=(9, "(11 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 21
        evans.System(measures=5, lbsd=(9, "(11 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 22
        evans.System(measures=4, lbsd=(3, "(11 14 14 14 14 14 14)"), x_offset=4),
        evans.System(measures=5, lbsd=(65, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 23
        evans.System(measures=3, lbsd=(3, "(12 14 14 14 14 14 14)"), x_offset=4),
        evans.System(measures=4, lbsd=(65, "(11 17 17 17 17 17 17)"), x_offset=4),
    ),
    evans.Page( # 24
        evans.System(measures=2, lbsd=(3, "(11 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(11 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 25
        evans.System(measures=2, lbsd=(3, "(11 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=3, lbsd=(65, "(11 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 26
        evans.System(measures=3, lbsd=(3, "(11 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(11 18 18 18 18 18 18)"), x_offset=4),
    ),
    evans.Page( # 27
        evans.System(measures=2, lbsd=(3, "(11 18 18 18 18 18 18)"), x_offset=4),
        evans.System(measures=2, lbsd=(65, "(11 18 18 18 18 18 18)"), x_offset=4),
    ),

    evans.Page( # 28
        evans.System(measures=4, lbsd=(8, "(11 12 14 12 14 12 14)"), x_offset=4),
    ),
    evans.Page( # 29
        evans.System(measures=4, lbsd=(8, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 30
        evans.System(measures=4, lbsd=(8, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 31
        evans.System(measures=4, lbsd=(8, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 32
        evans.System(measures=3, lbsd=(8, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 33
        evans.System(measures=2, lbsd=(8, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 34
        evans.System(measures=2, lbsd=(8, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),
    evans.Page( # 35
        evans.System(measures=2, lbsd=(8, "(11 14 14 14 14 14 14)"), x_offset=4),
    ),

    evans.Page( # 36
        evans.System(measures=5, lbsd=(3, "(11 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=5, lbsd=(45, "(11 13 15 13 15 13 15)"), x_offset=4),
    ),
    evans.Page( # 37
        evans.System(measures=5, lbsd=(8, "(12 15 15 15 15 15 15)"), x_offset=4),
    ),

    evans.Page( # 38
        evans.System(measures=3, lbsd=(3, "(11 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=3, lbsd=(65, "(11 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 39
        evans.System(measures=3, lbsd=(3, "(11 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=3, lbsd=(65, "(11 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 40
        evans.System(measures=3, lbsd=(3, "(11 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=3, lbsd=(65, "(11 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 41
        evans.System(measures=3, lbsd=(3, "(11 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=3, lbsd=(65, "(11 15 15 15 15 15 15)"), x_offset=4),
    ),
    evans.Page( # 42
        evans.System(measures=4, lbsd=(3, "(11 15 15 15 15 15 15)"), x_offset=4),
        evans.System(measures=4, lbsd=(65, "(11 15 15 15 15 15 15)"), x_offset=4),
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
