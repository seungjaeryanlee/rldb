"""
Ape-X DQN scores from Ape-X DQN paper.

  57 noop entries
  57 human entries
------------------------------------------------------------------------
 114 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Ape-X DQN",
    "algo-nickname": "Ape-X DQN",
    "algo-source-title": "Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation",

    # HYPERPARAMETERS
    # NOTE Assume closely following setup of DDQN also means the number of frames are same
    "algo-frames": 22800 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 114
