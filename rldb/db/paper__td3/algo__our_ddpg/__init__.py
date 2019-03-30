"""
Our DDPG scores from TD3 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Our Deep Deterministic Policy Gradient (from TD3)",
    "algo-nickname": "Our DDPG (from TD3)",
    "algo-source-title": "Continuous control with deep reinforcement learning",
}

# Populate entries  
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
