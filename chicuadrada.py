import numpy as np
from scipy import stats

def prueba_chi_cuadrada(datos, intervalos, alpha=0.05):
    n = len(datos)

    frec_observada, bins = np.histogram(datos, bins=intervalos)
    
    frec_esperada = n / intervalos
    
    chi_est, p_val = stats.chisquare(frec_observada, f_exp=[frec_esperada]*intervalos)
    
    gl = intervalos - 1
    valor_critico = stats.chi2.ppf(1 - alpha, gl)

    print(f"Estadístico Chi-cuadrada: {chi_est:.4f}")
    print(f"Valor Crítico (Tablas): {valor_critico:.4f}")
    print(f"P-valor: {p_val:.4f}")

    if chi_est <= valor_critico:
        print("RESULTADO: H0 (Hipótesis Nula) ACEPTADA")
        print("Los datos siguen la distribución (son uniformes).")
    else:
        print("RESULTADO: H1 (Hipótesis Alternativa) RECHAZADA")
        print("Los datos NO siguen la distribución.")

mis_datos = np.random.rand(100) 
prueba_chi_cuadrada(mis_datos, intervalos=10)