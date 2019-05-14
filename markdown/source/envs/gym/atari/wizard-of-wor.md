---
layout: page
title: Atari Wizard of Wor Environment
permalink: /envs/gym/atari/wizard-of-wor/

redirect_from:
 - /envs/gym/atari-2600/wizard-of-wor/
 - /env/gym/atari/wizard-of-wor/
 - /env/gym/atari-2600/wizard-of-wor/

nav:
 - name: Overview
   permalink: '#overview'
 - name: Performances
   permalink: '#performances'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/wizard-of-wor.mp4' | absolute_url }}" type="video/mp4">
</video>

The players' characters, called Worriors, must kill all the monsters by shooting them. Player one has yellow Worriors, on the right, and player two has blue Worriors, on the left. In a two-player game, the players are also able to shoot each other's Worriors, earning bonus points and causing the other player to lose a life. Team-oriented players can successfully advance through the game by standing back-to-back (such as in a corner) and firing at anything that comes at them.

Each dungeon consists of a single-screen rectangular grid with walls and corridors in various formations. The Worriors and the monsters can travel freely through the corridors. Each dungeon has doors at the left and right edges, which connect with each other, making the dungeon wrap around. Whenever a door is traversed by a player or monster, both of them deactivate for a short period, making them impassable. A player who exits the door can pop back through the door immediately when the Worluk or Wizard is in the dungeon. A small radar display indicates the positions of all active monsters.

As long as a player has at least one life in reserve, a backup Worrior is displayed in a small sealed cubbyhole at the corresponding bottom corner of the dungeon. When the current Worrior is killed, the cubbyhole opens and the player has 10 seconds to move the backup into play before automatically being forced in.

The various monsters include the following:

 * Burwor: A blue wolf-type creature.
 * Garwor: A yellow Tyrannosaurus rex-type creature.
 * Thorwor: A red scorpion-like creature.
 * Worluk: An Insectoid-type creature.
 * Wizard of Wor: A blue wizard.
Both Garwors and Thorwors have the ability to turn invisible at times, but will always appear on the radar. All enemies except the Worluk can shoot at the Worriors.

Each dungeon starts filled with six Burwors. In the first dungeon, killing the last Burwor will make a Garwor appear; in the second, the last two Burwors are replaced by Garwors when killed; and so on. From the sixth dungeon on, a Garwor will replace every Burwor when killed. On every screen, killing a Garwor causes a Thorwor to appear. There will never be more than six enemies on the screen at once. From the second dungeon on, after the last Thorwor is killed, a Worluk will appear and try to escape through one of the side doors. The level ends when the Worluk either escapes or is killed; in the latter case, all point values for the next dungeon are doubled.

The Wizard of Wor will appear in or after the second dungeon once the Worluk has either escaped or been killed. After a few seconds the Wizard will disappear and teleport across the dungeon, gradually approaching a Worrior. The Wizard remains in the dungeon until he shoots a Worrior or is killed. He uses a speech synthesizer to taunt the players throughout the game.

Players are referred to as "Worriors" during the first seven levels, then as "Worlords" beyond that point. The "Worlord Dungeons" are more difficult than the earlier levels because they have fewer interior walls.

There are two special dungeons with increased difficulty. Level 4 is "The Arena," with a large open area in its center, and Level 13 is "The Pit," with no interior walls at all. A bonus Worrior is awarded before each of these levels. Every sixth dungeon after Level 13 is another Pit. A player who survives any Pit level without losing a life earns the title of "Worlord Supreme."

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Wizard_of_Wor)*


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
