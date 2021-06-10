# World Happiness Report

## Abstract
<h3 style="color:red"> Copy from report ? </h3>
<h3 style="color:red"> Pending </h3>
This project is about the analysis of world happiness score. Detaily, a happiness score is based on the answer of individuals to a survey conducted by the “Gallup World Poll” where people across different countries were asked to rate their own happiness in life on a scale of 0 to 10. Also, a weighted estimate was then calculated amongst the 6 factors - economic production, social support, life expectancy, freedom, absence of corruption, and generosity - determining the extent to which each of them contributed to their happiness, in each country. The above dataset contains data from 150 countries across the globe for the years 2007 - 2020 with some missing parts. This allows us to analyze, see the  relationship between these factors and model the relationship between these factors and the happiness score. Then this model, which we expect to involve as few factors as possible and achieve high accuracy, can be used to predict the happiness score in the future. Also, a wide range of clustering techniques would help us to find  various patterns both amongst different countries and for a particular country over different years.


## How to read this project?

* Please go through the `reuslts/report.pdf` file to check out a discussion of our experiments and observations. The report details the methods and provides the results along with insights we gained.

* We have several Jupyter notebooks that contain the code and visualizations, the purpose of each notebook is detailed in the next section. The notebooks can be conveniently located at the `notebooks` folder.

* Finally, the `src` folder contains some custom library code that we have used in the notebooks. 

## File Directory Description

* `/notebooks/`: this folder contains all the jupyter notebooks used for analysis and modelling
	  
	* `standardization.ipynb`: <h3 style="color:red"> Pending Pending Pending Pending Pending </h3>
	  
	* `visualization.ipynb`: <h3 style="color:red"> Pending Pending Pending Pending Pending </h3>
	
	* `predict_happiness.ipynb`: Notebook for modelling the task of predicting happiness score based on country features (section 4 of the report)
	  
	* `preprocess_for_training.ipynb`: Notebook for preprocessing the data for missing values, standardization and encoding (section 4.4 of the report)
	  
	* `change_name.ipynb`: <h3 style="color:red"> Region based - pending, also change file name</h3>


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

<h3 style="color:red"> Add links ?</h3>

Girish Kumar ([Web](https://sites.google.com/view/girish-kumar/home), [LinkedIn](https://www.linkedin.com/in/kumagir/), [git](https://github.com/k-girish))

Appilineni Kushal ()

Xue Feng ()

## Data Source:
[Kaggle World Happiness Report 2021](https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021?select=world-happiness-report.csv)