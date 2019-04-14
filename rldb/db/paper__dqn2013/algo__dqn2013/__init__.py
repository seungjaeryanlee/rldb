"""
DQN2013 scores from DQN2013 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Q-Network (2013)",
    "algo-nickname": "DQN2013",
    "algo-source-title": "Playing Atari with Deep Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 10 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
