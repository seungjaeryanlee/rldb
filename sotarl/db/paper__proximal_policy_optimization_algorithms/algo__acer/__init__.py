from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Actor-Critic with Experience Replay",
    "algo-nickname": "ACER",

    # HYPERPARAMETERS
    "algo-frames": 40000000,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
