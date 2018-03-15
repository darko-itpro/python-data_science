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
si vous le souhaitez un [virtualenv](https://virtualenv.pypa.io/en/stable/)
dédié à la formation. Si vous utilisez un IDE tel que PyCharm, vous pouvez l'utiliser pour créer
ce virtualenv. Placez vous alors à la racine du projet et saisissez

```
pip install -r requirements.txt
```

Votre environnement contient alors toutes les dépendances nécessaires.

(documentation pas encore publiée)
Il ne reste plus qu'à générer la documentation. Placez-vous dans le répertoire
*docs* et exécutez
 
```
make html
```

La documentation est alors dispoible dans le sous répertoire *_build/html*.

## Cahiers d'exercices

Le répertoire *notebooks* contient des *cahiers d'exercices*. Ceux-ci sont
des documents type *Jupyter Notebooks* générés à l'aide de
[Jupyter](http://jupyter.org/). Ce dernier est inclus dans les dépendances.
 
Placez-vous dans le répertoire *notebooks* et exécutez la commande

```
jupyter notebook
```

Vous pouvez maintenant travailler avec les *notebooks*. Ceux-ci sont proposés
comme outil pour vous aider à vous familiariser avec le langage.

## Ressources

Le répertoire *assets* contient des fichiers issus de
l'[Opendata de la SNCF](https://data.sncf.com/). Les droits appartiennent
évidemment à la SNCF et ces fichiers sont présents ici pour disposer de documents
 texte volumineux à parcourir et explorer.