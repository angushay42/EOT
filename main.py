from sys import argv
from typing import Type


from order_package.utils import level, level_cost, display_level, optimal, display_optimal
from order_package.constants import MULTIPLIERS, VALUES, NAMES
from order_package.items import *
from order_package.armour import *
from order_package.tools import *
from order_package.weapons import * 

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

# Pickaxe * MEND UNBR FORT EFFI * Y
# already enchanted?
# UNBR-1 FORT-1 EFFI-2
def main():
    # Variables
    item = enchants = flag =None
    edition = 0
    # Check for nul string
    if len(argv) > 1:
        # For future implementation, allow edition to be specified. 
        # Default is Bedrock.
        if argv[1] == 'J':
            edition = 1
        # Split argv into 
        try:
            flag, item, enchants = ' '.join(argv[edition+1:]).split(':')
        except ValueError:
            return 1
    else:
        flag, item, enchants = 'l', 'Boots', 'UNBR SOUL DPTH FEAT PROT MEND THRN'
    # Clean up variables
    item = item.strip()
    enchants = enchants.strip().split(' ')

    # Initialise temp array.
    temp = []
    for idx, e in enumerate(enchants):
        # Ensure spelling is correct.
        if e in VALUES:
            # Multipliers[key][0] represents the multiplier from an item,
            # and can be implemented later however it is so inefficient to do so,
            # both in cost of levels and the comparative ease of books, it is not recommended.
            temp.append((VALUES[e] * MULTIPLIERS[e][1], enchants[idx]))
    
    # Sort vals array alongside enchants to ensure they match.
    vals = [x[0] for x in sorted(temp, reverse=True)]
    book_names = [NAMES[x[1]] for x in sorted(temp, reverse=True)] # For nicer printing.


    # Incorrect input.
    if not len(vals) == len(book_names):
        return 2
    
    # Class factory.
    obj = AllPurpose().create(item)()
    
    # Check mutually exclusive.
    if obj.mutual(enchants):
        return 3
    

    cost = order = None
    # Optimal
    if 'o' in flag:
        cost, order = optimal(vals)
        print("To enchant optimally: ")
        display_optimal(order, book_names)
    # Level
    elif 'l' in flag:
        cost, order = level(len(vals))
        cost += level_cost(vals)
        print('To enchant in level order: ')
        display_level(order, book_names)
    else: 
        return 4
    print('Total cost: {}'.format(cost))
    return 0


if __name__ == "__main__":
    error_codes = {0: 'Yay!',
                   1: 'Separating input',
                   2: 'Invalid enchantment names',
                   3: 'Mutually exclusive enchantments',
                   4: 'No flag'}
    print("Error: {}".format(error_codes[main()]))