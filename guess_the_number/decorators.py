"""Модуль, содержащий пользовательские декораторы"""
def log_attempts(func):
    """Декоратор для записи оставшихся попыток"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Попытка выполнена. Осталось попыток: {args[0].attempts - args[1]}")
        return result
    return wrapper