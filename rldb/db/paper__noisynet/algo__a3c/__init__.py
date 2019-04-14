"""
A3C scores from NoisyNet paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Asynchronous Advantage Actor Critic",
    "algo-nickname": "A3C",
    "algo-source-title": "Asynchronous Methods for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 320 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
