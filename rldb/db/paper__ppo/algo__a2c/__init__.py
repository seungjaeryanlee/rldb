"""
A2C scores from PPO paper.

   49 entries
------------------------------------------------------------------------
   49 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Advantage Actor Critic",
    "algo-nickname": "A2C",
    # A2C has no paper

    # HYPERPARAMETERS
    "algo-frames": 4 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
