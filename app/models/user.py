class User:
    def __init__(self, id: str, name: str, password: str):
        self.id = id
        self.name = name
        self.password = password

    def presentation(self):
        print(f"Hello! I'm {self.name}, and my password is {self.password}!")