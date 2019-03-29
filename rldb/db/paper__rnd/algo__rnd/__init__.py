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
    # Not specified
    "algo-frames": 1970000000,  # 1.97B
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 6
