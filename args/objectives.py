from constants.objectives import MAX_OBJECTIVES, MAX_CONDITIONS

def parse(parser):
    objectives = parser.add_argument_group("Objectives")
    for oi in range(MAX_OBJECTIVES):
        objectives.add_argument("-o" + chr(ord('a') + oi), "--objective_" + chr(ord('a') + oi),
                                type = str, help = "Objective " + chr(ord('A') + oi))

def process(args):
    from constants.objectives.results import types as result_types
    from constants.objectives.results import id_type as result_id_type
    from constants.objectives.conditions import types as condition_types

    class Result:
        def __init__(self, _id, name, format_string, value_range, args):
            self.id = _id
            self.name = name
            self.format_string = format_string
            self.value_range = value_range
            self.args = args

    class Condition:
        def __init__(self, name, string_function, value_range, min_max, args):
            self.name = name
            self.string_function = string_function
            self.value_range = value_range
            self.min_max = min_max
            self.args = args

    class Objective:
        def __init__(self, letter, result, conditions, conditions_required_min, conditions_required_max):
            self.letter = letter
            self.result = result
            self.conditions = conditions
            self.conditions_required_min = conditions_required_min
            self.conditions_required_max = conditions_required_max

    world_access_results = []
    from constants.objectives.results import category_types as category_types
    # build a list of all objective results in the World Access category type for detecting softlocks
    for result_name in category_types["World Access"]:
        world_access_results.append(result_name.name)
    args.objectives = []
    args.final_kefka_objective = False
    for oi in range(MAX_OBJECTIVES):
        lower_letter = chr(ord('a') + oi)
        upper_letter = chr(ord('A') + oi)

        values = getattr(args, "objective_" + lower_letter)
        if values is not None:
            values = values.split('.')
            for vi in range(len(values)):
                try:
                    values[vi] = int(values[vi])
                except ValueError:
                    pass
            value_index = 0

            result_type = result_id_type[values[value_index]]
            value_index += 1

            if result_type.value_range is not None:
                result_arg_count = 2
            else:
                result_arg_count = 0
            result_args = values[value_index : value_index + result_arg_count]
            value_index += result_arg_count

            for arg in result_args:
                if arg not in result_type.value_range:
                    import sys
                    args.parser.print_usage()
                    print(f"{sys.argv[0]}: error: {result_type.name}: invalid argument {arg}")
                    sys.exit(1)

            result = Result(*result_type, result_args)

            conditions_required_min = values[value_index]
            value_index += 1
            conditions_required_max = values[value_index]
            value_index += 1

            conditions = []
            while value_index < len(values) and len(conditions) < MAX_CONDITIONS:
                condition_type = condition_types[values[value_index]]
                value_index += 1

                if condition_type.name == "None":
                    continue

                if condition_type.min_max:
                    condition_arg_count = 2
                else:
                    condition_arg_count = 1
                condition_args = values[value_index : value_index + condition_arg_count]
                value_index += condition_arg_count

                for arg in condition_args:
                    if arg not in condition_type.value_range:
                        import sys
                        args.parser.print_usage()
                        print(f"{sys.argv[0]}: error: {condition_type.name}: invalid argument {arg}")
                        sys.exit(1)
                # code to prevent softlocks or unbeatable seeds with WOR/WOB access objectives
                # check if result name is WOR/WOB Access
                if result.name in world_access_results:
                    from constants.objectives.conditions import world_access_acceptable_conditions 
                    from constants.objectives.conditions import wor_access_acceptable_check_conditions
                    from constants.objectives.conditions import wor_access_acceptable_quest_conditions
                    from constants.objectives.conditions import wob_access_acceptable_check_conditions
                    from constants.objectives.conditions import wob_access_acceptable_quest_conditions
                    from constants.objectives.conditions import check_bit, quest_bit
                    # World of Ruin and World of Balance Access objective results MUST not contain any of the following Conditions:
                    # Random
                    # Characters
                    # Character
                    # Espers
                    # Esper
                    # Dragons
                    # Dragon
                    # Bosses
                    # Boss
                    if condition_type.name not in world_access_acceptable_conditions:
                        import sys
                        print(f"Objective Error: {condition_type.name} condition not valid with {result.name}")
                        sys.exit(1)
                    # if condition type is Check
                    elif condition_type.name == "Check":
                        # make sure the Check is not random
                        if condition_args == ['r']:
                            import sys
                            print(f"Objective Error: Random Check condition not valid with Result {result.name}")
                            sys.exit(1)
                        # else Check is not random
                        else:
                            # get name of the check specified
                            check_name = check_bit[condition_args[0]].name
                            # if result is WOR Access, make sure the Check is in the list of acceptable WOR Access checks
                            # ie: WOR Access cannot be a WOR check due to softlock
                            if result.name == "World of Ruin Access" and check_name not in wor_access_acceptable_check_conditions:
                                import sys
                                print(f"Objective Error: Check {check_name} condition not valid with Result {result.name}")
                                sys.exit(1)
                            # if result is WOB Access, make sure the Check is in the list of acceptable WOB Access checks
                            # ie: WOB Access cannot be a WOB check due to softlock
                            elif result.name == "World of Balance Access" and check_name not in wob_access_acceptable_check_conditions:
                                import sys
                                print(f"Objective Error: Check {check_name} condition not valid with Result {result.name}")
                                sys.exit(1)
                    # if condition type is Quest
                    elif condition_type.name == "Quest":
                        # ensure the Quest is not random
                        if condition_args == ['r']:
                            import sys
                            print(f"Objective Error: Random Quest condition not valid with Result {result.name}")
                            sys.exit(1)
                        # else Quest is not random
                        else:
                            # get name of the quest
                            quest_name = quest_bit[condition_args[0]].name
                            # if result is WOR Access, make sure the Quest is in the list of acceptable WOR Access quests
                            # ie: WOR Access cannot be a WOR quest due to softlock (this includes Suplex a Train and Set Zozo Clock)
                            if result.name == "World of Ruin Access" and quest_name not in wor_access_acceptable_quest_conditions:
                                import sys
                                print(f"Objective Error: Check {quest_name} condition not valid with Result {result.name}")
                                sys.exit(1)
                            # if result is WOB Access, make sure the Check is in the list of acceptable WOB Access quests
                            # ie: WOB Access cannot be a WOB quest due to softlock (this includes Suplex a Train and Set Zozo Clock)
                            elif result.name == "World of Balance Access" and quest_name not in wob_access_acceptable_quest_conditions:
                                import sys
                                print(f"Objective Error: Check {quest_name} condition not valid with Result {result.name}")
                                sys.exit(1)
                    # if condition type is Checks
                    elif condition_type.name == "Checks":
                        # get one end of range
                        range1 = condition_args[0]
                        # get other end of range
                        range2 = condition_args[1]
                        # if result is WOR Access, make sure the number of checks cannot be more than the count of total WOB checks
                        if result.name == "World of Ruin Access":
                            if range1 > len(wor_access_acceptable_check_conditions):
                                import sys
                                print(f"Objective Error: Checks {range1} condition not valid with Result {result.name}")
                                sys.exit(1)
                            elif range2 > len(wor_access_acceptable_check_conditions):
                                import sys
                                print(f"Objective Error: Checks {range2} condition not valid with Result {result.name}")
                                sys.exit(1) 
                        # if result is WOB Access, make sure the number of checks cannot be more than the count of total WOR checks
                        elif result.name == "World of Balance Access":
                            if range1 > len(wob_access_acceptable_check_conditions):
                                import sys
                                print(f"Objective Error: Checks {range1} condition not valid with Result {result.name}")
                                sys.exit(1)
                            elif range2 > len(wob_access_acceptable_check_conditions):
                                import sys
                                print(f"Objective Error: Checks {range2} condition not valid with Result {result.name}")
                                sys.exit(1) 

                condition = Condition(*condition_type, condition_args)
                conditions.append(condition)

            conditions_required_min = max(min(conditions_required_min, len(conditions)), 0)
            conditions_required_max = max(min(conditions_required_max, len(conditions)), 0)

            objective = Objective(upper_letter, result, conditions, conditions_required_min, conditions_required_max)
            args.objectives.append(objective)

def flags(args):
    flags = ""

    for oi in range(MAX_OBJECTIVES):
        lower_letter = chr(ord('a') + oi)

        values = getattr(args, "objective_" + lower_letter)
        if values is not None:
            flags += " -o" + lower_letter + " " + values

    return flags

def log(args):
    from log import format_option

    lentries = [[]]
    rentries = [[]]
    for oi, objective in enumerate(args.objectives):
        entry = []

        result = objective.letter + " " + objective.result.name
        if objective.result.name != "Random" and objective.result.format_string == "Random":
            result_args = "Random"
        else:
            result_args = '-'.join([str(arg) for arg in objective.result.args])
        entry.append(format_option(result, result_args, f"{objective.result.name}"))

        for condition in objective.conditions:
            if condition.min_max:
                condition_args = '-'.join([str(arg) for arg in condition.args])
            elif condition.name == "Random":
                condition_args = ""
            else:
                if condition.args[0] == 'r':
                    condition_args = "Random"
                else:
                    condition_args = condition.string_function(*condition.args)
            entry.append(format_option("  " + condition.name, condition_args, f"{objective.result.name}_{condition.name}"))

        conditions_required_args = f"{objective.conditions_required_min}-{objective.conditions_required_max}"
        entry.append(format_option("Conditions Required", conditions_required_args, f"{objective.result.name}_conditions_req"))

        if oi % 2:
            rentries.append(entry)
        else:
            lentries.append(entry)

    from log import section_entries
    section_entries("Objectives", lentries, rentries)
