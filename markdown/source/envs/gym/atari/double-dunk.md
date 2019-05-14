---
layout: page
title: Atari Double Dunk Environment
permalink: /envs/gym/atari/double-dunk/

redirect_from:
 - /envs/gym/atari-2600/double-dunk/
 - /env/gym/atari/double-dunk/
 - /env/gym/atari-2600/double-dunk/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/double-dunk.mp4' | absolute_url }}" type="video/mp4">
</video>

Double Dunk is a simulation of two-on-two, half-court basketball. Teams have two on-screen characters, a shorter "outside" man and a taller "inside" man. In a single-player game, the player controls the on-screen character closest to the ball, either the one holding the ball (on offense) or the one guarding the opponent with the ball (on defense). In two-player games, each player may control one of the two teams as in a one-player game, or both players may play on the same team against a computer-controlled opponent. At the start of each possession, both offense and defense select from a number of plays (such as the "pick and roll" on offense), then attempt to score or regain possession of the ball by intercepting or stealing it from the offense.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Double_Dunk)*


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
