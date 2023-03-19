# Tableau View Extractor

![Python](https://img.shields.io/badge/python-^3.8-blue.svg?longCache=true&style=flat-square&colorA=4c566a&colorB=5e81ac&logo=Python&logoColor=white)
![Tableau Server Client](https://img.shields.io/badge/tableauserverclient-0.25-blue.svg?longCache=true&style=flat-square&colorA=4c566a&colorB=5e81ac&logo=ChatBot&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-^v2.28.1-red.svg?longCache=true&style=flat-square&colorA=4c566a&colorB=5e81ac&logo=Python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-^2.0.0-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/tableau-extraction.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/tableau-extraction/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/tableau-extraction.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/tableau-extraction/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/tableau-extraction.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/tableau-extraction/network)

Application that provides an interface for extracting data from a Tableau Server instance. This project is part of a series of exercises that attempt to make data on self-hosted Tableau instances more available. Find the accompanying blog post [here](https://hackersandslackers.com/hostile-extraction-of-tableau-server-data/).

![Tableau View Extraction](./.github/img/tableauextraction_v2@2x.jpg)

## Status

This project is currently working as a POC and under active development. Upon completion, this application will be hosted on Google App Engine and allow for any Tableau server owner to build data pipelines using nothing but Tableau. If you're interested in seeing this project reach completion, please consider starring this project or express interest to let us gauge priority.

### In Development

The following features are currently in development:

* Tableau Server login
* Visual interface to specify external target database
* Scheduling
* Security hardening
* UI revamp
