class Пристрій:
    def увімкнути(self):
        print(f"Пристрій працює")
    def вимкнути(self):
        print(f"Пристрій вимкнений")

class Iphone(Пристрій):
    pass

class Навушники(Пристрій):
    pass

p1 = Iphone()
p2 = Навушники()
while True:
    a = int(input("Який пристрій вибрати?1=Телефон/2=Навушники: "))
    if a == 1:
        b = int(input("1=Увімкнути/2=Вимкнути: "))
        if b == 1:
            p1.увімкнути()
        if b == 2:
            p1.вимкнути()
    if a == 2:
        v = int(input("1=Увімкнути/2=Вимкнути: "))
        if v == 1:
            p2.увімкнути()
        if v == 2:
            p2.вимкнути()