from kidneyDiseaseClassifier.config.configuration import ConfigurationManager
from kidneyDiseaseClassifier.components.model_training import Training
from kidneyDiseaseClassifier import logger


STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_training_config()
        model_training = Training(config=model_training_config)
        model_training.get_base_model()
        model_training.train_valid_generator()
        model_training.train()


if __name__ == '__main__':
    try:
        logger.info("*********************************\n")
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> {STAGE_NAME} completed <<<<<<<\n **********************************")
    except Exception as e:
        logger.exception(e)
        raise e