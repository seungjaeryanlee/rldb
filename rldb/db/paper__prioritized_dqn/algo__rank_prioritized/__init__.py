from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Prioritized Deep Q-Network (rank)",
    "algo-nickname": "Prioritized DQN (rank)",
    "algo-source-title": "Prioritized Experience Replay",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
