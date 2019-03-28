from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Prioritized Double Deep Q-Network (proportional, tuned)",
    "algo-nickname": "Prioritized DDQN (prop, tuned)",
    "algo-source-title": "Prioritized Experience Replay",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
