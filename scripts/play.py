import argparse
import os
from web import app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('model_file1')
    parser.add_argument('model_file2')
    parser.add_argument('--engine1', type=str,
                        default="scripts/mcts_player.sh")
    parser.add_argument('--engine2', type=str,
                        default="scripts/mcts_player.sh")
    parser.add_argument('--name1', type=str,
                        default="engine1")
    parser.add_argument('--name2', type=str,
                        default="engine2")
    args = parser.parse_args()
    wd = os.getcwd()

    app.run(
        engine1=os.path.join(wd, args.engine1),
        engine2=os.path.join(wd, args.engine2),
        options1={'modelfile': args.model_file1},
        options2={'modelfile': args.model_file2},
        name1=args.name1,
        name2=args.name2,
        byoyomi=1000,
        host="0.0.0.0",
        port=5000
    )


if __name__ == "__main__":
    main()
