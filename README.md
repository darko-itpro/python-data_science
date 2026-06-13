# Data Science with Python

This is the practical cases for Python training I provide. Intended for french
trainee, the rest of the explanations are in french.

Suite à la demande croissante, je prépare une formation sur l'usage des
bibliothèques *scientifiques* de Python. Cette partie est donc destinée aux usages
en science, analyse de données, data-Science, machine learning…

Ce projet est en cours de réalisation et ne comporte actuellement en documents
publics que des illustrations d'usage.

## Mise en place de l'environnement

Il faut donc commencer par récupérer les sources en local.

Assurez-vous que [pip](https://pypi.python.org/pypi/pip) est installé. Créez
si vous le souhaitez un [virtualenv](https://docs.python.org/3/library/venv.html)
dédié à la formation. Si vous utilisez un IDE tel que PyCharm, vous pouvez l'utiliser pour créer
ce virtualenv.

À partir de la racine du projet saisissez

```
pip install -r requirements.txt
```

Votre environnement contient alors toutes les dépendances nécessaires.

## Environnement de travail

Nous allons pour cette formation utilser des documents de type
*Jupyter Notebooks* générés à l'aide du projet
[Jupyter](http://jupyter.org/). Ce dernier est inclus dans les dépendances.
 
Placez-vous dans le répertoire *notebooks* et exécutez la commande

```shell
jupyter notebook
```

ou

```shell
jupyter-lab
```

Vous pouvez maintenant travailler avec les *notebooks*. Ceux-ci sont proposés
comme outil pour vous aider à vous familiariser avec le langage.

Les démos Streamlit se lancent avec :
```shell
python -m streamlit run webapp/stockapp.py --browser.gatherUsageStats false
python -m streamlit run webapp/stockapp_light.py --browser.gatherUsageStats false
```

L'option `--browser.gatherUsageStats` désactive l'envoi de données d'usage.

## Travailler avec des Notebooks et des modules

Si pendant les exercices ou les démos, il est nécessaire de mutualiser du code, celui-ci sera écrit 
dans un module dans l'arborescence du répertoire `src/`. Cependant, pour qu'il soit retrouvé par les
notebooks, il est nécessaire que le répertoire `src/` soit dans les paths de Python.

Le plus simple est d'installer le projet courant en mode *éditable* avec l'option `-e` de 
`pip install`. Exécutez simplement :

```shell
pip install -e .
```

ou

```shell
uv pip install -e .
```

Attention cependant, dans un environnement iPython ou Notebook, un module n'est importé qu'une 
seule fois et s'il a été modifié, il est nécessaire soit de redémarrer le kernel soit de recharger 
le module.

iPython fournit l'extension [autoreload](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html#autoreload)
qui permet de recharger le module à chaque exécution de code (comme s'il s'agissait de scripts).

Au début de vos Notebooks, pendant le développement, vous pouvez ajouter les lignes suivantes :

```jupyter
%load_ext autoreload
%autoreload 2
```
Vous pouvez aussi exécuter ces deux lignes dans vos shells iPython.

## Ressources

Le répertoire *assets* contient des fichiers issus de
l'[Opendata de la SNCF](https://data.sncf.com/). Les droits appartiennent
évidemment à la SNCF et ces fichiers sont présents ici pour disposer de documents
 texte volumineux à parcourir et explorer.