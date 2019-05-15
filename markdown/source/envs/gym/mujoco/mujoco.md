---
layout: page
title: MuJoCo Environments
permalink: /envs/gym/mujoco/
redirect_from: /env/gym/mujoco/

nav:
- name: Overview
  permalink: '#overview'
- name: Environments
  permalink: '#environments'
- name: Installation
  permalink: '#installation'

---

## Overview

![]({{ "assets/_pages/envs/gym/mujoco.gif" | absolute_url }})

**MuJoCo** (**Mu**lti-**Jo**int dynamics with **Co**ntact) is a proprietary physics engine for detailed, efficient rigid body simulations with contacts. MuJoCo can be used to create environments with continuous control tasks such as walking or running. Thus, many policy gradient methods (TRPO, PPO) have been tested on various MuJoCo environments.



## Environments

We list various reinforcement learning algorithms that were tested with MuJoCo. These results are from [RL Database](https://github.com/seungjaeryanlee/rldb). If this page was helpful, please consider giving a star!

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/seungjaeryanlee/rldb" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star seungjaeryanlee/rldb on GitHub">Star</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>

$table

There are many papers that have experimented with the MuJoCo continuous control environment, but most papers decided not include exact scores and instead used performance curves. If you know other papers that report results on the MuJoCo environment, please [email me](mailto:seungjaeryanlee@gmail.com)!

## Installation

### Prerequisites

To install the MuJoCo environment, you need the OpenAI Gym toolkit. Read [this page](/envs/gym) to learn how to install OpenAI Gym.

You also need to purchase MuJoCo license. MuJoCo offers a 30-day trial license for everyone, and a free license for students using MuJoCo for personal projects only. Visit their [license page](https://www.roboti.us/license.html) for more information.

### Install MuJoCo binary 

1. Download the MuJoCo version 1.50 binaries for [Linux](https://www.roboti.us/download/mjpro150_linux.zip), [OSX](https://www.roboti.us/download/mjpro150_osx.zip), or [Windows](https://www.roboti.us/download/mjpro150_win64.zip).
2. Unzip the downloaded `mjpro150` directory into `~/.mujoco/mjpro150`, and place your license key (the `mjkey.txt` file from your email) at `~/.mujoco/mjkey.txt`.

### Install MuJoCo package

If you did a full install of OpenAI Gym, the MuJoCo package should already be installed. Otherwise, you can install the MuJoCo environments with a single `pip` command:

```bash
pip3 install gym[mujoco]
```

### Test Installation

You can try rendering the `Humanoid-v2` environment to make sure the MuJoCo environment was correctly installed.

```python
import gym
env = gym.make('Humanoid-v2')
env.reset()
env.render()
```
