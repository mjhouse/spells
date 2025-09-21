
# 1. have some number of basic components- fire, ice, water, force, earth etc.
# 2. have some number of modifiers- direction, strength, target etc.
# 3. combine them to create unique spells

from dataclasses import dataclass
from enum import Enum, unique

@unique
class ElementKind(Enum):
    Earth = 'earth'
    Fire = 'fire'
    Ice = 'ice'
    Water = 'water'
    Force = 'force'
    Wind = 'wind'

@dataclass
class Interaction:
    pass

@dataclass
class Element:
    kind: ElementKind
    interactions: list[Interaction]

class Modifier:
    pass

class Builder:
    pass

