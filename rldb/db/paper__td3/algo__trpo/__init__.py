"""
TRPO scores from TD3 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Policy Optimization",
    "algo-nickname": "TRPO",
    "algo-source-title": "Trust Region Policy Optimization",

    # HYPERPARAMETERS
    "algo-frames": 1 * 1000 * 1000,  # Number of frames
}

# Populate entries  
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
