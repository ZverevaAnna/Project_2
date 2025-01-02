"""Модуль, содержащий логику игры 'Угадай число'"""
import random
from pydantic import BaseModel, validator
from guess_the_number.exceptions import InvalidGuessError
from guess_the_number.utils.helpers import calculate_score

class NumberGuessGame(BaseModel):
    """Класс для управления игрой 'Угадай число'"""
    level: str
    range: tuple = (1, 10)
    attempts: int = 5

    @validator('level')
    def validate_level(cls, j):
        """Валидация уровня сложности"""
        valid_levels = ["легкий", "средний", "сложный"]
        if j not in valid_levels:
            raise ValueError("Некорректный уровень сложности. Выберите из: Легкий, Средний, Сложный")
        return j

    def __init__(self, **data):
        """Инициализация диапазона и количества попыток в зависимости от уровня сложности"""
        super().__init__(**data)
        if self.level == "средний":
            self.range = (1, 50)
            self.attempts = 7
        elif self.level == "сложный":
            self.range = (1, 100)
            self.attempts = 10

    def play(self):
        """Основной метод для запуска игры"""
        number_to_guess = random.randint(*self.range)
        print(f"Угадай число от {self.range[0]} до {self.range[1]} за {self.attempts} попыток")

        attempts_used = 0  # счетчик использованных попыток
        while attempts_used < self.attempts:
            try:
                guess = int(input(f"Попытка {attempts_used + 1}: "))
                if guess < self.range[0] or guess > self.range[1]:
                    raise InvalidGuessError(self.range)

                attempts_used += 1  # увеличиваем счетчик только при корректном вводе

                if guess == number_to_guess:
                    score = calculate_score(self.attempts, attempts_used)
                    print(f"Поздравляем! Вы угадали число за {attempts_used} попыток. Ваш счет: {score}")
                    name = input("Введите ваше имя для сохранения результата: ").strip() # сохраняем результат игрока
                    if name:
                        from .utils.helpers import save_record
                        save_record(name, score)
                    return
                elif guess < number_to_guess:
                    print("Загаданное число больше")
                else:
                    print("Загаданное число меньше")
            except InvalidGuessError as e:
                print(e)
            except ValueError:
                print("Пожалуйста, введите целое число")

        print(f"К сожалению, вы не угадали число. Это было {number_to_guess}")