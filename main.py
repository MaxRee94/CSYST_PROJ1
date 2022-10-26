import numpy as np
import ca_visualization as vis
from argparse import ArgumentParser


def main(verbose, gui, timesteps):
    print("Initializing...")

    state = np.random.randint(0, 2, (10000, 5000)).astype(np.float32)
    if gui:
        vis.show_image(state)


if __name__ == '__main__':
    parser = ArgumentParser()
    
    parser.add_argument(
        "-v",
        "--Verbose",
        type = bool,
        default = True,
        help = (
            "If True, the system will print all available runtime information to the console.\n"
            "If False, only warnings and errors will be printed. True by default."
        )
    )
    parser.add_argument(
        "-g",
        "--ShowGui",
        type = bool,
        default = True,
        help = (
            "If True, the system will run with a graphical user interface.\n"
            "If False, the system will run as a background process. True by default."
        )
    )
    parser.add_argument(
        "-t",
        "--Timesteps",
        type = int,
        help = (
            "Defines the number of timesteps that the cellular automaton should run for."
        )
    )

    args = parser.parse_args()
    print("args: ", args)

    main(args.Verbose, args.ShowGui, args.Timesteps)

