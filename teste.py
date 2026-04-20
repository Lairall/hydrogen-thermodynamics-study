from thermopack.cubic import PengRobinson

eos = PengRobinson("H2")

T = 300
P = 1e5

z = eos.zfac(T, P, [1.0], phase=1)          # fase 1 = vapor, 0 = líquido
# print(z)
