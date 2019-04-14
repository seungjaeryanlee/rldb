"""
DQN scores from Gorila DQN paper.

   98 entries
 - 49 no-op entries from DQN paper
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
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
