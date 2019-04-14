"""
Dynamics scores from RND paper.

 6 entries
------------------------------------------------------------------------
 6 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Modified Intrinsic Curiosity Module",
    "algo-nickname": "Dynamics",
    "algo-source-title": "Large-Scale Study of Curiosity-Driven Learning",

    # HYPERPARAMETERS
    "algo-frames": 1.97 * 1000 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 6
