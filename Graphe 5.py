graphe = [
    [0 ,4 ,2 ,99,99,99,99,99],
    [4 ,0 ,6 ,99,5 ,99,99,99],
    [2 ,6 ,0 ,3 ,99,99,99,5 ],
    [99,99,3 ,0 ,99,3 ,4 ,1 ],
    [99,5 ,99,99,0 ,2 ,99,99],
    [99,99,99,3 ,2 ,0 ,7 ,99],
    [99,99,99,4 ,99,7 ,0 ,10],
    [99,99,5 ,1 ,99,99,10,0 ]
    ]
départ = 0
arrivée = 6

def determine_adjacents(noeud) -> list:
    #*******************************************
    # Assert a faire
    #*******************************************
    # On sélectionne la ligne contenant les noeuds adjacent par rapport a notre point de départ
    ligne = graphe[noeud]

    # on détermine le nombre de noeuds adjacents pour ce point
    nb_adjacent = len(ligne)-ligne.count(99)-ligne.count(0)

     # Puis on crée la variable parcours sous forme de liste de listes
    liste_adjacents = [[] for i in range(0,nb_adjacent)]

    a = 0
    for i in range(0,len(ligne)):
        if (ligne[i] != 0 and ligne[i] != 99):
            liste_adjacents[a].append(noeud)
            liste_adjacents[a].append(i)
            a += 1
    return(liste_adjacents)

def recursive(liste) -> list:
    #************************************************************************
    # La fonction cursive établi la liste exhaustive des chemins possibles
    # Entrée : La liste de chemins déja établie
    # Sortie : la liste de chemins jusqu'au noeuds suivants
    #************************************************************************
    # On détermine le nombre de arc au départ des noeuds adjacents
    for i in range(0,len(liste)):
        if i == 0:
            new_liste_arcs_départs = determine_adjacents(liste[i][-1])
        else:
            #on filtre les éventuels doublons
            list = determine_adjacents(liste[i][-1])
            for element in list:
                if element not in new_liste_arcs_départs:
                    new_liste_arcs_départs.append(element)

    nb_new_listes = 0
    for i in range(0,len(liste)): # on boucle dans notre liste existante
        if liste[i][-1] == arrivée:  # on comptabilise les chemins menant au point d'arrivée
            nb_new_listes += 1
        for j in range(0,len(new_liste_arcs_départs)): # on boucle dans la liste qu'on vient d'obtenir
            if (new_liste_arcs_départs[j][0] == liste[i][-1] and
                new_liste_arcs_départs[j][-1] != liste[i][0] and
                new_liste_arcs_départs[j][-1] not in liste[i] and
                liste[i][-1] != arrivée):
                nb_new_listes += 1
        new_listes = [[] for i in range(0,nb_new_listes)]

    # Puis on renseigne les chemins possibles
    index = 0
    for i in range(0,len(liste)): # on boucle dans notre liste existante
        if liste[i][-1] == arrivée:  # on comptabilise les chemins menant au point d'arrivée
            new_listes[index] = liste[i]
            index += 1
        for j in range(0,len(new_liste_arcs_départs)): # on boucle dans la liste qu'on vient d'obtenir
            if (new_liste_arcs_départs[j][0] == liste[i][-1] and
                new_liste_arcs_départs[j][-1] != liste[i][0] and
                new_liste_arcs_départs[j][-1] not in liste[i] and
                liste[i][-1] != arrivée
               ):
                new_listes[index] = liste[i] + new_liste_arcs_départs[j][1:len(new_liste_arcs_départs)]
                index += 1
    return(new_listes)

# On détermine le nombre d'arcs au départ de notre noeud
liste_arcs_départs = determine_adjacents(départ)

#my_liste = recursive(liste_arcs_départs)
#print(my_liste)

#liste = recursive(my_liste)
#print(liste)

for i in range(0,len(graphe)):
    liste_arcs_départs = recursive(liste_arcs_départs)

print(liste_arcs_départs)

print(liste_arcs_départs)

this_distance = 0
court_distance = 9999
court_chemin =[]

for element in liste_arcs_départs:
    this_distance = 0
    for i in range(0,len(element)-1):
        this_distance += distance(element[i],element[i+1])
    if this_distance < court_distance:
        court_distance = this_distance
        court_chemin = element

print("le chemin le plus court est :",court_chemin)
print("la distance a parcourir est de:",court_distance )
