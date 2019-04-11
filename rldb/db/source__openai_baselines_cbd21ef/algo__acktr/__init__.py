"""
ACKTR scores from OpenAI Baselines.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Actor Critic using Kronecker-factored Trust Region",
    "algo-nickname": "ACKTR",
    "algo-source-title": "Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
