from order_package.utils import freq
from order_package.constants import MULTIPLIERS

'''
String input will be something like: Pickaxe ME UB EF5 FO3
Then, use the pickaxe class to see if the inputted enchants are valid (no mutually exclusive ones like silk touch and fortune) or unassociated enchants like sharpness.
Next calculate the minimum cost for the input; still working on how to do this, probably some simple DP style implementation as the diagram from the wiki looks like a DAG... 


FORMULA: 
    for each enchantment:
        (sacrifice - AllPurpose) * vals[enchantment][1] 
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

def main():
    print(freq(5))


if __name__ == "__main__":
    main()