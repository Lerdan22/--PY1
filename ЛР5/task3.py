import random

def get_unique_list_numbers() -> list[int]:
    random_l = []

    for _ in range(15):
        i = random.randint(-10, 10)
        if i not in random_l:
            random_l.append(i)
    return random_l


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
