"""
A2C scores from OpenAI Baselines.

 7 entries
------------------------------------------------------------------------
 7 unique entries

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

assert len(entries) == 7
