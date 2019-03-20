from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Policy Optimization - vine",
    "algo-nickname": "TRPO - vine",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
