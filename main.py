import ca_visualization as vis
import ca_core as core
from argparse import ArgumentParser

def main(verbose, headless, timesteps, f1, f2, _lambda):
    print("Initializing...") if verbose else None
    ca = core.CA(f1, f2, timesteps, _lambda, verbose=verbose)
    ca.set_initial_state()
    print("Running CA for {} timesteps...".format(timesteps)) if verbose else None
    for t in range(timesteps):
        if verbose and t % 100 == 0:
           print("Iteration {}/{}".format(t, timesteps))
        ca.update(t)

    print("\nFinished {} time steps. CA terminated.\nWriting image to file...\n".format(timesteps)) if verbose else None
    fpath = vis.write_image(ca.state, timesteps, f1, f2, _lambda)
    print("Image written to file at {}".format(fpath)) if verbose else None

    if not headless:
        vis.show_image(ca.state)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--Verbose",
        action = 'store_true',
        help = (
            "If specified, the system will print all available runtime information to the console.\n"
            "If not specified, only warnings and errors will be printed."
        )
    )
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
            "Defines the number of timesteps that the cellular automaton should run for."
        )
    )
    parser.add_argument(
        "-f1",
        type = int,
        required=True,
        help = (
            "Defines rule f1"
        )
    )
    parser.add_argument(
        "-f2",
        type = int,
        required=True,
        help = (
            "Defines rule f2"
        )
    )
    parser.add_argument(
        "-l",
        "--Lambda",
        type = float,
        required=True,
        help = (
            "Value between 0 and 1 that defines the probability that rule f2 will be chosen over f1"
        )
    )
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()
    main(args.Verbose, args.Headless, args.Timesteps, args.f1, args.f2, args.Lambda)

