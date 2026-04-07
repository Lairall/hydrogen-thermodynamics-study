from CoolProp.CoolProp import PropsSI

fluid = "Hydrogen"

def compute_Z(P, T):
    return PropsSI("Z", "P", P, "T", T, fluid)

def compute_density(P, T):
    return PropsSI("D", "P", P, "T", T, fluid)

def compute_viscosity(P, T):
    return PropsSI("V", "P", P, "T", T, fluid)