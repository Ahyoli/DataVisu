import pandas as pd
import os

# Correspondance entre code département et région
correspondance_region = {
    '9': 'Ariege',
    '11': 'Aude',
    '12': 'Aveyron',
    '30': 'Gard',
    '31': 'Haute-Garonne',
    '32': 'Gers',
    '34': 'Herault',
    '46': 'Lot',
    '48': 'Lozere',
    '65': 'Hautes-Pyrenees',
    '66': 'Pyrenees-Orientales',
    '81': 'Tarn',
    '82': 'Tarn-et-Garonne'
}

# Définir les colonnes importantes à garder
important_columns = [
    'code_departement',
    'nom_departement',
    'nom_commune',
    'code_commune',
    'valeur_fonciere',
    'surface_reelle_bati',
    'nombre_pieces_principales',
    'type_local',
    'surface_terrain',
]

# Définir le répertoire où se trouvent les fichiers DVF
dvf_dir = 'your\folder'
print(f"Directory: {dvf_dir}")

# Lire les données des fichiers DVF
files = [os.path.join(dvf_dir, file) for file in os.listdir(dvf_dir) if file.endswith('.csv')]
dfs = [pd.read_csv(file, low_memory=False) for file in files]
df = pd.concat(dfs, ignore_index=True)

# Lire les fichiers de loyer avec le bon délimiteur
dvf_mai_open = pd.read_csv(r'\DVF\mai.csv', delimiter=';')
dvf_app_open = pd.read_csv(r'\DVF\app.csv', delimiter=';')

# Affichage des noms des fichiers CSV
print("Fichiers CSV analysés :")
for file in files:
    print(os.path.join(dvf_dir, file))

# Vérifier les colonnes des fichiers de loyer
print("Colonnes dans dvf_mai_open :")
print(dvf_mai_open.columns)

print("Colonnes dans dvf_app_open :")
print(dvf_app_open.columns)

# Renommer les colonnes selon les besoins
dvf_mai_open = dvf_mai_open[['DEP', 'LIBGEO', 'loypredm2']].rename(columns={'DEP': 'code_departement', 'LIBGEO': 'nom_commune', 'loypredm2': 'loypredm2_mai'})
dvf_app_open = dvf_app_open[['DEP', 'LIBGEO', 'loypredm2']].rename(columns={'DEP': 'code_departement', 'LIBGEO': 'nom_commune', 'loypredm2': 'loypredm2_app'})

# Convertir les colonnes de fusion en string pour assurer la correspondance
df['code_departement'] = df['code_departement'].astype(str)
dvf_mai_open['code_departement'] = dvf_mai_open['code_departement'].astype(str)
dvf_app_open['code_departement'] = dvf_app_open['code_departement'].astype(str)

# Vérifier et convertir les colonnes en string
print(f"df['code_departement'] type: {df['code_departement'].dtype}")
print(f"dvf_mai_open['code_departement'] type: {dvf_mai_open['code_departement'].dtype}")
print(f"dvf_app_open['code_departement'] type: {dvf_app_open['code_departement'].dtype}")

# Vérifier les valeurs uniques de type_local
print("Valeurs uniques de type_local dans df :")
print(df['type_local'].unique())

# Informations par département
departement_info = {
    'code_departement': ['9', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82'],
    'nom_departement': ['Ariege', 'Aude', 'Aveyron', 'Gard', 'Haute-Garonne', 'Gers', 'Herault', 'Lot', 'Lozere',
                        'Hautes-Pyrenees', 'Pyrenees-Orientales', 'Tarn', 'Tarn-et-Garonne'],
    'nombre_transactions_maisons': [6735, 15873, 6456, 21308, 27088, 6565, 29960, 6139, 2000, 6166, 13954, 11406, 7599],
    'taux_transaction_maisons': [7.63, 8.41, 4.78, 7.81, 7.36, 7.20, 8.34, 6.12, 4.16, 6.25, 6.93, 6.71, 7.20],
    'nombre_transactions_appartements': [1121, 6376, 2665, 12323, 33000, 1190, 36364, 794, 308, 5236, 10648, 1970, 1905],
    'taux_transaction_appartements': [5.27, 8.43, 5.64, 7.73, 8.68, 5.93, 9.48, 4.27, 2.33, 8.22, 6.88, 4.40, 6.72],
    'population_2021': [157000, 377000, 279000, 748000, 1480000, 197000, 1564000, 174000, 76000, 230000, 480000, 387000, 263000],
    'population_2015': [153000, 360000, 276000, 736000, 1400000, 196000, 1444000, 173000, 76000, 224000, 471000, 388000, 261000],
    'pourcentage_chomage_2021': [10, 10.4, 6, 10.6, 8.4, 6.2, 11.1, 7.9, 4.9, 9.1, 12.3, 7.9, 9.2],
    'pourcentage_chomage_2020': [9.9, 10.4, 6, 10.6, 8.2, 6.1, 11, 7.80, 4.7, 8.8, 12.2, 8, 9.2],
    'pourcentage_taux_cambriolages': [3.1, 5.9, 1.8, 6.0, 8.5, 4.1, 5.7, 2.6, 1.3, 2.9, 4.0, 4.9, 5.1],
    'evolution_2016_2021': [-36.8, -23.7, -38.7, -27.6, -38.1, -42.3, -30.1, -46.3, -31.7, -34.6, -25.6, -35.6, -51.6]
}

# Convertir les informations par département en DataFrame
departement_info_df = pd.DataFrame(departement_info)

# Convertir la colonne 'code_departement' en string dans departement_info_df
departement_info_df['code_departement'] = departement_info_df['code_departement'].astype(str)

# Vérifier si les colonnes 'population_2021' et 'population_2015' sont bien présentes
if 'population_2021' in departement_info_df.columns and 'population_2015' in departement_info_df.columns:
    print("Les colonnes 'population_2021' et 'population_2015' sont bien présentes dans departement_info_df.")
else:
    print("Les colonnes 'population_2021' et 'population_2015' ne sont pas présentes dans departement_info_df.")

# Vérifier les types de colonnes avant la fusion
print(f"df['code_departement'] type before merge: {df['code_departement'].dtype}")
print(f"departement_info_df['code_departement'] type before merge: {departement_info_df['code_departement'].dtype}")

# Fusionner les données immobilières avec les informations par département
merged_df = pd.merge(df, departement_info_df, on='code_departement', how='inner')

# Ajouter la colonne 'nom_region' en utilisant la correspondance
merged_df['nom_region'] = merged_df['code_departement'].map(correspondance_region)

# Supprimer les lignes où la colonne 'surface_reelle_bati' est vide
merged_df.dropna(subset=['surface_reelle_bati', 'surface_terrain'], inplace=True)

# Sélectionner uniquement les colonnes importantes dans l'ordre requis
merged_df = merged_df[important_columns + ['population_2021', 'population_2015', 'pourcentage_chomage_2021', 'pourcentage_chomage_2020', 'pourcentage_taux_cambriolages', 'evolution_2016_2021']]

# Fusionner avec les loyers de maisons
merged_df = pd.merge(merged_df, dvf_mai_open, on=['code_departement', 'nom_commune'], how='left')

# Fusionner avec les loyers d'appartements
merged_df = pd.merge(merged_df, dvf_app_open, on=['code_departement', 'nom_commune'], how='left')

# Vérifier les valeurs après la fusion
print("Aperçu des valeurs après la fusion avec dvf_mai_open et dvf_app_open :")
print(merged_df[['code_departement', 'nom_commune', 'loypredm2_mai', 'loypredm2_app']].head())

# Ajouter la colonne 'loyer_moyen' en fonction du type de local
def get_loyer_moyen(row):
    if row['type_local'] == 'Maison':
        return row['loypredm2_mai']
    elif row['type_local'] == 'Appartement':
        return row['loypredm2_app']
    return None

merged_df['loyer_moyen'] = merged_df.apply(get_loyer_moyen, axis=1)

# Vérifier les valeurs de la colonne loyer_moyen
print("Aperçu des valeurs de loyer_moyen :")
print(merged_df[['type_local', 'loyer_moyen']].head())

# Supprimer les colonnes intermédiaires
merged_df.drop(columns=['loypredm2_mai', 'loypredm2_app'], inplace=True)

# Enregistrer le DataFrame final dans un fichier CSV
csv_file = 'dvf_occitanie_final_with_loyers.csv'
merged_df.to_csv(csv_file, index=False)

print(f"Fichier CSV '{csv_file}' généré avec succès!")
