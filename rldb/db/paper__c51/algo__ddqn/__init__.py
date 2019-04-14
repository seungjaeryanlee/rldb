"""
DDQN scores from C51 paper.

 51 entries
------------------------------------------------------------------------
 51 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Double Deep Q-Network",
    "algo-nickname": "DDQN",
    "algo-source-title": "A Distributional Perspective on Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
