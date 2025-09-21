
# Examples

Example list of spells that could be constructed.

* fireball (target x1 large bolt)
* firebolt (target xN small bolts)
* firewall (draw line)
* fireshield (draw circle + defense?)
* fire drawing (freehand)
* AOE fire (target area, slow DoT)
* fire trap (AoE fire on proximity trigger)
* explosion (target area, fast DoT)
* explosion trap (AoE explosion on proximity trigger)
* fire enchantment (eg sword +X fire damage)
* explosion enchantment (eg sword mini explosion on impact)
* warmth enchantment (eg sword warms user when equipped)
* fire resistance (self absorb enchantment)
* fire resistance enchantment (item)
* cold resistance ('warmth' on self/other)
* cold resistance ('warmth' enchantment on item)
* fire absorption AoE (inverse AoE fire)
* fire absorption line (inverse firewall)
* fire dispell (cancel fire)
* melt (warmth, target ice?)

# Fire

Fire is used here as an example effect that a spell can be constructed around, but the same pattern of symbols could be applied to any number of effects.

## Effect

This is the central spell component and mostly aligns with RPG-style "elements" like fire, ice, arcane, life, death etc. There will be a unique symbol for each effect that can be used to build a spell.

## Intensity

Intensity is a measure of the notional "direction" of the effects power, ranging from hard to embody. At the hard end of the scale, the effect is generative and damaging, while at the embody end of the scale, the effect is protective and negating.

### 1.0 (Hard)

example: *Target is burned*

Applies the effect.

### 0.5 (Soft)

example: *Target is warmed*

Applies moderate effect.

### 0.0 (Cancel)

example: *Target stops burning*

Negates an effect.

### -0.5 (Absorb)

example: *Target absorbs fire*

Draws the effect into self/target.

### -1.0 (Embody)

example: *Target becomes fire*

Transmutes self/target into the effect. 

## Target

The target of the spell is what the effect will be *applied to*. Multiple targets can be added to a spell to construct arbitrarily complex patterns of application.

### Entity

An entity is an object in the game. The caster themselves, another player, an object, item, armor, tree, etc.

### Region

A region is a pattern drawn/selected by the caster. Points, lines, circles, squares, area etc.

### Effect

An effect is a magical or environmental effect in the game world. Traps, in-flight fireballs, enchantments, summoned ice, etc.

## Modifiers

### Speed (default: max)

The application speed of the spell. For an effect like fire, this might be the difference between a slow warm-over-time spell and an explosion.

* Max (0)
* Other (>0)

### Delay (default: none)

How long to wait before the effect of the spell is applied. If the delay is set to "Trigger", then the spell will only go into effect under particular conditions.

* Trigger (-1)
* None (0)
* Value (>0)

**If delay is set to "Trigger", then Distance and Filter modifiers are evaluated**

### Duration (default: instant)

This is how long the spell will last. Changing this modifier from instant to any larger time will turn a fireball into a beam, or a burst of fire on a sword (intensity=-1) into an enchantment.

* Instant (0)
* Other (>0)

### Count (default: single)

The number of iterations of the spell to cast. Each iteration is treated as a totally self contained cast, and might require re-selecting targets. With a select type of "Random" or "Closest" this might create a pray-and-spray style spell.

* Single (1)
* Other (>1)

### Select (default: manual)

Changes how the caster selects targets. The default is manual selection at cast-time. Other options might be "Random" "Closest" etc.

* Manual
* Random
* Closest

### Disposition (default: any)

**Only applies to entity targets**

Filters valid targets for selection so that any/friendly/hostile/neutral targets are affected.

* Any
* Friend
* Hostile
* Neutral

### Distance (default: 0)

**Only evaluated if Delay=Trigger**

The distance at which the effect is triggered, between 0 and a max. Entities that come within this distance who fit the Filter will cause the effect to be applied.

### Filter (default: hostile)

**Only evaluated if Delay=Trigger**

The type of entity that may trigger the effect. Entities that fit this filter that come within the Distance will cause the effect to be applied.

* Hostile
* Friendly
* Neutral