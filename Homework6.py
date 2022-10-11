class Car:
    def __init__(self, stamp, model, year, speed):  # Определяем основные свойства класса Car
        self.stamp = stamp
        self.model = model
        self.year = year
        self.speed = speed

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def speed_stop(self):
        self.speed = 0

    def speed_show(self):
        print(self.speed)

    def speed_reserv(self):
        self.speed = -self.speed


mers = Car("Mersedes", "модель Е500", 2000, 50)
print(mers.stamp)
print(mers.model)
print(mers.year)
print(mers.speed)
while mers.speed != 100:  # пока скорость мерседеса не равна 100 выполняется цикл (при условии, что скорость кратна 5)
    if mers.speed < 100:  # если скорость меньше 100,  то увеличииваем скорость на 5
        mers.speed_up()
    elif mers.speed > 100:  # если скорость больше 100,  то  уменьшаем скорость на 5
        mers.speed_down()
mers.speed_show()  # показываем текущую скорость