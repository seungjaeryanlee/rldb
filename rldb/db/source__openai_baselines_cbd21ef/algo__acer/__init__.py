"""
ACER scores from OpenAI Baselines.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Actor-Critic with Experience Replay",
    "algo-nickname": "ACER",
    "algo-source-title": "Sample Efficient Actor-Critic with Experience Replay",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
