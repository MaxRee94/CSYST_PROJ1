import ca_visualization as vis
import ca_core as core
from argparse import ArgumentParser

def main(headless, timesteps, f1, f2, _lambda, size):
    print("Initializing...")
    ca = core.CA(f1, f2, timesteps, _lambda, size)
    ca.set_initial_state()
    print("Running CA for {} timesteps...".format(timesteps))
    for t in range(timesteps):
        if t % 100 == 0:
           print("Iteration {}/{}".format(t, timesteps))
        ca.update(t)

    print("\nFinished {} time steps. CA terminated.\nWriting image to file...\n".format(timesteps))
    fpath = vis.write_image(ca.state, timesteps, f1, f2, _lambda, size)
    print("Image written to file at {}".format(fpath))

    if not headless:
        vis.show_image(ca.state)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-g",
        "--Headless",
        action = 'store_true',
        help = (
            "If specified, the system will run without a graphical user interface.\n"
        )
    )
    parser.add_argument(
        "-t",
        "--Timesteps",
        type = int,
        default = 5000,
        help = (
            "Defines the number of timesteps that the cellular automaton should run for. Defaults to 5000"
        )
    )
    parser.add_argument(
        "-s",
        "--Size",
        type = int,
        default = 10000,
        help = (
            "Defines the number of cells in an iteration. Defaults to 10000"
        )
    )
    parser.add_argument(
        "-f1",
        type = int,
        default = 204,
        help = (
            "Defines rule f1. Defaults to 204 (identity)"
        )
    )
    parser.add_argument(
        "-f2",
        type = int,
        default = 204,
        help = (
            "Defines rule f2. Defaults to 204 (identity)"
        )
    )
    parser.add_argument(
        "-l",
        "--Lambda",
        type = float,
        default = 0.5,
        help = (
            "Value between 0 and 1 that defines the probability that rule f2 will be chosen over f1"
        )
    )
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()
    main(args.Headless, args.Timesteps, args.f1, args.f2, args.Lambda, args.Size)

