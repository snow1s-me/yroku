class ТранспортнийЗасіб:
    швидкість = 100

    def переміщення(self):
        print(f"Я їду {self.швидкість}км/год")
class Zhugyli(ТранспортнийЗасіб):
    pass
class Koenigsegg(ТранспортнийЗасіб):
    швидкість = 450
car1 = Zhugyli()
car2 = Koenigsegg()
car1.переміщення()
car2.переміщення()