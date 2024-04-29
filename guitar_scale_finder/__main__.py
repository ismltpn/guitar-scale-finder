import argparse

from scale_finder import ScaleFinder


def repl(tuning: str):
    sf = ScaleFinder(tuning=tuning)
    major_adds = [0, 2, 4, 5, 7, 9, 11]
    minor_adds = [0, 2, 3, 5, 7, 8, 10]
    # sf._print_scale(9, [0, 2, 4, 5, 7, 9, 11, 12])
    while True:
        try:
            key = input("Key(Eb, G, D# etc): ")
            is_minor = input("Is minor(y/n): ") == "y"
            sf.print_scale(
                key,
                minor_adds if is_minor else major_adds,
                "Minor" if is_minor else "Major",
            )
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Unknown key")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guitar Scale Finder")
    parser.add_argument(
        "tuning",
        help="The tuning of the scale | "
        "allowed characters: C,D,E,F,G,A,B,b,# | "
        "format: 'CGCGCE' 'D#ADGBE' 'EADGBEb'",
        type=str,
    )
    args = parser.parse_args()
    tuning: str = args.tuning
    assert (
        len(tuning.replace("b", "").replace("#", "")) == 6
    ), "Note count in tuning should be exactly 6"
    for c in tuning.replace("b", "").replace("#", ""):
        assert c not in ["a", "b", "c", "d", "e", "f", "g"], f"Unknown character: {c}"
    repl(tuning)
