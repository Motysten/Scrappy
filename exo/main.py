# Importation des libraries
import pandas as pd
import numpy as np
import re

# Ouverture et affichage simplifié du fichier CSV
data = pd.read_csv('operations.csv')

# On remarque qu'il manque 2 montants et 1 categ
print(data.isnull().sum())

# On récupère donc les lignes concernées
print(data.loc[data['montant'].isnull(), :])
print(data.loc[data['categ'].isnull(), :])

# On réattribue le montant si nécessaire a l'aide du solde précédent et du solde actuel
missing_montant = data.loc[data['montant'].isnull(), :]
for i in missing_montant.index:
    data.loc[i, 'montant'] = data.loc[i + 1, 'solde_avt_ope'] - data.loc[i, 'solde_avt_ope']

# On attribue ensuite la catégorie manquante (On défini "FACTURE TELEPHONE" car c'est la categorie assignée a toutes les operations du meme libellé)
data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'

# Il y a également 1 doublon
print(data.loc[data[['date_operation', 'libelle', 'montant', 'solde_avt_ope', 'categ']].duplicated(keep=False),:])

# On supprime donc le doublon
data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope', 'categ'], inplace=True, ignore_index=True)

# Enfin on remarque que les dates ne sont pas stockées dans le bon format
print(data.dtypes)

# On convertit donc nos dates dans le bon format
data['date_operation'] = pd.to_datetime(data['date_operation'])

data.to_csv('operations.csv')