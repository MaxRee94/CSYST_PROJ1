import ca_visualization as vis
import ca_core as core
from argparse import ArgumentParser


def main(verbose, headless, timesteps):
    print("Initializing...") if verbose else None
    ca = core.CA(204, 204, timesteps, verbose=verbose)
    ca.set_initial_state()
    print("Running CA for {} timesteps...".format(timesteps))
    for t in range(timesteps):
        if verbose and t % 100 == 0:
            print("Iteration {}/{}".format(t, timesteps))
        ca.update(t)

    print("\nFinished {} time steps. CA terminated.\n".format(timesteps))
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
        "-l",
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
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()
    main(args.Verbose, args.Headless, args.Timesteps)

