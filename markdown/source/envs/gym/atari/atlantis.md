---
layout: page
title: Atari Atlantis Environment
permalink: /envs/gym/atari/atlantis/

redirect_from:
 - /envs/gym/atari-2600/atlantis/
 - /env/gym/atari/atlantis/
 - /env/gym/atari-2600/atlantis/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/atlantis.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls the last defenses of the City of Atlantis against the Gorgon invaders. The city has seven bases, which are vulnerable to attack. Three of these have firepower capabilities to destroy the Gorgon ships before they manage to fire death rays at one of the settlements. The gun bases have fixed cannons; the center base fires straight up, while the far left and far right bases fire diagonally upwards across the screen. The center cannon also creates a shield that protects the settlements from the death rays, so once the center cannon is destroyed, the remaining settlements become vulnerable to attack. The enemy ships pass back and forth from left to right four times before they enter firing range, giving an ample opportunity to blow them away. Lost bases can be regained by destroying enough Gorgon ships.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Atlantis_%28video_game%29)*


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
