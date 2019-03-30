"""
DDPG scores from TD3 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Deterministic Policy Gradient",
    "algo-nickname": "DDPG",
    "algo-source-title": "Continuous control with deep reinforcement learning",
}

# Populate entries  
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
