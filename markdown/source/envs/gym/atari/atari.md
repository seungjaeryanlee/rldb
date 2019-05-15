---
layout: page
title: Atari Environments
permalink: /envs/gym/atari/
redirect_from:
 - /envs/gym/atari-2600
 - /env/gym/atari
 - /env/gym/atari-2600
 - /envs/atari

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
 - name: Installation
   permalink: '#installation'
 - name: Variants
   permalink: '#variants'

---

<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/beam-rider.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone mdl-cell--hide-phone">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/breakout.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone mdl-cell--hide-phone mdl-cell--hide-tablet">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/montezumas-revenge.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone mdl-cell--hide-phone mdl-cell--hide-tablet">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/qbert.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
</div>

## Overview

Atari 2600 is a video game console from Atari that was released in 1977. The game console included popular games such as *Breakout*, *Ms. Pacman* and *Space Invaders*. Since Deep Q-Networks were introduced by Mnih et al. in 2013, Atari 2600 has been the standard environment to test new Reinforcement Learning algorithms. Atari 2600 has been a challenging testbed due to its high-dimensional video input (size 210 x 160, frequency 60 Hz) and the discrepancy of tasks between games.

The Atari 2600 environments was originally provided through the [Arcade Learning Environment (ALE)](https://github.com/mgbellemare/Arcade-Learning-Environment). The environments have been wrapped by OpenAI Gym to create a more standardized interface. The OpenAI Gym provides 59 Atari 2600 games as environments.



## Performances

*Note: Most papers use 57 Atari 2600 games, and a couple of them are not supported by OpenAI Gym.*

These are the published results for Atari 2600 testbed. To test the robustness of the agent, most papers use one or both settings: the *no-op starts* and the *human starts*, both devised to provide a nondeterministic starting position. In *No-op start* setting, the agent selects the "do nothing" action for up to 30 times at the start of an episode. providing random starting positions to the agent. This originates from the [DQN2015 paper](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) by Mnih et al. (2015). In the *human start* setting,  the agents start from one of the 100 starting points sampled from a human professional's gameplay. The human starts setting originates from the [GorilaDQN paper](https://arxiv.org/abs/1507.04296) by Nair et al. (2015).

These results are from [RL Database](https://github.com/seungjaeryanlee/rldb). If this page was helpful, please consider giving a star!

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/seungjaeryanlee/rldb" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star seungjaeryanlee/rldb on GitHub">Star</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>



### Median

One popular method of checking the agent's overall performance is the *median human-normalized score*. You can read more about the choice of this metric in the [Rainbow paper](https://arxiv.org/abs/1710.02298). For better comparison of algorithms,  we only used results that were tested on majority of the games available.

#### No-op starts

| Median | Method                | Score from                                                   |
| ------ | --------------------- | ------------------------------------------------------------ |
| 434%   | Ape-X DQN<sup>1</sup> | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 331%   | UNREAL<sup>2</sup>    | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 223%   | Rainbow DQN           | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 178%   | C51                   | [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887) |
| 172%   | NoisyNet-Dueling DDQN | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 164%   | Distributional DQN    | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 151%   | Dueling DDQN          | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 140%   | Prioritized DDQN      | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 132%   | Dueling DDQN          | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 123%   | NoisyNet-DQN          | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 118%   | NoisyNet-DQN          | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 117%   | DDQN                  | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 96%    | Gorila DQN            | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 83%    | DQN<sup>3</sup>       | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 80%    | A3C                   | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 79%    | DQN<sup>3</sup>       | [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887) |

<sub>
<sup>1</sup> Ape-X DQN used a lot more (x100) environment frames compared to other results. The training time is half the time of other DQN results.<br/>
<sup>2</sup> Hyperparameters were tuned per game.<br/>
<sup>3</sup> Only evaluated on 49 games.
</sub>

#### Human starts

| Median | Method                | Score from                                                   |
| ------ | --------------------- | ------------------------------------------------------------ |
| 358%   | Ape-X DQN<sup>1</sup> | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 250%   | UNREAL<sup>2</sup>    | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 153%   | Rainbow DQN           | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 128%   | Prioritized DDQN      | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 125%   | C51                   | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 125%   | Distributional DQN    | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 117%   | Dueling DDQN          | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 116%   | A3C                   | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 110%   | DDQN                  | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 102%   | Noisy DQN             | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 78%    | Gorila DQN            | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 68%    | DQN<sup>3</sup>       | [Rainbow: Combining Improvements in Deep Reinforcement Learning]( https://arxiv.org/abs/1710.02298) |

<sub>
<sup>1</sup> Ape-X DQN used a lot more (x100) environment frames compared to other results. The training time is half the time of other DQN results.<br/>
<sup>2</sup> Hyperparameters were tuned per game. <br/>
<sup>3</sup> Only evaluated on 49 games.
</sub>

### Individual Environments

Although the metric above is a valuable way of comparing the general effectiveness of an algorithm, different algorithms have different strengths. Thus, we also included the state-of-the-art results for each game.

If you want to see how other methods performed in each Atari 2600 games, you can check the results of all methods by clicking the name of the game in the table below.

#### No-op Starts

$noop_envs_table

#### Human Starts

$human_envs_table




## Installation

### Prerequisites

To install the Atari 2600 environment, you need the OpenAI Gym toolkit. Read [this page](/envs/gym) to learn how to install OpenAI Gym.

### Installation via pip

If you did a full install of OpenAI Gym, the Atari 2600 should already be installed. Otherwise, you can install the Atari 2600 environment with a single `pip` command:

```bash
pip3 install gym[atari]
```

### Test Installation

You can run a simple random agent to make sure the Atari 2600 environment was correctly installed.

```python
import gym
env = gym.make('Pong-v0')
done = False
while not done:
    _, _, done, _ = env.step(env.action_space.sample())
    env.render()
env.close()
```



## Variants

In OpenAI Gym, each game has a few variants, distinguished by their suffixes. Through these variants, you can configure frame skipping and sticky actions. Frame skipping is a technique of using $$k$$-th frame. In other words, the agent only makes action every $$k$$ frames, and the same action is performed for $$k$$ frames. Sticky actions is a technique of setting some nonzero probability $$p$$ of action being repeated without agent's control. This adds  stochasticity to the deterministic Atari 2600 environments.

For example, there are six variants for the *Pong* environment.

| Name                                | Frame Skip $$k$$  | Repeat action probability $$p$$ |
| ----------------------------------- | --------------- | ----------------------------- |
| `Pong-v0`                           | 2~4<sup>1</sup> | 0.25                          |
| `Pong-v4`                           | 2~4<sup>1</sup> | 0                             |
| `PongDeterministic-v0`              | 4 <sup>2</sup>  | 0.25                          |
| `PongDeterministic-v4` <sup>3</sup> | 4 <sup>2</sup>  | 0                             |
| `PongNoFrameskip-v0`                | 1               | 0.25                          |
| `PongNoFrameskip-v4`                | 1               | 0                             |

<sub>
<sup>1</sup> $$k$$ is chosen randomly at every step from values $$\{2, 3, 4\}$$.<br/><sup>2</sup> For *Space Invaders*, the `Deterministic` variant $$k=3$$. This is because when $$k=4$$, the lasers are invisible because it frame skip coincides with the blinking frequency of lasers.<br/><sup>3</sup> `Deterministic-v4` is the configuration used to assess Deep Q-Networks.
</sub>

For more details about *frame skipping* and *sticky actions*, check Sections 2 and 5 of the ALE whitepaper: [Revisiting the Arcade Learning Environment](https://arxiv.org/abs/1709.06009).

Also, there are RAM environments such as `Pong-ram-v0`, where the observation is the RAM of the Atari machine instead of the 210 x 160 visual input. You can also add suffixes to RAM environments.

