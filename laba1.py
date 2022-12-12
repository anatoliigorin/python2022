# coding=windows-1251
import json
class Item:
    name = "Undefined"
    inventoryTab = "Items"

    def __init__(self, name):
        self.name = name

    def get_info(self):
        print(f"��������: {self.name}\n������� ���������: {self.inventoryTab}\n")

class Tool(Item):
    hardness = 0
    inventoryTab = "Tools"

    def __init__(self, name, hardness):
        super().__init__(name)
        if hardness >= 0:
            self.hardness = hardness
        else:
            print("������������ ���������")

    def get_info(self):
        print(f"��������: {self.name}\n������� ���������: {self.inventoryTab}\n���������: {self.hardness}\n")

class Weapon(Item):
    strength = 0
    inventoryTab = "Weapons"

    def __init__(self, name, hardness, strength):
        super().__init__(name)
        self.hardness = hardness
        if strength >= 0:
            self.strength = strength
        else:
            print("������������ ����")

    def get_info(self):
        print(f"��������: {self.name}\n������� ���������: {self.inventoryTab}\n���������: {self.hardness}\n����: {self.strength}\n")

class Bow(Weapon):
    stringTension = 0
    hardness = 64
    strength = 13
    name = "Bow"

    def __init__(self, stringTension):
        super().__init__(self.name, self.hardness, self.strength)
        if stringTension >= 0:
            self.stringTension = stringTension
        else:
            print("������������ ��������� ������")

    def get_info(self):
        print(f"��������: {self.name}\n������� ���������: {self.inventoryTab}\n���������: {self.hardness}\n����: {self.strength}\n���������: {self.stringTension}\n")

class Block(Item):
    inventoryTab = "Blocks"
    isDestructable = True
    isFluid = False

    def __init__(self, name, isDestructable, isFluid):
        super().__init__(name)
        self.isDestructable = isDestructable
        if isDestructable == False:
            self.isFluid = isFluid

    def get_info(self):
        print(f"��������: {self.name}\n������� ���������: {self.inventoryTab}\n�������������: {self.isDestructable}\n������: {self.isFluid}\n")


bow = Bow(14)
bow.get_info()

stone = Block("������", True, False)
stone.get_info()

sword = Weapon("���", 64, 15)
sword.get_info()

pickaxe = Tool("�����", 1024)
pickaxe.get_info()

data = {
    "bow":{
        "name": bow.name,
        "hardness" : bow.hardness
        },
    "stone":{
        "name": stone.name,
        "tab": stone.inventoryTab,
        "isDestructable": stone.isDestructable,
        "isFluid": stone.isFluid
        }
    }
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

with open("data_file.json", "r") as read_file:
    new_data = json.load(read_file)

print(new_data)