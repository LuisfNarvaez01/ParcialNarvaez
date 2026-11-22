Parcial práctico

Integrantes: Luis Felipe Narvaez

Opción escogida: B
Modelo de datos

Base de datos: huilasoft, con tres colecciones.

Agentes con ID, nombre, nivel, tickets_por_hora
Defectos con ID, semana, defectos

Relación: cada ticket guarda en agente el nombre del agente que lo atendió (referencia a agentes). defectos es independiente: describe la campaña de pruebas de la versión 11.0.
Resultados (opción B)
- Acumulados: 28, 51, 73, 90, 106, 118, 130, 139
- Ajuste con curve_fit: a ≈ 198.1, b ≈ 0.1519
- Defectos sin descubrir en la semana 8: ≈ 58.8
- Semana del 95 %: t = ln 20 / b ≈ 19.7
Gráfica en: graficas/resultado.png

Interpretación  
De acuerdo con el ajuste del modelo de Goel, la versión 11.0 presenta un total aproximado de 198 defectos (a ≈ 198), y en ocho semanas se han detectado 139. Si se publica hoy, quedarían alrededor de 59 defectos sin identificar, lo que representa cerca del 30 % del total. La gráfica indica que la curva ajustada se ajusta adecuadamente a los puntos reales y todavía no está estabilizada: la diferencia entre los puntos y la asíntota sigue siendo considerable. Se estima que el 95 % de los defectos se alcanzará hacia la semana 19.7, lo que significa casi doce semanas adicionales de pruebas. Sugerimos a HuilaSoft que no realice la liberación en este momento, que prolongue las pruebas unas ocho semanas más y que ajuste el modelo cada dos semanas con los nuevos datos. Si la fecha no se puede modificar, es recomendable lanzar solo los módulos críticos y establecer un plan de corrección para abordar los defectos restantes.
