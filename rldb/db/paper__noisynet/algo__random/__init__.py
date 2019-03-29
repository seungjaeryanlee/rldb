"""
Random scores from NoisyNet paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Random (from NoisyNet)",
    "algo-nickname": "Random (from NoisyNet)",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
