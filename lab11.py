import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Kazakhstan2025"
)
cursor = conn.cursor()
names = ['wfr','akwb']
numbers = ['112131vwr1','21242341312']
def search_phonebook(pattern=None):
    if pattern:
        cursor.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    else:
        cursor.execute("SELECT * FROM search_phonebook();")
    return cursor.fetchall()

def add_or_update_user(name, phone):
    cursor.execute("CALL add_or_update_user(%s, %s);", (name, phone))
    conn.commit()

def bulk_insert_users(names, phones):
    cursor.execute("CALL bulk_insert_users(%s::text[], %s::text[]);", (names, phones))
    conn.commit()


def get_page(limit, offset):
    cursor.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit, offset))
    values = cursor.fetchall()
    for i in values:
        print(i)

def delete_user(value):
    cursor.execute("CALL delete_user(%s);", (value,))
    conn.commit()
#bulk_insert_users(names,numbers)
# Простое меню
try:
    type = int(input("Выберите действие (1 - Поиск, 2 - Добавить/Обновить, 3 - Удалить): "))
    if type == 1:
        pattern = input("Введите имя, номер или часть для поиска (или нажмите Enter для всех): ")
        results = search_phonebook(pattern if pattern else None)
        for r in results:
            print(f"ID: {r[0]}, Name: {r[1]}, Phone: {r[2]}")
    elif type == 2:
        name = input("Введите имя: ")
        phone = input("Введите номер: ")
        add_or_update_user(name, phone)
        print("Пользователь добавлен/обновлён.")
    elif type == 3:
        value = input("Введите имя или номер для удаления: ")
        delete_user(value)
        print("Пользователь удалён.")
    elif type == 4:
        try:
            limit = int(input("Сколько записей на страницу? "))
            offset = int(input("С какого смещения? "))
        except ValueError:
            print("Нужно ввести целые числа.")
        else:
            get_page(limit, offset)

    else:
        print("Неверный выбор.")
except Exception as e:
    print("Ошибка:", e)
finally:
    cursor.close()
    conn.close()
