---
layout: page
title: Atari Phoenix Environment
permalink: /envs/gym/atari/phoenix/

redirect_from:
 - /envs/gym/atari-2600/phoenix/
 - /env/gym/atari/phoenix/
 - /env/gym/atari-2600/phoenix/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/phoenix.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls a spaceship that moves horizontally at the bottom of the screen, firing upward. Enemies, typically one of two types of birds, appear on the screen above the player's ship, shooting at it and periodically diving towards it in an attempt to crash into it. The ship is equipped with a shield that can be used to zap any of the alien creatures that attempt to crash into the spaceship. The player cannot move while the shield is active and must wait approximately five seconds before using it again.

The player starts with three or six lives, depending on the settings.

Each level has five separate rounds. The player must complete a round to advance to the next.

Rounds 1 and 2 – The player must destroy a formation of alien birds. While in formation, some of the birds fly down kamikaze style, in an attempt to destroy the player's spaceship by crashing into it. Hitting a bird flying diagonally awards a bonus score. The birds are yellow in round 1, pink in round 2. The player's spaceship is given rapid fire for round 2, where the birds fly somewhat more unpredictably.
Rounds 3 and 4 – Flying eggs float on the screen and seconds later hatch, revealing larger alien birds, resembling phoenices, which swoop down at the player's spaceship. The only way to fully destroy one of these birds is by hitting it in its belly; shooting one of its wings merely destroys that wing, and if both wings are destroyed, they will regenerate. From time to time the birds may also revert to the egg form for a brief period. The birds are blue in round 3, pink in round 4.
Round 5 – The player is pitted against the mothership, which is controlled by an alien creature sitting in its center. To complete this round, the player must create a hole in the conveyor belt-type shield to get a clear shot at the alien. Hitting the alien with a single shot ends the level. The mothership fires missiles at the player's ship, moves slowly down towards it, and has alien birds (from rounds 1 and 2) protecting it. Defeating all of the birds will produce a new wave.
The game continues with increasing speed and unpredictability of the bird and phoenix flights.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Phoenix_%28video_game%29)*


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
