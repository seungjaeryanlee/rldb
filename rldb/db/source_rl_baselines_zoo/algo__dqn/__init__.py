"""
A2C scores from PPO paper.

   12 entries
------------------------------------------------------------------------
   12 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Q-Network",
    "algo-nickname": "DQN",
    "algo-source-title": "Human-level Control through Deep Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 12
