"""
Distributional DQN scores from Rainbow paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Distributional Deep Q-Network",
    "algo-nickname": "Distributional DQN",
    "algo-source-title": "Rainbow: Combining Improvements in Deep Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 108
