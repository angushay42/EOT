# classes for all tools
'''
String input will be something like: Pickaxe ME UB EF5 FO3
Then, use the pickaxe class to see if the inputted enchants are valid (no mutually exclusive ones like silk touch and fortune) or unassociated enchants like sharpness.
Next calculate the minimum cost for the input; still working on how to do this, probably some simple DP style implementation as the diagram from the wiki looks like a DAG... 
'''
class Target():
    def __init__(self) -> None:
        self.enchants = ['ME', 'UB']


class Tools(Target):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['FO', 'ST', 'EF']
    
    
class Fishing_Rod(Tools):
    # enchants = ['LU','LOS']
    pass


class Shears(Tools):
    pass


class Pickaxe(Tools):
    def __init__(self) -> None:
        super().__init__()


x = Pickaxe()
y = Pickaxe
print(x.enchants, type(y))
