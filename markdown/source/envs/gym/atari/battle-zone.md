---
layout: page
title: Atari Battle Zone Environment
permalink: /envs/gym/atari/battle-zone/

redirect_from:
 - /envs/gym/atari-2600/battle-zone/
 - /env/gym/atari/battle-zone/
 - /env/gym/atari-2600/battle-zone/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/battle-zone.mp4' | absolute_url }}" type="video/mp4">
</video>

Gameplay is on a flat plane with a mountainous horizon featuring an erupting volcano, distant crescent moon, and various geometric solids (in vector outline) like pyramids and blocks. The player views the screen, which includes an overhead radar view, to find and destroy the rather slow tanks, or the faster-moving supertanks. Saucer-shaped UFOs and guided missiles occasionally appear for a bonus score. The saucers differ from the tanks in that they do not fire upon the player and do not appear on radar. The player can hide behind the solids or, once fired upon, maneuver in rapid turns to buy time with which to fire.

The geometric solid obstacles are indestructible, and can block the movement of a player's tank. However, they are also useful as shields as they block enemy fire as well.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Battlezone_%281980_video_game%29)*

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
