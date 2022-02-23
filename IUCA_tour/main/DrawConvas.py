from PIL import Image, ImageDraw
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def draw_by_points(way):

    first = way[0]
    last = way[len(way) - 1]

    way_name = f'from_{first}_to_{last}'

    grounnd_floor = Image.open('media/CrearMapTemplate/New-project-_Ground-floor_.jpg')

    first_floor = Image.open('media/CrearMapTemplate/New-project-_1st-floor_.jpg')

    second_floor = Image.open('media/CrearMapTemplate/New-project-_2nd-floor.jpg')

    third_floor = Image.open('media/CrearMapTemplate/New-project-_3rd-floor_.jpg')

    privius_point = ''

    flag = False

    for i in range(len(way)):

        if privius_point == '':
            privius_point = way[i]
            continue

        # first floor
        if way[i][0] == 'f':
            if privius_point == 's' or privius_point == 'g' or privius_point == 't':
                flag = True

            draw = ImageDraw.Draw(first_floor)

            # проверка на то находится ли следующая точка на другом этаже и рисовать линии не надо

            if i < (len(way) - 1):
                if way[i+1][0] == 's' or way[i+1][0] == 'g' or way[i+1][0] == 't':
                    flag = True

        # second floor
        if way[i][0] == 's':
            if privius_point == 'f' or privius_point == 'g' or privius_point == 't':
                privius_point = way[i]
                continue

            draw = ImageDraw.Draw(second_floor)

            # проверка на то находится ли следующая точка на другом этаже и рисовать линии не надо

            if i < (len(way) - 1):
                if way[i+1][0] == 'f' or way[i+1][0] == 'g' or way[i+1][0] == 't':
                    flag = True

        # third floor
        if way[i][0] == 't':
            if privius_point == 'f' or privius_point == 'g' or privius_point == 's':
                privius_point = way[i]
                continue

            draw = ImageDraw.Draw(third_floor)

            # проверка на то находится ли следующая точка на другом этаже и рисовать линии не надо

            if i < (len(way) - 1):
                if way[i + 1][0] == 'f' or way[i + 1][0] == 'g' or way[i+1][0] == 's':
                    flag = True

        # ground floor
        if way[i][0] == 'g':
            if privius_point == 's' or privius_point == 'f' or privius_point == 't':
                privius_point = way[i]
                continue

            draw = ImageDraw.Draw(grounnd_floor)

            # проверка на то находится ли следующая точка на другом этаже и рисовать линии не надо

            if i < (len(way) - 1):
                if way[i+1][0] == 's' or way[i+1][0] == 'f' or way[i+1][0] == 't':
                    flag = True


        draw.line((coordinats[privius_point][0], coordinats[privius_point][1], coordinats[way[i]][0], coordinats[way[i]][1]), fill=128, width=20)

        if flag:
            privius_point = ''
            flag = False
        else:
            privius_point = way[i]

    if not os.path.exists(os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), f'media/map_output/')):
        os.mkdir(os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), f'media/map_output/'))

    ground_floor_name = [os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), f'media/map_output/{way_name}_ground_floor.jpg'), f'media/map_output/{way_name}_ground_floor.jpg' ]
    first_floor_name = [os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), f"media/map_output/{way_name}_first_floor.jpg"), f"media/map_output/{way_name}_first_floor.jpg"]
    second_floor_name = [os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), f"media/map_output/{way_name}_second_floor.jpg"), f"media/map_output/{way_name}_second_floor.jpg"]
    third_floor_name = [os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), f"media/map_output/{way_name}_third_floor.jpg"), f"media/map_output/{way_name}_third_floor.jpg"]

    grounnd_floor.save(ground_floor_name[0])
    first_floor.save(first_floor_name[0])
    second_floor.save(second_floor_name[0])
    third_floor.save(third_floor_name[0])

    return [ground_floor_name[1], first_floor_name[1], second_floor_name[1], third_floor_name[1]]

# points


coordinats = {

    # ground floor

    'g1': [400, 2000],
    'g2': [400, 1300],
    'g3': [800, 1300],
    'g4': [800, 1050],
    'g5': [1000, 1500],
    'g6': [5550, 500],
    'g7': [5550, 1300],
    'g8': [5550, 1500],
    'g9': [6200, 1300],
    'g10': [6400, 1300],
    'g11': [6400, 1500],
    'g12': [6200, 1000],
    'g13': [6950, 1300],
    'g14': [6950, 1000],
    'g15': [7750, 1300],
    'g16': [7750, 1500],
    'g17': [8400, 1300],
    'g18': [8400, 1000],
    'g19': [9100, 1300],
    'g20': [9100, 1500],
    'g21': [9100, 1000],
    'g22': [9400, 1300],
    'g23': [9400, 1000],
    'g24': [9700, 1300],
    'g25': [9700, 1000],
    'g26': [10200, 1300],


    # first floor


    'f0': [300, 2500],
    'f1': [450, 2000],
    'f2': [450, 1300],
    'f3': [320, 1050],
    'f4': [570, 1300],
    'f5': [950, 1300],
    'f6': [950, 1550],
    'f7': [1200, 1300],
    'f8': [1200, 1050],
    'f9': [2550, 1300],
    'f10': [2550, 1050],
    'f11': [2650, 1300],
    'f12': [2650, 1550],
    'f13': [3550, 1300],
    'f14': [3550, 1050],
    'f15': [3550, 800],
    'f16': [4000, 800],
    'f17': [3550, 1550],
    'f18': [4100, 1300],
    'f19': [4100, 2200],
    'f20': [3550, 2500],
    'f21': [5000, 2200],
    'f22': [5000, 2500],
    'f23': [4700, 2500],
    'f24': [5100, 2700],
    'f25': [5500, 1700],
    'f26': [5600, 2150],
    'f27': [5600, 1200],
    'f28': [5000, 1200],
    'f29': [5600, 500],
    'f30': [5000, 600],
    'f31': [5000, 300],
    'f32': [6100, 2150],
    'f33': [6100, 1400],
    'f34': [6300, 1200],
    'f35': [6050, 200],
    'f36': [8150, 2150],
    'f37': [8150, 1350],
    'f38': [8400, 1350],
    'f39': [8400, 1200],
    'f40': [9000, 1350],
    'f41': [9000, 1550],
    'f42': [9400, 1350],
    'f43': [9400, 1550],
    'f44': [9600, 1350],
    'f45': [9600, 800],
    'f46': [10100, 1350],
    'f47': [550, 2500],
    'f48': [570, 1100],

    # second floor

    's0': [300, 2500],
    's1': [450, 1800],
    's2': [450, 1300],
    's3': [420, 1050],
    's4': [820, 1300],
    's5': [820, 1050],
    's6': [1050, 1300],
    's7': [1050, 1500],
    's8': [1100, 1900],
    's9': [1700, 1900],
    's10': [1300, 1300],
    's11': [1300, 1050],
    's12': [2200, 1300],
    's13': [2200, 1050],
    's14': [2650, 1300],
    's15': [2700, 1050],
    's16': [2600, 1500],
    's17': [3300, 1300],
    's18': [3300, 1050],
    's19': [3400, 1300],
    's20': [3400, 1500],
    's21': [3900, 1300],
    's22': [3900, 1050],
    's23': [4000, 1300],
    's24': [4000, 1500],
    's25': [5550, 1300],
    's26': [5550, 500],
    's27': [4800, 300],
    's28': [5550, 1500],
    's29': [6250, 1300],
    's30': [6250, 1500],
    's31': [6400, 1300],
    's32': [6400, 1050],
    's33': [6850, 1300],
    's34': [6900, 1000],
    's35': [6850, 1500],
    's36': [7600, 1300],
    's37': [7600, 1000],
    's38': [7600, 1500],
    's39': [8350, 1300],
    's40': [8325, 1000],
    's41': [8350, 1500],
    's42': [9100, 1300],
    's43': [9100, 1500],
    's44': [9100, 1000],
    's45': [9550, 1300],
    's46': [9550, 1000],
    's47': [9900, 1000],
    's48': [9700, 1500],
    's49': [9800, 1300],
    's50': [600, 2500],
    's51': [5000, 600],

    # third floor

    't1': [300, 2500],
    't2': [400, 1800],
    't3': [450, 1300],
    't4': [420, 1050],
    't5': [820, 1300],
    't6': [820, 1050],
    't7': [1050, 1300],
    't8': [1050, 1500],
    't9': [1300, 1300],
    't10': [1300, 1050],
    't11': [2100, 1300],
    't12': [2100, 1500],
    't13': [2100, 1050],
    't14': [2650, 1300],
    't15': [2600, 1500],
    't16': [2700, 1050],
    't17': [3300, 1300],
    't18': [3300, 1500],
    't19': [3300, 1050],
    't20': [3900, 1300],
    't21': [3900, 1050],
    't22': [4000, 1300],
    't24': [4000, 1500],
    't25': [5550, 1300],
    't26': [5550, 1500],
    't27': [5550, 500],
    't28': [4800, 300],
    't29': [6250, 1300],
    't30': [6250, 1500],
    't31': [6400, 1300],
    't32': [6400, 1050],
    't33': [6850, 1300],
    't34': [6900, 1000],
    't35': [6850, 1500],
    't36': [7600, 1300],
    't37': [7600, 1500],
    't38': [8350, 1300],
    't39': [8325, 1000],
    't40': [8350, 1500],
    't41': [9100, 1300],
    't42': [9100, 1500],
    't43': [9550, 1300],
    't44': [9550, 1000],
    't45': [9800, 1300],
    't46': [9900, 1000],
}


