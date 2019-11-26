# CS-WebApps : A collection of Web application for ML, DL models.

## About : 
I have always wanted to develop complete ML,DL applications where i would have an UI to feed in some inputs and the ML, DL model to produce an ouput on the learning that these models have done.

## Projects :
- Bar Stock Exchange
- On Demand Analytics
- Voice Based Chatbot
- Qunatitative Finance

## Machine Learning Models : 

**Topic 1 :** <br />
- [ Bayseian Network Model ], [ Probabilistics Graph Models ], [ Root Cause Analysis ]

**Topic 2 :** <br />
- [ Supervised Learning ], [ XGBoost ], [ EnSemble Learning]

**Topic 3:** <br />
- [ Cascade Modeling ]

**Topic 4:** <br />
- [ Stacking Modeling ]

**Topic 5:** <br />
- [ Stochastic Calculus ], [ Financial Mathematics ], [ Statistics ]
- ***Use Case:*** Microfinance

## Deep Learning Models : 

**Topic 1 :** <br />
- [ Mobile App ], [ Music Recommendation ]

**Topic 2 :**<br />
- [ Keras ], [ GAN's ]

**Topic 3 :**<br />
- [ PyTorch ], [ XLNet ]

**Topic 4 :**<br />
- [ OpenCV ] , [ Bert ], [ Transfer Learning ]

## Tech Stack : 

#### Tech for WebApps : 

1. JavaScript
2. React
3. Redux
4. Flask and Flask RESTPlus
5. Python
6. CSS
7. HTML
8. Php

#### Tech for ML,DL Models : 

1. Python / Java / Scala / C++
2. Pandas
3. Numpy
4. Dask
5. Numba
6. Talend
7. Pentaho
8. Matplotlib
9. Seaborn
10. Plotly
11. Keras
12. PyTorch
13. OpenCV
14. Tensorflow
15. Apache SparK
16. Apache Flink

#### Tech for Data Storage : 

1. Apache Hive
2. ElasticSearch
3. Apache Druid
4. NoobBase (Yep ! That's right. It's my creation.)

#### Pipeline Management
1. Apache Airflow


## Directory Structure For each Web Apps:
Below is the  template to be followed for each project
```
├── Project_Name
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Make this project pip installable with `pip install -e`
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```
Inspired By : [Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/)

**NOTE:** Each project is a deployment ready code in itself, hence the makefile and other production support files will be present in each project acordingly. 
