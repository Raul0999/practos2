import getpass

# Данные пользователей
users = [
    {
        'username': 'john_doe',
        'password': 'password',
        'role': 'user',
        'subscription_type': 'Premium',
        'purchase_history': []
    },
    {
        'username': 'admin',
        'password': 'adminpass',
        'role': 'admin',
        'subscription_type': None,
        'purchase_history': []
    }
]

# Данные услуг
services = [
    {'name': 'Фитнес-тренировка', 'price': 100, 'rating': 4.5},
    {'name': 'Йога', 'price': 80, 'rating': 4.0},
    {'name': 'Пилатес', 'price': 90, 'rating': 4.7},
    {'name': 'Силовая тренировка', 'price': 120, 'rating': 4.8},
]

def sort_services(criterion):
    reverse_order = False
    if criterion in ['price']:
        reverse_order = False  # Сортировка по возрастанию по умолчанию
    elif criterion == 'rating':
        reverse_order = True  # Сортировка по убыванию по умолчанию

    sorted_services = sorted(services, key=lambda x: x[criterion], reverse=reverse_order)
    return sorted_services

def filter_services(min_price, max_price, min_rating, max_rating):
    filtered = [
        service for service in services
        if min_price <= service['price'] <= max_price and min_rating <= service['rating'] <= max_rating
    ]
    return filtered

def search_services(query):
    """Функция для поиска услуг по названию."""
    return [service for service in services if query.lower() in service['name'].lower()]

def user_menu(user):
    while True:
        print(f"\nДобро пожаловать в фитнес-клуб, {user['username']}!")
        print("Выберите действие:")
        print("1. Просмотреть доступные услуги")
        print("2. Купить услугу")
        print("3. Просмотреть историю покупок")
        print("4. Обновить профиль")
        print("5. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            view_services()
        elif choice == '2':
            purchase_service(user)
        elif choice == '3':
            view_purchase_history(user)
        elif choice == '4':
            update_profile(user)
        elif choice == '5':
            print("Вы вышли из аккаунта.")
            break
        else:
            print("Неверный выбор. Повторите попытку.")

def view_services():
    print("\nКак вы хотите сортировать услуги?")
    print("1. По цене")
    print("2. По рейтингу")
    criteria_choice = input("Ваш выбор: ")

    if criteria_choice == '1':
        sorted_services = sort_services('price')
    elif criteria_choice == '2':
        sorted_services = sort_services('rating')
    else:
        print("Неверный выбор. Показываем услуги без сортировки.")
        sorted_services = services

    while True:
        print("\nХотите выполнить поиск по названию услуги? (да/нет)")
        search_choice = input().lower()

        if search_choice == 'да':
            query = input("Введите название услуги для поиска: ")
            sorted_services = search_services(query)
            break  # Выходим из цикла после успешного ввода
        elif search_choice == 'нет':
            break  # Выходим из цикла если пользователь не хочет проводить поиск
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

    print("\nДоступные услуги:")
    if not sorted_services:
        print("Нет услуг, удовлетворяющих выбранным критериям.")
    else:
        for service in sorted_services:
            print(f"Название: {service['name']}, Цена: {service['price']}, Рейтинг: {service['rating']}")

def purchase_service(user):
    service_name = input("Введите название услуги для покупки: ")
    for service in services:
        if service['name'].lower() == service_name.lower():
            user['purchase_history'].append(service)  # Запоминаем историю покупок
            print(f"Вы успешно приобрели услугу: {service['name']}")
            return
    print("Услуга не найдена.")

def view_purchase_history(user):
    if not user['purchase_history']:
        print("У вас нет истории покупок.")
    else:
        print("\nИстория покупок:")
        for item in user['purchase_history']:
            print(f"Услуга: {item['name']}, Цена: {item['price']}")

def update_profile(user):
    new_username = input("Введите новый логин (или нажмите Enter для пропуска): ")
    if new_username:
        user['username'] = new_username
    new_password = getpass.getpass("Введите новый пароль (или нажмите Enter для пропуска): ")
    if new_password:
        user['password'] = new_password
    print("Профиль обновлен!")

# Функции для администратора
def admin_menu():
    while True:
        print("\nДобро пожаловать в систему управления фитнес-клубом!")
        print("Выберите действие:")
        print("1. Добавить услугу")
        print("2. Удалить услугу")
        print("3. Просмотреть пользователей")
        print("4. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            add_service()
        elif choice == '2':
            remove_service()
        elif choice == '3':
            view_users()
        elif choice == '4':
            print("Вы вышли из системы управления.")
            break
        else:
            print("Неверный выбор. Повторите попытку.")

def add_service():
    name = input("Введите название новой услуги: ")
    price = float(input("Введите цену услуги: "))
    rating = float(input("Введите рейтинг услуги: "))
    services.append({'name': name, 'price': price, 'rating': rating})
    print("Услуга добавлена.")

def remove_service():
    name = input("Введите название услуги для удаления: ")
    global services
    services = [service for service in services if service['name'].lower() != name.lower()]
    print("Услуга удалена.")

def view_users():
    print("\nСписок пользователей:")
    for user in users:
        print(f"Логин: {user['username']}, Роль: {user['role']}, Тип подписки: {user['subscription_type']}")

def create_user():
    username = input("Введите логин для нового пользователя: ")
    password = getpass.getpass("Введите пароль для нового пользователя: ")
    subscription_type = input("Введите тип подписки (например, 'Стандарт' или 'Премиум'): ")

    # Проверка на уникальность логина
    if any(user['username'] == username for user in users):
        print("Пользователь с таким логином уже существует. Попробуйте другой логин.")
        return

    new_user = {
        'username': username,
        'password': password,
        'role': 'user',  # Все новые пользователи по умолчанию становятся пользователями
        'subscription_type': subscription_type,
        'purchase_history': []
    }
    users.append(new_user)
    print("Новый пользователь успешно создан.")

# Основной код
def main():
    while True:
        print("\nДобро пожаловать в фитнес-клуб!")
        print("1. Войти как пользователь")
        print("2. Войти как администратор")
        print("3. Создать нового пользователя")
        print("4. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            login_user('user')
        elif choice == '2':
            login_user('admin')
        elif choice == '3':
            create_user()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Повторите попытку.")

def login_user(role):
    username = input("Логин: ")
    password = getpass.getpass("Пароль: ")

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)

    if user:
        if user['role'] == 'user':
            user_menu(user)
        elif user['role'] == 'admin':
            admin_menu()
    else:
        print("Неверные учетные данные. Попробуйте еще раз.")

if __name__ == "__main__":
    main()