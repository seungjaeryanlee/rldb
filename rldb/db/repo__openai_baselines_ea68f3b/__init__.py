from .algo__trpo_mpi import entries as trpo_mpi_entries
from .algo__ppo2 import entries as ppo2_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "OpenAI Baselines ea68f3b",
    "source-nickname": "Baselines",
    "source-authors": [
        "Prafulla Dhariwal",
        "Christopher Hesse",
        "Oleg Klimov",
        "Alex Nichol",
        "Matthias Plappert",
        "Alec Radford",
        "John Schulman", 
        "Szymon Sidor",
        "Yuhuai Wu",
        "Peter Zhokhov",
    ],

    #  LINKS
    "source-links": [
        {
            "type": "GitHub",
            "url": "https://github.com/openai/baselines",
        },
    ],

    #  MISC.
    "source-bibtex": """\
@misc{baselines,
  author = {Dhariwal, Prafulla and Hesse, Christopher and Klimov, Oleg and Nichol, Alex and Plappert, Matthias and Radford, Alec and Schulman, John and Sidor, Szymon and Wu, Yuhuai and Zhokhov, Peter},
  title = {OpenAI Baselines},
  year = {2017},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\\url{https://github.com/openai/baselines}},
}""",
}

# Populate entries
entries = (
    []
    + trpo_mpi_entries
    + ppo2_entries
)
entries = [{**entry, **source} for entry in entries]
