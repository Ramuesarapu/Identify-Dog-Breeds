import argparse

def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/')
    parser.add_argument('--arch', type=str, default='vgg')
    parser.add_argument('--dogfile', type=str, default='dognames.txt')
    return parser.parse_args()
