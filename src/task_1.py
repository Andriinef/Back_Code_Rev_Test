# 1. Find the route that is driven by vehicle_id=2 from the routes array.
# 2. Find the fastest (the route with the smalest duration)
# route from the routes array.
# 3. Find the shortest (the route with the smalest distance between locations)
# route from the routes array.
# 1. Найдите маршрут, которым управляет Vehicle_id=2, из массива маршрутов.
# 2. Найдите самый быстрый (маршрут с наименьшей продолжительностью) маршрут
# из массива маршрутов.
# 3. Найдите кратчайший (маршрут с наименьшим расстоянием между точками)
# маршрут из массива маршрутов.


import math
from typing import List, TypedDict

from list_routes_by_vehicle import routes_by_vehicle as rbv


class LocationDef(TypedDict):
    lon: float
    lat: float


class RouteStepDef(TypedDict):
    id: int
    location: LocationDef
    arrival: int


class RouteDef(TypedDict):
    vehicle_id: int
    steps: List[RouteStepDef]


routes: List[RouteDef] = rbv  # type: ignore


def find_route_by_vehicle_id(routes: List[RouteDef], vehicle_id: int):
    """
    Находит маршрут по заданному идентификатору транспортного средства.

    Аргументы:
    - routes: Список маршрутов.
    - vehicle_id: Идентификатор транспортного средства.

    Возвращает:
    - Маршрут, соответствующий заданному идентификатору транспортного средства,
    или None, если маршрут не найден.
    """
    for route in routes:
        # import ipdb; ipdb.set_trace()
        if route["vehicle_id"] == vehicle_id:
            return route


def find_fastest_route(routes: List[RouteDef]):
    """
    Находит самый быстрый маршрут из списка маршрутов.

    Аргументы:
    - routes: Список маршрутов.

    Возвращает:
    - Самый быстрый маршрут или None, если маршруты не найдены.
    """
    fastest_route = None
    # Инициализация переменной с бесконечным значением
    smallest_duration = float("inf")

    for route in routes:
        duration = min([step["arrival"] for step in route["steps"]])
        # import ipdb; ipdb.set_trace()
        if duration < smallest_duration:
            smallest_duration = duration
            fastest_route = route

    return fastest_route


def calculate_distance(
    location1: LocationDef, location2: LocationDef
) -> float:
    """
    Вычисляет расстояние между двумя местоположениями с использованием формулы
    Хаверсина.

    Аргументы:
        location1: Координаты первого местоположения (долгота, широта).
        location2: Координаты второго местоположения (долгота, широта).

    Возвращает:
        Расстояние между двумя местоположениями в километрах.
    """
    lon1, lat1 = location1["lon"], location1["lat"]
    lon2, lat2 = location2["lon"], location2["lat"]

    # Haversine formula
    dlon = math.radians(lon2 - lon1)
    dlat = math.radians(lat2 - lat1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # Earth radius in kilometers

    return distance


def calculate_route_distance(route: RouteDef) -> float:
    """
    Вычисляет общее расстояние маршрута,
    складывая расстояния между последовательными местоположениями.

    Аргументы:
        route: Описание маршрута.

    Возвращает:
        Общее расстояние маршрута в километрах.
    """
    total_distance = 0.0
    for i in range(len(route["steps"]) - 1):
        location1 = route["steps"][i]["location"]
        location2 = route["steps"][i + 1]["location"]
        step_distance = calculate_distance(location1, location2)
        total_distance += step_distance

    return total_distance


def find_shortest_route(routes: List[RouteDef]) -> RouteDef:
    """
    Находит самый короткий маршрут из списка маршрутов
    на основе общего расстояния.

    Аргументы:
        routes: Список маршрутов.

    Возвращает:
        Самый короткий маршрут или None, если маршруты не найдены.
    """
    shortest_route = min(routes, key=calculate_route_distance)
    return shortest_route


if __name__ == "__main__":
    vehicle_id = 1

    route = find_route_by_vehicle_id(routes, vehicle_id)

    if route is not None:
        steps = route["steps"]
        print(f"Маршрут для транспортного средства с id: {vehicle_id}")
        for step in steps:
            step_id = step["id"]
            location = step["location"]
            arrival = step["arrival"]
            lon = location["lon"]
            lat = location["lat"]
            print(
                f"Шаг {step_id}: Arrival: {arrival}, Location: ({lon}, {lat})"
            )
        print()
    else:
        print(f"Не найден маршрут для Vehicle_id={vehicle_id}.")

    fastest_route = find_fastest_route(routes)

    if fastest_route is not None:
        print(f"Самый быстрый маршрут: {fastest_route['vehicle_id']}")
    else:
        print("Маршруты не найдены.")

    shortest_route = find_shortest_route(routes)

    if shortest_route is not None:
        print(f"Самый короткий маршрут: {shortest_route['vehicle_id']}")
    else:
        print("Маршруты не найдены.")
