---
layout: page
title: Atari Zaxxon Environment
permalink: /envs/gym/atari/zaxxon/

redirect_from:
 - /envs/gym/atari-2600/zaxxon/
 - /env/gym/atari/zaxxon/
 - /env/gym/atari-2600/zaxxon/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/zaxxon.mp4' | absolute_url }}" type="video/mp4">
</video>

he object of the game is to hit as many targets as possible without being shot down or running out of fuel—which can be replenished, paradoxically, by blowing up fuel drums.[19]

There are two fortresses to fly through, with an outer space segment between them. At the end of the second fortress is a boss in the form of the Zaxxon robot.

The player's ship casts a shadow to indicate its height.[20] An altimeter is also displayed; in space there is nothing for the ship to cast a shadow on.[21] The walls at the entrance and exit of each fortress have openings that the ship must be at the right altitude to pass through. Within each fortress are additional walls that the ship's shadow and altimeter aid in flying over successfully.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Zaxxon)*


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
