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
    "algo-title": "Dueling Deep Q-Network",
    "algo-nickname": "Dueling DQN",
    "algo-source-title": "Dueling Network Architectures for Deep Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
