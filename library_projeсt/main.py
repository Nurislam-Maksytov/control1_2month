from db.database import Database

db = Database()


def menu():
    while True:
        print("\n📚 Библиотека")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Найти книгу")
        print("4. Удалить книгу")
        print("5. Добавить читателя")
        print("6. Показать читателей")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            title = input("Название: ")
            author = input("Автор: ")
            year = int(input("Год: "))
            book_type = input("Тип (fiction/textbook): ")
            db.add_book(title, author, year, book_type)

        elif choice == "2":
            books = db.get_books()
            for b in books:
                print(b)

        elif choice == "3":
            q = input("Поиск: ")
            results = db.search_books(q)
            for r in results:
                print(r)

        elif choice == "4":
            book_id = int(input("ID книги: "))
            db.delete_book(book_id)

        elif choice == "5":
            name = input("Имя: ")
            email = input("Email: ")
            db.add_reader(name, email)

        elif choice == "6":
            readers = db.get_readers()
            for r in readers:
                print(r)

        elif choice == "0":
            break


if __name__ == "__main__":
    menu()