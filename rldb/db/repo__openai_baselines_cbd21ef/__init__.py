from .algo__ppo2 import entries as ppo2_entries
from .algo__deepq import entries as deepq_entries
from .algo__acktr import entries as acktr_entries
from .algo__acer import entries as acer_entries
from .algo__ppo2_mpi import entries as ppo2_mpi_entries
from .algo__a2c import entries as a2c_entries
from .algo__trpo_mpi import entries as trpo_mpi_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "OpenAI Baselines cbd21ef",
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
    + ppo2_entries
    + deepq_entries
    + acktr_entries
    + acer_entries
    + ppo2_mpi_entries
    + a2c_entries
    + trpo_mpi_entries
)
entries = [{**entry, **source} for entry in entries]
