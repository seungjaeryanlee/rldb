---
layout: page
title: Atari Yars Revenge Environment
permalink: /envs/gym/atari/yars-revenge/

redirect_from:
 - /envs/gym/atari-2600/yars-revenge/
 - /env/gym/atari/yars-revenge/
 - /env/gym/atari-2600/yars-revenge/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/yars-revenge.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls an insect-like creature called a Yar who must nibble or shoot through a barrier in order to fire his Zorlon Cannon into the breach. The objective is to destroy the evil Qotile, which exists on the other side of the barrier. The Qotile can attack the Yar, even if the barrier is undamaged, by turning into the Swirl and shooting across the screen. In early levels the player is warned before the Swirl is fired, and he can retreat to a safe distance to dodge the attack. The Yar can hide from a pursuing destroyer missile within a "neutral zone" in the middle of the screen, but the Yar cannot shoot while in the zone. The Swirl can kill the Yar anywhere, even inside the Neutral Zone.

To destroy the Qotile or the Swirl, the player has to either touch the Qotile or eat a piece of the shield to activate the Zorlon Cannon, aim the cannon by leading the with the Qotile or Swirl, then fire the cannon and fly the Yar out of the path of the cannon's shot. If the weapon finds its mark, the level ends. If the cannon blast hits a piece of the shield or misses, it is expended. The cannon itself is dangerous to the player, for once it is activated, the fire button launches it instead of firing the Yar's usual shots, and as the cannon tracks the Yar's vertical position, players effectively use the Yar itself as a target and therefore must immediately maneuver to avoid being hit by their own shot. The cannon shot can also rebound off the shield in later levels.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Yars%27_Revenge)*


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
