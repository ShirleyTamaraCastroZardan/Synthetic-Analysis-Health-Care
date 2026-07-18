import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# 1. Chargement des données
# ============================
df = pd.read_csv("healthcare_dataset.csv", sep=",")

# ============================
# 2. Data Quality Test : Billing Amount < 0
# ============================

# Correction : mettre les noms en majuscule

df["Name"] = df["Name"].str.title()

# Filtrer les patients avec un Billing Amount négatif
billing_negatif = df[df["Billing Amount"] < 0]

print("\n=== Data Quality Test : Patients avec Billing Amount < 0 ===")

if billing_negatif.empty:
    print("Aucun patient avec un Billing Amount négatif. Les données sont propres.")
else:
    print("ATTENTION : Des valeurs négatives ont été trouvées dans Billing Amount :")
    print(billing_negatif.iloc[:, :10])

# Correction : transformer les valeurs négatives en positives / deux décimales
df["Billing Amount"] = df["Billing Amount"].abs()

df["Billing Amount"] = df["Billing Amount"].round(2)

# ============================
# 3. Analyses globales
# ============================

# Quantité totale par Medical Condition
patients_par_condition = df["Medical Condition"].value_counts()
print("\n--- Quantité totale par Medical Condition ---")
print(patients_par_condition)

# Quantité totale par Hospital
patients_par_hopital = df["Hospital"].value_counts()
print("\n--- Quantité totale par Hospital ---")
print(patients_par_hopital)

# Quantité totale par Insurance Provider
patients_par_assurance = df["Insurance Provider"].value_counts()
print("\n--- Quantité totale par Insurance Provider ---")
print(patients_par_assurance)

# Moyenne du coût par Medical Condition
cout_moyen_par_condition = df.groupby("Medical Condition")["Billing Amount"].mean().round(2)
print("\n--- Coût moyen par Medical Condition ---")
print(cout_moyen_par_condition)

# ============================
# TABLE : Hôpital et Assurance moins cher / plus cher par Medical Condition
# ============================

# Coût moyen par hôpital et condition
cout_hopital_condition = df.groupby(["Medical Condition", "Hospital"])["Billing Amount"].mean()

# Hôpital le moins cher par condition
moins_cher_par_condition = cout_hopital_condition.groupby(level=0).idxmin()
# Hôpital le plus cher par condition
plus_cher_par_condition = cout_hopital_condition.groupby(level=0).idxmax()

# Construction de la table finale
table_hopitaux = []

for condition in cout_hopital_condition.index.levels[0]:
    hopital_moins_cher = moins_cher_par_condition[condition][1]
    hopital_plus_cher = plus_cher_par_condition[condition][1]

    # Coûts arrondis
    cout_moins_cher = round(cout_hopital_condition[condition][hopital_moins_cher], 2)
    cout_plus_cher = round(cout_hopital_condition[condition][hopital_plus_cher], 2)

    # Trouver l'assurance liée à cet hôpital et condition
    assurance_moins_cher = (
        df[(df["Medical Condition"] == condition) & (df["Hospital"] == hopital_moins_cher)]
        .sort_values("Billing Amount")
        ["Insurance Provider"]
        .iloc[0]
    )

    assurance_plus_cher = (
        df[(df["Medical Condition"] == condition) & (df["Hospital"] == hopital_plus_cher)]
        .sort_values("Billing Amount", ascending=False)
        ["Insurance Provider"]
        .iloc[0]
    )

    table_hopitaux.append({
        "Medical Condition": condition,
        "Hôpital moins cher": hopital_moins_cher,
        "Coût moins cher": cout_moins_cher,
        "Insurance Provider": assurance_moins_cher,
        "Hôpital plus cher": hopital_plus_cher,
        "Coût plus cher": cout_plus_cher,
        "Insurance Provider (plus cher)": assurance_plus_cher
    })

df_hopitaux = pd.DataFrame(table_hopitaux)

print("\n=== Tableau : Hôpital moins cher / plus cher par Medical Condition ===")
print(df_hopitaux)

# ============================
# 4. Visualisations
# ============================

sns.set(style="whitegrid")

# --- Tableau : Quantité totale par Medical Condition ---

fig, ax = plt.subplots(figsize=(10,4))
ax.axis('tight')
ax.axis('off')

table = ax.table(
    cellText=patients_par_condition.reset_index().values,
    colLabels=["Medical Condition", "Quantité"],
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Quantité totale par Medical Condition")
plt.show()


# --- Tableau : Quantité totale par Insurance Provider ---

fig, ax = plt.subplots(figsize=(10,4))
ax.axis('tight')
ax.axis('off')

table = ax.table(
    cellText=patients_par_assurance.reset_index().values,
    colLabels=["Insurance Provider", "Quantité"],
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Quantité totale par Insurance Provider")
plt.show()

#

fig, ax = plt.subplots(figsize=(10,4))
ax.axis('tight')
ax.axis('off')

table = ax.table(
    cellText=cout_moyen_par_condition.reset_index().values,
    colLabels=["Medical Condition", "Coût moyen"],
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Coût moyen par Medical Condition (arrondi)")
plt.show()

# --- Tableau : Hôpital moins cher / plus cher par Medical Condition ---

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14,6))
ax.axis('tight')
ax.axis('off')

table = ax.table(
    cellText=df_hopitaux.values,
    colLabels=df_hopitaux.columns,
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Tableau : Coût min. / max. Hôpital et Assurance par Medical Condition")
plt.show()
