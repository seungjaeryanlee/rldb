"""
DuDQN scores from NoisyNet paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Dueling Deep Q-Network (from NoisyNet)",
    "algo-nickname": "Dueling DQN (from NoisyNet)",
    "algo-source-title": "Dueling Network Architectures for Deep Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
