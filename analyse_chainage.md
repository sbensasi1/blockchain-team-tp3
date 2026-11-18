Analyse du chaînage cryptographique des blocs

## 1. Principe de liaison par empreinte (SHA-256)
Chaque bloc contient :
- Ses propres données (transactions, horodatage, index).
- L'empreinte cryptographique (empreinte_precedente) du bloc immédiatement antérieur.

## 2. Effet avalanche et détection d'altération
La fonction *SHA-256* produit une empreinte unique de 256 bits (64 caractères hexadécimaux). Si un seul caractère des données d'un bloc est modifié (par exemple passer de 10 unités à 1000 unités dans le bloc #1), son empreinte change complètement.

## 3. Conséquence sur l'intégrité de la chaîne
Comme le bloc #2 stocke l'ancienne empreinte du bloc #1 dans son champ empreinte_precedente, le lien cryptographique est rompu. La méthode verifier_integrite() détecte immédiatement l'incohérence sans avoir besoin d'une autorité centrale.
