# Enchantment Order Tool
Find the optimal order to enchant in Minecraft


## Usage
Command line interface, order is as follows:\
flag : item : enchantments\
Where flag is either 'o' or 'l' for Optimal or Level solutions respectively.\
item is capitalised name of desired item to enchant, represented in camel case so 
fishing rod becomes FishingRod.\
enchantments are individual enchantments separated by whitespaces: UNBR MEND FRST (Unbreaking, Mending, Frost Walker)

## Different solutions
Optimal solutions attempt to pair only once and combine with item greedily, this keeps cost low but results in an item
that has a high penalty (less chances to repair/modify).

Level solutions attempt to keep enchantments in a binary tree structure, using double-ended queue and recursion to calculate penalties, order enchantments and then unpack the nested list. These can sometimes be more expensive but will result in a lower penalty on the resulting item.

## Abbreviations
Located in the constants.py file in order_package are the multipliers, maximum enchantment levels and unabbreviated names.

### Notes
This project began as a proof of concept when I googled how to enchant items optimally. Using the [Minecraft](https://minecraft.wiki/w/Anvil_mechanics) Wiki page I saw a similarity to the Leetcode style problems and wondered if there was a way to use the patterns of problem solving from there and apply them to this problem, and I think overall I did well! 
I have plans to later use this program in a more interactive and user friendly web app, most likely using Flask, as the command line method currently implemented leaves a lot to be desired...
