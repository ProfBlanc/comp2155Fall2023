class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"Name = {self.name}, Address = {self.address}"

gbc = School(name="George Brown College", address="160 Kendal Ave")

print(gbc.name, gbc.address)
print(gbc)
