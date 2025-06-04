from kedro.io.core import AbstractDataset
from autogluon.tabular import TabularPredictor
import os

class AutoGluonTabularPredictorDataSet(AbstractDataset):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def _load(self) -> TabularPredictor:
        return TabularPredictor.load(self._filepath)

    def _save(self, predictor: TabularPredictor) -> None:
        # Ensure the directory exists
        os.makedirs(self._filepath, exist_ok=True)
        predictor.save(self._filepath)
        print(f'Saved autogluon model: {self._filepath}')

    def _describe(self) -> dict:
        return dict(filepath=self._filepath)
