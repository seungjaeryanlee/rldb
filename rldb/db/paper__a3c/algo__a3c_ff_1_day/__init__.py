"""
A3C FF 1 day scores from A3C paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Asynchronous Advantage Actor Critic Feed Forward 1 day",
    "algo-nickname": "A3C FF 1 day",
    "algo-source-title": "Asynchronous Methods for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    # NOTE 4M frames per epoch, 50 epochs, 1/4 since only 1 day instead of 4
    "algo-frames": 50 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
