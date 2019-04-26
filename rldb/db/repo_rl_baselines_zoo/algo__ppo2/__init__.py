"""
A2C scores from PPO paper.

   27 entries
------------------------------------------------------------------------
   27 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Proximal Policy Optimization",
    "algo-nickname": "PPO",
    "algo-source-title": "Proximal Policy Optimization Algorithms",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 27
