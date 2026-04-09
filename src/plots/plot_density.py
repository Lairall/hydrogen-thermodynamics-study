import numpy as np
import matplotlib.pyplot as plt
import os


def plot_density_vs_pressure(model_function, T, model_name):
    """
    Gráfico densidade vs pressão (T fixa)
    """

    os.makedirs("figures", exist_ok=True)

    pressures = np.linspace(1e5, 2e7, 50)
    densities = []

    for P in pressures:
        rho = model_function(P, T)
        densities.append(rho)

    plt.figure()
    plt.plot(pressures, densities)

    plt.xlabel("Pressão (Pa)")
    plt.ylabel("Densidade (kg/m³)")
    plt.title(f"Densidade vs Pressão - {model_name}")

    plt.grid()

    filename = f"figures/density_vs_P_{model_name}.png"
    plt.savefig(filename, dpi=300)

    plt.close()

def plot_density_vs_temperature(model_function, P, model_name):
    """
    Gráfico densidade vs temperatura (P fixa)
    """

    os.makedirs("figures", exist_ok=True)

    temperatures = np.linspace(200, 500, 50)
    densities = []

    for T in temperatures:
        rho = model_function(P, T)
        densities.append(rho)

    plt.figure()
    plt.plot(temperatures, densities)

    plt.xlabel("Temperatura (K)")
    plt.ylabel("Densidade (kg/m³)")
    plt.title(f"Densidade vs Temperatura - {model_name}")

    plt.grid()

    filename = f"figures/density_vs_T_{model_name}.png"
    plt.savefig(filename, dpi=300)

    plt.close()    


def plot_density_vs_Z(model_density, model_Z, T, model_name):
    """
    Gráfico densidade vs Z (variando pressão)
    """

    os.makedirs("figures", exist_ok=True)

    pressures = np.linspace(1e5, 2e7, 100)

    densities = []
    Z_values = []

    for P in pressures:
        rho = model_density(P, T)
        Z = model_Z(P, T)

        densities.append(rho)
        Z_values.append(Z)
        print(P, Z, rho)

    plt.figure()
    plt.plot(Z_values, densities)

    plt.xlabel("Fator de compressibilidade (Z)")
    plt.ylabel("Densidade (kg/m³)")
    plt.title(f"Densidade vs Z - {model_name}")

    plt.grid()

    filename = f"figures/density_vs_Z_{model_name}.png"
    plt.savefig(filename, dpi=300)

    plt.close()    