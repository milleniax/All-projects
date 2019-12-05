import numpy as np


def entering(id, x1, y1, x2, y2, area_x, area_y):
    """
    Проверка вхождения объекта в область
    :param id: идентификатор объекта
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param area_x:
    :param area_y:
    :return: answer
    """
    radius = 100
    distance = 111000 * np.sqrt((area_x - x1) ** 2 + (area_y - y1) ** 2)
    if distance <= radius:
        return True
    if distance > radius: return False


print(entering(1, 59.9390403, 30.3159109, 1, 1, 59.9390403, 30.3157754))

def entering_time(id, x1, y1, x2, y2, area_x, area_y):
    """
    Проверка вхождения объекта в область
    :param id: идентификатор объекта
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param area_x:
    :param area_y:
    :return: answer
    """
    timer = 5
    x = 0
    for i in range(timer):
        radius = 100
        distance = 111000 * np.sqrt((area_x - x1) ** 2 + (area_y - y1) ** 2)
        if distance <= radius:
            x += 1
        if distance > radius:
            break
        if x == timer:
            return True
        else:
            return False


print(entering_time(1, 59.9390403, 30.3159109, 1, 1, 59.9390403, 30.3157754))


def entering_neskolko(id, x1, y1, x2, y2, area_x, area_y):
    cheloveki = 5
    x = 0
    for i in range(cheloveki):
        radius = 100
        distance = 111000 * np.sqrt((area_x - x1) ** 2 + (area_y - y1) ** 2)
        if distance <= radius:
            x += 1
        if distance > radius:
            break
        if x == cheloveki:
            return True
        else:
            return False
