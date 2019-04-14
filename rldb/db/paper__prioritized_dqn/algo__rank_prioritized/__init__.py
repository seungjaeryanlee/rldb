"""
Prioritized DQN (rank) scores from Prioritized DQN paper.

   57 entries
------------------------------------------------------------------------
   57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Prioritized Deep Q-Network (rank)",
    "algo-nickname": "Prioritized DQN (rank)",
    "algo-source-title": "Prioritized Experience Replay",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
