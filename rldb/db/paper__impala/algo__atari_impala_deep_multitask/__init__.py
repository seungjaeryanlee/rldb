"""
IMPALA (deep, multitask) scores from IMPALA paper.

   57 entries
------------------------------------------------------------------------
   57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Importance Weighted Actor-Learner Architecture (deep, multitask)",
    "algo-nickname": "IMPALA (deep, multitask)",
    "algo-source-title": "IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
