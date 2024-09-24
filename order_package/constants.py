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

VALUES = {
    # All purpose
    'UNBR': 3,
    'MEND': 1,
    'BIND': 1,
    'VNSH': 1,

    # All armour
    'PROT': 4,
    'FIPR': 4,
    'BLPR': 4,
    'PRPR': 4,
    'THRN': 3,

    # Helmet
    'RESP': 3,
    'AQUA': 1,

    # Leggings
    'SWFT': 3,

    # Boots
    'FRST': 2,
    'SOUL': 3,
    'DPTH': 3,
    'FEAT': 4,

    # All mining tools
    'EFFI': 5,
    'SILK': 1,
    'FORT': 3,
    
    # Fishing Rod
    'LUCK': 3,
    'LURE': 3,

    # Damage Multipliers
    'SHRP': 5,
    'SMTE': 5,
    'BANE': 5,

    # Sword 
    'KNCK': 2,
    'FASP': 2,
    'LOOT': 3,

    # Bow
    'POWR': 5,
    'PNCH': 2,
    'FLME': 1,
    'INFI': 1,

    # Trident
    'IMPL': 5, 
    'RIPT': 3,
    'LOYL': 3,
    'CHAN': 1,

    # Crossbow
    'MLTI': 1,
    'PIER': 4,
    'QUIK': 3,

    # Mace
    'BRCH': 4,
    'WIND': 3,
    'DENS': 5
}

NAMES = {
    # All purpose
    'UNBR': 'Unbreaking',
    'MEND': 'Mending',
    'BIND': 'Curse of Binding',
    'VNSH': 'Curse of Vanishing',

    # All armour
    'PROT': 'Protection',
    'FIPR': 'Fire Protection',
    'BLPR': 'Blast Protection',
    'PRPR': 'Projectile Protection',
    'THRN': 'Thorns',

    # Helmet
    'RESP': 'Repsiration',
    'AQUA': 'Aqua Affinity',

    # Leggings
    'SWFT': 'Swift Sneak',

    # Boots
    'FRST': 'Frost Walker',
    'SOUL': 'Soul Speed',
    'DPTH': 'Depth Strider',
    'FEAT': 'Feather Falling',

    # All mining tools
    'EFFI': 'Efficiency',
    'SILK': 'Silk Touch',
    'FORT': 'Fortune',
    
    # Fishing Rod
    'LUCK': 'Luck of the Sea',
    'LURE': 'Lure',

    # Damage Multipliers
    'SHRP': 'Sharpness',
    'SMTE': 'Smite',
    'BANE': 'Bane of Anthropods',

    # Sword 
    'KNCK': 'Knockback',
    'FASP': 'Fire Aspect',
    'LOOT': 'Looting',

    # Bow
    'POWR': 'Power',
    'PNCH': 'Punch',
    'FLME': 'Flame',
    'INFI': 'Infinity',

    # Trident
    'IMPL': 'Impaling', 
    'RIPT': 'Riptide',
    'LOYL': 'Loyalty',
    'CHAN': 'Channeling',

    # Crossbow
    'MLTI': 'Multi Shot',
    'PIER': 'Piercing',
    'QUIK': 'Quick Charge',

    # Mace
    'BRCH': 'Breach',
    'WIND': 'Wind Burst',
    'DENS': 'Density'
}