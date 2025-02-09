import re

def get_reg_data():
    """
    Возвращает словарь с регулярными выражениями для проверки данных.
    """
    return {
        "phone": re.compile(r"\+7\d{10}"),
        "email": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
        "name": re.compile(r".+"),
        "birthdate": re.compile(r"\d{2}\.\d{2}\.\d{4}")
    }

def reg_check(data, patterns, users, field_to_check=None):
    """
    Проверяет данные на соответствие шаблонам и уникальность (только для телефона и email).

    Args:
        data: Словарь с данными пользователя.
        patterns: Словарь с регулярными выражениями для проверки данных.
        users: Список зарегистрированных пользователей.
        field_to_check: Поле, которое нужно проверить на уникальность.

    Returns:
        Словарь с данными пользователя, если данные корректны, иначе None.
    """
    for field, value in data.items():
        if field_to_check == field:
            # Проверка на уникальность для телефона и email
            for user in users:
                if user.get(field) == value:
                    return None

        # Проверка по шаблону для телефона и email
        if field in ["phone", "email"] and not patterns[field].match(value):
            return None

    return data