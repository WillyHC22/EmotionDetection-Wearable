from src.control_test import TestMovementControl_1
from utils.argparser import get_parser

if __name__ == '__main__':
    args = get_parser()
    if args["sadness"]:
        test_control = TestMovementControl_1(args)
        test_control.Sadness()

    if args["happiness"]:
        test_control = TestMovementControl_1(args)
        test_control.Happy()

    if args["angriness"]:
        test_control = TestMovementControl_1(args)
        test_control.Anger()
