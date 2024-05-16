def solve(flights):
    flight_map = {}
    for start, end in flights:
        flight_map[start] = end
    departures_cities = set(flight_map.keys())
    arrival_cities = set(flight_map.values())
    start_city = (departures_cities - arrival_cities).pop()

    cur_city = start_city
    route = []
    while cur_city in flight_map:
        route.append(cur_city)
        cur_city = flight_map[cur_city]
    route.append(cur_city)
    return route
flights1 = [("Moscow", "Belgrade")]
flights2 = [("Moscow", "Belgrade"), ("Erevan", "Moscow")]
print(solve(flights1),solve(flights2))
