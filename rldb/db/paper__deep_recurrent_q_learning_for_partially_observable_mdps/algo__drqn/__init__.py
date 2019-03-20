from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Deep Recurrent Q-Network",
    "algo-nickname": "DRQN",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 9
