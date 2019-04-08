"""
A2C scores from PPO paper.

   12 entries
------------------------------------------------------------------------
   12 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Advantage Actor Critic",
    "algo-nickname": "A2C",
    # A2C has no paper
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 12
