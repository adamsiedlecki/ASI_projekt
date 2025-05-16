"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from .pipelines.model_training import pipeline as model_training_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    print("Znalezione pipeline'y:", pipelines.keys())

    pipelines["model_training"] = model_training_pipeline.create_pipeline() # z jakiegoś dziwnego powodu nie znajduje


    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
