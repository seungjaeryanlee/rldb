"""
DRQN scores from DRQN paper.

    9 entries
 + 10 flickering entries
------------------------------------------------------------------------
   19 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Recurrent Q-Network",
    "algo-nickname": "DRQN",
    "algo-source-title": "Deep Recurrent Q-Learning for Partially Observable MDPs",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 9 + 10
