#!/usr/bin/env python3
"""Exemple de sous-programme (fonction). """
def index(sequence, element):
  """Chercher l'indice de la première occurrence de 'elemnt' dans 'sequence'
  
  :param sequence: la séquence
  :param element: l'élément cherché
  :returns: l'indice de la première occurrence de 'element'
  :raises ValueError: l'élément n'est pas dans la séquence
  """
  for indice, elt in enumerate(sequence):
    # print(indice, elt)
    if elt == element: # On l'a trouvé !
        return indice
  else: # jamais trouvé. Attention ici le else pour for pas pour if!
        raise ValueError('élement non trouvé')

if __name__ == "__main__": # Si Le fichier est exécuté comme programme principal 
    assert index([1, 4, 2, 6], 1) == 0
    assert index([1, 4, 2, 6], 4) == 1
    assert index([1, 4, 2, 6], 2) == 2
    assert index([1, 4, 2, 6], 6) == 3
    assert index('Bonjour', 'j') == 3
    try:
        ok = False
        index([1, 4, 2, 6], 7) # doit lever ValueError
    except ValueError:
        ok = True
    assert ok, "l'exception ValueError aurait dû se produire !"
