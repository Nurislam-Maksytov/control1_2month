from models.base import BaseModel


class Reader(BaseModel):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"{self.name} ({self.email})"

    def __str__(self):
        return self.get_info()