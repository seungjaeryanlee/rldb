---
layout: page
title: Atari Chopper Command Environment
permalink: /envs/gym/atari/chopper-command/

redirect_from:
 - /envs/gym/atari-2600/chopper-command/
 - /env/gym/atari/chopper-command/
 - /env/gym/atari-2600/chopper-command/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/chopper-command.mp4' | absolute_url }}" type="video/mp4">
</video>

In Chopper Command the player controls a military helicopter in a desert scenario protecting a convoy of trucks. The goal is to destroy all enemy fighter jets and helicopters that attack the player's helicopter and the friendly trucks traveling below, ending the current wave. The game ends when the player loses all of his or her lives or reaches 999,999 points. A radar, called a Long Range Scanner in the instruction manual, shows all enemies, including those not visible on the main screen.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Chopper_Command)*


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
