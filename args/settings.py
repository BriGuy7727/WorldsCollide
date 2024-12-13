def name():
    return "Settings"

def parse(parser):
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-open", "--open-world", action = "store_true",
                      help = "Unrestricted event access")
    mode.add_argument("-cg", "--character-gating", action = "store_true",
                      help = "Events locked until required characters recruited")
    # location-gating mode #1
    mode.add_argument("-lg1", "--location-gating1", action = "store_true",
                      help = "World of Ruin access locked until conditions are met. Locations contain specific rewards.")
    # location-gating mode #2
    mode.add_argument("-lg2", "--location-gating2", action = "store_true",
                      help = "World of Ruin access locked until conditions are met. Locations contain specific rewards.")

    seed_spoilers = parser.add_argument_group("seed_spoilers")
    seed_spoilers.add_argument("-s", dest = "seed", type = str, required = False, help = "RNG seed")
    seed_spoilers.add_argument("-sl", "--spoiler-log", action = "store_true",
                               help = "Generated log file also contains event rewards and other detailed information")

def process(args):
    pass

def flags(args):
    flags = ""

    if args.character_gating:
        flags += " -cg"
    elif args.open_world:
        flags += " -open"
    # location-gating mode #1
    elif args.location_gating1:
        flags += " -lg1"
    # location-gating mode #2
    elif args.location_gating2:
        flags += " -lg1"

    if args.spoiler_log:
        flags += " -sl"

    return flags

def options(args):
    game_mode = "Open World"
    if args.character_gating:
        game_mode = "Character Gating"
    # location-gating mode #1
    elif args.location_gating1:
        game_mode = "Location Gating 1"
    # location-gating mode #2
    elif args.location_gating2:
        game_mode = "Location Gating 2"

    return [
        ("Mode", game_mode, "game_mode"),
        ("Seed", args.seed, "seed"),
        ("Spoiler Log", args.spoiler_log, "spoiler_log"),
    ]

def menu(args):
    entries = options(args)
    for index, entry in enumerate(entries):
        if entry[0] == "Seed":
            if len(entry[1]) > 18:
                entries[index] = (entry[0], entry[1][:15] + "...", "seed")
            break
    return (name(), entries)

def log(args):
    from log import format_option
    log = [name()]

    entries = options(args)
    for entry in entries:
        log.append(format_option(*entry))

    return log
