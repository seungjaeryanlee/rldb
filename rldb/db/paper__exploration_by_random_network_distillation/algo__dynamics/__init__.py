from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Modified Intrinsic Curiosity Module",
    "algo-nickname": "Dynamics",
    "algo-source-title": "Large-Scale Study of Curiosity-Driven Learning",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 1970000000,  # 1.97B
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 6
