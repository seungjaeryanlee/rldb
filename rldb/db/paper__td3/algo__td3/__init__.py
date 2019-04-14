"""
TD3 scores from TD3 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Twin Delayed Deep Deterministic Policy Gradient",
    "algo-nickname": "TD3",
    "algo-source-title": "Addressing Function Approximation Error in Actor-Critic Methods",

    # HYPERPARAMETERS
    "algo-frames": 1 * 1000 * 1000,  # Number of frames
}

# Populate entries  
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
