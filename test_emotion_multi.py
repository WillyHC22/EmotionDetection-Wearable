from src.control import MovementControl
from utils.argparser import get_parser

if __name__ == '__main__':

    args = get_parser()
    control = MovementControl(args)

    if args["sadness"]:
        print("Sadness argument")
        if args["move"]:
            control.Sadness_move()
        else:
            control.Sadness()

    if args["happiness"]:
        if args["move"]:
            control.Happy_move()
        else:
            control.Happy()

    if args["angriness"]:
        if args["move"]:
            control.Anger_move()
        else:
            control.Anger()
