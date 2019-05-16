<img src="docs/rldb.png" align="right" width="20%"/>

# rldb

[![Build Status](https://travis-ci.com/seungjaeryanlee/rldb.svg?branch=master)](https://travis-ci.com/seungjaeryanlee/rldb)
[![PyPI version](https://badge.fury.io/py/rldb.svg)](https://pypi.org/project/rldb/)
![GitHub repo size](https://img.shields.io/github/repo-size/seungjaeryanlee/rldb.svg?color=brightgreen)

![Environments tracked in rldb](https://img.shields.io/badge/environments-114-blue.svg)
![Papers tracked in rldb](https://img.shields.io/badge/papers-23-blue.svg)
![Repos tracked in rldb](https://img.shields.io/badge/repos-2-blue.svg)
![Algorithms tracked in rldb](https://img.shields.io/badge/algorithms-60-blue.svg)
![Entries tracked in rldb](https://img.shields.io/badge/entries-3380-blue.svg)

Database of RL algorithms

| Atari Space Invaders Scores | MuJoCo Walker2d Scores |
|:-:|:-:|
| ![Atari Space Invaders Scores](/docs/atari-space-invaders.png) | ![MuJoCo Walker2d Scores](/docs/mujoco-walker2d.png) |

## Examples

You can use `rldb.find_all({})` to retrieve all existing entries in `rldb`.

```python
import rldb


all_entries = rldb.find_all({})
```

You can also filter entries by specifying key-value pairs that the entry must match:

```python
import rldb


dqn_entries = rldb.find_all({'algo-nickname': 'DQN'})
breakout_noop_entries = rldb.find_all({
    'env-title': 'atari-breakout',
    'env-variant': 'No-op start',
})
```

You can also use `rldbl.find_one(filter_dict)` to find one entry that matches the key-value pair specified in `filter_dict`:

```python
import rldb
import pprint


entry = rldb.find_one({
    'env-title': 'atari-pong',
    'algo-title': 'Human',
})
pprint.pprint(entry)
```


<details><summary>Output</summary>
<p>

```python
{
    'algo-nickname': 'Human',
    'algo-title': 'Human',
    'env-title': 'atari-pong',
    'env-variant': 'No-op start',
    'score': 14.6,
    'source-arxiv-id': '1511.06581',
    'source-arxiv-version': 3,
    'source-authors': [   'Ziyu Wang',
                          'Tom Schaul',
                          'Matteo Hessel',
                          'Hado van Hasselt',
                          'Marc Lanctot',
                          'Nando de Freitas'],
    'source-bibtex': '@article{DBLP:journals/corr/WangFL15,\n'
                     '    author    = {Ziyu Wang and\n'
                     '                 Nando de Freitas and\n'
                     '                 Marc Lanctot},\n'
                     '    title     = {Dueling Network Architectures for Deep '
                     'Reinforcement Learning},\n'
                     '    journal   = {CoRR},\n'
                     '    volume    = {abs/1511.06581},\n'
                     '    year      = {2015},\n'
                     '    url       = {http://arxiv.org/abs/1511.06581},\n'
                     '    archivePrefix = {arXiv},\n'
                     '    eprint    = {1511.06581},\n'
                     '    timestamp = {Mon, 13 Aug 2018 16:48:17 +0200},\n'
                     '    biburl    = '
                     '{https://dblp.org/rec/bib/journals/corr/WangFL15},\n'
                     '    bibsource = {dblp computer science bibliography, '
                     'https://dblp.org}\n'
                     '}',
    'source-nickname': 'DuDQN',
    'source-title': 'Dueling Network Architectures for Deep Reinforcement '
                    'Learning'
}
```

</p>
</details>

## Entry Structure

Here is the format of every entry:

```python3
{
    # BASICS
    "source-title": "",
    "source-nickname": "",
    "source-authors": [],

    # MISC.
    "source-bibtex": "",

    # ALGORITHM
    "algo-title": "",
    "algo-nickname": "",
    "algo-source-title": "",

    # SCORE
    "env-title": "",
    "score": 0,
}
```

- `source-title` is the full title of the source of the score: it can be the title of the paper or GitHub repository title. `source-nickname` is a popular nickname or acronym for that title if it exists, otherwise it is the same as `source-title`. 
- `source-authors` are a list of authors or contributors.
- `source-bibtex` is a BibTeX-format citation.
- `algo-title` is the full title of the algorithm used. `algo-nickname` is the nickname or acronym for that algorithm if it exists, otherwise it is the same as `algo-nickname`.
- `algo-source-title` is the title of the source of the **algorithm**. It can and often is different from `source-title`.

For example, the **Space Invaders** score of **Asynchronous Advantage Actor Critic (A3C)** algorithm in the **Noisy Networks for Exploration (NoisyNet)** paper is represented by the following entry:

```python3
{
    #  BASICS
    "source-title": "Noisy Networks for Exploration",
    "source-nickname": "NoisyNet",
    "source-authors": [
        "Meire Fortunato",
        "Mohammad Gheshlaghi Azar",
        "Bilal Piot",
        "Jacob Menick",
        "Ian Osband",
        "Alex Graves",
        "Vlad Mnih",
        "Remi Munos",
        "Demis Hassabis",
        "Olivier Pietquin",
        "Charles Blundell",
        "Shane Legg",
    ],

    #  ARXIV
    "source-arxiv-id": "1706.10295",
    "source-arxiv-version": 2,

    #  MISC.
    "source-bibtex": """
@article{DBLP:journals/corr/FortunatoAPMOGM17,
    author    = {Meire Fortunato and
                 Mohammad Gheshlaghi Azar and
                 Bilal Piot and
                 Jacob Menick and
                 Ian Osband and
                 Alex Graves and
                 Vlad Mnih and
                 R{\'{e}}mi Munos and
                 Demis Hassabis and
                 Olivier Pietquin and
                 Charles Blundell and
                 Shane Legg},
    title     = {Noisy Networks for Exploration},
    journal   = {CoRR},
    volume    = {abs/1706.10295},
    year      = {2017},
    url       = {http://arxiv.org/abs/1706.10295},
    archivePrefix = {arXiv},
    eprint    = {1706.10295},
    timestamp = {Mon, 13 Aug 2018 16:46:11 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/FortunatoAPMOGM17},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}""",

    # ALGORITHM
    "algo-title": "Asynchronous Advantage Actor Critic",
    "algo-nickname": "A3C",
    "algo-source-title": "Asynchronous Methods for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 320 * 1000 * 1000,  # Number of frames

    # SCORE
    "env-title": "atari-space-invaders",
    "env-variant": "No-op start",
    "score": 1034,
    "stddev": 49,
}
```

Note that, as shown here, the entry can contain additional information.

## Sources

### Papers

#### Deep Q-Networks

- [x] [Playing Atari with Deep Reinforcement Learning (Mnih et al., 2013)](https://arxiv.org/abs/1312.5602)
- [x] [Human-level control through deep reinforcement learning (Mnih et al., 2015)](https://deepmind.com/research/dqn/)
- [x] [Deep Recurrent Q-Learning for Partially Observable MDPs (Hausknecht and Stone, 2015)](https://arxiv.org/abs/1507.06527)
- [x] [Massively Parallel Methods for Deep Reinforcement Learning (Nair et al., 2015)](https://arxiv.org/abs/1507.04296)
- [x] [Deep Reinforcement Learning with Double Q-learning (Hasselt et al., 2015)](https://arxiv.org/abs/1509.06461)
- [x] [Prioritized Experience Replay (Schaul et al., 2015)](https://arxiv.org/abs/1511.05952)
- [x] [Dueling Network Architectures for Deep Reinforcement Learning (Wang et al., 2015)](https://arxiv.org/abs/1511.06581)
- [x] [Noisy Networks for Exploration (Fortunato et al., 2017)](https://arxiv.org/abs/1706.10295)
- [x] [A Distributional Perspective on Reinforcement Learning (Bellemare et al., 2017)](https://arxiv.org/abs/1707.06887)
- [x] [Rainbow: Combining Improvements in Deep Reinforcement Learning (Hessel et al., 2017)](https://arxiv.org/abs/1710.02298)
- [x] [Distributional Reinforcement Learning with Quantile Regression (Dabney et al., 2017)](https://arxiv.org/abs/1710.10044)
- [x] [Implicit Quantile Networks for Distributional Reinforcement Learning (Dabney et al., 2018)](https://arxiv.org/abs/1806.06923)
- [x] [Distributed Prioritized Experience Replay (Horgan et al., 2018)](https://arxiv.org/abs/1803.00933)


#### Policy Gradients

- [x] [Asynchronous Methods for Deep Reinforcement Learning (Mnih et al., 2016)](https://arxiv.org/abs/1602.01783)
- [x] [Trust Region Policy Optimization (Schulman et al., 2015)](https://arxiv.org/abs/1502.05477)
- [x] [Proximal Policy Optimization Algorithms (Schulman et al., 2017)](https://arxiv.org/abs/1707.06347)
- [x] [Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation (Wu et al., 2017)](https://arxiv.org/abs/1708.05144)
- [x] [Addressing Function Approximation Error in Actor-Critic Methods (Fujimoto et al., 2018)](https://arxiv.org/abs/1802.09477)
- [x] [IMPALA: Importance Weighted Actor-Learner Architectures (Espeholt et al., 2018)](https://arxiv.org/abs/1802.01561)
- [x] [The Reactor: A fast and sample-efficient Actor-Critic agent for Reinforcement Learning (Gruslys et al., 2017)](https://arxiv.org/abs/1704.04651)

#### Exploration

- [x] [Exploration by Random Network Distillation (Burda et al., 2018)](https://arxiv.org/abs/1810.12894)

#### Misc.

- [x] [Trust-PCL: An Off-Policy Trust Region Method for Continuous Control (Nachum et al., 2017)](https://arxiv.org/abs/1707.01891)

### Repositories

- [x] [OpenAI Baselines](https://github.com/openai/baselines)
- [x] [RL Baselines Zoo](https://github.com/araffin/rl-baselines-zoo)
