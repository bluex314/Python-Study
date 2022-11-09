class Biscuts:
    def __init__(self, name):
        self.name = name

bis = Biscuts('Oreo')

print(bis.name)

# deleting the object using del
del bis

print(bis.name)
