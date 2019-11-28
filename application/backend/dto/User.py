class User:
    def __init__(self, login, password, admin=bool):
        self.login = login
        self.password = password
        self.admin = admin
        