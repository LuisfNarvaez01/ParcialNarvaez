import math
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class CampanaP:
    def __init__(self, defectos):
        self.defe = list(defectos)
        self.sem = np.arange(1, len(self.defe) + 1)
        self.acum = np.cumsum(self.defe)
        self.a = None
        self.b = None

    def goel(self, t, a, b):
        """m(t) = a * (1 - e^(-b t))"""
        return a * (1 - np.exp(-b * t))

    def ajustar(self):
        """Ajusta a y b con curve_fit sobre los acumulados."""
        a0 = self.acum[-1] * 1.5 
        (self.a, self.b), _ = curve_fit(
            self.goel, self.sem, self.acum, p0=[a0, 0.1]
        )
        return self.a, self.b

    def restantes(self):
        """Defectos sin descubrir si se libera hoy: a - m(t) en la última semana."""
        t = self.sem[-1]
        return self.a - self.goel(t, self.a, self.b)

    def semana_95(self):
        """Semana en la que se alcanza el 95 % de los defectos: t = ln(20) / b."""
        return math.log(20) / self.b

    def graficar(self, ruta):
        t_fino = np.linspace(0, self.sem[-1] + 4, 200)
        plt.figure(figsize=(8, 5))
        plt.plot(self.sem, self.acum, "o", label="Acumulados reales")
        plt.plot(t_fino, self.goel(t_fino, self.a, self.b), "-", label="Curva ajustada (Goel)")
        plt.axhline(self.a, linestyle="--", color="gray", label=f"a = {self.a:.1f}")
        plt.title("Defectos acumulados y curva de Goel")
        plt.xlabel("Semana")
        plt.ylabel("Defectos acumulados")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig(ruta, dpi=150)
        plt.close()
