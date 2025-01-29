from memory.space import Bank, Allocate
from event.event_reward import CHARACTER_ESPER_ONLY_REWARDS, RewardType, choose_reward, weighted_reward_choice
import instruction.field as field

class Events():
    def __init__(self, rom, args, data):
        self.rom = rom
        self.args = args

        self.dialogs = data.dialogs
        self.characters = data.characters
        self.items = data.items
        self.maps = data.maps
        self.enemies = data.enemies
        self.espers = data.espers
        self.shops = data.shops

        events = self.mod()

        # TODO: need to figure out what this does in terms of validating the logic of seed
        if self.args.open_world or self.args.character_gating:
            self.validate(events)

    def mod(self):
        # generate list of events from files
        import os, importlib, inspect
        from event.event import Event
        events = []
        name_event = {}
        for event_file in sorted(os.listdir(os.path.dirname(__file__))):
            if event_file[-3:] != '.py' or event_file == 'events.py' or event_file == 'event.py':
                continue

            module_name = event_file[:-3]
            event_module = importlib.import_module('event.' + module_name)

            for event_name, event_class in inspect.getmembers(event_module, inspect.isclass):
                if event_name.lower() != module_name.replace('_', '').lower():
                    continue
                event = event_class(name_event, self.rom, self.args, self.dialogs, self.characters, self.items, self.maps, self.enemies, self.espers, self.shops)
                events.append(event)
                name_event[event.name()] = event

        # select event rewards
        if self.args.character_gating or self.args.location_gating1:
            self.character_gating_mod(events, name_event)
        elif self.args.location_gating2:
            self.location_gating2_mod(events, name_event)
        else:
            self.open_world_mod(events)

        # initialize event bits, mod events, log rewards
        log_strings = []
        space = Allocate(Bank.CC, 400, "event/npc bit initialization", field.NOP())
        for event in events:
            event.init_event_bits(space)
            event.mod()

            if self.args.spoiler_log and (event.rewards_log or event.changes_log):
                log_strings.append(event.log_string())
        space.write(field.Return())

        if self.args.spoiler_log:
            from log import section
            section("Events", log_strings, [])

        return events

    def init_reward_slots(self, events):
        import random
        reward_slots = []
        for event in events:
            event.init_rewards()
            for reward in event.rewards:
                if reward.id is None:
                    reward_slots.append(reward)

        random.shuffle(reward_slots)
        return reward_slots

    def choose_single_possible_type_rewards(self, reward_slots):
        for slot in reward_slots:
            if slot.single_possible_type():
                slot.id, slot.type = choose_reward(slot.possible_types, self.characters, self.espers, self.items)

    def choose_char_esper_possible_rewards(self, reward_slots):
        for slot in reward_slots:
            if slot.possible_types == (RewardType.CHARACTER | RewardType.ESPER):
                slot.id, slot.type = choose_reward(slot.possible_types, self.characters, self.espers, self.items)

    def choose_item_possible_rewards(self, reward_slots):
        for slot in reward_slots:
            slot.id, slot.type = choose_reward(slot.possible_types, self.characters, self.espers, self.items)

    def character_gating_mod(self, events, name_event):
        import random
        reward_slots = self.init_reward_slots(events)

        # for every event with only one reward type possible, assign random rewards
        # note: this includes start, which can get up to 4 characters
        self.choose_single_possible_type_rewards(reward_slots)

        # find characters that were assigned to start
        characters_available = [reward.id for reward in name_event["Start"].rewards]

        # find all the rewards that can be a character
        character_slots = []
        for event in events:
            for reward in event.rewards:
                if reward.possible_types & RewardType.CHARACTER:
                    character_slots.append(reward)

        iteration = 0
        slot_iterations = {} # keep track of how many iterations each slot has been available
        while self.characters.get_available_count():

            # build list of which slots are available and how many iterations those slots have already had
            unlocked_slots = []
            unlocked_slot_iterations = []
            for slot in character_slots:
                slot_empty = slot.id is None
                # if character gated, make sure to take gating into consideration
                if self.args.character_gating:
                    gate_char_available = (slot.event.character_gate() in characters_available or slot.event.character_gate() is None)
                # else location gating, this slot is available b/c there's no character gate
                else:
                    gate_char_available = True
                enough_chars_available = len(characters_available) >= slot.event.characters_required()
                if slot_empty and gate_char_available and enough_chars_available:
                    if slot in slot_iterations:
                        slot_iterations[slot] += 1
                    else:
                        slot_iterations[slot] = 0
                    unlocked_slots.append(slot)
                    unlocked_slot_iterations.append(slot_iterations[slot])

            # pick slot for the next character weighted by number of iterations each slot has been available
            slot_index = weighted_reward_choice(unlocked_slot_iterations, iteration)
            slot = unlocked_slots[slot_index]
            slot.id = self.characters.get_random_available()
            slot.type = RewardType.CHARACTER
            characters_available.append(slot.id)
            self.characters.set_character_path(slot.id, slot.event.character_gate())
            iteration += 1

        # get all reward slots still available
        reward_slots = [reward for event in events for reward in event.rewards if reward.id is None]
        random.shuffle(reward_slots) # shuffle to prevent picking them in alphabetical order

        # for every event with only char/esper rewards possible, assign random rewards
        self.choose_char_esper_possible_rewards(reward_slots)

        reward_slots = [slot for slot in reward_slots if slot.id is None]

        # assign rest of rewards where item is possible
        self.choose_item_possible_rewards(reward_slots)
        return

    def open_world_mod(self, events):
        import random
        reward_slots = self.init_reward_slots(events)

        # first choose all the rewards that only have a single type possible
        # this way we don't run out of that reward type before getting to the event
        self.choose_single_possible_type_rewards(reward_slots)

        reward_slots = [slot for slot in reward_slots if not slot.single_possible_type()]

        # next choose all the rewards where only character/esper types possible
        # this way we don't run out of characters/espers before getting to these events
        self.choose_char_esper_possible_rewards(reward_slots)

        reward_slots = [slot for slot in reward_slots if slot.id is None]

        # choose the rest of the rewards, items given to events after all characters/events assigned
        self.choose_item_possible_rewards(reward_slots)

    # location gating 2 reward selector
    # characters can only be at their own checks, so use the character gates to determine where a character can be placed
    def location_gating2_mod(self, events, name_event):
        import random
        # initialize the reward slots
        reward_slots = self.init_reward_slots(events)
        # for every event with only one reward type possible, assign random rewards
        # note: this includes start, which can get up to 4 characters
        self.choose_single_possible_type_rewards(reward_slots)
        # find characters that were assigned to start
        unavailable_chars = [reward.id for reward in name_event["Start"].rewards]
        # find all the rewards that can be a character and add to character_slots list (besides Start)
        character_slots = []
        narshe_battle_character = None
        for event in events:
            for reward in event.rewards:
                # if it's Start, don't add to possible slots
                if event.name() == "Start":
                    continue
                # if Narshe Battle, do special processing first before the algorithm to add non-starting characters
                elif event.name() == "Narshe Battle":
                    # give a 50/50 chance to reward a random available character (non-starting party)
                    if random.randint(0,1) == 0:
                        # get random available character
                        narshe_battle_character = self.characters.get_random_available()
                        # add this character to set of unavailable to reward
                        unavailable_chars.append(narshe_battle_character)
                        # the next line of code will append this slot to the next loop and we can special-case this
                # if there's a character as a possible reward, add this slot to list
                if reward.possible_types & RewardType.CHARACTER:
                    character_slots.append(reward)
        # shuffle the list so they're not in alphabetical order
        random.shuffle(character_slots)
        # loop over all of the character slots
        for slot in character_slots:
            # if the character gating for this slot is None, then it's the Narshe Battle
            if slot.event.character_gate() is None:
                # did we pick a character earlier? if so make sure this slot is updated
                if narshe_battle_character is not None:
                    # update the slot ID to be the character ID
                    slot.id = narshe_battle_character
                    # indicate a character is rewarded in this slot
                    slot.type = RewardType.CHARACTER
            # else if the slot's gated character is not in the unavailable list, pick that character for this slot
            # we'll also be adding it to the unavailable_chars list so they won't be picked again 
            elif slot.event.character_gate() not in unavailable_chars:
                # set this character to be unavailable for future rewards
                self.characters.set_unavailable(slot.event.character_gate())
                # fill slot with character ID
                slot.id = slot.event.character_gate()
                # indicate this slot is a character reward
                slot.type = RewardType.CHARACTER
                # add to unavailable_chars list
                unavailable_chars.append(slot.event.character_gate())
        # by now, all of the characters have been placed, so now place all of the espers/items in the rest of the slots
        # get all reward slots still available
        reward_slots = [reward for event in events for reward in event.rewards if reward.id is None]
        # for every event with only char/esper rewards possible, assign random espers
        self.choose_char_esper_possible_rewards(reward_slots)
        # get a new list of reward slots after placing espers
        reward_slots = [slot for slot in reward_slots if slot.id is None]
        # assign rest of rewards where item is possible
        self.choose_item_possible_rewards(reward_slots)
        return

    def validate(self, events):
        char_esper_checks = []
        for event in events:
            char_esper_checks += [r for r in event.rewards if r.possible_types == (RewardType.CHARACTER | RewardType.ESPER)]

        assert len(char_esper_checks) == CHARACTER_ESPER_ONLY_REWARDS, f"Number of char/esper only checks changed - Check usages of CHARACTER_ESPER_ONLY_REWARDS and ensure no breaking changes. Expected: {CHARACTER_ESPER_ONLY_REWARDS}, Actual: {len(char_esper_checks)}"
