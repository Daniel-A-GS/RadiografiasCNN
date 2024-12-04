from fastapi import FastAPI, UploadFile, File, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# TensorFlow
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

import os
import io

from models.radio_classifier import RadioClassifier

app = FastAPI(title="Análisis de Radiografías Médicas para la Clasificación de Patologías mediante CNN")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa el clasificador
classifier = RadioClassifier("dev_model/modelo_entrenado-7.h5")

@app.post("/clasification_image")
async def create_upload_file(file: UploadFile = File(...)):
    try: 
        # Leer el archivo
        contents = await file.read()
        # Convertir el contenido a una imagen PIL
        image = Image.open(io.BytesIO(contents))
        # Preprocesar la imagen
        img_array = classifier.preprocess_image(image)
        # Hacer la predicción
        result = classifier.predict(img_array)
        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing the image: {str(file)}")