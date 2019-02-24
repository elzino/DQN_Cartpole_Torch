import argparse


defaults_train = {
    "load_path": None,
    "num_episode": 1000,
    "batch_size": 128,
    "gamma": 0.999,
    "eps_start": 0.9,
    "eps_end": 0.05,
    "eps_decay": 0.01,
    "target_update": 10,
    "replay_memory_capacity": 3000,
}


def check_args_train(args):
    """Check commandline argument validity."""
    assert args.num_episode >= 1, "Number of episode must be a positive integer"

    assert args.batch_size >= 1, "Size of batch must be a positive integer"

    assert 0 <= args.gamma <= 1, "gamma must be between 0 and 1"

    assert 0 <= args.eps_end <= args.eps_start <= 1, "eps_start and eps_end must be valid value between 0 and 1"

    assert 0 <= args.eps_decay <= 1, "eps_decay must be between 0 and 1"

    assert args.target_update >= 1, "target_update must be a positive integer"

    assert args.replay_memory_capacity >= 1, "replay_memory_capacity must be a non-negative integer"

    return args


def get_args_train():
    """Parse arguments from commandline."""
    parser = argparse.ArgumentParser(
        description="Pytorch Implementation of DQN about Cart-Pole Problem")

    parser.add_argument("-l", "--load_path",
                        type=str, default=defaults_train['load_path'], help="Path of model file")

    parser.add_argument("-e", "--num_episode",
                        type=int, default=defaults_train['num_episode'], help="Number of episode")

    parser.add_argument("-s", "--batch_size",
                        type=int, default=defaults_train['batch_size'], help="Size of batch from Replay Memory")

    parser.add_argument("-g", "--gamma",
                        type=float, default=defaults_train['gamma'],
                        help="Discount factor of reward")

    parser.add_argument("-es", "--eps_start",
                        type=float, default=defaults_train['eps_start'], help="Start value of epsilon")

    parser.add_argument("-ee", "--eps_end",
                        type=float, default=defaults_train['eps_end'], help="End value of epsilon")

    parser.add_argument("-ed", "--eps_decay",
                        type=float, default=defaults_train['eps_decay'], help="epsilon = exp(eps_decay * steps_done)")

    parser.add_argument("-t", "--target_update",
                        type=int, default=defaults_train['target_update'],
                        help="Number of episode needed to update target network")

    parser.add_argument("-c", "--replay_memory_capacity",
                        type=int, default=defaults_train['replay_memory_capacity'],
                        help="Capacity of Replay Memory")

    return check_args_train(parser.parse_args())