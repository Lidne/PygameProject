class RoadBlock:
    def __init__(self, pos_x: float, pos_y: float, objects: list):
        self.pos_y = pos_y
        self.objects = objects
        # Начало координат всех обьектов отсчитывается от верхнего левого края блока дороги (должно)

    def app_object(self, obj):
        self.objects.append(obj)

    def move(self, fps):
        self.pos_y += 40 / fps

    def render(self):
        for i in self.objects:
            pass
