"""
DQN scores from NoisyNet paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Q-Network",
    "algo-nickname": "DQN",
    "algo-source-title": "Human-level control through deep reinforcement learning",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
