"""
PPO scores from PPO paper.

   49 entries
------------------------------------------------------------------------
   49 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Proximal Policy Optimization",
    "algo-nickname": "PPO",
    "algo-source-title": "Proximal Policy Optimization Algorithm",

    # HYPERPARAMETERS
    "algo-frames": 4 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
