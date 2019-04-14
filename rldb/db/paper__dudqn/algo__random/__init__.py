"""
Random scores from Dueling paper.

  114 entries
 - 49 no-op entries from DQN
 -  8 no-op entries from DDQN
 - 49 human entries from Gorila DQN
------------------------------------------------------------------------
    8 unique entries

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

assert len(entries) == 8
