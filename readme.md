# Generador de Melodías con Cadenas de Markov 🎵

Este proyecto utiliza una **cadena de Markov** para generar melodías musicales a partir de un conjunto de notas y una matriz de transición que define la probabilidad de pasar de una nota a otra. La melodía es reproducida mediante generación de tonos con frecuencias y duraciones definidas para cada nota.

## ¿Qué es una cadena de Markov?

Una cadena de Markov es un modelo probabilístico donde el siguiente estado depende únicamente del estado actual. En este proyecto, cada estado representa una nota musical, y la matriz de transición indica la probabilidad de ir de una nota a otra.

## ¿Qué hace este proyecto?

1. Define un conjunto de notas musicales (por ejemplo: DO, RE, MI, FA, SOL, LA, SI).
2. Crea una **matriz de transición** con probabilidades de pasar de una nota a otra.
3. Usa un generador de números aleatorios para determinar las transiciones.
4. En cada paso, **imprime** la nota seleccionada y la reproduce como un tono de cierta frecuencia y duración.
5. Genera una melodía con un número definido de transiciones.

## Ejemplo de matriz de transición

|      | DO  | RE  | MI  | FA  | SOL | LA  | SI  |
|------|-----|-----|-----|-----|-----|-----|-----|
| DO   | 0.1 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 |
| RE   | 0.2 | 0.1 | 0.3 | 0.1 | 0.1 | 0.1 | 0.1 |
| ...  | ... | ... | ... | ... | ... | ... | ... |

## Reflexión 🤔

Después de realizar este ejercicio, me di cuenta de que el uso de una cadena de Markov para modelar melodías tiene sentido porque muchas piezas musicales presentan transiciones entre notas que no son completamente aleatorias, sino que siguen ciertas probabilidades condicionadas por la nota anterior. El modelo permite capturar esa dependencia local, y con una matriz de transición bien ajustada se pueden generar melodías que suenan coherentes. Sin embargo, también noté que, al depender solo del estado actual (la nota presente), se pierde el contexto más amplio, como frases musicales completas o estructuras repetitivas más grandes.

Una forma de incorporar patrones repetitivos al modelo sería extender la cadena de Markov a un orden superior, donde las transiciones dependen no solo de la última nota sino de las dos o tres anteriores. Esto permitiría capturar secuencias más complejas y reflejar mejor el estilo musical. También podría entrenarse el modelo con melodías reales para que aprenda transiciones más naturales de un estilo específico, como jazz o música clásica. Sin embargo, la principal limitación es que Markov no comprende ritmo, armonía o intención musical; solo replica patrones estadísticos. Para superar esto, sería necesario usar modelos más avanzados, como redes neuronales recurrentes o transformers, que sí pueden aprender dependencias más largas y complejas.

---

**Autor:** Santiago Vera Espinoza 

**Materia:** Desarrollo de aplicaciones avanzadas de ciencias computacionales

**Lenguaje:** Python  
