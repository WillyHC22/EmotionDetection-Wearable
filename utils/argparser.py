import argparse

##Make arg for each pin

def get_parser():
    parser = argparse.ArgumentParser(description="Control for servo")
    parser.add_argument("-p1", "--servo_pin1", type=int, default=8, help="pin used on raspberry board for servo 1")
    parser.add_argument("-p2", "--servo_pin2", type=int, default=9, help="pin used on raspberry board for servo 2")
    parser.add_argument("-p3", "--servo_pin3", type=int, default=10, help="pin used on raspberry board for servo 3")
    parser.add_argument("-p4", "--servo_pin4", type=int, default=11, help="pin used on raspberry board for servo 4")
    parser.add_argument("--init_duty", type=int, default=0, help="Initial duty when all 4 servos start")
    parser.add_argument("-d", "--depth", type=int, default=5, help="Depth of the trembling (3 -> Everytime it trembles, it goes 3 degrees back)")
    parser.add_argument("-i", "--interval", type=int, default=10, help="Interval in terms of angle to make the servo tremble (5 -> Every 5 degrees, it trembles)")
    parser.add_argument("-nrep", "--repetition", type=int, default=2, help="Number of repetition for one movement (one back and forth = one movement)")

    parser.add_argument("-sp", "--servo_pin", type=int, default=8, help="pin used on raspberry board")
    parser.add_argument("-ct", "--update_interval", default=3, help="Time interval between two updates for the emotion detection")
    parser.add_argument("-ts", "--time_sleep", default=1, help="Time sleeping between each movement of the servo")

    parser.add_argument("-mv", "--move", action="store_true", help="To use the other movement script")

    parser.add_argument("-sad", "--sadness", action="store_true", help="For sad emotion")
    parser.add_argument("-happy", "--happiness", action="store_true", help="For happy emotion")
    parser.add_argument("-angry", "--angriness", action="store_true", help="For angry emotion")
    args = vars(parser.parse_args())
    return args