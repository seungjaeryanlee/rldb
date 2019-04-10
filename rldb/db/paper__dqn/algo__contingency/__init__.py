"""
Contingency scores from DQN paper.

 49 entries
------------------------------------------------------------------------
 49 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Contingency (SARSA)",
    "algo-nickname": "Contingency",
    "algo-source-title": "Human-level control through deep reinforcement learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
