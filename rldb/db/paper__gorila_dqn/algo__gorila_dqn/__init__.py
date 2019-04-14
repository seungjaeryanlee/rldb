"""
Gorila DQN scores from Gorila DQN paper.

 98 entries
------------------------------------------------------------------------
 98 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "General Reinforcement Learning Architecture Deep Q-Network",
    "algo-nickname": "Gorila DQN",
    "algo-source-title": "General Reinforcement Learning Architecture Deep Q-Network",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49 + 49
