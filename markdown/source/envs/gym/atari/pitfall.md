---
layout: page
title: Atari Pit Fall Environment
permalink: /envs/gym/atari/pitfall/

redirect_from:
 - /envs/gym/atari-2600/pit-fall/
 - /env/gym/atari/pit-fall/
 - /env/gym/atari-2600/pit-fall/
 - /envs/gym/atari/pit-fall/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/pitfall.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls the character (Pitfall Harry) through a maze-like jungle in an attempt to recover 32 treasures in a 20-minute time period. Along the way, players must maneuver through numerous hazards, including pits, quicksand, rolling logs, fire, rattlesnakes, scorpions, and crocodiles. Harry may jump over or otherwise avoid these obstacles by climbing, running, or swinging on vines. Treasure includes bags of money, gold and silver bars, and diamond rings, which range in value from 2000 to 5000 points in 1000 point increments. There are eight of each treasure type, with 32 in total. A perfect score of 114,000 is achieved by claiming all 32 treasures without losing any points. Points are deducted by either falling in a hole (100 points) or touching logs; point loss depends on how long contact is made with the log. Under the jungle there is a tunnel which Harry can access through ladders found at various points. Traveling though the tunnel moves forward three screens at a time, which is necessary in order to collect all the treasures within the time limit. However, the tunnels are filled with dead-ends blocked by brick walls, forcing the player to return to the surface at one of the ladders, and try to find a way around again, thus wasting time. The tunnels also contain scorpions. The player loses a life if Harry comes in contact with any obstacle (except logs) or falls into a tar pit, quicksand, waterhole, or mouth of a crocodile. The game ends when either all 32 treasures have been collected, all three lives have been lost, or the time has run out.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Pitfall!)*


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
