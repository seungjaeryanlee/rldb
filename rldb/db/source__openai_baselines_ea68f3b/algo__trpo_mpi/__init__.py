"""
TRPO (MPI) scores from OpenAI Baselines.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Policy Optimization (MPI)",
    "algo-nickname": "TRPO (MPI)",
    "algo-source-title": "Trust Region Policy Optimization",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
