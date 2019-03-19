from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Proximal Policy Optimization",
    "algo-nickname": "PPO",

    # HYPERPARAMETERS
    "algo-frames": 40000000,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
