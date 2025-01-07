from objectives.results._objective_result import *
import data.event_bit as event_bit

class Field(field_result.Result):
    def src(self):
        return [
            field.SetEventBit(event_bit.UNLOCKED_IMP_BASE_TREASURE),
        ]

class Battle(battle_result.Result):
    def src(self):
        return [
            battle_result.SetBit(event_bit.address(event_bit.UNLOCKED_IMP_BASE_TREASURE), event_bit.UNLOCKED_IMP_BASE_TREASURE),
        ]

class Result(ObjectiveResult):
    NAME = "Imperial Base Treasure"
    def __init__(self):
        super().__init__(Field, Battle)