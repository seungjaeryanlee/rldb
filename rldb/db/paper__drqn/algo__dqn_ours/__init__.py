"""
DQN Ours scores from DRQN paper.

    9 entries
 + 10 flickering entries
------------------------------------------------------------------------
   19 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Q-Network Ours",
    "algo-nickname": "DQN Ours",
    "algo-source-title": "Human-level control through deep reinforcement learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 9 + 10
