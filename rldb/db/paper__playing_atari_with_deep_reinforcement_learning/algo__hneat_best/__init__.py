from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "HyperNEAT Best",
    "algo-nickname": "HNeat Best",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
