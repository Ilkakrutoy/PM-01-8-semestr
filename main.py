from manager import CharacterManager
from storage import Storage

def main():
    manager = CharacterManager()

    # загрузка
    data = Storage.load()
    for item in data:
        manager.add_character(item["name"], item["role"], item["level"])

    while True:
        print("\n1. Добавить персонажа")
        print("2. Показать персонажей")
        print("3. Изменить персонажа")
        print("4. Удалить персонажа")
        print("5. Сохранить и выйти")

        choice = input("Выбор: ")

        if choice == "1":
            name = input("Имя: ")
            role = input("Роль: ")
            level = int(input("Уровень: "))
            manager.add_character(name, role, level)

        elif choice == "2":
            for i, c in enumerate(manager.get_all()):
                print(i, c)

        elif choice == "3":
            i = int(input("Индекс: "))
            name = input("Новое имя: ")
            role = input("Новая роль: ")
            level = int(input("Новый уровень: "))
            manager.edit_character(i, name, role, level)

        elif choice == "4":
            i = int(input("Индекс: "))
            manager.delete_character(i)

        elif choice == "5":
            Storage.save(manager.get_all())
            print("Сохранено!")
            break

if __name__ == "__main__":
    main()
