import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from kidneyDiseaseClassifier.entity.config_entity import PrepareBaseModelConfig
from pathlib import Path


class PrepareBaseModel:
    """Class for preparing base models.

    This class provides methods for loading a base model, preparing a full model,
    and saving a model to a specified path.

    Attributes:
        config (PrepareBaseModelConfig): The configuration for preparing base models.
    """

    def __init__(self, config: PrepareBaseModelConfig):
        """Initializes the PrepareBaseModel.

        Args:
            config (PrepareBaseModelConfig): The configuration for preparing base models.
        """
        self.config = config

    def get_base_model(self):
        """Loads the base model and saves it to the specified path."""
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        """Prepares the full model by freezing specified layers and adding additional layers.

        Args:
            model (tf.keras.Model): The base model to be prepared.
            classes (int): The number of classes in the model.
            freeze_all (bool): Whether to freeze all layers of the model.
            freeze_till (int): The index of the last layer to freeze.
            learning_rate (float): The learning rate for the model.

        Returns:
            tf.keras.Model: The prepared full model.
        """
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[: -freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """Saves the model to the specified path.

        Args:
            path (Path): The path where the model will be saved.
            model (tf.keras.Model): The model to be saved.
        """
        model.save(path)
