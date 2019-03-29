"""
UCC-I scores from TRPO paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "UCT to Classification-Interleaved",
    "algo-nickname": "UCC-I",
    "algo-source-title": "Deep Learning for Real-Time Atari Game Play Using Offline Monte-Carlo Tree Search Planning",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
