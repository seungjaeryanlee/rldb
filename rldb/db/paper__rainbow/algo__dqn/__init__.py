"""
DQN scores from Rainbow paper.

   57 entries
 - 49 entries from DQN paper
------------------------------------------------------------------------
    8 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Q-Network (from Rainbow)",
    "algo-nickname": "DQN (from Rainbow)",
    "algo-source-title": "Human-level Control through Deep Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 16
