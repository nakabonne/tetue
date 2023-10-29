import argparse
import cshogi.web.app
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('model_file1')
    parser.add_argument('model_file2')
    parser.add_argument('--engine1', type=str,
                        default="bonne/player/mcts_player.py")
    parser.add_argument('--engine2', type=str,
                        default="bonne/player/mcts_player.py")
    args = parser.parse_args()

    cshogi.web.app.run(
        engine1=args.engine1,
        engine2=args.engine2,
        options1={'modelfile': args.model_file1},
        options2={'modelfile': args.model_file2},
        byoyomi=1000
    )


if __name__ == "__main__":
    main()
