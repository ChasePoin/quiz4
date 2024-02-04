import argparse as ap
import random

def argparser() -> None:
    parser=ap.ArgumentParser()
    parser.add_argument(help='Your favorite color', dest='color', type=str)
    parser.add_argument(help='Your favorite month number', dest='month', type=int)
    parser.add_argument(help='Your favorite number', dest='num', type=float)

    arguments = parser.parse_args()

    favColor = arguments.color
    favMonth = arguments.month
    favNumber = arguments.num

    if((favNumber > 0)):
        print(f"You will be happiest next year if you wear {favColor} on {favMonth}/{random.randrange(1,30)}/25.")
    else:
        print(f"You will be unhappiest next year if you wear {favColor} on {favMonth}/{random.randrange(1,30)}/25.")

if __name__ == "__main__":
    argparser()
