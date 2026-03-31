from character import Character

class CharacterManager:
    def __init__(self):
        self.characters = []

    def add_character(self, name, role, level):
        character = Character(name, role, level)
        self.characters.append(character)

    def delete_character(self, index):
        if 0 <= index < len(self.characters):
            self.characters.pop(index)

    def edit_character(self, index, name, role, level):
        if 0 <= index < len(self.characters):
            self.characters[index].name = name
            self.characters[index].role = role
            self.characters[index].level = level

    def get_all(self):
        return [c.to_dict() for c in self.characters]
