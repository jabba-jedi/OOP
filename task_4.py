#!/usr/bin/env python3

class Kg:
  @staticmethod
  def tonne_to_kg(weight_in_kg: float) -> float:
    """Takes the weight in metric tonnes (float), returns
    weight in kilograms (float)"""
    return weight_in_kg * 1000

  def quintal_to_kg(weight_in_kg: float) -> float:
    """Takes the weight in quintals (float), returns
    weight in kilograms (float)"""
    return weight_in_kg * 100

  def pound_to_kg(weight_in_kg: float) -> float:
    """Takes the weight in pounds (float), returns
    weight in kilograms (float)"""
    return weight_in_kg * 0.45359237

  def pood_to_kg(weight_in_kg: float) -> float:
    """Takes the weight in poods (float), returns
    weight in kilograms (float)"""
    return weight_in_kg * 16.38

print("Tonne(s): " , Kg.tonne_to_kg(125))
print("Quintal(s): " , Kg.quintal_to_kg(125))
print("Pound(s): " , Kg.pound_to_kg(125))
print("Pood(s): " , Kg.pood_to_kg(125))