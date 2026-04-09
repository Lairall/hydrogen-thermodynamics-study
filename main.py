from src.models.coolprop_model import calculate_Z, calculate_density, calculate_viscosity
from src.plots.plot_z import plot_Z_vs_pressure, plot_Z_vs_temperature
from src.plots.plot_density import plot_density_vs_pressure, plot_density_vs_temperature, plot_density_vs_Z 
from src.plots.plot_viscosity import plot_viscosity_vs_pressure, plot_viscosity_vs_temperature

# parâmetros
T = 300  # temperatura em K
P = 10e7  # 100 bar = 10 MPa = 10e7 Pa


# ========
# plots:
# ========

# Z vs Pressão (T fixa)
plot_Z_vs_pressure(calculate_Z, 300, "Hydrogen - CoolProp")  
# plot_Z_vs_pressure(calculate_Z_thermo, 300, "Hydrogen - Thermo")
# plot_Z_vs_pressure(calculate_Z_tp, 300, "Hydrogen - ThermoPack")

# Z vs Temperatura (P fixa)
plot_Z_vs_temperature(calculate_Z, P, "Hydrogen - CoolProp")

# densidade vs pressão (T fixa)
plot_density_vs_pressure(calculate_density, T, "Hydrogen - CoolProp")

# densidade vs temperatura (P fixa)
plot_density_vs_temperature(calculate_density, P, "Hydrogen - CoolProp")

# densidade vs Z (T fixa)
plot_density_vs_Z(calculate_density, calculate_Z, T, "Hydrogen - CoolProp")

# viscosidade vs pressão (T fixa)
plot_viscosity_vs_pressure(calculate_viscosity, T, "Hydrogen - CoolProp")

# viscosidade vs temperatura (P fixa)
plot_viscosity_vs_temperature(calculate_viscosity, P, "Hydrogen - CoolProp")