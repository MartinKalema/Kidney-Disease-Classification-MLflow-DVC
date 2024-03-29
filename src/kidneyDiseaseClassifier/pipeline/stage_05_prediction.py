import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os 

# Encapsulates the prediction process.
class PredictionPipeline:
    def __init__(self, filename) -> None:
        self.filename = filename


    def predict(self):
        model = load_model(os.path.join('model', 'model.h5'))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size= (224,224))  
        test_image = image.img_to_array(test_image)
        # convert array to row vector
        test_image = np.expand_dims(test_image, axis=0)
        # return index of maximum value along each row
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{"image": prediction}]
        else:
            prediction = 'Normal'
            return [{"image": prediction}]