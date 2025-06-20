from itertools import permutations
import random
import time
a, filtered_pairs = [], []
K = int(input("Введите количество членов комиссии (K): "))
ratings = {i: random.randint(1, 10) for i in range(1, K + 1)}
print(ratings)
def first_part():
    members = list(ratings.keys())
    pairs_data = [(chair, deputy) for chair in members for deputy in members if chair != deputy and -3 < ratings[chair] - ratings[deputy] < 3]
    print("\nДопустимые варианты после фильтрации:")
    for chair, deputy in pairs_data:
        print(f"Председатель: {chair} (рейтинг {ratings[chair]}), Заместитель: {deputy} (рейтинг {ratings[deputy]})")
    optimal_pair = max(pairs_data, key=lambda pair: ratings[pair[0]] + ratings[pair[1]])
    chair, deputy = optimal_pair
    total_rating = ratings[chair] + ratings[deputy]
    end_time = time.time()
    print(f"Оптимальная пара: Председатель {chair} ({ratings[chair]}), Заместитель {deputy} ({ratings[deputy]}), Общий рейтинг: {total_rating}")
    print(f"Время выполнения: {end_time - start_time:.5f} секунд")
def second_part():
    print("Рейтинги членов комиссии:", ratings)
    members = list(ratings.keys())
    all_pairs = permutations(members, 2)
    filtered_pairs = [(chair, deputy) for chair, deputy in all_pairs if abs(ratings[chair] - ratings[deputy]) <= 3]
    print("\nДопустимые варианты после фильтрации:")
    for chair, deputy in filtered_pairs:
        print(f"Председатель: {chair} (рейтинг {ratings[chair]}), Заместитель: {deputy} (рейтинг {ratings[deputy]})")
    if filtered_pairs:
        optimal_pair = max(filtered_pairs, key=lambda pair: ratings[pair[0]] + ratings[pair[1]])
        chair, deputy = optimal_pair
        total_rating = ratings[chair] + ratings[deputy]
        end_time = time.time()
        print(f"\nОптимальная пара: Председатель {chair} (рейтинг {ratings[chair]}), Заместитель {deputy} (рейтинг {ratings[deputy]})")
        print(f"Сумма рейтингов: {total_rating}")
    print(f"Время выполнения: {end_time - start_time:.5f} секунд")
start_time = time.time()
first_part()
start_time = time.time()
second_part()
