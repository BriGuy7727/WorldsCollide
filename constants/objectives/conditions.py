from constants.objectives.condition_bits import check_bit, quest_bit, boss_bit, dragon_bit
from constants.entities import id_character
from constants.espers import id_esper

from collections import namedtuple
ConditionType = namedtuple("ConditionType", ["name", "string_function", "value_range", "min_max"])

types = [
    ConditionType("None", "", None, False),
    ConditionType("Random", "Random", ["r"], False),
    ConditionType("Characters", lambda count : f"Recruit {count} Characters",
                  list(range(1, len(id_character) + 1)), True),
    ConditionType("Character", lambda character : f"Recruit {id_character[character].capitalize()}",
                  ["r"] + sorted(id_character, key = id_character.get), False),
    ConditionType("Espers", lambda count : f"Find {count} Espers",
                  list(range(1, len(id_esper) + 1)), True),
    ConditionType("Esper", lambda esper : f"Find {id_esper[esper]}",
                  ["r"] + sorted(id_esper, key = id_esper.get), False),
    ConditionType("Dragons", lambda count : f"Defeat {count} Dragons",
                  list(range(1, len(dragon_bit) + 1)), True),
    ConditionType("Dragon", lambda dragon : f"Defeat {dragon_bit[dragon].name}",
                  ["r"] + list(range(len(dragon_bit))), False),
    ConditionType("Bosses", lambda count : f"Defeat {count} Bosses",
                  list(range(1, len(boss_bit) + 1)), True),
    ConditionType("Boss", lambda boss : f"Defeat {boss_bit[boss].name}",
                  ["r"] + list(range(len(boss_bit))), False),
    ConditionType("Checks", lambda count : f"Complete {count} Checks",
                  list(range(1, len(check_bit) + 1)), True),
    ConditionType("Check", lambda check : f"{check_bit[check].name}",
                  ["r"] + list(range(len(check_bit))), False),
    ConditionType("Quest", lambda quest : f"{quest_bit[quest].name}",
                  ["r"] + list(range(len(quest_bit))), False),
]

name_type = {_type.name : _type for _type in types}

names = list(name_type.keys())

# list out the acceptable condition types for World Access objectives to prevent softlocks
world_access_acceptable_conditions = [ 
    "None", 
    "Checks", 
    "Check", 
    "Quest" 
]
# list out the acceptable check conditions for World of Ruin Access objective to prevent softlocks
wor_access_acceptable_check_conditions = [ 
    "Baren Falls", 
    "Burning House",
    "Doma Siege",
    "Esper Mountain", 
    "Figaro Castle Throne",
    "Floating Cont. Arrive",
    "Floating Cont. Beast", 
    "Floating Cont. Escape",
    "Gau's Father's House",
    "Imperial Camp", 
    "Kohlingen Cafe", 
    "Lete River",
    "Lone Wolf Chase",
    "Magitek Factory Trash", 
    "Magitek Factory Guard",
    "Magitek Factory Finish",
    "Mt. Kolts",
    "Narshe Battle", 
    "Opera House Disruption",
    "Phantom Train", 
    "Sealed Gate", 
    "Serpent Trench",
    "South Figaro Prisoner", 
    "South Figaro Cave",
    "Tzen Thief", 
    "Veldt", 
    "Whelk Gate", 
    "Zozo Tower", 
    "Narshe Moogle Defense", 
    "Auction 1", 
    "Auction 2", 
]
# list out the acceptable quest conditions for World of Ruin Access objective to prevent softlocks
wor_access_acceptable_quest_conditions = [ 
    "Defeat Sealed Cave Ninja", 
    "Help Injured Lad",
    "Pass Security Checkpoint",
    "Perform In Opera", 
    "Win An Auction", 
]
# list out the acceptable check conditions for World of Balance Access objective to prevent softlocks
wob_access_acceptable_check_conditions = [ 
    "Ancient Castle", 
    "Ancient Castle Dragon", 
    "Burning House", 
    "Collapsing House", 
    "Daryl's Tomb", 
    "Doma Dream Door", 
    "Doma Dream Awaken", 
    "Doma Dream Throne", 
    "Ebot's Rock", 
    "Fanatic's Tower Dragon",
    "Fanatic's Tower Leader", 
    "Fanatic's Tower Follower",
    "Figaro Castle Throne", 
    "Figaro Castle Engine",
    "Kefka's Tower Cell Beast", 
    "Kefka's Tower Dragon G",
    "Kefka's Tower Dragon S",
    "Kohlingen Cafe",
    "Mobliz Attack",
    "Mt. Zozo", 
    "Mt. Zozo Dragon",
    "Narshe Dragon", 
    "Narshe Weapon Shop",
    "Opera House Dragon", 
    "Owzer's Mansion", 
    "Phoenix Cave", 
    "Phoenix Cave Dragon", 
    "Search The Skies", 
    "South Figaro Prisoner", 
    "Tritoch Cliff", 
    "Tzen Thief", 
    "Umaro's Cave", 
    "Veldt Cave", 
    "Zone Eater",  
    "Auction 1", 
    "Auction 2", 
]
# list out the acceptable quest conditions for World of Balance Access objective to prevent softlocks
wob_access_acceptable_quest_conditions = [ 
    "Let Cid Die", 
    "Save Cid",
    "Win An Auction",
    "Win A Coliseum Match", 
    "Defeat KT Ambusher", 
    "Defeat KT Robot", 
    "Defeat KT Left Statue", 
    "Defeat KT Mid Statue", 
    "Defeat KT Right Statue", 
]