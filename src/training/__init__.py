import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

from src.utils import view_all_df


class MultiModelPipeline:
    def __init__(self, parameters={'estimator': [RandomForestRegressor()]}, cv=None, verbose=1, scoring='r2'):
        self.parameters = parameters
        self.pipeline = Pipeline(steps=[('estimator', RandomForestRegressor())])
        self.model = GridSearchCV(self.pipeline, parameters, cv=cv, n_jobs=-1, verbose=verbose, scoring=scoring)

    def fit(self, X, y):
        self.model.fit(X, y)
        self.results_df = pd.DataFrame(self.model.cv_results_)

    def show_fit_results(self):
        print(f'Best estimator is: \n{self.model.best_params_}')
        print(f'Best estimator cross validation score is: \n{self.model.best_score_}')
        view_all_df(pd.DataFrame(
            self.results_df.loc[:, ['rank_test_score', 'param_estimator', 'mean_fit_time', 'mean_test_score']]))

    def show_scores(self, X_train, y_train, X_test, y_test):
        print('For the best estimator:')
        print(f'Cross validation R2 score: {self.model.best_score_}')

        y_pred = self.model.predict(X_train)
        print(f'Training MSE: {mean_squared_error(y_train, y_pred)}')
        print(f'Training R2 score: {r2_score(y_train, y_pred)}')

        y_pred_test = self.model.predict(X_test)
        print(f'Test MSE: {mean_squared_error(y_test, y_pred_test)}')
        print(f'Test R2 score: {r2_score(y_test, y_pred_test)}')
