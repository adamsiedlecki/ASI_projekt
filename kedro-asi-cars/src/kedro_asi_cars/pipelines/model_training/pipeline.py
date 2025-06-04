"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from .nodes import train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model,
            inputs=dict(train_data="car_prices_with_mileage_per_years"),
            outputs="best_model",
            name="train_model"
        )
    ])
