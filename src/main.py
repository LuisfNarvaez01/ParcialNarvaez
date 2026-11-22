import os
from pymongo import MongoClient
from modelo import CampanaP

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def main():
    cliente = MongoClient("mongodb://127.0.0.1:27017")
    docs = cliente["huilasoft"]["defectos"].find({}, {"_id": 0}).sort("semana", 1)
    defectos = [d["defectos"] for d in docs]
    campana = CampanaP(defectos)
    a, b = campana.ajustar()
    print(f"Acumulados: {campana.acum.tolist()}")
    print(f"a = {a:.2f}   b = {b:.4f}")
    print(f"Defectos sin descubrir hoy (semana 8): {campana.restantes():.1f}")
    print(f"Semana del 95 %: {campana.semana_95():.2f}")
    campana.graficar(os.path.join(RAIZ, "graficas", "resultado.png"))

if __name__ == "__main__":
    main()
