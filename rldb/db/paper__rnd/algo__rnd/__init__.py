"""
RND scores from RND paper.

 6 entries
------------------------------------------------------------------------
 6 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Random Network Distillation",
    "algo-nickname": "RND",
    "algo-source-title": "Exploration by Random Network Distillation",

    # HYPERPARAMETERS
    "algo-frames": 1.97 * 1000 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 6
