# Semaine 2/16

- [ ] Paradigme orienté objet
- [ ] Data Model (quelques bases)
- [ ] numpy
- [ ] Exercice

## Notes

- Tout est objet dans Python
- Le contenu des instances est accessible en interactif avec l'opérateur `.` (utiliser <tab> pour autocompléter)
- Il existe des méthodes "Magiques" qui commencent et se terminent par un double underscore p.ex. `__add__`
- L'initialiseur d'une class (une sorte de constructeur), c'est la méthode `__init__`
- Chaque méthode doit avoir, un argument `self`, qui est une référence à l'instance courante.

# Type scalaires

- Nombres entiers `n = 42`
- Nombres réels `f = 3.14`
- Booléens `b = False`
- Complexes `c = 1 + 2j`

Le typage est dynamique :

```python
>>> a = 12
>>> type(a)
int
>>> a = 12 + 0.1
>>> type(a)
float
```

# Type Composite

- Chaîne de caractère `'foo'`, `"foo"`
- Listes `[1, 2, 3]`

## Listes []

```python
>>> v = [12, 3.14, "hello", 12 + 2j]
>>> for element in v:
       print(type(element))
<class 'int'>
<class 'float'>
<class 'str'>
<class 'complex'>
```

- Ajouter un élément (à la fin)
- Ajouter un élément (au début)
- Ajouter un élément (après l'élément n)
- Supprimer le dernier élément
- Supprimer le premier élément
- Supprimer l'élément à la position n
- Indexer un élément (aller chercher une valeur à une position particulière)
- Compter le nombre d'éléments

## Tuples ()

C'est une liste non modifiable

## Set {}

C'est liste non ordonnée d'éléments uniques

## Dictionnaire {key: valeur}

Association de paires "clé" et "valeur"

