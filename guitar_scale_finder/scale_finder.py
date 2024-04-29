class ScaleFinder:
    _note_to_value_dict = {
        "C": 0,
        "D": 2,
        "E": 4,
        "F": 5,
        "G": 7,
        "A": 9,
        "B": 11,
    }

    _value_to_note_dict = {
        0: "C",
        1: "C#/Db",
        2: "D",
        3: "D#/Eb",
        4: "E",
        5: "F",
        6: "F#/Gb",
        7: "G",
        8: "G#/Ab",
        9: "A",
        10: "A#/Bb",
        11: "B",
    }

    open_string_values: list[int]

    def __init__(self, tuning: str):
        i = 0
        self.open_string_values = []
        while i < len(tuning):
            value = self._note_to_value_dict[tuning[i]]
            if not i + 1 == len(tuning):
                if tuning[i + 1] == "b":
                    value -= 1
                    i += 1
                elif tuning[i + 1] == "#":
                    value += 1
                    i += 1
            self.open_string_values.append(value)
            i += 1
        pass

    def _print_scale(self, key_val: int, scale_add: list[int]):
        string_name_len = max(
            *[len(self._value_to_note_dict[v]) for v in self.open_string_values],
            len("String"),
        )
        print("String " + "".join(f" {i: <2}|" for i in range(24)))
        scale_values = {(key_val + v) % 12: i + 1 for i, v in enumerate(scale_add)}
        for open_string_val in reversed(self.open_string_values):
            string_note = self._value_to_note_dict[open_string_val]
            print(f"{string_note: <{string_name_len}}", end=":")
            for i in range(24):
                fret_val = (open_string_val + i) % 12
                if fret_val in scale_values:
                    if scale_values[fret_val] in [1, 3, 5]:
                        print(f"-{scale_values[fret_val]}-", end="|")
                    else:
                        print("-X-", end="|")
                else:
                    print("---", end="|")
            print()

    def print_scale(self, key: str, scale_add: list[int], scale_name: str):
        val = self._note_to_value_dict[key[0]]
        if len(key) > 1:
            if key[1] == "#":
                val += 1
            elif key[1] == "b":
                val -= 1
        print(self._value_to_note_dict[val] + " " + scale_name)
        self._print_scale(val, scale_add)
