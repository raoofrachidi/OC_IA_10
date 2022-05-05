# Développez un chatbot pour réserver des vacances

Fly Me est une agence qui propose des voyages clé en main pour les particuliers ou les professionnels. 

Fly Me a lancé un projet ambitieux de développement d’un chatbot pour aider les utilisateurs à choisir une offre de voyage.

La première étape de ce projet est de construire un MVP qui aidera les employés de Fly Me à réserver facilement un billet d’avion pour leurs vacances.

La V1 devra pouvoir identifier dans la demande de l’utilisateur les cinq éléments suivants :
* Ville de départ
* Ville de destination
* Date aller souhaitée du vol
* Date retour souhaitée du vol
* Budget maximum pour le prix total des billets.

Si un des éléments est manquant, le chatbot devra pouvoir poser les questions pertinentes (en anglais) à l’utilisateur pour comprendre complètement sa demande. Lorsque le chatbot pense avoir compris tous les éléments de la demande de l’utilisateur, il doit pouvoir reformuler la demande de l’utilisateur et lui demander de valider sa compréhension.

Il faudra t'appuyer sur ce jeu de données : https://www.microsoft.com/en-us/research/project/frames-dataset/#!download.

## Livrables

* L’application web chatbot développée à l’aide de la version Python du Microsoft Bot Builder SDK qui permettra à l’utilisateur de communiquer avec le chatbot (interface simple de messagerie style Whatsapp) et qui prendra en entrée les commentaires de l’utilisateur et renverra en sortie les réponses du chatbot ;
  * Ce livrable permettra de démontrer les fonctionnalités de l’application à des futurs utilisateurs 
* L’outil de suivi et d’analyse de l’activité du chatbot en production à l’aide d’Azure application insight
  * Ce livrable permettra de rassurer les managers qui s’inquiètent du suivi de la performance du chatbot en production.
* Une présentation de la méthodologie sur le pilotage de la performance du modèle en production contenant la description des critères d’évaluation du modèle, le schéma du mécanisme d’évaluation du modèle en production, les modalités de mise à jour du modèle (seuil, fréquence,…) :
  * Ce livrable vous permettra d’expliciter auprès de la product manager la méthodologie de pilotage et de mise à jour opérationnelle du modèle. 
* Les scripts développés stockés sur Github permettant l’exécution du pipeline complet pour générer l’application web chatbot, entraîner et évaluer le modèle :
  * Ce livrable vous servira à montrer le caractère “industrialisable” de votre travail.
* Une présentation Powerpoint pour présenter votre travail. 
