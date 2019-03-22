from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Q-Network Ours",
    "algo-nickname": "DQN2015 Ours",
    "algo-source-title": "Human-level Control through Deep Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 9
