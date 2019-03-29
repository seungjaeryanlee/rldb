"""
DDQN scores from C51 paper.

 51 entries
------------------------------------------------------------------------
 51 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Double Deep Q-Network (from C51)",
    "algo-nickname": "DDQN (from C51)",
    "algo-source-title": "A Distributional Perspective on Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
