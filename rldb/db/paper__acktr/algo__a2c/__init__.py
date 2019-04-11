"""
A2C scores from ACKTR paper.

 6 atari entries
 8 mujoco entries
------------------------------------------------------------------------
 14 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Advantage Actor Critic",
    "algo-nickname": "A2C",
    "algo-source-title": "Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation",
}

# Populate entries  
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 6 + 8
