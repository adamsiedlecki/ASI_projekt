from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_age_feature,
    generate_mileage_per_year_feature,
    deleteOutliers,
    deleteUnimportantColumns,
    deleteGeneration,
    deleteYear,
    makeModelLowercase
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=deleteUnimportantColumns,
                inputs="car_prices",
                outputs="car_prices_cleaned",
                name="delete_unimportant_columns",
            ),
            node(
                func=deleteGeneration,
                inputs="car_prices_cleaned",
                outputs="car_prices_without_generation",
                name="deleteGeneration",
            ),
            node(
                func=makeModelLowercase,
                inputs="car_prices_without_generation",
                outputs="car_prices_model_lowercase",
                name="modelLowercase",
            ),
            # node(
            #     func=deleteOutliers,
            #     inputs="car_prices_without_generation",
            #     outputs="car_prices_without_outliers",
            #     name="deleteOutliers",
            # ),
            node(
                func=generate_age_feature,
                inputs="car_prices_model_lowercase",
                outputs="car_prices_with_age",
                name="generate_age_of_cars",
            ),
            node(
                func=deleteYear,
                inputs="car_prices_with_age",
                outputs="car_prices_without_year",
                name="delete_year_of_cars",
            ),
            node(
                func=generate_mileage_per_year_feature,
                inputs="car_prices_without_year",
                outputs="car_prices_with_mileage_per_years",
                name="generate_mileage_per_years_of_cars",
            )
        ]
    )
