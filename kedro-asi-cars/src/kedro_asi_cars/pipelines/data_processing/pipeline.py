from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_age_feature,
    generate_mileage_per_year_feature,
    deleteOutliers,
    deleteRowCounter
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=deleteRowCounter,
                inputs="car_prices",
                outputs="car_prices_without_row_counter",
                name="deleteRowCounter",
            ),
            node(
                func=deleteOutliers,
                inputs="car_prices_without_row_counter",
                outputs="car_prices_without_outliers",
                name="deleteOutliers",
            ),
            node(
                func=generate_age_feature,
                inputs="car_prices_without_outliers",
                outputs="car_prices_with_age",
                name="generate_age_of_cars",
            ),
            node(
                func=generate_mileage_per_year_feature,
                inputs="car_prices_with_age",
                outputs="car_prices_with_mileage_per_years",
                name="generate_mileage_per_years_of_cars",
            )
        ]
    )
