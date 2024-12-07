# NLP Project

## Meta information

Authors: Parker Hutcinson and Jackson Miskill
Purpose: UVA CS 6501: NLP Final Project Repository

### Introduction

Independent companies in the United States play a huge role in helping mitigate the effects of climate change through energy consumption and general safe environmental practices. We have noticed that on most companies websites, there is a plethora of ESG literature. However, we have reason to believe that this is just a form of signaling for a company; they are trying to show that they are taking steps towards helping the environment, even if they aren't actually taking those steps. Given this textual information and ratings about these companies, we would like to use NLP techniques to develop a classifier for identifying corporations that likely need to be looked into in further detail based on their textual information.

### Data sources

We are using a S&P Global rating system for ratings on companies.

### Set up

Use a Pythonic virtual environment like normal. However, the environment needs to be 3.11, because of some deprecated modules in 3.12 that are required for Tensorflow. Thus, run the following code for set up:

```
python3.11 -m venv venv-3.11
source venv-3.11/bin/activate
pip install -r requirements.txt
```
