print("=== GESTION DES TACHES ===")
print("1.ajouter une tache  2.afficher  3.rechercher  0.quitter")
ls=[]
choix=input("votre choix :")
if int(choix)==1:
    titre=input("titre de la tache :")
    if titre=="":
        print("erreur, saisie est vide")
    else:
        ls.append(titre)
        print("tache ajoutee")
elif int(choix)==2:
    if len(ls)==0:
        print("aucune tache")
    else:
        print(ls)
elif int(choix)==0:
    print("see ya")
