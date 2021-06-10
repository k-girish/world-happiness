import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

from src.utils import view_all_df


class MultiModelPipeline:
    def __init__(self, parameters={'estimator': [RandomForestRegressor()]}, cv=None, verbose=1, scoring='r2'):
        """
        Initialize the MultiModelPipeline class by storing the provided parameters, creating a pipeline to be fit
        using the initialized GridSearchCv object

        :param parameters: the hyper-parameters (including a variable estimator) over which the Cross-Validation is
        to be performed
        :param cv: parameter value will be passed to the 'cv' argument of sklearn.model_selection.GridSearchCV
        :param verbose: parameter value will be passed to the 'verbose' argument of sklearn.model_selection.GridSearchCV
        :param scoring: parameter value will be passed to the 'scoring' argument of sklearn.model_selection.GridSearchCV
        """
        self.parameters = parameters
        self.pipeline = Pipeline(steps=[('estimator', RandomForestRegressor())])
        self.model = GridSearchCV(self.pipeline, parameters, cv=cv, n_jobs=-1, verbose=verbose, scoring=scoring)

    def fit(self, X, y):
        """
        Fit the GridSearchCv estimator

        :rtype: a pandas dataframe with the results
        :param X: numpy array of training data to be used by GridSearchCV estimator
        :param y: numpy array of target value to be used by GridSearchCV estimator
        """
        self.model.fit(X, y)
        self.results_df = pd.DataFrame(self.model.cv_results_)

    def show_fit_results(self):
        """
        Prints the relevant metrics obtained from fitting the GridSearchCV estimator
        Metrics are only based on the training data

        """
        print(f'Best estimator is: \n{self.model.best_params_}')
        print(f'Best estimator cross validation score is: \n{self.model.best_score_}')
        view_all_df(pd.DataFrame(
            self.results_df.loc[:, ['rank_test_score', 'mean_test_score', 'params', 'mean_fit_time']]))

    def show_scores(self, X_train, y_train, X_test, y_test):
        """
        Predicts the target on training data and test data and shown the MSE and R2 score by comparing with true values

        :param X_train: numpy array of training data
        :param y_train: numpy 1D-array of true target values corresponding to training data
        :param X_test: numpy array of test data
        :param y_test: numpy 1D-array of true target values corresponding to test data
        """
        print('For the best estimator:')
        print(f'Cross validation R2 score: {self.model.best_score_}')

        y_pred = self.model.predict(X_train)
        print(f'Training MSE: {mean_squared_error(y_train, y_pred)}')
        print(f'Training R2 score: {r2_score(y_train, y_pred)}')

        y_pred_test = self.model.predict(X_test)
        print(f'Test MSE: {mean_squared_error(y_test, y_pred_test)}')
        print(f'Test R2 score: {r2_score(y_test, y_pred_test)}')
