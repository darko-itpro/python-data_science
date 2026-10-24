# Data Science with Python

This is the practical cases for Python training I provide. Intended for french
trainee, the rest of the explanations are in french.

Suite à la demande croissante, je prépare une formation sur l'usage des
bibliothèques *scientifiques* de Python. Cette partie est donc destinée aux usages
en science, analyse de données, data-Science, machine learning…

Ce projet est en cours de réalisation et ne comporte actuellement en documents
publics que des illustrations d'usage.

## Mise en place de l'environnement

Depuis sa version `2026.10.dev1`, ce projet n'utilise plus le `requirements.txt`. Les dépendances 
sont déclarées dans le fichier `pyproject.yaml` et accompagnées d'un `uv.lock`.

Installez le projet par :

```shell
pip install -e .
```

## Compatibilité `uv`

Le passage à une configuration dans le `pyproject.toml` rends ce projet immédiatement utilisable 
avec `uv`. Mais ce projet est déjà géré avec `uv` comme le témoigne la présence du fichier 
`uv.lock`. Si vous utilisez `uv`, Vous pouvez donc exécuter :

```shell
uv sync
```

## Environnement de travail

### Les notebooks Jupyter et Jupyter Lab

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

### Les démos web

Le porjet propose une démo Streamlit. Cette démo nécessite l'installation du projet avec ses 
dépendances optionneles `web `. 

Vous devez les installer soit avec :

```shell
pip install -e ".[web]"
```

soit avec :

```shell
uv sync --extra web
```

Streamlit se lance avec :

```shell
python -m streamlit run webapp/stockapp.py --browser.gatherUsageStats false
python -m streamlit run webapp/stockapp_light.py --browser.gatherUsageStats false
```

L'option `--browser.gatherUsageStats` désactive l'envoi de données d'usage.

## Travailler avec des Notebooks et des modules

Depuis sa version `2026.10.dev1`, ce projet a adopté une structure en *package*. Le code doit donc 
être dans l'arborescence du répertoire `src/`.

Le projet a été installé en mode *éditable* avec l'option `-e` de `pip install` par 
`pip install -e`.

Avec `uv`, `uv sync` a installé le projet en mode éditable.

Ceci vous permet utiliser le code dans l'arborescence du répertoire `src/` dans les notebooks.

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