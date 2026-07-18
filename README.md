# Synthetic-Analysis-Health-Care
Data Quality and Preview Analysis for the data set : Healthcare Dataset found in Kaggle (https://www.kaggle.com/datasets/prasad22/healthcare-dataset). À partir de ce dataset, il est possible de formuler la conclusion suivante :

# 1. Coût moyen par condition médicale : des écarts faibles mais révélateurs
Les coûts moyens par condition médicale sont étonnamment proches : tous se situent entre **25 164 €** (Cancer) et **25 808 €** (Obésité).  
Cette faible dispersion suggère que **le coût global des soins est relativement homogène**, quel que soit le diagnostic. 

# 2. Hôpital le moins cher / plus cher : un contraste extrême
Le deuxième tableau est le plus frappant : il montre des **écarts gigantesques** entre l’hôpital le moins cher et le plus cher pour chaque condition.

Exemple :  
- **Arthritis** : de **26 €** à **52 170 €**  
- **Cancer** : de **9 €** à **52 373 €**  
- **Hypertension** : de **23 €** à **52 764 €**

Ces écarts ne sont pas simplement importants : ils sont **structurellement disproportionnés**. 

Cela révèle :

## 1. Une variabilité extrême des pratiques tarifaires
Certains hôpitaux facturent des montants symboliques (9 €, 23 €, 36 €), ce qui semble presque irréaliste pour des soins médicaux.  
D’autres appliquent des tarifs massifs dépassant les **52 000 €**.

## 2. Le rôle des assureurs
Les assureurs associés aux hôpitaux les plus chers sont variés : Cigna, Aetna, Blue Cross, Medicare.  
Cela montre que **l’assureur n’est pas le facteur déterminant du coût**, mais plutôt l’hôpital lui-même.

## 3. Quantité totale par condition médicale : une distribution équilibrée
Les quantités par condition médicale sont très proches : entre **9185** (Asthma) et **9308** (Arthritis).  

Arthritis est légèrement en tête, ce qui peut refléter une prévalence plus élevée ou un dépistage plus systématique.

## 4. Quantité totale par assureur : un marché très équilibré
Les assureurs ont des volumes très proches également : entre **10 913** (Aetna) et **11 249** (Cigna).  

Cigna apparaît comme l’assureur le plus présent, mais l’écart reste faible.

## **Question pour aller plus loin**
Souhaites‑tu que je transforme cette analyse en **présentation PowerPoint**, **rapport écrit**, ou **visualisations graphiques** pour ton projet de data ?
