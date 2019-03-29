from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Human (from Dueling DQN)",
    "algo-nickname": "Human (from Dueling DQN)",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57 * 2  # 57 environments, 2 variants
