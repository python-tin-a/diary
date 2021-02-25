# Semaine 1/16

- [x] Tour de table
- [x] Fiche d'unité
- [x] Littérature et ressources
- [x] Git / GitHub
- [x] Présentation succinte de Python
- [x] Modes d'utilisation
- [x] Présentation WSL / Anaconda

Travail pratique :

- [ ] Installation d'un environnement Python (3.8.x .. 3.9.x)
- [ ] Installation de IPython
- [ ] Prise en main de vscode
  - [ ] Créer un fichier Python
  - [ ] L'exécuter avec un breakpoint
- [ ] Installer un paquet avec Pip
  - [ ] Installer le paquet `pint`
  - [ ] Essayer d'utiliser `pint` (depuis Ipython)

## Installation Python sous "Ubuntu 20.04"

```console
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install -U pint
```

## Références

- [StackOverflow](https://stackoverflow.com/)
- [Learn X in Y](https://learnxinyminutes.com/docs/python/)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- Learning Python Mark Lutz ISBN 978-1-449-35573-9
- Python Cookbook ISBN 978-1-449-34037-7
- [Python Source](https://github.com/python/cpython)
- [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)

## C'est quoi Python

- Python c'est un programme créé en 1990 (Guido van Rossum)
- Open-source (les sources disponibles sur GitHub)
- Langage vivant (à vous de vous adapter aux évolution du langage)
- Langage multiparadigmes (impératif, procédural, l'objet, fonctionnel, réflectif...)
- Une interface interactive (REPL) : ipython
- C'était un langage interprété aujourd'hui un langage JIT (Just In Time)
- Python c'est un langage écrit en C, et en Python.

## Utilisation de Python

1. En ligne de commande
2. En mode interactif
3. Via IDE en mode debug (Visual Studio Code ou [PyCharm](https://www.jetbrains.com/pycharm/))
4. Jupyter Notebook (`jupyter notebook`, `pip3 install -U jupyter-notebook`)

## REPL

1. Repeat
2. Evaluate
3. Parse
4. Loop (goto 1)

## Installation de Python 3

(Python 2 est obsolète)

1. Python under POSIX (WSL, Windows Subsystem For Linux)
2. [Python for Windows](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)
3. [Anaconda](https://www.anaconda.com/)
4. Python via Docker

## WSL 1 ou 2

1. Activer fonctionnalité WSL sous Windows (+ reboot)
2. Installer Kernel linux (https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
3. Ubuntu 20.04 depuis le Windows Store
  a. Enter a login (court, et en minuscule)
  b. Password
  c. Repeat your password
  d. `sudo apt-get update`
  e. `sudo apt-get install python3 python3-pip`
4. `pip3 install -U ipython`

## Tour de table

- C (impératif et du procédural)
- TSA (Bressy Python) Jupyter Docker
- Un peu de Python (Minecraft)
- ProgOOx
- Automate programmable (IEC 1131-3)

## Trucs et astuces

### Copier Coller sous "Bash" (Git Bash ou Linux Terminal)

- **Copier**: Selectionner simplement le texte sous Windows Terminal
- **Coller**: <M-Ins> (majuscule insert) ou clic droit de la souris
