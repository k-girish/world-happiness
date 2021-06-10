# World Happiness Report

## Abstract

In this project, we apply various machine learning algorithms to the data collected from world happiness report between the years 2007 - 2020. First, we find the correlation between the happiness score and each of the 6 indicators (logged GDP, social support, healthy life expectancy, freedom to make life choices, generosity
and lower corruption) and plot a time series. We see that happiness is strongly correlated to logged GDP, social support, healthy life expectancy and weakly (or negatively) correlated to freedom, generosity and perception of corruption. Furthermore, there are very little changes in these correlations over the years as seen in the time series plot. We then apply Kmeans, Agglomerative Clustering, Affinity Propagation clustering algorithms to the data to see any underlying clustersing. We find no meaningful clustering in the data. Next, use a suite of modelling approaches to find the best model which could predict happiness score when fed with raw data of a country. Using partial dependency plots, we determine that happiness is strongly correlated to logged GDP, social support, healthy life expectancy, as concluded earlier. We explain the erroneous predictions even in our best fit model using LIME. Lastly, we model countries belonging to a particular region to check for features previously not captured. We see that happiness score is not related (weakly dependent) on health life expectancy in European countries, which is a deviation from previous results. 

## How to read this project?

* Please go through the `report.pdf` file to check out a discussion of our experiments and observations. The report details the methods and provides the results along with insights we gained.

* We have several Jupyter notebooks that contain the code and visualizations, the purpose of each notebook is detailed in the next section. The notebooks can be conveniently located at the `notebooks` folder.

* Finally, the `src` folder contains some custom library code that we have used in the notebooks. 

## File Directory Description

* `/notebooks/`: this folder contains all the jupyter notebooks used for analysis and modelling
	  
	* `standardization.ipynb`: Notebook for preprocessing the data like standardization 
	  
	* `visualization.ipynb`: Notebook for plotting the correlation between factors and visializing happiness socre

        * `clustering.ipynb`: Notebook for clustering the dataset
	
	* `predict_happiness.ipynb`: Notebook for modelling the task of predicting happiness score based on country features (section 4 of the report)
	  
	* `preprocess_for_training.ipynb`: Notebook for preprocessing the data for missing values, standardization and encoding (section 4.4 of the report)
	  
	* `regionbasedmodels.ipynb`: Notebook containing all region based and continent based modelling.


* `/src/`: this folder contains custom library functions used in the jupyter notebooks

	* `training/MultiModelPipeline`: Class that allows cross-validation across multiple models and hyper-parameter using the sklearn pipeline and GridSearchCv features.

	* `utils`: Module containing utility functions

* `/data/`: data files can be found in this folder

	* `final_data.csv`: the world-happiness data downloaded from Kaggle

	* `final_training_data.csv`: data obtained after preprocessing the data using the jupyter notbeook `preprocess_for_training.ipynb`

* `report.pdf`: this is a writeup to detail everything about this project.

## How to run the code

If starting with a new/virtual environment, please install all dependencies mentioned in the `requirements.txt` file. All the libraries used are pretty standard, so it should not be a problem if you have an already setup environment. Running a particular jupyter notebook is sufficient to reproduce the results.


## Authors

Girish Kumar ([Web](https://sites.google.com/view/girish-kumar/home), [LinkedIn](https://www.linkedin.com/in/kumagir/), [git](https://github.com/k-girish))

Appilineni Kushal 

Xue Feng ([git](https://github.com/xue1993))

## Data Source:
[Kaggle World Happiness Report 2021](https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021?select=world-happiness-report.csv)
