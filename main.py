from src.models.coolprop_model import calculate_Z, calculate_density, calculate_viscosity

from src.plots.plot_z import plot_Z_vs_pressure, plot_Z_vs_temperature
from src.plots.plot_density import plot_density_vs_pressure, plot_density_vs_temperature, plot_density_vs_Z 
from src.plots.plot_viscosity import plot_viscosity_vs_pressure, plot_viscosity_vs_temperature

from src.models.thermo_model import calculate_density as density_thermo
from src.models.thermo_model import calculate_Z as Z_thermo
from src.models.thermo_model import calculate_viscosity as mu_thermo


from src.models.thermo_model import calculate_density as density_th
from src.models.coolprop_model import calculate_density as density_cp

from src.models.thermo_pr_model import calculate_Z as Z_PR
from src.models.thermo_pr_model import calculate_density as rho_PR

# parâmetros
T = 300  # temperatura em K
P = 10e7  # 100 bar = 10 MPa = 10e7 Pa


rho_cp = density_cp(P, T)
rho_th = density_th(P, T)

print("=== Comparação de densidade ===")
print("CoolProp:", rho_cp)
print("Thermo:", rho_th)

# ========
# plots:
# ========

# Z vs Pressão (T fixa)
plot_Z_vs_pressure(calculate_Z, 300, "Hydrogen - CoolProp")  
plot_Z_vs_pressure(Z_thermo, T, "Hydrogen - Thermo")
plot_Z_vs_pressure(Z_PR, T, "Hydrogen - Thermo_PR")

# Z vs Temperatura (P fixa)
plot_Z_vs_temperature(calculate_Z, P, "Hydrogen - CoolProp")
plot_Z_vs_temperature(Z_thermo, P, "Hydrogen - Thermo")
plot_Z_vs_temperature(Z_PR, P, "Hydrogen - Thermo_PR")


# densidade vs pressão (T fixa)
plot_density_vs_pressure(calculate_density, T, "Hydrogen - CoolProp")
plot_density_vs_pressure(density_thermo, T, "Hydrogen - Thermo")
plot_density_vs_pressure(rho_PR, T, "Hydrogen - Thermo_PR")


# densidade vs temperatura (P fixa)
plot_density_vs_temperature(calculate_density, P, "Hydrogen - CoolProp")
plot_density_vs_temperature(density_thermo, P, "Hydrogen - Thermo")
plot_density_vs_temperature(rho_PR, P, "Hydrogen - Thermo_PR")


# densidade vs Z (T fixa)
plot_density_vs_Z(calculate_density, calculate_Z, T, "Hydrogen - CoolProp")
plot_density_vs_Z(density_thermo, Z_thermo, T, "Hydrogen - Thermo")
plot_density_vs_Z(rho_PR, Z_PR, T, "Hydrogen - Thermo_PR")


# viscosidade vs pressão (T fixa)
plot_viscosity_vs_pressure(calculate_viscosity, T, "Hydrogen - CoolProp")
plot_viscosity_vs_pressure(mu_thermo, T, "Hydrogen - Thermo")


# viscosidade vs temperatura (P fixa)
plot_viscosity_vs_temperature(calculate_viscosity, P, "Hydrogen - CoolProp")
plot_viscosity_vs_temperature(mu_thermo, P, "Hydrogen - Thermo")

