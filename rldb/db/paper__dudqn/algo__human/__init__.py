"""
DuDQN scores from DuDQN paper.

   114 entries
 -  49 human entries from Gorila DQN
------------------------------------------------------------------------
    65 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Human",
    "algo-nickname": "Human",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 8 + 57
