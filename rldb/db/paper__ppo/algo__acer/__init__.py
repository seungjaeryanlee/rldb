"""
ACER scores from PPO paper.

   49 entries
------------------------------------------------------------------------
   49 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Actor-Critic with Experience Replay",
    "algo-nickname": "ACER",
    "algo-source-title": "Sample Efficient Actor-Critic with Experience Replay",

    # HYPERPARAMETERS
    "algo-frames": 4 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
