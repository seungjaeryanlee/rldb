from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Best Linear Learner",
    "algo-nickname": "Linear",
    "algo-source-title": "Human-level Control through Deep Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
