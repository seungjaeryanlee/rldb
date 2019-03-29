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
    "algo-frames": 40000000,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
