import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Hyperparameters to train and do style transfer")
    parser.add_argument("-lr", "--learning_rate", type=float, default = 0.003)
    parser.add_argument("-steps", type=int, default=5000)
    parser.add_argument("--save_every", type=int, default=400, help="Save the target image every x step, must be lower than the total number of steps")
    parser.add_argument("-alpha", type=float, default=1, help="Content Weights according to the style transfer paper")
    parser.add_argument("-beta", type=float, default=1e-4, help="Style Weights according to the paper (lower=more abstract)")
    parser.add_argument("-c", "--content", type=str, required=True, help="path for the image used as the content image (the one getting modified)")
    parser.add_argument("-s", "--style", type=str, required=True, help="path for the image used as the style image (the one whose style is getting transferred)")
    
    
    args = vars(parser.parse_args())
    return args