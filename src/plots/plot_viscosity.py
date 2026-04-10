import numpy as np
import matplotlib.pyplot as plt
import os


def plot_viscosity_vs_pressure(model_function, T, model_name):
    """
    μ vs P (T fixa)
    """

    os.makedirs("figures", exist_ok=True)

    pressures = np.linspace(1e5, 2e7, 50)
    viscosities = []

    for P in pressures:
        mu = model_function(P, T)
        viscosities.append(mu)

    plt.figure()
    plt.plot(pressures, viscosities)

    plt.xlabel("Pressão (Pa)")
    plt.ylabel("Viscosidade (Pa·s)")
    plt.title(f"Viscosidade vs Pressão - {model_name}")

    plt.grid()

    filename = f"figures/viscosity/viscosity_vs_P_{model_name}.png"
    plt.savefig(filename, dpi=300)

    plt.close()


def plot_viscosity_vs_temperature(model_function, P, model_name):
    """
    μ vs T (P fixa)
    """

    os.makedirs("figures", exist_ok=True)

    temperatures = np.linspace(200, 500, 50)
    viscosities = []

    for T in temperatures:
        mu = model_function(P, T)
        viscosities.append(mu)

    plt.figure()
    plt.plot(temperatures, viscosities)

    plt.xlabel("Temperatura (K)")
    plt.ylabel("Viscosidade (Pa·s)")
    plt.title(f"Viscosidade vs Temperatura - {model_name}")

    plt.grid()

    filename = f"figures/viscosity/viscosity_vs_T_{model_name}.png"
    plt.savefig(filename, dpi=300)

    plt.close()