"""
DuDQN scores from DuDQN paper.

 114 entries
------------------------------------------------------------------------
 114 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Dueling Deep Q-Network",
    "algo-nickname": "DuDQN",
    "algo-source-title": "Dueling Network Architectures for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    # NOTE Assume closely following setup of DDQN also means the number of frames are same
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57 * 2  # 57 environments, 2 variants
