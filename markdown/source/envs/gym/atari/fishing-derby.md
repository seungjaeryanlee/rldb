---
layout: page
title: Atari Fishing Derby Environment
permalink: /envs/gym/atari/fishing-derby/

redirect_from:
 - /envs/gym/atari-2600/fishing-derby/
 - /env/gym/atari/fishing-derby/
 - /env/gym/atari-2600/fishing-derby/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/fishing-derby.mp4' | absolute_url }}" type="video/mp4">
</video>

In Fishing Derby, two fishermen sit on opposite docks over a lake filled with fish (and a shark that passes through). Using the joystick the player is able to move his line left right and up and down in the water. When a fish is hooked, the line slowly comes up to the surface of the water. Pressing the fire button on the joystick reels in the fish faster. However, if both fishermen have fish hooked, only one person can reel theirs in (the one who hooked theirs first). The shark that roams the water will try to eat hooked fish before they surface.

The objective for both fishermen is to reach 99 pounds of fish first. There are six rows of fish; the top two rows have 2 lb. fish, the middle two rows have 4 lb. fish, and the two bottom rows have 6 lb. fish. The more valuable fish sit at the bottom, but they are harder to bring in as they run a higher risk of being eaten by the shark.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Freeway_%28video_game%29)*


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
