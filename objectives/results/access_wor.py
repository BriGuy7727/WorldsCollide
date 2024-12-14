from objectives.results._objective_result import *
import data.event_bit as event_bit

class Field(field_result.Result):
    def src(self):
        return [
            field.SetEventBit(event_bit.UNLOCKED_WOR),
        ]

class Battle(battle_result.Result):
    def src(self):
        return [
            battle_result.SetBit(event_bit.address(event_bit.UNLOCKED_WOR), event_bit.UNLOCKED_WOR),
        ]

class Result(ObjectiveResult):
    NAME = "World of Ruin Access"
    def __init__(self):
        super().__init__(Field, Battle)
