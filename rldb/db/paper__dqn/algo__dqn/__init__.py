"""
DQN scores from DQN paper.

 49 entries
------------------------------------------------------------------------
 49 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Q-Network",
    "algo-nickname": "DQN",
    "algo-source-title": "Human-level control through deep reinforcement learning",

    # HYPERPARAMETERS
    # NOTE Is this really 50M and not 200M?
    "algo-frames": 50 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
