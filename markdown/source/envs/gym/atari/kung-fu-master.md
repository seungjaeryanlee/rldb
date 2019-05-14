---
layout: page
title: Atari Kung-Fu Master Environment
permalink: /envs/gym/atari/kung-fu-master/

redirect_from:
 - /envs/gym/atari-2600/kung-fu-master/
 - /env/gym/atari/kung-fu-master/
 - /env/gym/atari-2600/kung-fu-master/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/kung-fu-master.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls Thomas with a four-way joystick and two attack buttons for punching and kick. Unlike more conventional side-scrolling games, the joystick is used not only to crouch, but also to jump. Punches and kicks can be performed from a standing, crouching or jumping position. Punches award more points than kicks and do more damage, but their range is shorter.

Underlings encountered by the player include Grippers, who can grab Thomas and drain his energy until shaken off; Knife Throwers, who can throw at two different heights and must be hit twice; and Tom Toms, short fighters who can either grab Thomas or somersault to strike his head when he is crouching. On even-numbered floors, the player must also deal with falling balls and pots, snakes, poisonous moths, fire-breathing dragons, and exploding confetti balls.

The temple has five floors, each ending with a different boss who are "sons of the devil" which are the Stick Fighter of the first floor, the Boomerang Fighter of the second floor, the Strongman of the third floor, the Black Magician of the fourth floor and Mr. X of the final floor who must all be defeated before Thomas can climb the stairs to the next floor so he can rescue Silvia. Thomas must complete each floor within a fixed time; if time runs out or his energy is completely drained, he loses one life and must replay the entire floor. If a boss defeats Thomas, the boss laughs. Although there are five bosses, the game only uses two different synthesized laughs. (The NES version uses a third, high-pitched synthesized laugh for the Black Magician, the fourth boss.)

Once the player has completed all five floors, the game restarts with a more demanding version of the Devil's Temple, although the essential details remain unchanged. A visual indication of the current house is displayed on the screen. For each series of five completed floors, a dragon symbol appears in the upper-right corner of the screen. After three dragons have been added, the dragon symbols blink.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Kung-Fu_Master_(video_game))*


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
