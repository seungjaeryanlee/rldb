"""
A2C scores from ACKTR paper.

 6 atari entries
 8 mujoco entries
------------------------------------------------------------------------
 14 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Advantage Actor Critic",
    "algo-nickname": "A2C",
    "algo-source-title": "Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation",
}

# Populate entries
# From Figure 3 caption: "1 timestep equals 4 frames"
entries = [{**entry, **algo} for entry in entries]
for entry in entries:
    if "atari" in entry["env-title"]:
        entry["algo-frames"] = 4 * 50 * 1000 * 1000
    elif "mujoco" in entry["env-title"]:
        entry["algo-frames"] = 4 * 10 * 1000 * 1000

assert len(entries) == 6 + 8
