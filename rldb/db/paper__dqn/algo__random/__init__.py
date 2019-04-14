"""
Random scores from DQN paper.

 49 entries
------------------------------------------------------------------------
 49 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Random",
    "algo-nickname": "Random",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
