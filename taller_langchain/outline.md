# Creando aplicaciones con LLM's usando LangChain

## Introducción

Por qué debería interesarte esto hoy

## Conceptos básicos

Antes de empezar a programar es importante comprender los conceptos básicos de lo que estamos haciendo. Así que hablemos de las cosas que vamos a usar en este taller y con las que puede empezar a avanzar.

### LLM

LLM son las siglas de **"Gran Modelo de Lenguaje"**, lo que quiere decir que es un modelo de inteligencia artificial que tiene muchos parámetros y que se he entrenado con una gran cantidad de texto. Normalmente estos modelos tienen una arquitectura de transformación.

### Embeddings (Incorporaciones)

Algo que vas a escuchar muy seguido en este entorno es la palabra "embeddings" (algunos lo traducen como "incorporaciones"). Para saber qué son y por qué existen, hay que saber un poco de cómo funcionan internamente los LLM's con arquitectura de transformador.

La forma que tienen los _embeddings_ es un conjunto de vectores con valores de coma flotante. Estos vectores tienen una longitud fija y cada uno de ellos representa una palabra.

Se llaman incorporaciones porque son una forma de "incorporar" el texto en un espacio vectorial. Esto quiere decir que cada vector representa un texto en un espacio vectorial.

Aquí puedes aprender más sobre estos elementos: [Incorporaciones en Google](https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture?hl=es-419)

Una incorporación es un espacio de dimensiones relativamente bajas al que se pueden trasladar vectores de dimensiones altas. Las incorporaciones facilitan el aprendizaje automático en entradas grandes, como vectores dispersos que representan palabras. Lo ideal es que una incorporación capture parte de la semántica de la entrada mediante la colocación de entradas semánticamente similares cerca en el espacio de incorporaciones.

Una incorporación se puede aprender y reutilizar en todos los modelos.

### Prompts

Algo que probablemente ya conoces son los **prompts**: los textos que les pasas a un modelo para que complete o actúe como lo esperas.

### LangChain

LangChain es un proyecto que provee de un conjunto de herramientas para
fortalecer las capacidades de los LLM's. Estas herramientas son (entre otras):

- Cargadores y divisores de texto
- Índices
- Abstracciones sobre modelos (una interfaz de programación para conectarte a distintos modelos)

### Componentes

Toda aplicación de software bien estructurada está hecha por componentes que
pueden ser reutilizados, o que están siendo reutilizados ya.

### Índices

Los índices son una forma de almacenar información de forma que sea fácil de consultar después.

### Agentes

Actuar dirigidos po la

### Bases de datos vectoriales

### Cadenas

### Ejemplo: creando un agente para crear chatbots

