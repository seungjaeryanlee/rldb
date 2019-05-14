---
layout: page
title: Atari Surround Environment
permalink: /envs/gym/atari/surround/

redirect_from:
 - /envs/gym/atari-2600/surround/
 - /env/gym/atari/surround/
 - /env/gym/atari-2600/surround/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/surround.mp4' | absolute_url }}" type="video/mp4">
</video>

Like its predecessor Blockade, the object of Surround is to maneuver a square across the screen, leaving a trail behind. A player wins by forcing the other player to crash into one of the trails. Twelve game variations include options allow for speed-up, diagonal movement, wrap-around, and "erase" (the choice to not draw at a given moment). In addition, the sprites can be set to operate at a slower speed, or progressively speed up through five speeds.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Surround_(video_game))*


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
