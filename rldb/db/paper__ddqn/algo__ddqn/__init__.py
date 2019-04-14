from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Double Deep Q-Network",
    "algo-nickname": "DDQN",
    "algo-source-title": "Deep Reinforcement Learning with Double Q-learning",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57 + 49
