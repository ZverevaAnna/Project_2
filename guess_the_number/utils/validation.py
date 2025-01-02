"""Модуль для валидации данных"""
def validate_level(level):
    """Проверяет корректность уровня сложности"""
    valid_levels = ["легкий", "средний", "сложный"]
    if level not in valid_levels:
        raise ValueError("Некорректный уровень сложности")
    return level