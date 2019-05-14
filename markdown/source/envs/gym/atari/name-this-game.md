---
layout: page
title: Atari Name This Game Environment
permalink: /envs/gym/atari/name-this-game/

redirect_from:
 - /envs/gym/atari-2600/name-this-game/
 - /env/gym/atari/name-this-game/
 - /env/gym/atari-2600/name-this-game/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/name-this-game.mp4' | absolute_url }}" type="video/mp4">
</video>

In the game, the player controls a scuba diver who must protect a treasure from an octopus at the top of the screen: The octopus tries to capture the treasure with its tentacles. Meanwhile, a great white shark tries to distract the diver by swimming back and forth toward the bottom of the screen.

The diver loses a life if he is captured by the shark or the octopus's tentacles, or if the air meter runs out. The diver can refill his air meter by touching a long pole which extends from a boat that appears from time to time.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Name_This_Game)*


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
