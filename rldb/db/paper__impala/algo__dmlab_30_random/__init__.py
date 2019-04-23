"""
Random scores from IMPALA paper.

   30 entries
------------------------------------------------------------------------
   30  unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Random",
    "algo-nickname": "Random",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 30
