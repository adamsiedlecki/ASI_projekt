"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.12
"""


from autogluon.tabular import TabularPredictor


def train_model(train_data, target_column: str) -> TabularPredictor:
    predictor = TabularPredictor(label=target_column).fit(train_data)
    return predictor
