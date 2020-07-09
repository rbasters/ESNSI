#************************************************************************
# Transcription du graphe sous forme de liste de listes
#************************************************************************

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

def distance(Noeud_A, Noeud_B) -> int:
    #************************************************************************
    # Donne la distance entre deux noeuds adjacents Noeud_A et Noeud_B
    # Entrée : Le noeud de départ
    # Sortie : la liste des noeuds adjacents
    #************************************************************************
    # on vérifie que les valeurs de départ et arrivée sont bien des entiers
    assert type(Noeud_A) == int, "la valeur départ n'est pas un entier"
    assert type(Noeud_B) == int, "la valeur départ n'est pas un entier"
    assert graphe[Noeud_A][Noeud_B] != 99, "les noeuds ne sont pas adjacent"

    # On retourne la distance entre les deux noeuds
    return(graphe[Noeud_A][Noeud_B])


def determine_adjacents(noeud) -> list:
    #************************************************************************
    # A partir d'un noeud en entrée, la fonction donne la liste des noeuds adjacents
    # Entrée : Le noeud de départ
    # Sortie : la liste des noeuds adjacents
    #************************************************************************
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

    # On retourne la liste des noeuds adjacents
    return(liste_adjacents)

def recursive2(liste) -> list:
    #************************************************************************
    # La fonction récursive établit la liste exhaustive des chemins possibles
    # Entrée : La liste de chemins déja établie
    # Sortie : la liste de chemins jusqu'au noeuds suivants
    #************************************************************************

    sommets_adjacents = []
    # On détermine le nombre d'arcs adjacents aux noeuds
    for i in range(0,len(liste)): # on boucle dans notre liste existante
        for element in determine_adjacents(liste[i][-1]): # pour chaque sommet dans la liste des adjacents
            if element not in sommets_adjacents:          # si le sommets n'est pas encore dans notre liste
                 sommets_adjacents.append(element)        # alors on le rajoute

    # On identifie les chemins qu'on doit créer, en ignorant les chemins:
        # - où on revient sur un noeud déja visité
        # - déja existant dans la liste
        # Puis on renseigne les chemins possibles

    entrees_a_supprimer = []                              # On va garder en mémoire les entrées a supprimer
    for i in range(0,len(liste)) :                        # on boucle dans notre liste existante
        if liste[i][-1] != arrivée:                       # on ignore les chemins menant déja au point d'arrivée
            for j in range(0,len(sommets_adjacents)):     # on boucle dans la liste qu'on vient d'obtenir
                if (sommets_adjacents[j][0] == liste[i][-1] and
                    sommets_adjacents[j][-1] != liste[i][0] and
                    sommets_adjacents[j][-1] not in liste[i]
                    ):
                    liste.append(liste[i] + sommets_adjacents[j][1:len(sommets_adjacents)])
            entrees_a_supprimer.append(i)                 # On va garder en mémoire les entrées a supprimer

    for i in range(0,len(entrees_a_supprimer)):           # avant de retourner notre résultat on supprime les entrées superflus
        del liste[entrees_a_supprimer[i]-i]
    return(liste)


#********************************************************************************
# Début du programme principal
#********************************************************************************

# on définit un point de départ et d'arrivée
départ = 0
arrivée = 6
passages =[2,7]

# On détermine le nombre d'arcs partant de notre sommet départ
liste_arcs_départs = determine_adjacents(départ)


# Construction de la liste de chemins possibles
for i in range(0,len(graphe)):
    liste_arcs_départs = recursive2(liste_arcs_départs)

# On imprime le nombre de chemins et les chemins possibles
print("Il y a",len(liste_arcs_départs),"chemins possibles:",liste_arcs_départs)

# On identifie le chemin le plus court
this_distance = 0
court_distance = 9999
court_chemin =[]

for element in liste_arcs_départs:
    this_distance = 0
    for i in range(0,len(element)-1):
        this_distance += distance(element[i],element[i+1])
    if (this_distance < court_distance and
        passages[0] in element and
        passages[1] in element
        ):
        court_distance = this_distance
        court_chemin = element

# Ecrivez votre réponse à la question 5.1 ici
print("Le chemin le plus court est:", court_chemin)
print("La distance a parcourir est:", court_distance)