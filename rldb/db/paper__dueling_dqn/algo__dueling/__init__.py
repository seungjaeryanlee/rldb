from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Dueling Deep Q-Network",
    "algo-nickname": "Dueling DQN",
    "algo-source-title": "Dueling Network Architectures for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57 * 2  # 57 environments, 2 variants
