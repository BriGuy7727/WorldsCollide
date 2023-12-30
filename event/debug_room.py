from event.event import *
from data.npc import NPC
from music.song_utils import get_character_theme

class DebugRoom(Event):
    # Using the 3 Scenarios room as our debug map
    DEBUG_ROOM = 0x9

    def name(self):
        return "Debug Room"
    
    def init_event_bits(self, space):
        pass

    def remove_npcs_mod(self):
        # Remove all existing NPCs
        while(self.maps.get_npc_count(self.DEBUG_ROOM) > 0):
            self.maps.remove_npc(self.DEBUG_ROOM, 0)

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

    def _add_teleport_npc(self, source_map, source_x, source_y, direction, dest_map, dest_x, dest_y):
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
        teleport_npc.sprite = 16
        teleport_npc.palette = 3
        teleport_npc.direction = direction
        teleport_npc.set_event_address(space.start_address)
        self.maps.append_npc(source_map, teleport_npc)

    def add_teleport_npcs_mod(self):
        # get to and from the debug room via WoB Airship
        BLACKJACK_EXTERIOR_MAP = 0x06
        self._add_teleport_npc(BLACKJACK_EXTERIOR_MAP, 15, 4, direction.DOWN, self.DEBUG_ROOM, 8, 9)
        self._add_teleport_npc(self.DEBUG_ROOM, 8, 10, direction.UP, BLACKJACK_EXTERIOR_MAP, 15, 5)
    
    def boss_test_mod(self):
        # Test code to add a random boss battle NPC to Blackjack
        from data.bosses import name_pack
        from data.bosses import normal_pack_name
        from instruction.field.instructions import BattleType
        import random

        '''
        boss_packs = list(normal_pack_name)
        for boss in boss_packs:
            battle_bg = random.randint(0,48)
            src = [
                # invoke the boss with random battle_bg
                field.InvokeBattle(boss, battle_bg),
                field.FadeInScreen(),
                field.WaitForFade(),
                field.Return(),
            ]
        space = Write(Bank.CC, src, "Fight {boss}")
        fight_{boss} = space.start_address
        '''
        src = []
        battle_bg = random.randint(0,55)
        battle_bg = 44
        if battle_bg > 48 or battle_bg == 37:
            battle_bg = random.randint(54,55)
        # battles where party is all on right side, force a FRONT fight
        elif battle_bg == 13 or battle_bg == 41 or battle_bg == 44 or battle_bg == 49:
            src += [
                field.InvokeBattleType(name_pack["MagiMaster"], BattleType.FRONT, battle_bg),
            ]
        else:
            src += [
                # invoke random boss pack, with random background
                field.InvokeBattle(name_pack["MagiMaster"], battle_bg),
            ]
        src += [
            field.FadeInScreen(),
            field.WaitForFade(),
            field.Return(),
        ]
        space = Write(Bank.CC, src, "Fight MagiMaster")
        fight_MagiMaster = space.start_address

        battle_bg = random.randint(0,55)
        if battle_bg > 48:
            battle_bg = random.randint(54,55)
        src = [
            # invoke random boss pack, with random background
            field.InvokeBattle(name_pack["Doom"], battle_bg),
            field.FadeInScreen(),
            field.WaitForFade(),
            field.Return(),
        ]
        space = Write(Bank.CC, src, "Fight Doom")
        fight_Doom = space.start_address

        battle_bg = random.randint(0,55)
        if battle_bg > 48:
            battle_bg = random.randint(54,55)
        src = [
            # invoke random boss pack, with random background
            field.InvokeBattle(name_pack["Goddess"], battle_bg),
            field.FadeInScreen(),
            field.WaitForFade(),
            field.Return(),
        ]
        space = Write(Bank.CC, src, "Fight Goddess")
        fight_Goddess = space.start_address

        battle_bg = random.randint(0,55)
        if battle_bg > 48:
            battle_bg = random.randint(54,55)
        src = [
            # invoke random boss pack, with random background
            field.InvokeBattle(name_pack["Poltrgeist"], battle_bg),
            field.FadeInScreen(),
            field.WaitForFade(),
            field.Return(),
        ]

        space = Write(Bank.CC, src, "Fight Poltrgeist")
        fight_Poltrgeist = space.start_address

        boss_choice_dialog = 2987
        self.dialogs.set_text(boss_choice_dialog, '<choice>MagiMaster<line><choice>Doom<line><choice>Goddess<line><choice>Poltrgeist<end>')
        '''
            324 : "GhostTrain",
            325 : "Dadaluma",
            326 : "Ifrit/Shiva",
            327 : "Cranes",
            328 : "Number 024",
            329 : "Number 128",
            335 : "FlameEater",
            336 : "AtmaWeapon",
            337 : "Nerapa",
            338 : "SrBehemoth",
            340 : "Tentacles",
            341 : "Dullahan",
            342 : "Chadarnook",
            345 : "Air Force",
            346 : "Stooges",
            348 : "Wrexsoul",
            349 : "Doom Gaze",
            350 : "Hidon",
            354 : "Doom",
            355 : "Goddess",
            356 : "Poltrgeist",
            359 : "Ultros 1",
            360 : "Ultros 2",
            363 : "Ultros/Chupon",
            368 : "Atma",
            370 : "Inferno",
            373 : "Umaro",
            375 : "Tritoch",
            381 : "Ultros 3",
            386 : "Phunbaba 3",
            387 : "Phunbaba 4",
            396 : "Guardian", # defeatable guardian in kefka's tower
            401 : "MagiMaster"
        '''
        
        space = Allocate(Bank.CA, 298, "Boss Selection", field.NOP())
        boss_choice = space.next_address
        space.write(
            field.DialogBranch(boss_choice_dialog,
                            dest1 = fight_MagiMaster,
                            dest2 = fight_Doom,
                            dest3 = fight_Goddess,
                            dest4 = fight_Poltrgeist),
        )

        test_npc = NPC()
        test_npc.x = 16
        test_npc.y = 4
        test_npc.sprite = 22
        test_npc.palette = 0
        test_npc.direction = direction.DOWN
        test_npc.speed = 0
        test_npc.set_event_address(boss_choice)
        self.maps.append_npc(0x6, test_npc)

    def mod(self):
        if self.args.debug:
            self.remove_npcs_mod()
            self.add_recruit_npcs_mod()
            self.add_teleport_npcs_mod()
            self.boss_test_mod()
