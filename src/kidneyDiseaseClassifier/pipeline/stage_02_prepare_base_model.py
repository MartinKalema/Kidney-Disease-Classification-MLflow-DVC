from kidneyDiseaseClassifier.config.configuration import ConfigurationManager
from kidneyDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from kidneyDiseaseClassifier import logger


STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info("*********************************\n")
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> {STAGE_NAME} completed <<<<<<<\n **********************************")
    except Exception as e:
        logger.exception(e)
        raise e
