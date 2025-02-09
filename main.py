from utils import get_reg_data, reg_check

def main():
    """
    Основная функция приложения.
    """
    users = []
    reg_patterns = get_reg_data()
    fields = ["name", "phone", "email", "birthdate"]

    print("Добро пожаловать в систему регистрации!")

    while len(users) < 3:
        user_data = {}
        print(f"\nРегистрация пользователя #{len(users) + 1}")

        for field in fields:
            while True:
                if field == "name":
                    prompt = "Введите имя: "
                elif field == "phone":
                    prompt = "Введите номер телефона (Пример: +71234567890): "
                elif field == "email":
                    prompt = "Введите email (Пример: user@mail.ru): "
                elif field == "birthdate":
                    prompt = "Введите дату рождения (Пример: 01.01.1990): "
                user_input = input(prompt)

                user_data[field] = user_input

                # Проверяем только телефон и email на соответствие формату
                if field in ["phone", "email"]:
                    validated_data = reg_check(user_data, reg_patterns, users, field)
                    if validated_data is not None:
                        user_data = validated_data
                        break
                    else:
                        print(f"Ошибка: Некорректные данные для поля {field}. Попробуйте еще раз.\n")
                else:
                    break  # Для имени и даты рождения проверки минимальны

        users.append(user_data)
        print("Пользователь успешно зарегистрирован!")

    print("\nВсе пользователи зарегистрированы:")
    for user in users:
        print(user)

if __name__ == "__main__":
    main()