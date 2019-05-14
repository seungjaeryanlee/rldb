---
layout: page
title: Atari Seaquest Environment
permalink: /envs/gym/atari/seaquest/

redirect_from:
 - /envs/gym/atari-2600/seaquest/
 - /env/gym/atari/seaquest/
 - /env/gym/atari-2600/seaquest/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/seaquest.mp4' | absolute_url }}" type="video/mp4">
</video>

Seaquest is an underwater shooter in which the player controls a submarine. Enemies include sharks and submarines. The player must ward off the enemies while trying to rescue divers swimming through the water. The sub can hold up to eight divers at a time. Each time the player resurfaces, all rescued divers are emptied out in exchange for points. To add to the challenge, the submarine has a limited amount of oxygen. The player must surface often in order to replenish the oxygen, but if the player resurfaces without any rescued divers, they will lose a life. If the player resurfaces with the maximum amount of divers, they will gain bonus points for the sub's remaining oxygen. Each time the player surfaces, the game's difficulty increases; enemies increase in number and speed. Eventually an enemy sub begins patrolling the surface, leaving the player without a safe haven.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Seaquest_%28video_game%29)*


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
