"""
TRPO+GAE scores from Trust-PCL paper.

 5 entries
------------------------------------------------------------------------
 5 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Policy Optimization + Generalized Advantage Estimation",
    "algo-nickname": "TRPO+GAE",
    "algo-source-title": "High-Dimensional Continuous Control Using Generalized Advantage Estimation",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 10000000,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 5
