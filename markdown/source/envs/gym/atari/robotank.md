---
layout: page
title: Atari Robotank Environment
permalink: /envs/gym/atari/robotank/

redirect_from:
 - /envs/gym/atari-2600/robotank/
 - /env/gym/atari/robotank/
 - /env/gym/atari-2600/robotank/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/robotank.mp4' | absolute_url }}" type="video/mp4">
</video>

The player remotely controls a robot tank in 2019. The mission is to locate enemy rebel tanks rampaging across the countryside with radar, then destroy them with a cannon to stop them from reaching downtown Santa Clara, California, United States. The enemy is organized into squadrons of 12 tanks each. By defeating an enemy squadron, the player earns an additional reserve tank to the initial three, to a maximum of 12. The game ends when all of a player's tanks are destroyed.

As the player's tank is damaged, firepower and/or visual display capabilities are irreparably worsened. Enough damage will eventually destroy a tank. Combat can take place at any time of day or night (displayed on-screen), possibly with rain, snow, or fog (announced in a weather report each morning), which adds additional challenge in tracking enemy combatants by radar alone.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Robot_Tank)*


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
