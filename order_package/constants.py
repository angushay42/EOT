'''
Enchantments and their multipliers are immutable.
'''

MULTIPLIERS = {
    # All purpose
    'UNBR': (2,1),
    'MEND': (4,2),
    'BIND': (8,4),
    'VNSH': (8,4),

    # All armour
    'PROT': (1,1),
    'FIPR': (2,1),
    'BLPR': (4,2),
    'PRPR': (2,1),
    'THRN': (8,4),

    # Helmet
    'RESP': (4,2),
    'AQUA': (4,2),

    # Leggings
    'SWFT': (8,4),

    # Boots
    'FRST': (4,2),
    'SOUL': (8,4),
    'DPTH': (4,2),
    'FEAT': (2,1),

    # All mining tools
    'EFFI': (1,1),
    'SILK': (8,4),
    'FORT': (4,2),
    
    # Fishing Rod
    'LUCK': (4,2),
    'LURE': (4,2),

    # Damage Multipliers
    'SHRP': (1,1),
    'SMTE': (2,1),
    'BANE': (2,1),

    # Sword 
    'KNCK': (2,1),
    'FASP': (4,2),
    'LOOT': (4,2),

    # Bow
    'POWR': (1,1),
    'PNCH': (4,2),
    'FLME': (4,2),
    'INFI': (8,4),

    # Trident
    'IMPL': (2,1), # JE has x2 the multipliers than bedrock, so use BE as standard.
    'RIPT': (4,2),
    'LOYL': (1,1),
    'CHAN': (8,4),

    # Crossbow
    'MLTI': (4,2),
    'PIER': (1,1),
    'QUIK': (2,1),

    # Mace
    'BRCH': (4,2),
    'WIND': (4,2),
    'DENS': (2,1)
}