"""
Prioritized DDQN (prop, tuned) scores from Prioritized DQN paper.

   57 entries
------------------------------------------------------------------------
   57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Prioritized Double Deep Q-Network (proportional, tuned)",
    "algo-nickname": "Prioritized DDQN (prop, tuned)",
    "algo-source-title": "Prioritized Experience Replay",

    # HYPERPARAMETERS
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
