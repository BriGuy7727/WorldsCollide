from event.event import *
import random

class Start(Event):
    def name(self):
        return "Start"

    def init_rewards(self):
        party = [None] * len(self.args.start_chars)

        # assign explicit character rewards first to prevent randomly choosing them first
        # e.g. random, random, random, terra choosing terra first, second or third and making her unavailable fourth
        for index, start_char in enumerate(self.args.start_chars):
            if start_char != "random" and start_char != "randomngu":
                party[index] = self.characters.get_by_name(start_char).id
                self.characters.set_unavailable(party[index])

        gogo_umaro = [self.characters.GOGO, self.characters.UMARO]
        for index, start_char in enumerate(self.args.start_chars):
            if start_char == "random":
                party[index] = self.characters.get_random_available()
            elif start_char == "randomngu":
                party[index] = self.characters.get_random_available(exclude = gogo_umaro)

        # assign chosen character rewards
        for character_id in party:
            if character_id is not None:
                reward = self.add_reward(RewardType.CHARACTER)
                reward.id = character_id
                reward.type = RewardType.CHARACTER

    def init_event_bits(self, space):
        self.event_bit_init = space.start_address
        space.write(
            field.SetEventBit(event_bit.NAMED_SABIN),
            field.SetEventBit(event_bit.NAMED_SHADOW),

            field.SetEventBit(event_bit.MET_BANON),
            field.SetEventBit(event_bit.GOT_GENJI_GLOVES_OR_GAUNTLET),

            field.SetEventBit(event_bit.FINISHED_LOCKE_SCENARIO),
            field.SetEventBit(event_bit.FINISHED_TERRA_SCENARIO),
            field.SetEventBit(event_bit.FINISHED_SABIN_SCENARIO),
            field.SetEventBit(event_bit.FINISHED_GESTAHL_DINNER),

            field.SetEventBit(event_bit.SAW_SHADOW_DREAM1),
            field.SetEventBit(event_bit.SAW_SHADOW_DREAM2),
            field.SetEventBit(event_bit.SAW_SHADOW_DREAM3),
            field.SetEventBit(event_bit.SAW_SHADOW_DREAM4),

            field.SetEventBit(event_bit.CONTINENT_IS_FLOATING),

            field.SetEventBit(event_bit.DISABLE_SAVE_POINT_TUTORIAL),
            field.SetEventBit(event_bit.DISABLE_CHOCOBO_TUTORIAL),

            field.SetEventWord(event_word.CHARACTERS_AVAILABLE, 0),
            field.SetEventWord(event_word.ESPERS_FOUND, 0),

            field.SetBattleEventBit(battle_bit.MAGIC_POINTS_AFTER_BATTLE),
        )

    def mod(self):
        self.intro_loop_mod()
        self.init_characters_mod()
        self.start_party_mod()
        self.start_esper_mod()
        self.start_gold_mod()
        self.start_items_mod()
        self.start_game_mod()

        # where the game begins after intro/pregame
        space = Reserve(0xc9a4f, 0xc9ad4, "setup and start game", field.NOP())
        space.write(
            field.Call(self.event_bit_init),
            field.Call(self.character_init),
            field.Call(self.start_party),
            field.Call(self.start_esper),
            field.Call(self.start_gold),
            field.Call(self.start_items),
            field.Call(self.start_game),

            field.CheckObjectives(),
            field.Return(),
        )

        for reward in self.rewards:
            self.log_reward(reward)

    def intro_loop_mod(self):
        space = Reserve(0xa5e34, 0xa5e7d, "create/initialize ??????/biggs/wedge", field.NOP())
        space.write(
            field.Branch(space.end_address + 1), # skip nops
        )

        space = Reserve(0xa5e8e, 0xa5e91, "call text intro, terra/wedge/vicks on cliff", field.NOP())
        space = Reserve(0xa5e92, 0xa5e92, "call magitek walking intro credits scene", field.NOP())

    def init_characters_mod(self):
        # this has to be done in a very specific way
        # MUST set properties before creating character
        # MUST create all characters in separate loop before deleting them all in a different loop
        #      (cannot create, initialize, refresh then delete all in same loop) (why?)
        # MUST delete all characters or some npcs won't show up (e.g. in narshe)
        # MUST refresh objects between chars created and deleted
        # to test these things: start new game with terra, immediately check for npc in narshe outside tutorial
        #                       start new game with terra, immediately go to doma and sleep (why do other inns work?)
        space = Allocate(Bank.CC, 207, "start character initialization", field.NOP())
        for character in range(self.characters.CHARACTER_COUNT):
            palette = self.characters.get_palette(character)
            space.write(
                field.SetProperties(character, character),
                field.CreateEntity(character),
                field.SetName(character, character),
                field.SetSprite(character, character),
                field.SetPalette(character, palette),
            )
        space.write(
            field.AddStatusEffects(self.characters.SHADOW, field.Status.DOG_BLOCK),
            field.RefreshEntities(),
            field.Call(field.DELETE_ALL_CHARACTERS),
            field.RefreshEntities(),

            field.Return(),
        )
        self.character_init = space.start_address

    def start_party_mod(self):
        src = []
        for reward in self.rewards:
            if reward.type == RewardType.CHARACTER:
                character = reward.id
                src += [
                    field.CreateEntity(character),
                    field.RecruitCharacter(character),
                    field.AddCharacterToParty(character, 1),
                ]

        src += [
            field.SetParty(1),
            field.RefreshEntities(),
            field.UpdatePartyLeader(),
            field.Return(),
        ]
        space = Write(Bank.CC, src, "start party")
        self.start_party = space.start_address

    def start_esper_mod(self):
        src = []

        for esper_id in self.espers.starting_espers:
            src += [
                field.AddEsper(esper_id, sound_effect = False)
            ]

        src += [
            field.Return()
        ]

        space = Write(Bank.CC, src, "start espers")
        self.start_esper = space.start_address

    def start_gold_mod(self):
        gold = self.args.gold
        if self.args.debug:
            gold += 300000

        src = []
        max_value = 2 ** 16 - 1 # AddGP has 2 byte argument
        while gold > max_value:
            src += [
                field.AddGP(max_value),
            ]
            gold -= max_value
        if gold > 0:
            src += [
                field.AddGP(gold),
            ]
        src += [
            field.Return(),
        ]
        space = Write(Bank.CC, src, "start gold")
        self.start_gold = space.start_address

    def start_items_mod(self):
        src = []
        for mc in range(self.args.start_moogle_charms):
            src += [
                field.AddItem("Moogle Charm", sound_effect = False),
            ]
        for mc in range(self.args.start_sprint_shoes):
            src += [
                field.AddItem("Sprint Shoes", sound_effect = False),
            ]
        for ws in range(self.args.start_warp_stones):
            src += [
                field.AddItem("Warp Stone", sound_effect = False),
            ]
        for fd in range(self.args.start_fenix_downs):
            src += [
                field.AddItem("Fenix Down", sound_effect = False),
            ]

        tools = ["NoiseBlaster", "Bio Blaster", "Flash", "Chain Saw",
                 "Debilitator", "Drill", "Air Anchor", "AutoCrossbow"]
        start_tools = random.sample(tools, self.args.start_tools)
        for tool in start_tools:
            src += [
                field.AddItem(tool, sound_effect = False),
            ]

        from constants.items import id_name
        from data.shop_item_tiers import tiers
        from data.item import Item
        junk = []
        junk += tiers[Item.WEAPON][0]
        junk += tiers[Item.SHIELD][0]
        junk += tiers[Item.HELMET][0]
        junk += tiers[Item.ARMOR][0]
        junk += tiers[Item.RELIC][0]

        start_junk = random.sample(junk, self.args.start_junk)

        for junk_id in start_junk:
            src += [
                field.AddItem(id_name[junk_id], sound_effect = False)
            ]

        # If doing Practice mod, but user requested not all items, randomize the set of starting items
        if self.args.prac3:
            from data.item_names import name_id
            # 50% chance of 1 Megalixir or not
            if random.randint(0,1) == 0:
                src += [
                    field.AddItem(name_id["Megalixir"], sound_effect = False),
                ]
            # 50% chance of 1 Paladin Shld or not
            if random.randint(0,1) == 0:
                src += [
                    field.AddItem(name_id["Paladin Shld"], sound_effect = False),
                ]
            # Do we simulate opening 50 chests?
            # give consumables separately
            # 50 is enough so that we'll get lots of decent items in other tiers
            i = 1
            while i <= 50:
                # don't grab chest from tier 0-4 as they're consumable items, we will distribute them differently, 
                # otherwise grab a random item from tiers 5-9, weighted as follows: 10, 20, 25, 30, 15
                # this code copied from random_tiered function to return an item based on random tier, but updated slightly to fit above criteria
                from data.chest_item_tiers import tiers as chesttiers, tier_s_distribution
                from utils.weighted_random import weighted_random
                weights = [0, 0, 0, 0, 0, 0.10, 0.20, 0.25, 0.30, 0.15]
                random_tier = weighted_random(weights)
                random_tier_index = random.randrange(5,9)
                # always use equal distribution
                random_tier_index = random.randrange(len(chesttiers[random_tier]))
                src += [
                    field.AddItem(chesttiers[random_tier][random_tier_index], sound_effect = False)
                ]
                # end of code copied from random_tiered function to return an item based on random tier
                # Give 6 Fenix Downs
                if i <= 6:
                    src += [
                        field.AddItem(name_id["Fenix Down"], sound_effect = False)
                    ]
                # 4 50% chances of getting status clearing items & Elixir, X-Potion, X-Ether
                # Always give 4 Earrings
                if i <= 4:
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Antidote"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Echo Screen"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Eyedrop"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Green Cherry"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Soft"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Remedy"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["X-Potion"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Elixir"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["X-Ether"], sound_effect = False),
                        ]
                    if random.randint(0,1) == 0:
                        src += [
                            field.AddItem(name_id["Revivify"], sound_effect = False),
                        ]
                    src += [
                        field.AddItem(name_id["Earrings"], sound_effect = False),
                    ]
                i += 1
        # If doing Practice mod with all items settting 
        elif self.args.prac:
            from objectives.results.throwables import THROWABLES
            from objectives.results.restoratives import RESTORATIVES
            i = 1
            while i <= 6:
                for item_id in id_name:
                    # Do not give any "Junk" AKA Tier 0 items (if a low-equipment run, can use default stuff)
                    # Do not give Throwables or Restoratives (can use an objective instead)
                    # Do not give CursedShld or Rename Card
                    # Do not give > 1 tool
                    # Do not give any relics other than:
                    # RunningShoes, Cherub Down, DragoonBoots, Earrings, Atlas Armlet, Blizzard Orb, Rage Ring
                    # Hero Ring, Ribbon, Muscle Belt, Crystal Orb, Gold Hairpin, Economizer, Gauntlet, GenjiGlove,
                    # Hyper Wrist, Offering, Beads, Gem Box, Dragon Horn, Merit Award, Memento Ring, Safety Bit,
                    # Marvel Shoes, Sniper Sight, Wall Ring, True Knight
                    ignore_items = ["Goggles", "Star Pendant", "Amulet", "White Cape", "Jewel Ring", "Fairy Ring", "Barrier Ring"
                                    "MithrilGlove", "Guard Ring", "Cure Ring", "Zephyr Cape", "Czarina Ring", "Cursed Ring", 
                                    "Sneak Ring", "Pod Bracelet", "Thief Glove", "Black Belt", "Coin Toss", "FakeMustache", "Relic Ring", 
                                    "Moogle Charm", "Charm Bangle", "Back Guard", "Gale Hairpin", "Exp. Egg", "Tintinabar", "Sprint Shoes",
                                    "Rename Card", "Cursed Shld"]
                    if id_name[item_id] not in junk and id_name[item_id] not in THROWABLES and id_name[item_id] not in RESTORATIVES and id_name[item_id] not in tools and id_name[item_id] not in ignore_items:
                        src += [
                            field.AddItem(id_name[item_id], sound_effect = False)
                        ]
                i += 1

        if self.args.debug:
            src += [
                field.AddItem("Dried Meat", sound_effect = False),
                field.AddItem("Dried Meat", sound_effect = False),
                field.AddItem("Dried Meat", sound_effect = False),
                field.AddItem("Warp Stone", sound_effect = False),
                field.AddItem("Warp Stone", sound_effect = False),
                field.AddItem("Warp Stone", sound_effect = False),
            ]
        src += [
            field.Return(),
        ]
        space = Write(Bank.CC, src, "start items")
        self.start_items = space.start_address

    def start_game_mod(self):
        src = [
            # place airship on wob, right outside narshe, start on airship deck
            field.LoadMap(0x00, direction.DOWN, default_music = False,
                          x = 84, y = 34, fade_in = True, airship = True),
            vehicle.SetPosition(84, 34),
            vehicle.LoadMap(0x06, direction.DOWN, default_music = True,
                            x = 16, y = 6, entrance_event = True),

            field.EntityAct(field_entity.PARTY0, True,
                field_entity.CenterScreen(),
            ),
            field.ShowEntity(field_entity.PARTY0),
            field.RefreshEntities(),
            field.FreeScreen(),
            field.FadeInScreen(speed = 4),
        ]
        if self.args.prac:
            src += [
                field.Dialog(2986),
            ]
        src += [
            field.Return(),
        ]
        space = Write(Bank.CC, src, "start game")
        self.start_game = space.start_address
