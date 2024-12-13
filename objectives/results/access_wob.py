from objectives.results._objective_result import *
import data.event_bit as event_bit

class Field(field_result.Result):
    def src(self):
        return [
            field.SetEventBit(event_bit.UNLOCKED_WOB),
        ]

class Battle(battle_result.Result):
    def src(self):
        return [
            battle_result.SetBit(event_bit.address(event_bit.UNLOCKED_WOB), event_bit.UNLOCKED_WOB),
        ]

class Result(ObjectiveResult):
    NAME = "Access World of Balance"
    def __init__(self):
        super().__init__(Field, Battle)
