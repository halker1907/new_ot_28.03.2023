from random import randint
import os



class War:
    def __init__(self, name) -> None:
        self.name = name
        self.hp = 100
        self.attack = 10
        self.lvl = 1
        self.xp = 0
        self.money = 10
        self.inventory = []

    def combat_turn(self):
        if p3.hp > 0:
            damage = p3.attack
            p1.hp -= damage
            print(f"{p3.name} ударил {p1.name} на {damage} жизней!")
            
    def combat_turn2(self):
        if p1.hp > 0:
            damage = p1.attack
            p3.hp -= damage
            print(f"{p3.name} ударил {p1.name} на {damage} жизней!")        

    def fight(self):
        while p3.hp > 0 and p1.hp > 0:
            combat_turn()
            combat_turn2()
            print("")
            print(f"{p1.name} {p1.hp}")
            print(f"{p3.name} {p3.hp}")
            input("\nНажмите ENTER чтобы сделать следующий ход")
        os.system("cls")
        if p3.hp > 0 and p1.hp <= 0:
            print(f"{p3.name} победил!")

        elif p3.hp <= 0 and p1.hp > 0:
            print(f"{p1.name} победил!")
        else:
            print(f"{p1.name} и {p3.name} пали в бою:(")

def sworld(self):
    re = Sword("меч")
    self.inventory.append(re.name)
    print(f"инвентарь {self.name} состоит из {self.inventory}")

class Item:
    def __init__(self, name="предмет", price=0):
        self.name = name
        self.price = price


class Weapon(item):
    def __init__(self):
        super().__init__()
        self.damage

a = Item()
print(a.name)
print(a.price)

a = Weapon()
if isinstance(a, Weapon):
    pass