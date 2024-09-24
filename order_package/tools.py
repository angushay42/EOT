from .items import AllPurpose


class Tools(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['FORT', 'SILK'])
        self.enchants += ['FORT', 'SILK', 'EFFI']

@AllPurpose.register_subclass('Pickaxe')
class Pickaxe(Tools):
    def __init__(self) -> None:
        super().__init__()

@AllPurpose.register_subclass('Axe')
class Axe(Tools):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(self.damages)
        self.enchants += self.damages

@AllPurpose.register_subclass('Hoe')
class Hoe(Tools):
    def __init__(self) -> None:
        super().__init__()

@AllPurpose.register_subclass('Shovel')
class Shovel(Tools):
    def __init__(self) -> None:
        super().__init__()

@AllPurpose.register_subclass('FishingRod')
class FishingRod(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['LUCK','LURE']