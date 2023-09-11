class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def go_to_school(self):
        return "Attend school " + self.name
    def __str__(self):
        return f"Name = {self.name}, Address = {self.address}"


gbc = School(name="George Brown College", address="160 Kendal Ave")
print(gbc)
print(gbc.go_to_school())
