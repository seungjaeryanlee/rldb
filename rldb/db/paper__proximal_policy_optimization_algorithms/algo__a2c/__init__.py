from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Advantage Actor Critic",
    "algo-nickname": "A2C",

    # HYPERPARAMETERS
    "algo-frames": 40000000,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
