from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Human (from Gorila DQN)",
    "algo-nickname": "Human (from Gorila DQN)",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49 + 49  # 49 human, 49 noop
