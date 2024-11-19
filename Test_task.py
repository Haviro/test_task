# Тестовое задание для STEK

# Эта функция отвечает за чтение маршрутов из файла
def read_routes(file_path):
    routes = {}
    all_next_ids = set()  # Словарь для хранения всех ID, упоминаемых в качестве следующего
    start_addresses = set()

    with open(file_path, 'r', encoding='utf-8') as file:

        # Начинается цикл, который проходит по каждой строке файла.
        # Каждая строка разделяется по символу ;, и присваиваются значения: ID здания, адрес и ID следующего здания.
        for line in file:
            building_id, address, next_building_id = line.strip().split(';')
            routes[building_id] = (address, next_building_id)
            if next_building_id:
                all_next_ids.add(next_building_id)

        # Определяем начальные адреса, исключая любые IDs, которые были следующими
        for building_id in routes.keys():
            if building_id not in all_next_ids:
                start_addresses.add(building_id)

    return routes, start_addresses


# Эта функция ищет самый длинный маршрут
def find_longest_route(routes, start_addresses):
    longest_route = []

    for start_id in start_addresses:
        current_route = []
        current_id = start_id

        while current_id:
            address, next_id = routes[current_id]
            current_route.append(address)
            current_id = next_id

        if len(current_route) > len(longest_route):
            longest_route = current_route

    return longest_route


# Эта функция записывает найденный маршрут в выходной файл
def write_route_to_file(route, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(' -> '.join(route))

# Главная функция, управляющая выполнением всего скрипта
def main(input_file, output_file):
    routes, start_addresses = read_routes(input_file)
    longest_route = find_longest_route(routes, start_addresses)
    write_route_to_file(longest_route, output_file)



input_file = r"C:\Users\Leadi\PycharmProjects\MainDevelop\Dlya_sebya\Входной файл.txt" # Путь ко входному файлу
output_file = r'Выходной файл.txt'  # Путь к выходному файлу
main(input_file, output_file)

# Пояснение работы алгоритма:
# 1. Чтение данных из файла, где каждая строка содержит маршрут.
# 2. Сбор данных о маршрутах в словарь и поиск начальных адресов.
# 3. Поиск самого длинного маршрута, начиная с каждого из начальных адресов.
# 4. Запись самого длинного маршрута в выходной файл, используя форматирование с разделением адресов символом «->».