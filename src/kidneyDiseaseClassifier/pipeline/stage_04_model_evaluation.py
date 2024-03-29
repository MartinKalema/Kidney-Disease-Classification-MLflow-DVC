from kidneyDiseaseClassifier.config.configuration import ConfigurationManager
from kidneyDiseaseClassifier.components.model_evaluation_mlflow import Evaluation
from kidneyDiseaseClassifier import logger


STAGE_NAME = "Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        # evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info("*********************************\n")
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(
            f">>>>>> {STAGE_NAME} completed <<<<<<<\n **********************************")
    except Exception as e:
        logger.exception(e)
        raise e