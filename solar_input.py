# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star" or object_type =="planet":  # FIXME: do the same for planet
                if object_type == "star":
                    star = parse_star_parameters(line)
                    objects.append(star)
                if object_type == "planet":
                    planet = parse_planet_parameters(line)
                    objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star = Star()
    line_elems = line.split(' ')
    star.size = float(line_elems[1])
    star.color = str(line_elems[2])
    star.m = float(line_elems[3])
    star.x = float(line_elems[4])
    star.y = float(line_elems[5])
    star.Vx = float(line_elems[6])
    star.Vy = float(line_elems[7])
    
    return star

    pass  # FIXME: not done yet

def parse_planet_parameters(line):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet = Planet()
 
    line_elems = line.split(' ')
    planet.size = float(line_elems[1])
    planet.color = str(line_elems[2])
    planet.m = float(line_elems[3])
    planet.x = float(line_elems[4])
    planet.y = float(line_elems[5])
    planet.Vx = float(line_elems[6])
    planet.Vy = float(line_elems[7])
    
    return planet
    pass  # FIXME: not done yet...


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
