---
layout: page
title: Atari Freeway Environment
permalink: /envs/gym/atari/freeway/

redirect_from:
 - /envs/gym/atari-2600/freeway/
 - /env/gym/atari/freeway/
 - /env/gym/atari-2600/freeway/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/freeway.mp4' | absolute_url }}" type="video/mp4">
</video>

One or two players control chickens who can be made to run across a ten lane highway filled with traffic in an effort to "get to the other side." Every time a chicken gets across a point is earned for that player. If hit by a car, a chicken is forced back either slightly, or pushed back to the bottom of the screen, depending on what difficulty the switch is set to. The winner of a two player game is the player who has scored the most points in the two minutes, sixteen seconds allotted. The chickens are only allowed to move up or down. A cluck sound is heard when a chicken is struck by a car.

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
