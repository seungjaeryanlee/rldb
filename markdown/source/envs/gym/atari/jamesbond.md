---
layout: page
title: Atari James Bond Environment
permalink: /envs/gym/atari/jamesbond/

redirect_from:
 - /envs/gym/atari-2600/james-bond/
 - /env/gym/atari/james-bond/
 - /env/gym/atari-2600/james-bond/
 - /envs/gym/atari/james-bond/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/jamesbond.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls the titular character of James Bond across four levels. The player is given a multi-purpose vehicle that acts as an automobile, a plane, and a submarine. The vehicle can fire shots and flare bombs, and travels from left to right as the player progresses through each level. The player can shoot or avoid enemies and obstacles that appear throughout the game, including boats, frogmen, helicopters, missiles, and mini-submarines.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/James_Bond_007_(1983_video_game))*


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
