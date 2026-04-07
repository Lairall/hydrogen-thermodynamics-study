from CoolProp.CoolProp import PropsSI
from src.coolprop_model import compute_Z

Z = PropsSI("Z", "P", 1e5, "T", 300, "Hydrogen")
print(Z)

Z = compute_Z(1e5, 300)
print(Z)