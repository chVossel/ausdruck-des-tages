from datetime import datetime

class Ausdruck():
    def __init__(self, ausdruck):
        self.ausdruck = ausdruck
        self.zeit = datetime.now()
        self.likes = 0
    
    def like_hinzufuegen(self):
        self.likes = self.likes + 1

    def __lt__(self, other):
        return self.likes < other.likes
