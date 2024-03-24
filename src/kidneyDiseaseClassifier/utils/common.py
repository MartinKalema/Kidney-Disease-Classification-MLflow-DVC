import os
from box.exceptions import BoxValueError
import yaml
from src import kidneyDiseaseClassifier
import json
import joblib
from ensure import ensure_annotations # catch type annotation errors
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

logger = kidneyDiseaseClassifier.logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents wrapped in a ConfigBox.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: Any other unexpected error that occurs during file reading.

    Returns:
        ConfigBox: A ConfigBox containing the contents of the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories specified in the list.

    Args:
        path_to_directories (list): A list of directory paths to be created.
        verbose (bool, optional): If True, log messages will be displayed for each directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save JSON data to a file.

    Args:
        path (Path): The path to the JSON file.
        data (dict): The data to be saved to the JSON file.

    Raises:
        IOError: If an error occurs while writing to the file.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the file: {e}")
    
    logger.info(f"Json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON file data and return as a ConfigBox.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: Data loaded from the JSON file as class attributes.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the JSON file is invalid.
    """
    try:
        with open(path, 'r') as f:
            content = json.load(f)
    except FileNotFoundError as e:
        logger.error(f"File not found at: {path}")
        raise e
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON file at: {path}. Reason: {e}")
        raise e

    logger.info(f"JSON file loaded successfully from: {path}")

    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save file as binary

    Args:
        data (Any): data to be saved as binary
        path (Path): path where the binary file will be saved.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load a binary file.

    This function loads a binary file located at the specified path using the joblib library.

    Args:
        path (Path): The path to the binary file to be loaded.

    Returns:
        Any: The object stored in the binary file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file cannot be deserialized.
    """
    
    if not path.exists():
        raise FileNotFoundError(f"File not found at: {path}")

    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data
    except Exception as e:
        raise ValueError(f"Error loading data from {path}: {e}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in kilobytes.

    Args:
        path (Path): The path to the file whose size is required.

    Returns:
        str: A string representing the size of the file in kilobytes, rounded to the nearest whole number.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"


def decodeImage(imageString,  fileName):
    """
    Decode a base64-encoded image string and save it to a file.

    Parameters:
        imageString (str): A base64-encoded image string.
        fileName (str): The name of the file to save the decoded image to.

    Returns:
        None
    """
    imageData = base64.b64decode(imageString)
    with open(fileName, "wb") as f:
        f.write(imageData)
        f.close()

def encodeImageIntoBase64(imagePath):
    """Encode an image file into base64 format.

    Args:
        imagePath (str): Path to the image file.

    Returns:
        bytes: Base64-encoded image data.
    """
    with open(imagePath, "rb") as f:
        return base64.b64encode(f.read())