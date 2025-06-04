"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.12
"""


from pycaret.regression import setup, compare_models, pull, save_model


def train_model(train_data):
    # Initialize the PyCaret environment
    setup(data=train_data, target='price')

    # Train and evaluate multiple models
    best_model = compare_models(include=['lr', 'ridge', 'lasso', 'rf'])

    # Optionally, pull and log comparison results
    comparison_results = pull()
    print(comparison_results)  # or use logging
    save_model(best_model, 'data/06_models/best_price_model')

    return best_model
