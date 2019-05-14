---
layout: page
title: Atari Ms. Pacman Environment
permalink: /envs/gym/atari/ms-pacman/

redirect_from:
 - /envs/gym/atari-2600/ms-pacman/
 - /env/gym/atari/ms-pacman/
 - /env/gym/atari-2600/ms-pacman/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/ms-pacman.mp4' | absolute_url }}" type="video/mp4">
</video>

The gameplay of Ms. Pac-Man is very similar to that of the original Pac-Man. The player earns points by eating pellets and avoiding ghosts (contact with one causes Ms. Pac-Man to lose a life). Eating an energizer (or "power pellet") causes the ghosts to turn blue, allowing them to be eaten for extra points. Bonus fruits can be eaten for increasing point values, twice per round. As the rounds increase, the speed increases, and energizers generally lessen the duration of the ghosts' vulnerability, eventually stopping altogether.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Ms._Pac-Man)*


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
