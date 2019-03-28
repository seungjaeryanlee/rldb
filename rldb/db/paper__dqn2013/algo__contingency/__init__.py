from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Contingency Learning",
    "algo-nickname": "Contingency",
    "algo-source-title": "Investigating Contingency Awareness Using Atari 2600 Games",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
