# Zero-Shot Classification

Este proyecto provee una implementación genérica de un clasificador zero-shot para tareas de clasificación de texto. Está diseñado para ser adaptable a diferentes dominios y tipos de datos, permitiendo clasificar textos en categorías definidas sin necesidad de entrenamiento supervisado específico para cada caso.

## Estructura del Proyecto

```
zero-shot-classification/
├── data/
│   ├── raw/                  # Archivos de datos originales sin procesar
│   └── processed/            # Archivos de datos limpios y procesados
├── notebooks/                 # Notebooks para análisis exploratorio y pruebas
│   └── example_usage.ipynb
├── src/                      # Código fuente del proyecto
│   ├── __init__.py           # Indica que src es un paquete
│   ├── classifier.py         # Implementación del clasificador zero-shot genérico
│   ├── data_processing.py    # Funciones para limpieza y preparación de datos
│   └── utils.py              # Funciones auxiliares varias
├── tests/                    # Tests unitarios para el código fuente
│   └── test_classifier.py
├── requirements.txt          # Dependencias del proyecto
├── .gitignore                # Archivos y carpetas ignoradas por Git
└── README.md                 # Documentación del proyecto
```

## Instalación

Para preparar el entorno y ejecutar el proyecto, clona este repositorio e instala las dependencias:

```bash
git clone <repository-url>
cd zero-shot-classification
pip install -r requirements.txt
```

## Uso

1. **Preparación de datos:** Coloca tus archivos de texto en la carpeta `data/raw`. Utiliza las funciones en `src/data_processing.py` para limpiar y preparar los datos.

2. **Clasificación zero-shot:** Emplea el módulo `src/classifier.py` para realizar la clasificación zero-shot en tus textos, definiendo las etiquetas o categorías de interés.

3. **Análisis y experimentación:** Usa los notebooks en `notebooks/` para explorar y probar la funcionalidad del clasificador con distintos datasets y escenarios.

4. **Testing:** Ejecuta los tests en la carpeta `tests/` para verificar la integridad del código.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir issues o pull requests para sugerencias, mejoras o correcciones.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT — para más detalles consulta el archivo [LICENSE](LICENSE).

---
