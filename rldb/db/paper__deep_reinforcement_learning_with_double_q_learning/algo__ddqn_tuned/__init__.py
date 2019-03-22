from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Double Deep Q-Network (tuned)",
    "algo-nickname": "DDQN (tuned)",
    "algo-source-title": "Deep Reinforcement Learning with Double Q-learning",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57  # 57 human
