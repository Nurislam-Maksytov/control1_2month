from models.base import BaseModel


class SearchMixin:
    def matches(self, query):
        query = query.lower()
        return query in self.title.lower() or query in self.author.lower()


class Book(BaseModel, SearchMixin):
    total_count = 0

    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.__year = None
        self.year = year
        self.available = available

        Book.total_count += 1

    # инкапсуляция
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not Book.validate_year(value):
            raise ValueError("Некорректный год")
        self.__year = value

    @staticmethod
    def validate_year(year):
        from datetime import datetime
        return 1000 <= year <= datetime.now().year

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def get_info(self):
        return f"{self.title} — {self.author} ({self.year})"

    def __str__(self):
        return self.get_info()

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"


class FictionBook(Book):
    def get_info(self):
        return f"[Художественная] {super().get_info()}"


class TextBook(Book):
    def __init__(self, title, author, year, subject, available=True):
        super().__init__(title, author, year, available)
        self.subject = subject

    def get_info(self):
        return f"[Учебник: {self.subject}] {super().get_info()}"