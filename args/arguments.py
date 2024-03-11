class Arguments:
    def __init__(self):
        import importlib
        self.groups = [
            "settings",
            "objectives",
            "starting_party", "characters", "swdtechs", "blitzes", "lores", "rages", "dances", "steal", "sketch_control", "commands",
            "xpmpgp", "scaling", "bosses", "encounters", "boss_ai",
            "espers", "natural_magic", "misc_magic",
            "starting_gold_items", "items", "shops", "chests",
            "graphics",
            "coliseum", "auction_house", "challenges", "bug_fixes", "misc",
        ]
        self.group_modules = {}
        for group in self.groups:
            self.group_modules[group] = importlib.import_module("args." + group)

        from argparse import ArgumentParser
        self.parser = ArgumentParser()

        self.parser.add_argument("-i", dest = "input_file", required = True, help = "FFIII US v1.0 rom file")
        self.parser.add_argument("-o", dest = "output_file", required = False, help = "Modified FFIII US v1.0 rom file")
        self.parser.add_argument("-url", dest = "website_url", required = False, help = "Url to the shareable link for the seed")
        self.parser.add_argument("-manifest", dest = "manifest_file", required = False, help = "Output location for api metadata")
        self.parser.add_argument("-debug", dest = "debug", action = "store_true", help = "Debug mode")
        self.parser.add_argument("-sid", dest = "seed_id", action = "store_true", help = "Key used for api tracking")

        self.parser.add_argument("-nro", dest = "no_rom_output", action = "store_true", help = "Do not output a modified rom file")
        self.parser.add_argument("-slog", dest = "stdout_log", action = "store_true", help = "Write log to stdout instead of file")
        self.parser.add_argument("-hf", dest = "hide_flags", action = "store_true", help = "Hide Flags (no log, no flags menu)")

        # add practice arguments here since it will radically alter the options for the seed
        # -prac is "default" practice mode that grants everything
        self.parser.add_argument("-prac", dest = "prac", action = "store_true", help = "Practice")
        # -prac2 eliminates Calmness protection (Fenrir, Golem, Phantom, Life 3)
        self.parser.add_argument("-prac2", dest = "prac2", action = "store_true", help = "Practice")
        # -prac3 does not give the player all of the items
        self.parser.add_argument("-prac3", dest = "prac3", action = "store_true", help = "Practice")        

        for group in self.group_modules.values():
            group.parse(self.parser)

        self.parser.parse_args(namespace = self)

        from constants.spells import spell_id
        # if Practice with no calmness protection (prac2), set on prac flag
        if self.prac2 or self.prac3:
            self.prac = True
            if self.prac2:
                args.remove_learnable_spell_ids.append(spell_id["Life 3"])

        # if Practice, add debug option for character recruitment
        if self.prac:
           self.debug = True
           self.spoiler_log = True
        
        from args.espers import MAX_STARTING_ESPERS
        # if character gating, ensure the min and max starting espers <= 21 (MAX_STARTING_ESPERS)
        if args.settings.character_gating and args.starting_espers_min > MAX_STARTING_ESPERS:
            args.starting_espers_min = MAX_STARTING_ESPERS
        if args.settings.character_gating and args.starting_espers_max > MAX_STARTING_ESPERS:
            args.starting_espers_max = MAX_STARTING_ESPERS

        self.flags = ""
        self.seed_rng_flags = ""
        for group_name, group in self.group_modules.items():
            group.process(self)
            group_flags = group.flags(self)

            self.flags += group_flags
            if group_name != "graphics":
                # graphics flags are not used for seeding rng
                self.seed_rng_flags += group_flags
        self.flags = self.flags.strip()
        self.seed_rng_flags = self.seed_rng_flags.strip()

        # seed game based on given flags as well so players can't change them for competitions without changing the rest of the game
        from seed import seed_rng
        self.seed = seed_rng(self.seed, self.seed_rng_flags)

        import sprite_hash, version
        self.sprite_hash = sprite_hash.generate_hash(self.seed + self.seed_rng_flags + version.__version__)

        import os
        if self.output_file is None:
            # if no output_file given add seed to output name
            name, ext = os.path.splitext(self.input_file)
            self.output_file = f"{name}_wc_{self.seed}{ext}"

        if self.debug:
            self.spoiler_log = True

    def _process_min_max(self, arg_name):
        values = getattr(self, arg_name)
        if values:
            if values[0] > values[1]:
                values[0], values[1] = values[1], values[0]
            setattr(self, arg_name + "_min", values[0])
            setattr(self, arg_name + "_max", values[1])

if __name__ == "__main__":
    import os, sys

    # execute from parent directory for import paths
    sys.path[0] = os.path.join(sys.path[0], os.path.pardir)

    args = Arguments()
    print(args.flags)
