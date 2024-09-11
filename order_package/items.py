from collections import deque


# classes for all tools

class AllPurpose():
    def __init__(self) -> None:
        self.enchants = ['MEND', 'UNBR']

class Tools(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['FORT', 'SILK', 'EFFI']
    
    
class FishingRod(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['LUCK','LURE']
    pass


class Shears(AllPurpose):
    def __init__(self) -> None:
        super().__init__()


class Pickaxe(Tools):
    def __init__(self) -> None:
        super().__init__()


# x = Pickaxe()
# y = Pickaxe
# print(x.enchants, type(y))