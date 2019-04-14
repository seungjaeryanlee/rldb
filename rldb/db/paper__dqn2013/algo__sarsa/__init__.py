"""
Sarsa scores from DQN2013 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Sarsa",
    "algo-nickname": "Sarsa",
    # NOTE SARSA is very old, and this is not the first paper
    # "algo-source-title": "The Arcade Learning Environment: An Evaluation Platform for General Agents",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
