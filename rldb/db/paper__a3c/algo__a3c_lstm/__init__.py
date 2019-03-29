"""
A3C LSTM scores from A3C paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Asynchronous Advantage Actor Critic Long Short-Term Memory",
    "algo-nickname": "A3C LSTM",
    "algo-source-title": "Asynchronous Methods for Deep Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
