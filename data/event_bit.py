# NOTE: (address - 1e80) * 0x8 + bit
# e.g. (1eb7 - 1e80) * 0x8 + 0x1 = 1b9 (airship visible)
#      (1f43 - 1e80) * 0x8 + 0x3 = 61b (characters on narshe battlefield)
# See bottom of file for event bit list; if adding a new event, use an Unused? one

DISABLE_SAVE_POINT_TUTORIAL = 0x133
DISABLE_CHOCOBO_TUTORIAL = 0x134

VICKS_BROKE_WHELK_GATE = 0x12c
NARSHE_GUARDS_SAW_TERRA_ON_BRIDGE = 0x12d
FINISHED_MOOGLE_DEFENSE = 0x12e # custom, used to be terra fell in narshe cave hole
MET_ARVIS = 0x001 # characters no longer ride mtek armor in mines when set
DEFEATED_WHELK = 0x135
NAMED_EDGAR = 0x004
NAMED_SABIN = 0x005
PRISON_DOOR_OPEN_FIGARO_CASTLE = 0x2b7
MET_KEFKA_FIGARO_CASTLE = 0x006
FIRST_NOISE_FIGARO_CAVE = 0x0ae
SECOND_NOISE_FIGARO_CAVE = 0x0af
THIRD_NOISE_FIGARO_CAVE = 0x0b0
DEFEATED_TUNNEL_ARMOR = 0x0b1 # custom, used to be south figaro cave recovery spring
SAW_SHADOW_WALKING_TO_CAFE_SOUTH_FIGARO = 0x00a
NAMED_SHADOW = 0x00b
SAW_VARGAS_SHADOW1 = 0x00d
SAW_VARGAS_SHADOW2 = 0x00e
SAW_VARGAS_SHADOW3 = 0x00f
DEFEATED_VARGAS = 0x010
MET_BANON = 0x011
GOT_GENJI_GLOVES_OR_GAUNTLET = 0x017
RODE_RAFT_FIRST_TIME_LETE_RIVER = 0x019
FOUGHT_ULTROS_LETE_RIVER = 0x01a
RODE_RAFT_LETE_RIVER = 0x257
WOUND_THE_CLOCK_SOUTH_FIGARO = 0x10d
CELES_LOCKE_ESCAPED_SOUTH_FIGARO = 0x01b
NAMED_CELES = 0x01c
FREED_CELES = 0x01d
FINISHED_LOCKE_SCENARIO = 0x01e
NARSHE_SECRET_ENTRANCE_ACCESS = 0x020
FINISHED_NARSHE_CHECKPOINT = 0x2d8 # custom, used to be narshe checkpoint explanation
FINISHED_TERRA_SCENARIO = 0x021
SAW_SHADOW_DREAM1 = 0x024
SAW_SHADOW_DREAM2 = 0x026
SAW_SHADOW_DREAM3 = 0x027
SAW_SHADOW_DREAM4 = 0x028
RECRUITED_SHADOW_GAU_FATHER_HOUSE = 0x162
CYAN_FOUND_POISONED_KING_DOMA = 0x031
CYAN_FOUND_POISONED_FAMILY_DOMA = 0x032
FINISHED_DOMA_WOB = 0x040 # custom
GENERAL_LEO_IMPERIAL_CAMP = 0x02b
BRIDGE_BLOCKED_IMPERIAL_CAMP = 0x02c
CHASING_KEFKA1_IMPERIAL_CAMP = 0x02d
CHASING_KEFKA2_IMPERIAL_CAMP = 0x02e
CHASING_KEFKA3_IMPERIAL_CAMP = 0x02f
FINISHED_CHASING_KEFKA_IMPERIAL_CAMP = 0x155
FINISHED_IMPERIAL_CAMP = 0x037
LUMP_CHEST_DOOR_GHOST_PHANTOM_TRAIN = 0x180 # used for both door ghost in wob and lump of metal chest in wor
GOT_PHANTOM_TRAIN_REWARD = 0x192 # custom, used to be phantom forest recovery spring
FOUND_PHANTOM_TRAIN = 0x038
STOPPED_PHANTOM_TRAIN = 0x03a
DEFEATED_PHANTOM_TRAIN = 0x03b
NAMED_GAU = 0x03f
FOUND_DIVING_HELMET = 0x041
FINISHED_SABIN_SCENARIO = 0x044
FIGHTING_KEFKA_NARSHE_WOB = 0x132
FINISHED_NARSHE_BATTLE = 0x046
RECRUITED_SHADOW_KOHLINGEN = 0x18e
CAN_LEARN_BUM_RUSH = 0x04b # custom, set when all other blitzes learned or bum rush last disabled
LEARNED_BUM_RUSH = 0x2af
GOT_SERPENT_TRENCH_REWARD = 0x050 # custom
SET_ZOZO_CLOCK = 0x51
GOT_ZOZO_REWARD = 0x052 # custom
SAW_OPERA_OVERTURE = 0x055
READY_CELES_OPERA_SCENE = 0x056
BEGAN_OPERA_DISRUPTION = 0x110
FINISHED_OPERA_PERFORMANCE = 0x111
SAW_OPERA_DUEL_SCENE = 0x2ba
OPERA_MAP_MODIFIED1 = 0x057
FOUND_ULTROS_LETTER_OPERA = 0x58
OPERA_MAP_MODIFIED2 = 0x059
OPERA_MAP_MODIFIED3 = 0x05a
FINISHED_OPERA_DISRUPTION = 0x05b # custom
SETZER_ABDUCTED_CELES = 0x05c
TOSSED_CELES_SETZER_COIN = 0x05d
DEFEATED_NINJA_CAVE_TO_SEALED_GATE = 0x075 # custom
TERRA_AGREED_TO_OPEN_SEALED_GATE = 0x076
DEFEATED_NUMBER_024 = 0x05f # custom, used to be saw kefka throw ifrit/shiva in trash
DEFEATED_IFRIT_SHIVA_MAGITEK_FACTORY = 0x060
GOT_IFRIT_SHIVA = 0x061
TALKED_TO_IFRIT_MAGITEK_FACTORY = 0x272
TALKED_TO_SHIVA_MAGITEK_FACTORY = 0x274
DISABLE_HOOK_MAGITEK_FACTORY = 0x273
RODE_MINE_CART_MAGITEK_FACTORY = 0x069
MET_SETZER_AFTER_MAGITEK_FACTORY = 0x06a # locke/celes not required in airship changing room after set
DEFEATED_CRANES = 0x06b
SAW_MADUIN_DIE = 0x070 # enables lone wolf
ESPERS_CRASHED_AIRSHIP = 0x242 # allows entry to imperial base without terra
FINISHED_GESTAHL_DINNER = 0x07d
MET_STRAGO_RELM = 0x08d
DEFEATED_FLAME_EATER = 0x090
DEFEATED_ULTROS_ESPER_MOUNTAIN = 0x095
ESPER_MOUNTAIN_GATED = 0x097 # custom, if true relm won't appear and ultros battle won't happen, previously used for statues found
ESPER_MOUNTAIN_ACCESSIBLE = 0x098
FOUND_ESPERS_ESPER_MOUNTAIN = 0x099
DEFEATED_KEFKA_THAMASA = 0x09b
LEO_BURIED_THAMASA = 0x09c
FINISHED_THAMASA_KEFKA = 0x09d
CONTINENT_IS_FLOATING = 0x09e
LEARNED_TO_FLY_AIRSHIP = 0x16f
AIRSHIP_VISIBLE = 0x1b9
AIRSHIP_FLYING = 0x246
GOT_FALCON = 0x0cd
WON_AN_AUCTION = 0x166 # custom
AUCTION_BOUGHT_ESPER1 = 0x16c # normally zoneseek
AUCTION_BOUGHT_ESPER2 = 0x16d # normally golem
WON_A_COLISEUM_MATCH = 0x1ef # custom, used to be shadow available at coliseum
BOUGHT_ESPER_TZEN = 0x27c # normally sraphim
RECRUITED_SHADOW_FLOATING_CONTINENT = 0x02a
DEFEATED_ATMAWEAPON = 0x0a1 # custom
DEFEATED_ATMA = 0x0a2 # custom
LEFT_SHADOW_FLOATING_CONTINENT = 0x0a3
IN_WOR = 0x0a4
FINISHED_FLOATING_CONTINENT = 0x0a5 # custom
STARTED_FEEDING_CID = 0x0b2 # custom, previously found cid dead
CID_SURVIVED = 0x0b3
CID_DIED = 0x0b4
FINISHED_FEEDING_CID = 0x0b9 # custom
BOARDED_CRIMSON_ROBBERS_BOAT_NIKEAH = 0x0ac
DEFEATED_TENTACLES_FIGARO = 0x0c6
LIGHT_JUDGEMENT_TZEN = 0x27d
FINISHED_COLLAPSING_HOUSE = 0x28a
HELPED_INJURED_LAD = 0x28d
DOGS_BARKED_MOBLIZ_WOR = 0x28e
MET_TERRA_WOR = 0x28f
SAW_MOBLIZ_LIGHT_OF_JUDGEMENT_SCENE = 0x290
FOUGHT_PHUNBABA1 = 0x291
GOT_FENRIR = 0x2d7
KATARIN_PREGNANT = 0x0be
CHOSE_RAGNAROK_ESPER = 0x0b5 # custom
GOT_RAGNAROK = 0x0b6
GOT_BOTH_REWARDS_WEAPON_SHOP = 0x0b7 # custom
CHASING_LONE_WOLF1 = 0x239
CHASING_LONE_WOLF7 = 0x23f
GOT_BOTH_REWARDS_LONE_WOLF = 0x241
MET_LONE_WOLF_WOR = 0x29b
RECRUITED_MOG_WOB = 0x29f
RECRUITED_UMARO_WOR = 0x07e
DARYL_TOMB_TURTLE1_MOVED = 0x2b4
DARYL_TOMB_TURTLE2_MOVED = 0x2b6
DEFEATED_DULLAHAN = 0x2b2
RUST_RID_FOR_SALE = 0x298
GOT_RUST_RID = 0x1db
FOUND_CYAN_MT_ZOZO = 0x0d1 # custom
FINISHED_MT_ZOZO = 0x0d2
DEFEATED_SR_BEHEMOTH = 0x199
FOUND_DREAM_STOOGE1 = 0x189
FOUND_DREAM_STOOGE2 = 0x18b
FOUND_INTERCEPTOR_VELDT_CAVE_WOR = 0x195
DEFEATED_CHADARNOOK = 0x253
FOUND_EBOTS_ROCK = 0x19a
MET_EBOTS_ROCK_CHEST = 0x19b
DEFEATED_HIDON = 0x19c
RECRUITED_GOGO_WOR = 0x0d4
DEFEATED_STOOGES = 0x0d8
FINISHED_DOMA_WOR = 0x0da
GOT_ALEXANDR = 0x0db
DEFEATED_MAGIMASTER = 0x2db
RECRUITED_STRAGO_FANATICS_TOWER = 0x0ba
DEFEATED_DOOM_GAZE = 0x2a1 # custom
RECRUITED_LOCKE_PHOENIX_CAVE = 0x0d7
RECRUITED_TERRA_MOBLIZ = 0x0bf
GOT_TRITOCH = 0x29e
GOT_RAIDEN = 0x2dd
FOUND_ANCIENT_CASTLE = 0x2df
GOT_ODIN = 0x0c8
SUPLEXED_TRAIN = 0x2b0 # custom, previously unused but set in nikeah entrance event

DEFEATED_NARSHE_DRAGON = 0x11a # custom
DEFEATED_MT_ZOZO_DRAGON = 0x11b # custom
DEFEATED_OPERA_HOUSE_DRAGON = 0x11c # custom
DEFEATED_KEFKA_TOWER_DRAGON_G = 0x11d # custom, gold dragon location
DEFEATED_KEFKA_TOWER_DRAGON_S = 0x11e # custom, skull dragon location
DEFEATED_ANCIENT_CASTLE_DRAGON = 0x11f # custom
DEFEATED_PHOENIX_CAVE_DRAGON = 0x120 # custom
DEFEATED_FANATICS_TOWER_DRAGON = 0x121 # custom
# used in Location Gating modes
UNLOCKED_WOR = 0x088 # custom
UNLOCKED_WOB = 0x08a # custom

# KT Battles
DEFEATED_GUARDIAN = 0x0bc
DEFEATED_INFERNO = 0x0bd
DEFEATED_DOOM = 0x072
DEFEATED_GODDESS = 0x073
DEFEATED_POLTERGEIST = 0x074

LEFT_WEIGHT_PUSHED_KEFKA_TOWER = 0x063
RIGHT_WEIGHT_PUSHED_KEFKA_TOWER = 0x064
WEST_PATH_BLOCKED_KEFKA_TOWER = 0x065   # path to doom in switch room
EAST_PATH_BLOCKED_KEFKA_TOWER = 0x066   # path to goddess in switch room
NORTH_PATH_OPEN_KEFKA_TOWER = 0x067     # path to guardian in switch room
SOUTH_PATH_OPEN_KEFKA_TOWER = 0x071     # path to balcony in switch room
CENTER_DOOR_KEFKA_TOWER = 0x080         # center door in weights room
LEFT_RIGHT_DOORS_KEFKA_TOWER = 0x0d0    # doors to doom/goddess opened on balcony
UNLOCKED_KT_SKIP = 0x093 # custom
UNLOCKED_FINAL_KEFKA = 0x094 # custom

SIEGFRIED_LUMP_OF_METAL_CHESTS = 0x187 # set after siegfried chest in phantom train and lump of metal chest in cyan's dream
VELDT_WORLD_MUSIC = 0x1bb
VELDT_REWARD_OBTAINED = 0x1bc # custom
DISABLE_SPRINT = 0x1c1
DISABLE_MENU_ACCESS = 0x1c2
TEMP_SONG_OVERRIDE = 0x1cc
CONTINUE_MUSIC_DURING_BATTLE = 0x2bc
ENABLE_Y_PARTY_SWITCHING = 0x1ce
ALWAYS_CLEAR = 0x176 # this event_bit is always clear, used for branching

from constants.objectives import MAX_OBJECTIVES
for index in range(MAX_OBJECTIVES):
    globals()["OBJECTIVE" + str(index)] = 0xe0 + index

def byte(event_bit):
    return event_bit // 8

def bit(event_bit):
    return event_bit % 8

def address(event_bit):
    return 0x1e80 + byte(event_bit)

def character_recruited(char):
    # char in shops, items, gogo menu
    return 0x2e0 + char

def character_available(char):
    # char can be chosen in party select menus
    return 0x2f0 + char

def multipurpose(index):
    assert index >= 0 and index <= 15
    return 0x1a0 + index

def multipurpose_map(index):
    # cleared on map load
    assert index >= 0 and index <= 15
    return 0x1f0 + index

def multipurpose_party1_step(index):
    # cleared on each step by party1
    assert index >= 0 and index <= 3
    return 0x2c4 + index

def multipurpose_party2_step(index):
    # cleared on each step by party2
    assert index >= 0 and index <= 3
    return 0x2c8 + index

def multipurpose_party3_step(index):
    # cleared on each step by party3
    assert index >= 0 and index <= 3
    return 0x2cc + index

def objective(index):
    assert index >= 0 and index <= MAX_OBJECTIVES
    return 0xe0 + index

'''
Bit RAM  Description
-------------------------------------------------------------------------------
000 80:0 Unused?
001 80:1 Met Arvis (disables a Magitek Armor-related function in the mines)
002 80:2 Unused?
003 80:3 Initiated the tripartite battle with the Moogles (pointless?)
004 80:4 Named Edgar (affects Figaro Castle and Narshe)
005 80:5 Named Sabin
006 80:6 Met Kefka in Figaro Castle
007 80:7 Saw Sabin say he has to wander around Figaro Castle for a while
008 81:0 Locke is inside the library of Figaro Castle
009 81:1 Unused?
00A 81:2 Saw Shadow heading toward the Cafe
00B 81:3 Named Shadow
00C 81:4 Unused?
00D 81:5 Shadowy "Vargas" 1
00E 81:6 Shadowy "Vargas" 2
00F 81:7 Shadowy "Vargas" 3
010 82:0 Defeated Vargas (affects South Figaro and Sabin's Cabin)
011 82:1 Met Banon
012 82:2 Awakening plays in the Returners' Hideout; can find the scrap of paper
013 82:3 Accepted Banon's offer (useless?)
014 82:4 Declined Banon's offer 1
015 82:5 Declined Banon's offer 2
016 82:6 Declined Banon's offer 3 (useless?)
017 82:7 Got either Gauntlet or Genji Glove
018 83:0 Banon joined the party
019 83:1 Boarded the raft (affects Narshe and Lete River)
01A 83:2 Fought Ultros at Lete River (affects various locations)
01B 83:3 Celes asked Locke why he was helping her
01C 83:4 Named Celes
01D 83:5 Removed Celes's chains
01E 83:6 Completed Locke's scenario
01F 83:7 Banon and the others were denied entry to Narshe
020 84:0 Discovered how to open the secret entrance in Narshe
021 84:1 Completed Terra's scenario
022 84:2 Saw the scene involving Gau's father's stove
023 84:3 Unused?
024 84:4 Shadow's dream 1
025 84:5 Unused? (It possibly had a connection with a dummy dream in Thamasa.)
026 84:6 Shadow's dream 2
027 84:7 Shadow's dream 3
028 85:0 Shadow's dream 4
029 85:1 Saw the scene preceding the parties' entry into Kefka's Tower
02A 85:2 Met Shadow initially on the Floating Continent
02B 85:3 Saw the scene with Leo in the Imperial camp 1
02C 85:4 Saw the scene with Leo in the Imperial camp 2
02D 85:5 Chasing Kefka 1
02E 85:6 Chasing Kefka 2
02F 85:7 Chasing Kefka 3
030 86:0 The river surrounding Doma has been contaminated with poison
031 86:1 Cyan found the poisoned King of Doma
032 86:2 Cyan discovered his dead family
033 86:3 Cyan arrived at the Imperial camp (useless?)
034 86:4 Uncontrollable Cyan battle 1
035 86:5 Uncontrollable Cyan battle 2
036 86:6 Uncontrollable Cyan battle 3
037 86:7 Left the Imperial camp for good
038 87:0 Noticed the Phantom Train
039 87:1 Locked in the Phantom Train
03A 87:2 No train anymore in Phantom Forest
03B 87:3 Defeated GhostTrain (useless?)
03C 87:4 Reached Baren Falls
03D 87:5 Saw a ghost emerge from and obstruct an entryway (cleared eventually)
03E 87:6 Unused?
03F 87:7 Named Gau
040 88:0 Unused? -> FF6WC Finished Doma WOB
041 88:1 Unearthed the diving helmet
042 88:2 Unused?
043 88:3 Saw the scene with Cyan and the dancer in Nikeah
044 88:4 Completed Sabin's scenario (clears the rockslide at Nikeah)
045 88:5 Concluded the scenarios (useless?)
046 88:6 Defeated Kefka at Narshe (useless?)
047 88:7 Unused?
048 89:0 Searching for Terra (affects Narshe, Figaro Castle, South Figaro)
049 89:1 Enables the optional scene with Edgar and Sabin in Figaro Castle
04A 89:2 Saw the optional scene with Edgar and Sabin in Figaro Castle
04B 89:3 Unused? -> FF6WC set when all other blitzes learned or bum rush last disabled
04C 89:4 Saw the scene with Sabin and Duncan's wife
04D 89:5 Saw Locke's flashback inside Rachel's house
04E 89:6 Unused?
04F 89:7 Saw the flashback of Rachel in the doctor's basement
050 8A:0 Unused? FF6WC -> GOT_SERPENT_TRENCH_REWARD
051 8A:1 Unused? FF6WC -> SET_ZOZO_CLOCK
052 8A:2 Unused? FF6WC -> GOT_ZOZO_REWARD
053 8A:3 Met Ramuh
054 8A:4 Formed a party in Zozo (affects Narshe and Jidoor)
055 8A:5 Watched the overture
056 8A:6 Celes is ready to go on stage
057 8A:7 Theater map variation featuring the wedding waltz
058 8B:0 Discovered Ultros's note
059 8B:1 Theater map reconfiguration 1
05A 8B:2 Theater map reconfiguration 2
05B 8B:3 Unused?
05C 8B:4 Setzer imprisoned Celes (needlessly affects the party change room)
05D 8B:5 Celes tossed Edgar's coin (affects Setzer, Kohlingen, Narshe)
05E 8B:6 Landed the airship near Albrook (affects the airship's exit door)
05F 8B:7 Kefka disposed of Ifrit and Shiva
060 8C:0 Fought Ifrit and Shiva
061 8C:1 Unused?
062 8C:2 Puts the metal platform on the right in Kefka's Tower
063 8C:3 Removes a barrier in Kefka's Tower 1
064 8C:4 Removes a barrier in Kefka's Tower 2
065 8C:5 Erects a barrier in Kefka's Tower 1
066 8C:6 Erects a barrier in Kefka's Tower 2
067 8C:7 Forms a passageway leading to Guardian in Kefka's Tower
068 8D:0 Threw the switch in the Magitek Research Facility
069 8D:1 Rode the mine cart (affects Vector, Albrook, and the Magitek Factory)
06A 8D:2 Setzer joined the party (affects the party change room of the airship)
06B 8D:3 Defeated the Cranes (affects Vector, Narshe, and the Auction House)
06C 8D:4 One day later in Esperville (brightens the outdoors map)
06D 8D:5 Unused?
06E 8D:6 Two days later in Esperville
06F 8D:7 Two years later in Esperville (darkens the outdoors map)
070 8E:0 Saw Maduin die (affects the airship's party change room and exit door)
071 8E:1 Forms a passageway leading to the balcony in Kefka's Tower
072 8E:2 Defeated Doom
073 8E:3 Defeated Goddess
074 8E:4 Defeated Poltrgeist
075 8E:5 Unused?
076 8E:6 Next stop, the sealed gate
077 8E:7 Affects the airship's exit door (always remains clear?)
078 8F:0 Unused?
079 8F:1 The Espers broke through the sealed gate (affects various locations)
07A 8F:2 The Espers attacked the Blackjack
07B 8F:3 The Espers attacked the Empire
07C 8F:4 Dinner preparations are underway
07D 8F:5 Dinner is over (affects various locations)
07E 8F:6 Recruited Umaro
07F 8F:7 Clears the rockslide in Kefka's Tower
080 90:0 Opens the gate in Kefka's Tower
081 90:1 Saw the scene with Cid and Setzer in the Blackjack
082 90:2 (Set at the same time as the previous bit. Seems useless.)
083 90:3 Boarded the ship in Albrook
084 90:4 (Set at the same time as the next bit. Seems useless.)
085 90:5 Met Leo and the others in Albrook
086 90:6 Saw the scene with Terra and Leo at night on the ship to Thamasa
087 90:7 Saw the scene with Locke and Celes at night in Albrook
088 91:0 Unused? -> FF6WC UNLOCKED_WOR
089 91:1 Received Leo's instructions before arriving at Crescent Island
08A 91:2 Unused? -> FF6WC UNLOCKED_WOB
08B 91:3 Saw the scene at Thamasa involving the child casting Fire
08C 91:4 Saw the scene at Thamasa involving the child needing Cure
08D 91:5 Named Strago and Relm
08E 91:6 Strago woke the party at night in Thamasa
08F 91:7 Saw the initial scene in the burning house (useless?)
090 92:0 Defeated FlameEater
091 92:1 Next stop, Gathering Place of the Espers
092 92:2 Shadow decided to search for the Espers in his own way
093 92:3 Unused? -> FF6WC UNLOCKED_KT_SKIP
094 92:4 Unused? -> FF6WC UNLOCKED_FINAL_KEFKA
095 92:5 Fought Ultros at Gathering Place of the Espers
096 92:6 (Set at the same time as the next bit. Seems useless.)
097 92:7 Noticed the Statues at Gathering Place of the Espers
098 93:0 Gathering Place of the Espers is accessible from the overworld map
099 93:1 Found the Espers at Gathering Place of the Espers
09A 93:2 Shadow's theme plays in Albrook (set for when naming Shadow)
09B 93:3 Fought Kefka at Thamasa (affects Albrook and, needlessly, Thamasa)
09C 93:4 Leo is buried in Thamasa; disables the scene with the imprisoned Kefka
09D 93:5 Completed the mandatory Thamasa scenario (affects various locations)
09E 93:6 The Floating Continent exists (affects overworld, Blackjack, Albrook)
09F 93:7 Disables access to the Floating Continent (always remains clear?)
0A0 94:0 Disables the IAF sequence
0A1 94:1 Unused?
0A2 94:2 Unused?
0A3 94:3 Left Shadow behind on the Floating Continent
0A4 94:4 In the World of Ruin
0A5 94:5 Unused?
0A6 94:6 Hides Party Character 0 on map 10 (always remains clear?)
0A7 94:7 Met Crimson Robber 1
0A8 95:0 Met Crimson Robber 2
0A9 95:1 Met Crimson Robber 3
0AA 95:2 Met Crimson Robber 4
0AB 95:3 Saw one of the Crimson Robbers leave the Cafe
0AC 95:4 Boarded the Crimson Robbers' ship
0AD 95:5 Disables a music-related function in Figaro Cave
0AE 95:6 Noise in Figaro Cave 1
0AF 95:7 Noise in Figaro Cave 2
0B0 96:0 Noise in Figaro Cave 3
0B1 96:1 Drank from the spring in Figaro Cave
0B2 96:2 Examined Cid's dead body
0B3 96:3 Cid recovered (enables access to the cliffs)
0B4 96:4 Cid succumbed (enables access to the cliffs)
0B5 96:5 Unused?
0B6 96:6 Got Ragnarok
0B7 96:7 Unused?
0B8 97:0 Got Cursed Shld
0B9 97:1 Unused?
0BA 97:2 Recruited Strago in the World of Ruin
0BB 97:3 Unused?
0BC 97:4 Defeated Guardian
0BD 97:5 Defeated Inferno
0BE 97:6 Terra and Katarin went missing
0BF 97:7 Recruited Terra in the World of Ruin
0C0 98:0 Unused?
0C1 98:1 Unused?
0C2 98:2 Memorized "DLRO"
0C3 98:3 Memorized "ERAU"
0C4 98:4 Memorized "QSSI"
0C5 98:5 Memorized "WEHT"
0C6 98:6 Recruited Edgar in the World of Ruin
0C7 98:7 Saw Figaro Castle rise to the surface following the Tentacles battle
0C8 99:0 Got Odin
0C9 99:1 Unused?
0CA 99:2 Recruited Setzer in the World of Ruin
0CB 99:3 Uncovered the entrance to Darill's Tomb
0CC 99:4 Saw the flashback scene in Darill's Tomb
0CD 99:5 Acquired the Falcon (affects Mobliz and Figaro Castle)
0CE 99:6 Unused?
0CF 99:7 Unused?
0D0 9A:0 Generates two doorways in Kefka's Tower
0D1 9A:1 Unused?
0D2 9A:2 Recruited Cyan in the World of Ruin
0D3 9A:3 Unused?
0D4 9A:4 Recruited Gogo (useless?)
0D5 9A:5 Unused?
0D6 9A:6 Unused?
0D7 9A:7 Recruited Locke in the World of Ruin
0D8 9B:0 Unused?
0D9 9B:1 (Set upon acquiring the Starlet Magicite. Seems useless.)
0DA 9B:2 Cleansed Cyan's soul
0DB 9B:3 Unused?
0DC 9B:4 Figaro Castle lies in the western desert in the World of Ruin
0DD 9B:5 Unused?
0DE 9B:6 Sets Figaro Castle ablaze
0DF 9B:7 Unused?
0E0 9C:0 Unused?
0E1 9C:1 Unused?
0E2 9C:2 Unused?
0E3 9C:3 Unused?
0E4 9C:4 Unused?
0E5 9C:5 Unused?
0E6 9C:6 Unused?
0E7 9C:7 Unused?
0E8 9D:0 Unused?
0E9 9D:1 Unused?
0EA 9D:2 Unused?
0EB 9D:3 Unused?
0EC 9D:4 Unused?
0ED 9D:5 Unused?
0EE 9D:6 Unused?
0EF 9D:7 Unused?
0F0 9E:0 Unused?
0F1 9E:1 Unused?
0F2 9E:2 Unused?
0F3 9E:3 Unused?
0F4 9E:4 Unused?
0F5 9E:5 Unused?
0F6 9E:6 Unused?
0F7 9E:7 Unused?
0F8 9F:0 Unused?
0F9 9F:1 Unused?
0FA 9F:2 Unused?
0FB 9F:3 Unused?
0FC 9F:4 Unused?
0FD 9F:5 Unused?
0FE 9F:6 Unused?
0FF 9F:7 Unused?
100 A0:0 Edgar commented on Sabin's Cabin
101 A0:1 The cider deliveryman is heading toward the old man's house
102 A0:2 The cider deliveryman is heading toward the Cafe
103 A0:3 Locke is dressed as an officer
104 A0:4 Locke is dressed as a merchant
105 A0:5 The Empire invaded South Figaro
106 A0:6 Figaro Castle lies in the eastern desert in the World of Ruin
107 A0:7 Delivered cider to the old man
108 A1:0 Can command the guard blocking the entrance to Figaro Cave to leave
109 A1:1 Unused?
10A A1:2 Vargas made his appearance
10B A1:3 Figaro Castle lies in the eastern desert in the World of Balance
10C A1:4 Figaro Castle lies in the western desert in the World of Balance
10D A1:5 Wound the clock
10E A1:6 Named Setzer (useless?)
10F A1:7 Unused?
110 A2:0 Ultros threatened to disrupt the opera
111 A2:1 Celes performed admirably
112 A2:2 Correctly assembled the message in Darill's Tomb
113 A2:3 Ejected from the Opera House 1
114 A2:4 Ejected from the Opera House 2
115 A2:5 Ejected from the Opera House 3
116 A2:6 The elder of Esperville unveiled his audacious plan
117 A2:7 Madonna took Terra to the gate
118 A3:0 A wind blew the soldiers and Gestahl through the gate
119 A3:1 Shadow left during the overture
11A A3:2 Unused?
11B A3:3 Unused?
11C A3:4 Unused?
11D A3:5 Unused?
11E A3:6 Unused?
11F A3:7 Unused?
120 A4:0 Unused?
121 A4:1 Unused?
122 A4:2 Unused?
123 A4:3 Can jump on the turtle in Figaro Cave
124 A4:4 Serves to determine the number of characters in the active party 1
125 A4:5 Serves to determine the number of characters in the active party 2
126 A4:6 Serves to determine the number of characters in the active party 3
127 A4:7 Serves to ensure that branching always occurs 1 (always remains clear)
128 A5:0 Introductory battle 1
129 A5:1 Introductory battle 2
12A A5:2 Introductory battle 3
12B A5:3 Wedge commented on the mines
12C A5:4 Vicks destroyed the gate
12D A5:5 The Narshe guards spotted Terra on the bridge
12E A5:6 Terra fell through a hole in the mines
12F A5:7 Enables action queues for NPCs in the Moogle tripartite battle area
130 A6:0 Introductory battle 4
131 A6:1 Introductory battle 5
132 A6:2 Initiated the tripartite battle with Kefka
133 A6:3 Disables the Save Point tutorial
134 A6:4 Disables the Chocobo tutorial
135 A6:5 Defeated Whelk
136 A6:6 Fought Guard x2 at Vector
137 A6:7 Forces a battle with Guardian at the Imperial Castle
138 A7:0 Guardian is encountered differently at the Imperial Castle
139 A7:1 Disables action queues for NPCs on the snowfield
13A A7:2 Received word that the Emperor is expecting us
13B A7:3 Saw the hooded man walk northward in the Imperial Castle 
13C A7:4 Dinner preparations have concluded
13D A7:5 Unused?
13E A7:6 Defeated green soldier 1 once on the snowfield
13F A7:7 Defeated green soldier 2 once on the snowfield
140 A8:0 Defeated green soldier 3 once on the snowfield
141 A8:1 Defeated green soldier 4 once on the snowfield
142 A8:2 Defeated green soldier 5 once on the snowfield
143 A8:3 Defeated green soldier 6 once on the snowfield
144 A8:4 Defeated brown soldier 1 once on the snowfield
145 A8:5 Defeated brown soldier 2 once on the snowfield
146 A8:6 Defeated brown soldier 3 once on the snowfield
147 A8:7 Defeated brown soldier 4 once on the snowfield
148 A9:0 Defeated brown soldier 5 once on the snowfield
149 A9:1 Unused?
14A A9:2 Unused?
14B A9:3 Unused?
14C A9:4 Unused?
14D A9:5 Unused?
14E A9:6 Unused?
14F A9:7 Talked to 1 soldier
150 AA:0 Unused?
151 AA:1 Named Cyan
152 AA:2 Unused?
153 AA:3 Unused?
154 AA:4 Unused?
155 AA:5 Fought Templar x2, Soldier x2
156 AA:6 Fought Nightshade x3
157 AA:7 Unused?
158 AB:0 Unused?
159 AB:1 Unused?
15A AB:2 Talked to Locke at the Returners' Hideout
15B AB:3 Talked to Sabin at the Returners' Hideout
15C AB:4 Talked to Edgar at the Returners' Hideout
15D AB:5 The guard said Banon went outside (can be set repeatedly; useless?)
15E AB:6 Abbreviates the exchange between Terra and Locke at Returners' Hideout
15F AB:7 Unused?
160 AC:0 Unused?
161 AC:1 Unused?
162 AC:2 Recruited Shadow during Sabin's scenario (useless?)
163 AC:3 Unused?
164 AC:4 Unused?
165 AC:5 Unused?
166 AC:6 Unused?
167 AC:7 The party walked systematically after "Uncontrollable Cyan battle 3"
168 AD:0 The party'll walk systematically after "Uncontrollable Cyan battle 3"
169 AD:1 Met the mounted merchant
16A AD:2 Left the scrap of paper on the floor
16B AD:3 Noticed the scrap of paper
16C AD:4 Bought ZoneSeek at the Auction House
16D AD:5 Bought Golem at the Auction House
16E AD:6 Threw the switch in the Cave in the Veldt
16F AD:7 Learned how to operate the airship
170 AE:0 The world map is no longer loaded automatically when using the wheel
171 AE:1 Fought M-TekArmor x2 at the Imperial camp (optional)
172 AE:2 Noticed the absence of soldiers at the Imperial base
173 AE:3 Generates a doorway in the Cave to the Sealed Gate 1
174 AE:4 Constructs the "grand stairway" in the Cave to the Sealed Gate
175 AE:5 Generates a doorway in the Cave to the Sealed Gate 2
176 AE:6 Serves to ensure that branching always occurs 2 (always remains clear)
177 AE:7 (Set during an unused event involving Owzer. Seems useless.)
178 AF:0 Met Gungho in the World of Balance (cleared eventually)
179 AF:1 Multipurpose bit (cleared manually)
17A AF:2 Removes a barrier in the Phantom Train (World of Ruin)
17B AF:3 Multipurpose bit (cleared manually)
17C AF:4 Multipurpose bit (cleared manually)
17D AF:5 Multipurpose bit (cleared manually)
17E AF:6 Multipurpose bit (cleared manually)
17F AF:7 Removes a barrier in the Phantom Train (World of Balance)
180 B0:0 Multipurpose bit (cleared manually)
181 B0:1 The first warp point in Ebot's Rock pseudo-randomly selects a location
182 B0:2 Introduced the idea of detaching the rear train cars
183 B0:3 Detached the rear train cars
184 B0:4 Multipurpose bit (cleared manually)
185 B0:5 Multipurpose bit (cleared manually)
186 B0:6 Multipurpose bit (cleared manually)
187 B0:7 Multipurpose bit (cleared manually)
188 B1:0 Disables the scene with Siegfried in the Phantom Train (never set)
189 B1:1 Confronted Dream Stooge 1
18A B1:2 The Empire invaded Thamasa (cleared eventually)
18B B1:3 Confronted Dream Stooge 2
18C B1:4 Extends two walkways in Gogo's lair
18D B1:5 Returns Shadow to the party after leaving the train station
18E B1:6 Shadow can no longer be found in Kohlingen
18F B1:7 Unused? (Cleared at the beginning of the World of Ruin.)
190 B2:0 The house in Thamasa is burning (cleared eventually)
191 B2:1 (Set and subsequently cleared in Cyan's soul. Seems useless.)
192 B2:2 Drank from the spring in Phantom Forest
193 B2:3 Saw the flashback scene in Cyan's soul 1
194 B2:4 Saw the flashback scene in Cyan's soul 2
195 B2:5 Met Interceptor in the Cave in the Veldt
196 B2:6 Leaving Thamasa allows Shadow or Relm to recover from their wounds
197 B2:7 Saw Cyan escape from a ghost in Cyan's soul
198 B3:0 Saw the flashback scene in Cyan's soul 3
199 B3:1 Fought SrBehemot x2
19A B3:2 Next stop, Ebot's Rock (reconfigures the overworld map)
19B B3:3 Met the talking treasure chest
19C B3:4 Defeated Hidon
19D B3:5 Sabin ordered food on the Phantom Train
19E B3:6 Either Shadow or Relm has partially recovered from their wounds
19F B3:7 Either Shadow or Relm has recovered fully from their wounds
1A0 B4:0 Multipurpose, Terra-related bit; CaseWord bit 0
1A1 B4:1 Multipurpose, Locke-related bit; CaseWord bit 1
1A2 B4:2 Multipurpose, Cyan-related bit; CaseWord bit 2
1A3 B4:3 Multipurpose, Shadow-related bit; CaseWord bit 3
1A4 B4:4 Multipurpose, Edgar-related bit
1A5 B4:5 Multipurpose, Sabin-related bit
1A6 B4:6 Multipurpose, Celes-related bit
1A7 B4:7 Multipurpose, Strago-related bit
1A8 B5:0 Multipurpose, Relm-related bit
1A9 B5:1 Multipurpose, Setzer-related bit
1AA B5:2 Multipurpose, Mog-related bit
1AB B5:3 Multipurpose, Gau-related bit
1AC B5:4 Multipurpose, Gogo-related bit
1AD B5:5 Multipurpose, Umaro-related bit
1AE B5:6 Multipurpose, Actor 14-related bit
1AF B5:7 Multipurpose, Actor 15-related bit
1B0 B6:0 Facing up
1B1 B6:1 Facing right
1B2 B6:2 Facing down
1B3 B6:3 Facing left
1B4 B6:4 Pressing the A button
1B5 B6:5 Multipurpose bit (cleared on each step)
1B6 B6:6 Maintains the state of NPCs (after a battle, for instance)
1B7 B6:7 Bear left at the fork in the Serpent Trench
1B8 B7:0 Alternate overworld music (includes WoB and Serpent Trench)
1B9 B7:1 The airship is visible
1BA B7:2 The airship is anchored
1BB B7:3 Veldt music plays on the overworld map
1BC B7:4 Unused?
1BD B7:5 Unused?
1BE B7:6 Not enough money
1BF B7:7 Enables "Save" in menu (cleared on each step)
1C0 B8:0 Unused?
1C1 B8:1 Disables dashing
1C2 B8:2 Disables menu access (cleared on Tent use)
1C3 B8:3 Unused?
1C4 B8:4 Unused?
1C5 B8:5 Unused?
1C6 B8:6 Required to properly display portraits after command $E7 is executed
1C7 B8:7 Unused?
1C8 B9:0 Unused?
1C9 B9:1 Unused?
1CA B9:2 (This bit is manipulated in various situations. It seems useless.)
1CB B9:3 Relm's theme plays in Thamasa (set for when naming Relm)
1CC B9:4 Temporary song override (maps only)
1CD B9:5 Disables random encounters (cleared on Warp use)
1CE B9:6 Enables party switching with the Y button
1CF B9:7 Disables certain buttons and affects map display in multiparty areas
1D0 BA:0 Rare item: Cider
1D1 BA:1 Rare item: Old Clock-Key
1D2 BA:2 Rare item: Fish ("A yummy fish")
1D3 BA:3 Rare item: Fish ("Just a fish")
1D4 BA:4 Rare item: Fish ("A rotten fish")
1D5 BA:5 Rare item: Fish ("Fish")
1D6 BA:6 Rare item: Lump of Metal
1D7 BA:7 Rare item: Lola's Letter
1D8 BB:0 Rare item: Coral
1D9 BB:1 Rare item: Books
1DA BB:2 Rare item: Royal Letter
1DB BB:3 Rare item: Rust-Rid
1DC BB:4 Rare item: Autograph (unused)
1DD BB:5 Rare item: Manicure (unused)
1DE BB:6 Rare item: Opera Record (unused)
1DF BB:7 Rare item: Magn.Glass (unused)
1E0 BC:0 Rare item: Eerie Stone (unused)
1E1 BC:1 Rare item: Odd Picture (unused)
1E2 BC:2 Rare item: Dull Picture (unused)
1E3 BC:3 Rare item: Pendant
1E4 BC:4 Rare item: (None)
1E5 BC:5 Rare item: (None)
1E6 BC:6 Rare item: (None)
1E7 BC:7 Rare item: (None)
1E8 BD:0 Unused, as the SNES version features 20 rare item slots rather than 30
1E9 BD:1 Unused, as the SNES version features 20 rare item slots rather than 30
1EA BD:2 Unused, as the SNES version features 20 rare item slots rather than 30
1EB BD:3 Unused, as the SNES version features 20 rare item slots rather than 30
1EC BD:4 Unused, as the SNES version features 20 rare item slots rather than 30
1ED BD:5 Unused, as the SNES version features 20 rare item slots rather than 30
1EE BD:6 Selected an item to bet at the Colosseum
1EF BD:7 Shadow has gone to the Colosseum (cleared upon recruiting Shadow)
1F0 BE:0 Multipurpose bit (cleared on map load)
1F1 BE:1 Multipurpose bit (cleared on map load)
1F2 BE:2 Multipurpose bit (cleared on map load)
1F3 BE:3 Multipurpose bit (cleared on map load)
1F4 BE:4 Multipurpose bit (cleared on map load)
1F5 BE:5 Multipurpose bit (cleared on map load)
1F6 BE:6 Multipurpose bit (cleared on map load)
1F7 BE:7 Multipurpose bit (cleared on map load)
1F8 BF:0 Multipurpose bit (cleared on map load)
1F9 BF:1 Multipurpose bit (cleared on map load)
1FA BF:2 Multipurpose bit (cleared on map load)
1FB BF:3 Multipurpose bit (cleared on map load)
1FC BF:4 Multipurpose bit (cleared on map load)
1FD BF:5 Multipurpose bit (cleared on map load)
1FE BF:6 Multipurpose bit (cleared on map load)
1FF BF:7 Multipurpose bit (cleared on map load)
200 C0:0 Talked to 2 soldiers
201 C0:1 Talked to 3 soldiers
202 C0:2 Talked to 4 soldiers
203 C0:3 Talked to 5 soldiers
204 C0:4 Talked to 6 soldiers
205 C0:5 Talked to 7 soldiers
206 C0:6 Talked to 8 soldiers
207 C0:7 Talked to 9 soldiers
208 C1:0 Talked to 10 soldiers
209 C1:1 Talked to 11 soldiers
20A C1:2 Talked to 12 soldiers
20B C1:3 Talked to 13 soldiers
20C C1:4 Talked to 14 soldiers
20D C1:5 Talked to 15 soldiers
20E C1:6 Talked to 16 soldiers
20F C1:7 Talked to 17 soldiers
210 C2:0 Talked to 18 soldiers
211 C2:1 Talked to 19 soldiers
212 C2:2 Talked to 20 soldiers
213 C2:3 Talked to 21 soldiers
214 C2:4 Talked to 22 soldiers
215 C2:5 Talked to 23 soldiers
216 C2:6 Talked to 24 soldiers
217 C2:7 Talked to soldier 1
218 C3:0 Talked to soldier 2
219 C3:1 Talked to soldier 3
21A C3:2 Talked to soldier 4
21B C3:3 Talked to soldier 5
21C C3:4 Talked to soldier 6
21D C3:5 Talked to soldier 7
21E C3:6 Talked to soldier 8
21F C3:7 Talked to soldier 9
220 C4:0 Talked to soldier 10
221 C4:1 Talked to soldier 11
222 C4:2 Talked to soldier 12
223 C4:3 Talked to soldier 13
224 C4:4 Talked to soldier 14
225 C4:5 Talked to soldier 15
226 C4:6 Talked to soldier 16
227 C4:7 Talked to soldier 17
228 C5:0 Talked to soldier 18
229 C5:1 Talked to soldier 19
22A C5:2 Talked to soldier 20
22B C5:3 Talked to soldier 21
22C C5:4 Talked to soldier 22
22D C5:5 Talked to soldier 23
22E C5:6 Talked to soldier 24
22F C5:7 Serves to ensure that branching always occurs 3 (always remains clear)
230 C6:0 Gestahl was asked one of three possible questions (pointless?)
231 C6:1 Gestahl was asked the first question initially
232 C6:2 Gestahl was asked the second question initially
233 C6:3 Gestahl was asked the third question initially
234 C6:4 Gestahl was asked the first question
235 C6:5 Gestahl was asked the second question
236 C6:6 Gestahl was asked the third question
237 C6:7 Fought Sp Forces x3
238 C7:0 Received rewards from Gestahl
239 C7:1 Chasing Lone Wolf 1
23A C7:2 Chasing Lone Wolf 2
23B C7:3 Chasing Lone Wolf 3
23C C7:4 Chasing Lone Wolf 4
23D C7:5 Chasing Lone Wolf 5
23E C7:6 Chasing Lone Wolf 6
23F C7:7 Chasing Lone Wolf 7
240 C8:0 Recruited Relm in the World of Ruin
241 C8:1 Unused?
242 C8:2 Saw the scene at the Imperial base leading to the airship crash
243 C8:3 Can climb the stairs to the art gallery without being pushed back
244 C8:4 Unused?
245 C8:5 (Set for when Gau meets his father. Its usefulness is questionable.)
246 C8:6 Trapped inside a flying airship (affects the Blackjack only)
247 C8:7 Gau met his father
248 C9:0 Unused?
249 C9:1 (Set after Gau meets his father. Seems useless.)
24A C9:2 Can read Owzer's diary
24B C9:3 Sabin introduced the idea that the aged man might be Gau's father
24C C9:4 Brightens Owzer's basement
24D C9:5 Unearthed Inviz Edge in the Cave to the Sealed Gate
24E C9:6 Unearthed Water Edge in the Cave to the Sealed Gate
24F C9:7 Unearthed Soft in the Cave to the Sealed Gate
250 CA:0 Unearthed 293 GP in the Cave to the Sealed Gate
251 CA:1 Turned the lights on in Owzer's house
252 CA:2 Fought Dahling x2
253 CA:3 Fought Chadarnook x2
254 CA:4 Fought Still Life
255 CA:5 Bought Hero Ring at the Auction House
256 CA:6 Asked Gau's father about Gestahl's map
257 CA:7 Boarded the raft but not for the first time
258 CB:0 Fought the monsters in the chair painting
259 CB:1 Floating chest 1
25A CB:2 Floating chest 2
25B CB:3 Floating chest 3
25C CB:4 Floating chest 4
25D CB:5 Bought Zephyr Cape at the Auction House
25E CB:6 Returners plays in the Returners' Hideout; features in unused code
25F CB:7 Relm has gone to Owzer's house, which is haunted (cleared eventually)
260 CC:0 Unused? (Terra...)
261 CC:1 Unused? (Locke...)
262 CC:2 Puts Cyan in a seat once Ultros is noticed on the girders (never set)
263 CC:3 Unused? (Shadow...)
264 CC:4 Puts Edgar in a seat once Ultros is noticed on the girders (never set)
265 CC:5 Puts Sabin in a seat once Ultros is noticed on the girders (never set)
266 CC:6 Celes was already in the party on the Floating Continent
267 CC:7 Unused? (Strago...)
268 CD:0 Unused? (Relm...)
269 CD:1 Unused? (Setzer...)
26A CD:2 Unused? (Mog...)
26B CD:3 Puts Gau in a seat once Ultros is noticed on the girders (never set)
26C CD:4 Unused? (Umaro...)
26D CD:5 Unused? (Gogo...)
26E CD:6 Saw the scene with Gerad and the injured soldier
26F CD:7 Figaro Castle bumped into something, says the engineer
270 CE:0 Can grab the hook from the left side in the Magitek Factory
271 CE:1 Can grab the hook from the right side in the Magitek Factory
272 CE:2 Talked to Ifrit
273 CE:3 Disables the hook in the room with Ifrit and Shiva
274 CE:4 Talked to Shiva
275 CE:5 Unused?
276 CE:6 Imperial troops have withdrawn from South Figaro
277 CE:7 Imperial troops have withdrawn from Doma (useless?)
278 CF:0 Earned the right to take weapons from the Imperial base (useless?)
279 CF:1 (Set by stepping on a certain tile in Umaro's cave. Seems useless.)
27A CF:2 Defeated Umaro
27B CF:3 Johnny C. Bad plays in the Cafe and Relic shop in Albrook
27C CF:4 Got Sraphim
27D CF:5 Kefka unleashed his Light of Judgment on Tzen
27E CF:6 Another letter has arrived
27F CF:7 Read Lola's letter 1
280 D0:0 Read Lola's letter 2
281 D0:1 Read Lola's letter 3
282 D0:2 Read Lola's letter 4
283 D0:3 Read Lola's letter 5
284 D0:4 Posted letter 1
285 D0:5 Posted record
286 D0:6 Posted Tonic
287 D0:7 Posted letter 2
288 D1:0 Posted book
289 D1:1 Met the injured lad
28A D1:2 Recruited Sabin in the World of Ruin
28B D1:3 Picked up the child
28C D1:4 Met Sabin in Tzen
28D D1:5 Got Tintinabar from the injured lad
28E D1:6 Saw the scene with the barking dogs in Mobliz
28F D1:7 Met Terra in Mobliz
290 D2:0 Saw the scene in which Terra says she has lost her will to fight
291 D2:1 Fought Phunbaba the first time
292 D2:2 Saw the scene with Terra, Duane, and Katarin in the secret room
293 D2:3 Saw the dog go behind the bookshelf
294 D2:4 Met Lola in the World of Ruin
295 D2:5 Noticed the handwriting looks a lot like Cyan's
296 D2:6 Consented to attach Lola's reply to a carrier pigeon
297 D2:7 Found the key to Cyan's treasure chest
298 D3:0 Attached Lola's reply to a carrier pigeon
299 D3:1 Released Storm Drgn
29A D3:2 Defeated Storm Drgn
29B D3:3 Met Lone Wolf in the World of Ruin
29C D3:4 Cyan and Lola met each other
29D D3:5 Cyan exchanged the letters
29E D3:6 Got Tritoch
29F D3:7 Recruited Mog in the World of Balance
2A0 D4:0 (Set repeatedly in Narshe in the World of Ruin. Seems useless.)
2A1 D4:1 Unused?
2A2 D4:2 Party 1 is standing on a switch in Phoenix Cave 1
2A3 D4:3 Party 1 is standing on a switch in Phoenix Cave 2
2A4 D4:4 Spikes have been temporarily lowered 1
2A5 D4:5 Extends a bridge in Phoenix Cave
2A6 D4:6 Party 2 is standing on a switch in Phoenix Cave 1
2A7 D4:7 Party 2 is standing on a switch in Phoenix Cave 2
2A8 D5:0 Lays stepping stones over the lava in Phoenix Cave
2A9 D5:1 Spikes have been temporarily lowered 2
2AA D5:2 Puts the platform on the left in Phoenix Cave
2AB D5:3 Prevents resetting timers on Game Over 1 (always remains clear?)
2AC D5:4 Prevents resetting timers on Game Over 2 (always remains clear?)
2AD D5:5 Prevents resetting timers on Game Over 3 (always remains clear?)
2AE D5:6 Prevents resetting timers on Game Over 4 (always remains clear?)
2AF D5:7 Learned Bum Rush from Duncan
2B0 D6:0 (Set repeatedly in Nikeah in the World of Ruin. Seems useless.)
2B1 D6:1 Generates a doorway in Darill's Tomb 1
2B2 D6:2 Defeated Dullahan
2B3 D6:3 Raises the water level in Darill's Tomb 1
2B4 D6:4 Relocates a turtle in Darill's Tomb 1 (cleared on Warp use)
2B5 D6:5 Raises the water level in Darill's Tomb 2
2B6 D6:6 Relocates a turtle in Darill's Tomb 2 (cleared on Warp use)
2B7 D6:7 The prison door is open
2B8 D7:0 Generates a doorway in Darill's Tomb 2
2B9 D7:1 Figaro Castle continues its journey by travelling toward Kohlingen
2BA D7:2 Saw the duel scene of the opera
2BB D7:3 Bet Striker to fight Shadow (cleared with any other match-up)
2BC D7:4 Temporary song override (battles only)
2BD D7:5 Hides Party Character 0 on map 3 (set for rise of Floating Continent)
2BE D7:6 Warp handler for Kefka's Tower
2BF D7:7 Warp handler for Phoenix Cave (useless; Dragon's Den in GBA version)
2C0 D8:0 Cinematic effect
2C1 D8:1 Unused?
2C2 D8:2 Unused?
2C3 D8:3 Unused?
2C4 D8:4 Multipurpose bit (cleared on each step taken by party 1)
2C5 D8:5 Multipurpose bit (cleared on each step taken by party 1)
2C6 D8:6 Multipurpose bit (cleared on each step taken by party 1)
2C7 D8:7 Multipurpose bit (cleared on each step taken by party 1)
2C8 D9:0 Multipurpose bit (cleared on each step taken by party 2)
2C9 D9:1 Multipurpose bit (cleared on each step taken by party 2)
2CA D9:2 Multipurpose bit (cleared on each step taken by party 2)
2CB D9:3 Multipurpose bit (cleared on each step taken by party 2)
2CC D9:4 Multipurpose bit (cleared on each step taken by party 3)
2CD D9:5 Multipurpose bit (cleared on each step taken by party 3)
2CE D9:6 Multipurpose bit (cleared on each step taken by party 3)
2CF D9:7 Multipurpose bit (cleared on each step taken by party 3)
2D0 DA:0 Drained the water in Phoenix Cave
2D1 DA:1 Spikes have been temporarily lowered 3
2D2 DA:2 Party 1 has temporarily rearranged stones in Phoenix Cave
2D3 DA:3 Party 2 has temporarily rearranged stones in Phoenix Cave
2D4 DA:4 Party 1 has temporarily created stepping stones in Phoenix Cave
2D5 DA:5 Party 2 has temporarily created stepping stones in Phoenix Cave
2D6 DA:6 Lowers a platform in Phoenix Cave
2D7 DA:7 Got Fenrir
2D8 DB:0 Saw the scene about the security checkpoint in Narshe
2D9 DB:1 No music in Rachel's house
2DA DB:2 Stepped on the tile in front of the Gem Box chest
2DB DB:3 Defeated MagiMaster
2DC DB:4 Pressed the switch in the Fanatics' Tower
2DD DB:5 Got Raiden
2DE DB:6 Pressed the switch in the Ancient Castle
2DF DB:7 Saw the flashback scene in the Ancient Castle
2E0 DC:0 Terra is covered by the shop and item menus and Gogo's Status screen
2E1 DC:1 Locke is covered by the shop and item menus and Gogo's Status screen
2E2 DC:2 Cyan is covered by the shop and item menus and Gogo's Status screen
2E3 DC:3 Shadow is covered by the shop and item menus and Gogo's Status screen
2E4 DC:4 Edgar is covered by the shop and item menus and Gogo's Status screen
2E5 DC:5 Sabin is covered by the shop and item menus and Gogo's Status screen
2E6 DC:6 Celes is covered by the shop and item menus and Gogo's Status screen
2E7 DC:7 Strago is covered by the shop and item menus and Gogo's Status screen
2E8 DD:0 Relm is covered by the shop and item menus and Gogo's Status screen
2E9 DD:1 Setzer is covered by the shop and item menus and Gogo's Status screen
2EA DD:2 Mog is covered by the shop and item menus and Gogo's Status screen
2EB DD:3 Gau is covered by the shop and item menus and Gogo's Status screen
2EC DD:4 Gogo is covered by the shop and item menus and Gogo's Status screen
2ED DD:5 Umaro is covered by the shop and item menus and Gogo's Status screen
2EE DD:6 Actor 14's covered by the shop and item menus and Gogo's Status screen
2EF DD:7 Actor 15's covered by the shop and item menus and Gogo's Status screen
2F0 DE:0 Terra is available
2F1 DE:1 Locke is available
2F2 DE:2 Cyan is available
2F3 DE:3 Shadow is available
2F4 DE:4 Edgar is available
2F5 DE:5 Sabin is available
2F6 DE:6 Celes is available
2F7 DE:7 Strago is available
2F8 DF:0 Relm is available
2F9 DF:1 Setzer is available
2FA DF:2 Mog is available
2FB DF:3 Gau is available
2FC DF:4 Gogo is available
2FD DF:5 Umaro is available
2FE DF:6 The game proceeds normally after the opening credits
2FF DF:7 A save file was detected in the battery
'''