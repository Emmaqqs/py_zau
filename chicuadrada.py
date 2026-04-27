import numpy as np
from scipy import stats

def prueba_chi_cuadrada(numeros, k=10, alfa=0.05):
    """
    Calcula la prueba de Chi-cuadrada para uniformidad.
    numeros: lista de números entre [0, 1)
    k: cantidad de intervalos (clases)
    alfa: nivel de significancia (comúnmente 0.05)
    """
    n = len(numeros)
    frecuencia_esperada = n / k
    
    # 1. Agrupar los números en sus respectivos intervalos (Frecuencia Observada)
    # np.histogram cuenta cuántos números caen en cada uno de los k rangos
    frecuencia_observada, bins = np.histogram(numeros, bins=k, range=(0, 1))
    
    # 2. Calcular el estadístico Chi-cuadrada
    # Formula: sum((Oi - Ei)^2 / Ei)
    chi_est, p_valor = stats.chisquare(frecuencia_observada, f_exp=frecuencia_esperada)
    
    # 3. Obtener el valor crítico de la tabla (distribución Chi-cuadrada)
    gl = k - 1
    valor_critico = stats.chi2.ppf(1 - alfa, gl)
    
    # Resultados
    print("--- Resultados de la Prueba Chi-Cuadrada ---")
    print(f"Frecuencia Esperada por intervalo: {frecuencia_esperada}")
    print(f"Estadístico Chi-cuadrada calculado: {chi_est:.4f}")
    print(f"Valor crítico (tablas): {valor_critico:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    print("-" * 40)
    
    if chi_est <= valor_critico:
        print("RESULTADO: No se rechaza la Hipótesis Nula (H0).")
        print("Conclusión: Los números se distribuyen uniformemente.")
    else:
        print("RESULTADO: Se rechaza la Hipótesis Nula (H0).")
        print("Conclusión: Los números NO son uniformes.")

# --- Ejemplo de uso ---
# Generamos 100 números pseudoaleatorios con numpy para probar el script
np.random.seed(42) # Para que los resultados sean replicables
datos_ejemplo = np.random.uniform(0, 1, 100)

prueba_chi_cuadrada(datos_ejemplo, k=10)