print("=== Pathway Debate Mastery ===")

import alchemy.transmutation.basic
print("Testing Absolute Imports (from basic.py):\n")
print(f"lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}\n")

""" import alchemy.transmutation.advanced """
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
print("Testing Relative Imports (from advanced.py):")
print(f"philosopher_stone(): {philosophers_stone()}")
print(f"elixir_of_life(): {elixir_of_life()}\n")

import alchemy.transmutation
print("Testing Packages Access:")
print(f"alchemy.transmutation.lead_to_gold(): "
      f" {alchemy.transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone(): "
      f"{alchemy.transmutation.philosophers_stone()}\n")

print("Both pathways work! Absolute: clear, Relative: concise")
