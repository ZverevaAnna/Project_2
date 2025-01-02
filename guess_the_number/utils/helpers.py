"""Модуль, содержащий вспомогательные функции"""
def calculate_score(max_attempts, attempts_used):
    """Вычисляет очки на основе количества использованных попыток"""
    return max_attempts * 10 - attempts_used * 5

def save_record(name, score):
    """Сохраняет результат игрока в файл records.txt"""
    with open("records.txt", "a") as file:
        file.write(f"{name}:{score}\n")

def display_records():
    """Читает и отображает лучшие результаты из файла records.txt"""
    try:
        with open("records.txt", "r") as file:
            records = file.readlines()

        if not records:
            print("Рекордов пока нет")
            return

        #Преобразуем записи в список кортежей (имя, очки)
        records = [line.strip().split(":") for line in records]
        records = [(name, int(score)) for name, score in records]

        #Сортируем по очкам (по убыванию)
        records.sort(key=lambda x: x[1], reverse=True)

        print("\nЛучшие результаты:")
        for i, (name, score) in enumerate(records[:5], 1):  #топ-5 результатов
            print(f"{i}. {name}: {score} очков")
    except FileNotFoundError:
        print("Рекордов пока нет")