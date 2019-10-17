class juros_simples:
    def calcular_fv(pv, i, t):
        return float(pv*(1+i*t))
    
    def calcular_pv(fv, i, t):
        return float(fv/(1+i*t))

    def calcular_i(pv, fv, t):
        return 

    def calcular_t(pv, fv, i):
        return 

print(juros_simples.calcular_fv(1000, 10, 2))
print(juros_simples.calcular_pv(21000, 10, 2))
