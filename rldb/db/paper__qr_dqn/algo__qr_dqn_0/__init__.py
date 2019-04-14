"""
QR-DQN-0 scores from QR-DQN paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Quantile Regression Deep Q-Network with Strict Quantile Loss",
    "algo-nickname": "QR-DQN-0",
    "algo-source-title": "Distributional Reinforcement Learning with Quantile Regression",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
