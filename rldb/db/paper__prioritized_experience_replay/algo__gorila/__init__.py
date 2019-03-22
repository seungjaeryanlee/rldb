from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "General Reinforcement Learning Architecture DQN",
    "algo-nickname": "Gorila DQN",
    "algo-source-title": "Massively Parallel Methods for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
