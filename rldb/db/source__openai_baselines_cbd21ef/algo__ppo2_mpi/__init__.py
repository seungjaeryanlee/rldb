"""
PPO2 (MPI) scores from OpenAI Baselines.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Proximal Policy Optimization (MPI) (from OpenAI Baselines cbd21ef)",
    "algo-nickname": "PPO (MPI) (from OpenAI Baselines cbd21ef)",
    "algo-source-title": "Proximal Policy Optimization Algorithms",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
