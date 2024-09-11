from collections import deque
# classes for all tools
'''
String input will be something like: Pickaxe ME UB EF5 FO3
Then, use the pickaxe class to see if the inputted enchants are valid (no mutually exclusive ones like silk touch and fortune) or unassociated enchants like sharpness.
Next calculate the minimum cost for the input; still working on how to do this, probably some simple DP style implementation as the diagram from the wiki looks like a DAG... 


FORMULA: 
    for each enchantment:
        (sacrifice - target) * vals[enchantment][1] 
    for each PWP:
        2^(prior count) - 1

users separate current enchantments from desired enchantments with "|" 

sort input string into values based on multipliers
pickaxe FORT3 UNBR3 MEND EFFI5

Should the functions be defined in main.py?
functions should be in a separate file and then called in main.py, they are utils 

imports are:
standard,
third party 
local, library specific




'''
class Target():
    vals = {
        'PROT': (1,1),
        'FIPR': (2,1),
        'FEAT': (2,1),
        'BLPR': (4,2),
        'PRPR': (2,1),
        'THRN': (8,4),
        'RESP': (4,2),
        'DPTH': (4,2),
        'AQUA': (4,2),
        'SHRP': (1,1),
        'SMTE': (2,1),
        'BANE': (2,1),
        'KNCK': (2,1),
        'FASP': (4,2),
        'LOOT': (4,2),
        'EFFI': (1,1),
        'SILK': (8,4),
        'UNBR': (2,1),
        'FORT': (4,2),
        'POWR': (1,1),
        'PNCH': (4,2),
        'FLME': (4,2),
        'INFI': (8,4),
        'LUCK': (4,2),
        'FRST': (4,2),
        'MEND': (4,2),
        'BIND': (8,4),
        'VNSH': (8,4),
        'IMPL': (2,1), # JE has x2 the multipliers than bedrock, so use BE as standard.
        'RIPT': (4,2),
        'LOYL': (1,1),
        'CHAN': (8,4),
        'MLTI': (4,2),
        'PIER': (1,1),
        'QUIK': (2,1),
        'SOUL': (8,4),
        'SWFT': (8,4),
        }
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


# x = Pickaxe()
# y = Pickaxe
# print(x.enchants, type(y))