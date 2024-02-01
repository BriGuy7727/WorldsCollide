from event.event import *
from data.npc import NPC
from music.song_utils import get_character_theme

class DebugRoom(Event):
    # Using the 3 Scenarios room as our debug map
    DEBUG_ROOM = 0x9
    #DEBUG_ROOM2 = 0xd9
    DEBUG_ROOM2 = 0xfc
    BLACKJACK_INTERIOR_MAP = 0x07

    def name(self):
        return "Debug Room"
    
    def init_event_bits(self, space):
        pass

    def remove_npcs_mod(self):
        # Remove all existing NPCs in debug rooms
        while(self.maps.get_npc_count(self.DEBUG_ROOM) > 0):
            self.maps.remove_npc(self.DEBUG_ROOM, 0)

        while(self.maps.get_npc_count(self.DEBUG_ROOM2) > 0):
            self.maps.remove_npc(self.DEBUG_ROOM2, 0)
        
        # If Kefka Practice, don't need NPCs anywhere except the ones we add and Airship one
        if self.args.kprac:
            BLACKJACK_INTERIOR_MAP = 0x07
            STRAGO_HOUSE_MAP = 0x15d
            while(self.maps.get_npc_count(0xd9) > 0):
                self.maps.remove_npc(0xd9, 0)
            #MAP_MAX = 413
            #for map in range(BLACKJACK_INTERIOR_MAP+1,MAP_MAX):
            #    if map != STRAGO_HOUSE_MAP:
            #        while(self.maps.get_npc_count(int(hex(map),16)) > 0):
            #            self.maps.remove_npc(int(hex(map),16), 0)


    def _add_recruit_npc(self, character, x, y, direction):
        # Add an NPC to recruit each character
        src = [
            field.RecruitCharacter(character),
            field.PlaySoundEffect(150),
            field.StartSong(get_character_theme(character)),
            field.Return(),
        ]
        space = Write(Bank.CC, src, "Recruit NPC")

        recruit_npc = NPC()
        recruit_npc.x = x
        recruit_npc.y = y
        recruit_npc.direction = direction
        recruit_npc.sprite = self.characters.get_sprite(character)
        recruit_npc.palette = self.characters.get_palette(character)
        recruit_npc.set_event_address(space.start_address)
        self.maps.append_npc(self.DEBUG_ROOM, recruit_npc)

    def add_recruit_npcs_mod(self):
        self._add_recruit_npc(self.characters.TERRA,  1, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.LOCKE,  2, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.CYAN,   3, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.SHADOW, 4, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.EDGAR,  5, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.SABIN,  6, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.CELES,  7, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.STRAGO, 8, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.RELM,   9, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.SETZER, 10, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.MOG,    11, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.GAU,    12, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.GOGO,   13, 8, direction.DOWN)
        self._add_recruit_npc(self.characters.UMARO,  14, 8, direction.DOWN)
    
    def add_boss_npcs_mod(self):
        # Add an NPC to fight each boss cluster
        from data.bosses import name_pack
        from data.bosses import normal_pack_name
        from instruction.field.instructions import BattleType
        import random
        boss_packs = list(normal_pack_name)     # gives a list of all keys (formation #s)
        fight_bosses = {}

        # populate the fight_bosses dictionary with a boss formation + code starting address for dialogue box later
        for boss in boss_packs:
            src = []
            # pick random background
            battle_bg = random.randint(0,55)
            # if 37 -> WOB Airship (party all in center) OR a background that doesn't look right (Kefka Climb or Phantom Train boss)
            if battle_bg > 48 or battle_bg == 37:
                # pick between Final Kefka & Tentacles
                battle_bg = random.randint(54,55)
            # battles where party is all on right side, force a FRONT fight 
            # 13 -> Lete River (party all on right)
            # 41 -> WOR Airship (party all right)
            # 44 -> Magitek Car (party all right)
            # 49 -> WOB Airship (party all right)
            if battle_bg == 13 or battle_bg == 41 or battle_bg == 44 or battle_bg == 49:
                src += [
                    field.InvokeBattleType(boss, BattleType.FRONT, battle_bg),
               ]
            # otherwise doesn't matter
            else:
                src += [
                    # invoke random boss pack, with random background
                    field.InvokeBattle(boss, battle_bg),
                ]
            src += [
                field.FadeInScreen(),
                field.WaitForFade(),
                field.Return(),
            ]
            space = Write(Bank.CC, src, "Fight {boss}")
            fight_bosses.update({boss:space.start_address})
        

        # 2987-3018
        # prep dialogue boxes for each of the NPCs then add the NPC to the map
        boss_choice_dialog1 = 2987
        self.dialogs.set_text(boss_choice_dialog1, '<choice>Marshal<line><choice>Whelk<line><choice>Kefka (Narshe)<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog1,
                            dest1 = fight_bosses.get(name_pack["Marshal"]),
                            dest2 = fight_bosses.get(name_pack["Whelk"]),
                            dest3 = fight_bosses.get(name_pack["Kefka (Narshe)"]),
                            dest4 = field.RETURN),
        )
        boss_choice1 = space.start_address
        # Narshe Guard            Marshal, Whelk, Kefka (Narshe)
        boss_npc = NPC()
        boss_npc.x = 75
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 52
        boss_npc.palette = 1
        boss_npc.set_event_address(boss_choice1)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog2 = 2988
        self.dialogs.set_text(boss_choice_dialog2, '<choice>Umaro<line><choice>Tritoch<line><choice>Ifrit/Shiva<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog2,
                            dest1 = fight_bosses.get(name_pack["Umaro"]),
                            dest2 = fight_bosses.get(name_pack["Tritoch"]),
                            dest3 = fight_bosses.get(name_pack["Ifrit/Shiva"]),
                            dest4 = field.RETURN),
        )
        boss_choice2 = space.start_address
        # Umaro                   Umaro, Tritoch, Ifrit/Shiva
        boss_npc = NPC()
        boss_npc.x = 76
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 13
        boss_npc.palette = 5
        boss_npc.set_event_address(boss_choice2)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog3 = 2989
        self.dialogs.set_text(boss_choice_dialog3, '<choice>Vargas<line><choice>Dadaluma<line><choice>TunnelArmr<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog3,
                            dest1 = fight_bosses.get(name_pack["Vargas"]),
                            dest2 = fight_bosses.get(name_pack["Dadaluma"]),
                            dest3 = fight_bosses.get(name_pack["TunnelArmr"]),
                            dest4 = field.RETURN),
        )
        boss_choice3 = space.start_address
        # Vargas/Dadaluma         Vargas, Dadaluma, TunnelArmr
        boss_npc = NPC()
        boss_npc.x = 77
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 50
        boss_npc.palette = 4
        boss_npc.set_event_address(boss_choice3)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog4 = 2990
        self.dialogs.set_text(boss_choice_dialog4, '<choice>GhostTrain<line><choice>Rizopas<line><choice>Tentacles<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog4,
                            dest1 = fight_bosses.get(name_pack["GhostTrain"]),
                            dest2 = fight_bosses.get(name_pack["Rizopas"]),
                            dest3 = fight_bosses.get(name_pack["Tentacles"]),
                            dest4 = field.RETURN),
        )
        boss_choice4 = space.start_address
        # Siegfried               GhostTrain, Rizopas, Tentacles
        boss_npc = NPC()
        boss_npc.x = 78
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 46
        boss_npc.palette = 4
        boss_npc.set_event_address(boss_choice4)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog5 = 2991
        self.dialogs.set_text(boss_choice_dialog5, '<choice>Leader<line><choice>Stooges<line><choice>Wrexsoul<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog5,
                            dest1 = fight_bosses.get(name_pack["Leader"]),
                            dest2 = fight_bosses.get(name_pack["Stooges"]),
                            dest3 = fight_bosses.get(name_pack["Wrexsoul"]),
                            dest4 = field.RETURN),
        )
        boss_choice5 = space.start_address
        # Soldier                 Leader, Stooges, WrexSoul
        boss_npc = NPC()
        boss_npc.x = 79
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 14
        boss_npc.palette = 4
        boss_npc.set_event_address(boss_choice5)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog6 = 2992
        self.dialogs.set_text(boss_choice_dialog6, '<choice>Ultros 1<line><choice>Ultros 2<line><choice>Ultros 3<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog6,
                            dest1 = fight_bosses.get(name_pack["Ultros 1"]),
                            dest2 = fight_bosses.get(name_pack["Ultros 2"]),
                            dest3 = fight_bosses.get(name_pack["Ultros 3"]),
                            dest4 = field.RETURN),
        )
        boss_choice6 = space.start_address
        # Ultros                  Ultros 1/2/3
        boss_npc = NPC()
        boss_npc.x = 80
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 31
        boss_npc.palette = 5
        boss_npc.set_event_address(boss_choice6)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog7 = 2993
        self.dialogs.set_text(boss_choice_dialog7, '<choice>Ultros/Chupon<line><choice>Hidon<line><choice>FlameEater<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog7,
                            dest1 = fight_bosses.get(name_pack["Ultros/Chupon"]),
                            dest2 = fight_bosses.get(name_pack["Hidon"]),
                            dest3 = fight_bosses.get(name_pack["FlameEater"]),
                            dest4 = field.RETURN),
        )
        boss_choice7 = space.start_address
        # Hidon/Chupon            Ultros 4, Hidon, FlameEater
        boss_npc = NPC()
        boss_npc.x = 81
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 61
        boss_npc.palette = 0
        boss_npc.set_event_address(boss_choice7)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog8 = 2994
        self.dialogs.set_text(boss_choice_dialog8, '<choice>Number 024<line><choice>Number 128<line><choice>Cranes<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog8,
                            dest1 = fight_bosses.get(name_pack["Number 024"]),
                            dest2 = fight_bosses.get(name_pack["Number 128"]),
                            dest3 = fight_bosses.get(name_pack["Cranes"]),
                            dest4 = field.RETURN),
        )
        boss_choice8 = space.start_address
        # Number 024              Number 024, Number 128, Cranes
        boss_npc = NPC()
        boss_npc.x = 82
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        #boss_npc.no_face_on_trigger = 1
        boss_npc.sprite = 83
        boss_npc.palette = 5
        #boss_npc.unknown1 = 1
        #boss_npc.unknown2 = 1
        #boss_npc.const_sprite = 1
        boss_npc.set_event_address(boss_choice8)
        number024_npc_id = self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)
        space.write(
            field.EntityAct(number024_npc_id, True,
                field_entity.AnimateStaticNPC(),
            )
        )
        boss_choice_dialog9 = 2995
        self.dialogs.set_text(boss_choice_dialog9, '<choice>SrBehemoth<line><choice>Doom Gaze<line><choice>Phunbaba 4<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog9,
                            dest1 = fight_bosses.get(name_pack["SrBehemoth"]),
                            dest2 = fight_bosses.get(name_pack["Doom Gaze"]),
                            dest3 = fight_bosses.get(name_pack["Phunbaba 4"]),
                            dest4 = field.RETURN),
        )
        boss_choice9 = space.start_address
        # Monster                 SrBehemoth, Doom Gaze, Phunbaba 4
        boss_npc = NPC()
        boss_npc.x = 83
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 51
        boss_npc.palette = 4
        boss_npc.set_event_address(boss_choice9)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog10 = 2996
        self.dialogs.set_text(boss_choice_dialog10, '<choice>MagiMaster<line><choice>Dullahan<line><choice>Chadarnook<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog10,
                            dest1 = fight_bosses.get(name_pack["MagiMaster"]),
                            dest2 = fight_bosses.get(name_pack["Dullahan"]),
                            dest3 = fight_bosses.get(name_pack["Chadarnook"]),
                            dest4 = field.RETURN),
        )
        boss_choice10 = space.start_address
        # Emperor's Servant       MagiMaster, Dullahan, Chadarnook
        boss_npc = NPC()
        boss_npc.x = 84
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 62
        boss_npc.palette = 4
        boss_npc.set_event_address(boss_choice10)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)
        
        boss_choice_dialog11 = 2997
        self.dialogs.set_text(boss_choice_dialog11, '<choice>Atma<line><choice>AtmaWeapon<line><choice>Nerapa<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog11,
                            dest1 = fight_bosses.get(name_pack["Atma"]),
                            dest2 = fight_bosses.get(name_pack["AtmaWeapon"]),
                            dest3 = fight_bosses.get(name_pack["Nerapa"]),
                            dest4 = field.RETURN),
        )
        boss_choice11 = space.start_address
        # Atma                    Atma, AtmaWeapon, Nerapa
        boss_npc = NPC()
        boss_npc.x = 85
        boss_npc.y = 21
        boss_npc.direction = direction.DOWN
        #boss_npc.no_face_on_trigger = 1
        boss_npc.sprite = 86
        boss_npc.palette = 3
        #boss_npc.unknown1 = 1
        #boss_npc.unknown2 = 1
        #boss_npc.const_sprite = 1
        boss_npc.set_event_address(boss_choice11)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)
        
        boss_choice_dialog12 = 2998
        self.dialogs.set_text(boss_choice_dialog12, '<choice>Inferno<line><choice>Guardian<line><choice>Air Force<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog12,
                            dest1 = fight_bosses.get(name_pack["Inferno"]),
                            dest2 = fight_bosses.get(name_pack["Guardian"]),
                            dest3 = fight_bosses.get(name_pack["Air Force"]),
                            dest4 = field.RETURN),
        )
        boss_choice12 = space.start_address
        # Inferno                 Inferno, Guardian, Air Force
        boss_npc = NPC()
        boss_npc.x = 74
        boss_npc.y = 19
        boss_npc.direction = direction.DOWN
        #boss_npc.no_face_on_trigger = 1
        boss_npc.sprite = 69
        boss_npc.palette = 4
        #boss_npc.unknown1 = 1
        #boss_npc.unknown2 = 1
        #boss_npc.const_sprite = 1
        boss_npc.set_event_address(boss_choice12)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)
        
        boss_choice_dialog13 = 2999
        self.dialogs.set_text(boss_choice_dialog13, '<choice>Doom<line><choice>Poltrgeist<line><choice>Goddess<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog13,
                            dest1 = fight_bosses.get(name_pack["Doom"]),
                            dest2 = fight_bosses.get(name_pack["Poltrgeist"]),
                            dest3 = fight_bosses.get(name_pack["Goddess"]),
                            dest4 = field.RETURN),
        )
        boss_choice13 = space.start_address
        # Kefka                   Doom, Poltrgeist, Goddess
        boss_npc = NPC()
        boss_npc.x = 86
        boss_npc.y = 19
        boss_npc.direction = direction.UP
        boss_npc.sprite = 87
        boss_npc.palette = 3
        boss_npc.split_sprite = 1
        boss_npc.set_event_address(boss_choice13)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        
        boss_choice_dialog14 = 2897
        self.dialogs.set_text(boss_choice_dialog14, '<choice>Red Dragon<line><choice>Ice Dragon<line><choice>Gold Drgn<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog14,
                            dest1 = fight_bosses.get(name_pack["Red Dragon"]),
                            dest2 = fight_bosses.get(name_pack["Ice Dragon"]),
                            dest3 = fight_bosses.get(name_pack["Gold Drgn"]),
                            dest4 = field.RETURN),
        )
        boss_choice14 = space.start_address
        # Dragon 1                Red Dragon, Ice Dragon, Gold Drgn
        boss_npc = NPC()
        boss_npc.x = 31
        boss_npc.y = 11
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 57
        boss_npc.palette = 1
        boss_npc.set_event_address(boss_choice14)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)
        '''
        boss_choice_dialog15 = 2898
        self.dialogs.set_text(boss_choice_dialog15, '<choice>White Drgn<line><choice>Blue Drgn<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 100, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog15,
                            dest1 = fight_bosses.get(name_pack["White Drgn"]),
                            dest2 = fight_bosses.get(name_pack["Blue Drgn"]),
                            dest3 = field.RETURN),
        )
        boss_choice15 = space.start_address
        # Dragon 2                White Drgn, Blue Drgn
        boss_npc = NPC()
        boss_npc.x = 32
        boss_npc.y = 17
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 57
        boss_npc.palette = 4
        boss_npc.set_event_address(boss_choice15)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)

        boss_choice_dialog16 = 2899
        self.dialogs.set_text(boss_choice_dialog16, '<choice>Storm Drgn<line><choice>Dirt Drgn<line><choice>Skull Drgn<line><choice>(cancel)<end>')
        space = Allocate(Bank.CA, 500, "Boss Selection", field.NOP())
        space.write(
            field.DialogBranch(boss_choice_dialog16,
                            dest1 = fight_bosses.get(name_pack["Storm Drgn"]),
                            dest2 = fight_bosses.get(name_pack["Dirt Drgn"]),
                            dest3 = fight_bosses.get(name_pack["Skull Drgn"]),
                            dest4 = field.RETURN),
        )
        boss_choice16 = space.start_address
        # Storm Drgn, Dirt Drgn, Skull Drgn
        boss_npc = NPC()
        boss_npc.x = 33
        boss_npc.y = 17
        boss_npc.direction = direction.DOWN
        boss_npc.sprite = 57
        boss_npc.palette = 0
        boss_npc.set_event_address(boss_choice16)
        self.maps.append_npc(self.DEBUG_ROOM2, boss_npc)  
        '''
        # add an NPC to heal party
        heal_npc = NPC()
        heal_npc.x = 81
        heal_npc.y = 25
        heal_npc.direction = direction.DOWN
        heal_npc.sprite = 15
        heal_npc.palette = 0
        src = [
            field.Call(field.HEAL_PARTY_HP_MP_STATUS),
            # play Lagomorph sound effect
            field.PlaySoundEffect(0x4f),
            field.Pause(0.25),
        ]
        space = Write(Bank.CB, src, "Heal NPC")
        heal_npc.set_event_address(space.start_address)
        self.maps.append_npc(self.DEBUG_ROOM2, heal_npc)
        # add the NPC to change party
        party_npc = NPC()
        party_npc.x = 79
        party_npc.y = 25
        party_npc.direction = direction.DOWN
        party_npc.sprite = 60
        party_npc.palette = 2
        # use the Airship party change guy
        # Need to figure out how to teleport back to this room instead of Airship...
        party_npc.set_event_address(0xc3510)
        self.maps.append_npc(self.DEBUG_ROOM2, party_npc)
        

    def _add_teleport_npc(self, source_map, source_x, source_y, direction, dest_map, dest_x, dest_y, npc_sprite, npc_palette):
        # Test code to add a Marshal battle NPC to Blackjack
        from data.bosses import name_pack
        src = [
            field.LoadMap(dest_map, direction, True, dest_x, dest_y, fade_in = True),
            field.Return(),
        ]
        space = Write(Bank.CC, src, "Teleport NPC")

        teleport_npc = NPC()
        teleport_npc.x = source_x
        teleport_npc.y = source_y
        teleport_npc.sprite = npc_sprite
        teleport_npc.palette = npc_palette
        teleport_npc.direction = direction
        teleport_npc.set_event_address(space.start_address)
        self.maps.append_npc(source_map, teleport_npc)

    def add_teleport_npcs_mod(self):
        # get to and from the debug room via WoB Airship
        BLACKJACK_EXTERIOR_MAP = 0x06
        # Leo for characters
        self._add_teleport_npc(BLACKJACK_EXTERIOR_MAP, 15, 4, direction.DOWN, self.DEBUG_ROOM, 8, 9, 16, 0)
        self._add_teleport_npc(self.DEBUG_ROOM, 8, 10, direction.UP, BLACKJACK_EXTERIOR_MAP, 15, 5, 16, 0)
        # Gehstal for bosses
        self._add_teleport_npc(BLACKJACK_EXTERIOR_MAP, 16, 4, direction.DOWN, self.DEBUG_ROOM2, 80, 23, 22, 3)
        self._add_teleport_npc(self.DEBUG_ROOM2, 80, 24, direction.UP, BLACKJACK_EXTERIOR_MAP, 16, 5, 22, 3)
        #self._add_teleport_npc(BLACKJACK_EXTERIOR_MAP, 16, 4, direction.DOWN, self.DEBUG_ROOM2, 26, 29, 22, 3)
        #self._add_teleport_npc(self.DEBUG_ROOM2, 27, 29, direction.UP, BLACKJACK_EXTERIOR_MAP, 16, 5, 22, 3)
        #self._add_teleport_npc(BLACKJACK_EXTERIOR_MAP, 16, 4, direction.DOWN, self.DEBUG_ROOM2, 28, 50, 22, 3)
        #self._add_teleport_npc(self.DEBUG_ROOM2, 29, 50, direction.UP, BLACKJACK_EXTERIOR_MAP, 16, 5, 22, 3)
    

    def mod(self):
        if self.args.debug:
            self.remove_npcs_mod()
            self.add_recruit_npcs_mod()
            self.add_boss_npcs_mod()
            self.add_teleport_npcs_mod()