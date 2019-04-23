"""
IMPALA scores from IMPALA paper.

   30 entries
------------------------------------------------------------------------
   30  unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Importance Weighted Actor-Learner Architecture",
    "algo-nickname": "IMPALA",
    "algo-source-title": "IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 30
