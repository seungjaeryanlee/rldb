"""
C51 scores from C51 paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Categorical 51-atom",
    "algo-nickname": "C51",
    "algo-source-title": "A Distributional Perspective on Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
