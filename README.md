# 💊 Pharma Radar - Pipeline de Farmacovigilancia

Pharma Radar es un sistema de extracción y análisis de datos diseñado para detectar discrepancias entre los efectos adversos oficiales de medicamentos y los síntomas reportados por usuarios en plataformas digitales.

Este proyecto nació originalmente como parte del FACMED UANL - Harvard Health Systems Innovation Hackathon 2026.

## 🎯 El Problema
La farmacovigilancia tradicional depende de reportes médicos formales, lo que puede causar retrasos en la detección de efectos secundarios emergentes. Mientras tanto, los pacientes frecuentemente reportan sus síntomas en tiempo real utilizando lenguaje informal en redes sociales o foros.

## 🚀 La Solución
Pharma Radar automatiza el monitoreo cruzando dos fuentes de información utilizando algoritmos de similitud de texto (*Fuzzy Matching*):
1.  **Datos Oficiales:** Extracción automatizada de estudios y efectos adversos desde la API oficial de `ClinicalTrials.gov`.
2.  **Escucha Social:** Análisis de reportes de pacientes (procesamiento de lenguaje natural sobre datos informales).

## 🛠️ Tecnologías y Arquitectura
*   **Lenguaje:** Python 3.x
*   **Extracción de Datos:** `requests` (Consumo de APIs REST).
*   **Procesamiento de Datos:** `pandas` (Limpieza, transformación y estructuración de DataFrames).
*   **Algoritmo de Similitud:** `thefuzz` / `python-Levenshtein` (Cálculo de distancia de Levenshtein para empatar terminología médica con lenguaje coloquial).

## ⚙️ Configuración e Instalación (Desarrollo Local)

Sigue estos pasos para ejecutar el pipeline en tu computadora:

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/Pharma-Radar-2.0.git](https://github.com/TU_USUARIO/Pharma-Radar-2.0.git)
   cd Pharma-Radar-2.0