from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Sarsa",
    "algo-nickname": "Sarsa",
    # NOTE SARSA is very old, and this is not the first paper
    # "algo-source-title": "The Arcade Learning Environment: An Evaluation Platform for General Agents",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
