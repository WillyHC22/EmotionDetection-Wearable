import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Control for servo")
    parser.add_argument("--sp", "--servo_pin", default=40, description="pin used on raspberry board")
    parser.add_argument("--ct", "--update_interval", default=3, description="Time interval between two updates")
    parser.add_argument("--ts", "--time_sleep", default=1, description="Time sleeping between each movement of the servo")
    parser.add_argument("--stabilize", action="store_true", description = "Use this to test the stabilized version")
    args = vars(argparse.parse_args())
    return args