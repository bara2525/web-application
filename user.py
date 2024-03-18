class User:
    def __init__(self, user_id: int, username: str, password: str, role: int):
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
        self.user_id = str(user_id).encode("utf-8").decode("utf-8")
        self.password = password
        # custom attributes
        self.username = username
        self.role = role

    def get_id(self):
        return self.user_id

