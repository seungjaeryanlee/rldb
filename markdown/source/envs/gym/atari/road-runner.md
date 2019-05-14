---
layout: page
title: Atari Road Runner Environment
permalink: /envs/gym/atari/road-runner/

redirect_from:
 - /envs/gym/atari-2600/road-runner/
 - /env/gym/atari/road-runner/
 - /env/gym/atari-2600/road-runner/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/road-runner.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls Road Runner, who is chased by Wile E. Coyote. In order to escape, Road Runner runs endlessly to the left. While avoiding Wile E. Coyote, the player must pick up bird seeds on the street, avoid obstacles like cars, and get through mazes. Sometimes Wile E. Coyote will just run after the Road Runner, but he occasionally uses tools like rockets, roller skates, and pogo-sticks.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Road_Runner_%28video_game%29)*


## Performances of RL Agents {#performances}

We list various reinforcement learning algorithms that were tested in this environment. These results are from [RL Database](https://github.com/seungjaeryanlee/rldb). If this page was helpful, please consider giving a star!

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/seungjaeryanlee/rldb" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star seungjaeryanlee/rldb on GitHub">Star</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
