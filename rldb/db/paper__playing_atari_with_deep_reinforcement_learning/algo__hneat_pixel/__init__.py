from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "HyperNEAT Pixel",
    "algo-nickname": "HNeat Pixel",
    "algo-source-title": "A Neuroevolution Approach to General Atari Game Playing",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
