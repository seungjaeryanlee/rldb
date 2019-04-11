"""
Human scores from DDQN paper.

  106 entries
 - 49 no-op entries from DQN
 - 49 human entries from Gorila DQN
------------------------------------------------------------------------
    8 unique entries

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

assert len(entries) == 8
