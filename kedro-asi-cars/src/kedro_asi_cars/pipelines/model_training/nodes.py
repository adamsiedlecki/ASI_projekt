"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.12
"""


from autogluon.tabular import TabularPredictor


def train_model(train_data) -> TabularPredictor:
    target_column = 'price'
    predictor = TabularPredictor(label=target_column, path='data/06_models/AutogluonModels').fit(train_data,
        hyperparameters={
            "FASTAI": {}
        })
    return predictor
