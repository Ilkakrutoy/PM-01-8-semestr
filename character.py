class Character:
    def __init__(self, name, role, level):
        self.name = name
        self.role = role
        self.level = level

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "level": self.level
        }
