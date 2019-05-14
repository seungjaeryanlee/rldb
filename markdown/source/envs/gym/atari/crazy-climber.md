---
layout: page
title: Atari Crazy Climber Environment
permalink: /envs/gym/atari/crazy-climber/

redirect_from:
 - /envs/gym/atari-2600/crazy-climber/
 - /env/gym/atari/crazy-climber/
 - /env/gym/atari-2600/crazy-climber/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/crazy-climber.mp4' | absolute_url }}" type="video/mp4">
</video>

In Crazy Climber the player assumes the role of a person attempting to climb to the top of four skyscrapers. The climber is controlled via two joysticks.. There are a number of obstacles and dangers to avoid including:

 * Windows that open and close (the most common danger).
 * Bald-headed residents (a.k.a. Mad Doctors), who throw objects such as flower pots, buckets of water and fruit in an effort to knock the climber off the building (with larger objects appearing by more aggressive Mad Doctors in later levels).
 * A giant condor, who drops eggs and excrement aimed at the climber (two at a time in the early stages, four in later levels).
 * A giant ape (styled like King Kong), whose punch can prove deadly (he becomes more aggressive in later levels).
 * Falling steel girders and iron dumbbells (more numerous in the later levels).
 * Live wires, which protrude off electric signs.
 * Falling 'Crazy Climber' signs.

Some of these dangers appear at every level of the game; others make appearances only in later stages. Should the climber succumb to any one of these dangers, a new climber takes his place at the exact point where he fell; the last major danger is eliminated.

One ally the climber has is a pink "Lucky Balloon"; if he is able to grab it, the climber is transported up 8 stories to a window. The window onto which it drops the climber may be about to close. If the window that the climber is dropped onto is fully closed, the balloon pauses there until the window opens up again. The player does not actually earn bonus points for catching the balloon, but he is awarded the normal 'step value' for each of the eight floors that he passes while holding the balloon.

If the climber is able to ascend to the top of a skyscraper and grabs the runner of a waiting helicopter, he earns a bonus and is transported to another skyscraper, which presents more dangers than the past. The helicopter would only wait about 30 seconds, then fly off.

If the player completes all four skyscrapers, he is taken back to the first skyscraper and the game restarts from the beginning, but the player keeps his score.

The difficulty level of any game was modified to take into account the skill of previous players. Hence if a player pushed the high score up to say 250,000 (needed a really good player), any novice player following would get thoroughly wiped out for several games due to the increased difficulty level, and would have to play until it dropped back down.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Crazy_Climber)*


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
