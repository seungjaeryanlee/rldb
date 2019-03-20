from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Policy Optimization - single path",
    "algo-nickname": "TRPO - single path",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
