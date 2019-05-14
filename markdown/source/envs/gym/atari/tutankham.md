---
layout: page
title: Atari Tutankham Environment
permalink: /envs/gym/atari/tutankham/

redirect_from:
 - /envs/gym/atari-2600/tutankham/
 - /env/gym/atari/tutankham/
 - /env/gym/atari-2600/tutankham/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/tutankham.mp4' | absolute_url }}" type="video/mp4">
</video>

Taking on the role of an explorer grave robbing Tutankhamun's tomb while exploring dozens of rooms, the player is chased by creatures such as asps, vultures, parrots, bats, dragons, and even curses, all that kill the player on contact. The explorer can fight back by firing lasers at the creatures, but he can only cover the left and right directions. The player is also endowed with a single screen-clearing "flash bomb" per room or life. Finally, each room has warp zones that teleport the player around the room, which enemies cannot use.

To progress, the player collects keys open locked doors throughout the rooms, searching for the large exit door. Optional treasures can be picked-up for bonus points. Each room has a timer; when it reaches zero the explorer can no longer fire lasers, and once a room is cleared the remaining time is converted to bonus points.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Tutankham)*


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
