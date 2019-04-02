"""
TRPO (ours) scores from Trust-PCL paper.

 5 entries
------------------------------------------------------------------------
 5 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Policy Optimization (from Trust-PCL)",
    "algo-nickname": "TRPO (from Trust-PCL)",
    "algo-source-title": "Trust Region Policy Optimization",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 10000000,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 5
