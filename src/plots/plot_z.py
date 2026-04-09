import numpy as np
import matplotlib.pyplot as plt
import os


def plot_Z_vs_pressure(model_function, T, model_name):
    """
    Gráfico Z vs Pressão (T fixa)
    """
    os.makedirs("figures", exist_ok=True)

    pressures = np.linspace(1e5, 2e7, 50)
    Z_values = []

    for P in pressures:
        Z = model_function(P, T)
        Z_values.append(Z)

    plt.figure()
    plt.plot(pressures, Z_values)

    plt.xlabel("Pressão (Pa)")
    plt.ylabel("Z")
    plt.title(f"Z vs Pressão - {model_name}")

    plt.grid()

    filename = f"figures/Z_vs_P_{model_name}.png"
    plt.savefig(filename, dpi=300)

    plt.close()


def plot_Z_vs_temperature(model_function, P, model_name):
    """
    Gráfico Z vs Temperatura (P fixa)
    """
    os.makedirs("figures", exist_ok=True)

    temperatures = np.linspace(200, 500, 50)
    Z_values = []

    for T in temperatures:
        Z = model_function(P, T)
        Z_values.append(Z)

    plt.figure()
    plt.plot(temperatures, Z_values)

    plt.xlabel("Temperatura (K)")
    plt.ylabel("Z")
    plt.title(f"Z vs Temperatura - {model_name}")

    plt.grid()

    filename = f"figures/Z_vs_T_{model_name}.png"
    plt.savefig(filename, dpi=300)

    plt.close()