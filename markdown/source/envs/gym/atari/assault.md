---
layout: page
title: Atari Assault Environment
permalink: /envs/gym/atari/assault/

redirect_from:
 - /envs/gym/atari-2600/assault/
 - /env/gym/atari/assault/
 - /env/gym/atari-2600/assault/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/assault.mp4' | absolute_url }}" type="video/mp4">
</video>

The player is presented with an alien mother ship, which continually deploys three smaller ships during play.[2] The mother ship and the smaller vessels shoot at a weapon the player is in command of, and the player's aim is to eliminate the opposition while preventing the weapon from receiving enough fire to destroy it.[2] The player uses a joystick to operate the game, and only one player at a time can play.[1]

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Assault_(1983_video_game))*


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
