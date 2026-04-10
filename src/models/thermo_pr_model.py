# EOS cúbica (Peng–Robinson (PR)) onde Z é diferente de 1 (aproximação)

from thermo import ChemicalConstantsPackage
from thermo import PRMIX
from thermo import CEOSGas

# Definindo o fluido
fluids = ['hydrogen']

# Constantes críticas e propriedades
constants, correlations = ChemicalConstantsPackage.from_IDs(fluids)

# Criando modelo Peng-Robinson
eos_kwargs = {  # keyword arguments (argumentos nomeados)
    "Tcs": constants.Tcs,
    "Pcs": constants.Pcs,
    "omegas": constants.omegas  # acentric factor
}

# Modelo gás com PR
gas = CEOSGas(PRMIX, eos_kwargs=eos_kwargs)  # CEOSGas resolve a equação de estado


def calculate_Z(P, T):
    """
    Calcula Z usando Peng-Robinson
    """
    gas.T = T
    gas.P = P
    return float(gas.Z())


def calculate_density(P, T):
    """
    Calcula densidade via Z
    """
    R = 4124  # J/kg.K (hidrogênio)

    Z = calculate_Z(P, T)

    rho = P / (Z * R * T)

    return rho