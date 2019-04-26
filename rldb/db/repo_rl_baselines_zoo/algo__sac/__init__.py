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
    "algo-title": "Soft Actor Critic",
    "algo-nickname": "SAC",
    "algo-source-title": "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 12
