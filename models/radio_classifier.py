import tensorflow as tf
from PIL import Image
import numpy as np
import keras

class RadioClassifier:
    def __init__(self, model_path: str):
        """
        Inicializa el clasificador cargando el modelo.

        :param model_path: Ruta del archivo del modelo (.h5).
        """
        self.model = tf.keras.models.load_model(model_path, compile=True)

    def preprocess_image(self, image: Image.Image) -> np.ndarray:
        """
        Preprocesa una imagen para hacerla compatible con el modelo.

        :param image: Imagen en formato PIL.
        :return: Imagen preprocesada como un array de NumPy.
        """
        image = image.resize((224, 224))
        image = np.array(image, dtype=np.float32) / 255.0 
        if len(image.shape) == 2:  # Si es una imagen en escala de grises, agregar canales
            image = np.expand_dims(image, axis=-1)
            image = np.repeat(image, 3, axis=-1)  # Repetir para simular 3 canales (RGB)
        return np.expand_dims(image, axis=0)  # Añadir dimensión para batch

    def get_class_name(self, class_idx: int) -> str:
        """
        Obtiene el nombre de la clase correspondiente a un índice.

        :param class_idx: Índice de la clase.
        :return: Nombre de la clase.
        """
        class_names = [
            "Atelectasis", "Cardiomegaly", "Consolidation" ,"Effusion", "Infiltration",
            "Mass", "No Finding", "Nodule", "Pleural_Thickening", "Pneumothorax", 
        ]
        return class_names[class_idx]

    def predict(self, img_array: np.ndarray) -> dict:
        """
        Realiza una predicción en la imagen preprocesada y devuelve las 3 clases más probables.
        
        :param img_array: Imagen preprocesada como un array de NumPy.
        :return: Diccionario con las 3 clases más probables y sus probabilidades.
        """
        predictions = self.model.predict(img_array)[0]
        
        # Ordena las probabilidades en orden descendente y obtiene los índices de las 3 clases más probables
        top_3_indices = np.argsort(predictions)[::-1][:3]

        # Confianza y nombre de las clases
        top_3_classes = {
            self.get_class_name(idx): round(predictions[idx] * 100, 2) for idx in top_3_indices
        }

        return {
            "Condición detectada": top_3_classes
        }