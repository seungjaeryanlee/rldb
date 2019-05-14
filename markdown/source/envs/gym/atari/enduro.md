---
layout: page
title: Atari Enduro Environment
permalink: /envs/gym/atari/enduro/

redirect_from:
 - /envs/gym/atari-2600/enduro/
 - /env/gym/atari/enduro/
 - /env/gym/atari-2600/enduro/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/enduro.mp4' | absolute_url }}" type="video/mp4">
</video>

nduro consists of maneuvering a race car in the National Enduro, a long-distance endurance race. The object of the race is to pass a certain number of cars each day. Doing so will allow the player to continue racing for the next day. The driver must avoid other racers and pass 200 cars on the first day, and 300 cars with each following day.

As the time in the game passes, visibility changes as well. When it is night in the game the player can only see the oncoming cars' taillights. As the days progress, cars will become more difficult to avoid as well. Weather and time of day are factors in how to play. During the day the player may drive through an icy patch on the road which would limit control of the vehicle, or a patch of fog may reduce visibility.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Enduro_%28video_game%29)*


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
