from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Random Network Distillation",
    "algo-nickname": "RND",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 1970000000,  # 1.97B
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 6
