"""
Contingency scores from DQN2013 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Contingency",
    "algo-nickname": "Contingency",
    "algo-source-title": "Investigating Contingency Awareness Using Atari 2600 Games",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
