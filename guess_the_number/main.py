from guess_the_number.game import NumberGuessGame
from guess_the_number.exceptions import InvalidLevelError
from guess_the_number.utils.helpers import display_records
from pydantic import ValidationError


def main():
    """Основная функция для запуска игры"""
    print("Добро пожаловать в игру 'Угадай число'!")
    while True:
        try:
            level = input("Выберите уровень сложности (Легкий, Средний, Сложный): ").strip().lower()
            game = NumberGuessGame(level=level)
            game.play()
            break
        except (InvalidLevelError, ValidationError) as e:
            if isinstance(e, ValidationError):
                error_message = e.errors()[0]["msg"]
                if error_message.startswith("Value error, "):
                    error_message = error_message[len("Value error, "):]
                print(f"Ошибка: {error_message}")
            else:
                print(f"Ошибка: {e}")
    display_records()


if __name__ == "__main__":
    main()