from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "UCT to Classification-Interleaved",
    "algo-nickname": "UCC-I",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
