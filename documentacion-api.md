# Índice

1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Instalación](#instalación)
4. [Clonación del Repositorio](#clonación-del-repositorio)
5. [Endpoints de la API](#endpoints-de-la-api)
6. [Manejo de Errores](#manejo-de-errores)
7. [Observaciones](#observaciones)

# Introducción

Esta API permite clasificar radiografías de tórax para detectar si contienen alguna patología. Es ideal para integrarse en PACS.

## Fecha de actualización

Última actualización realizada el 3-12-2024

# Requisitos Previos

* Git instalado.
* Python 3.10.
* Configuración básica del sistema operativo.

# Instalación 

# Clonación del Repositorio

```
git clone https://github.com/Daniel-A-GS/CNN-radiografias.git
cd CNN-radiografias
```

### Carga del modelo

Debido al peso del modelo, no se incluye en este repositorio. El archivo se encuentra en [drive](#https://drive.google.com/file/d/18iZR1U9gi7n2rFyyXZhuKdm7SOcv0HFR/view)
Por favor, guarda el archivo en la ubicación indicada en la configuración del modelo (/API/models/model.h5).

# End Points de la API

### Post /clasification_image

**Descripción**: Clasifica una imagen para detectar una enfermedad pulmonar o cardiomegalia.

**Request Body**:
  * `img.png` (png file): Imagen png de cualquier tamaño, puede ser RGB o en escala de grises

**Response**:
```
{
  "Condición detectada":{
    "Diagnóstico 1": confidence,
    "Diagnóstico 2": confidence,
    "Diagnóstico 3": confidence
  }
}
```

# Manejo de Errores

La API devuelve respuestas HTTP con códigos de error estándar:

* 400: Error en la solicitud (p. ej., imagen inválida o no soportada).
* 404: Endpoint no encontrado.
* 500: Error interno del servidor.

# Observaciones

El modelo (archivo .h5) debe estar disponible en el directorio /API/dev_model.