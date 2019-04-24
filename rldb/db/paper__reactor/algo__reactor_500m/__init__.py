"""
Reactor 500m scores from Reactor paper.

   57 entries
------------------------------------------------------------------------
   57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Retrace-Actor",
    "algo-nickname": "Reactor",
    "algo-source-title": "The Reactor: A fast and sample-efficient Actor-Critic agent for Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 500 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
