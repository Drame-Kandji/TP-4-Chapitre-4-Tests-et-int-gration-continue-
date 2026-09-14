# Pipeline CI - SunuSanté

Nom / Groupe : Aliou Dramé & Mamadou Yassarou Dillo & Nafissatou Niang

## 1. Le workflow d'intégration continue (chapitre 4, partie 1)

Le cours décrit 6 étapes, du commit au feedback. Remplissez la colonne de
droite avec le nom exact du stage Jenkins qui correspond, tel qu'il
apparaît dans votre `Jenkinsfile` et dans la Stage View de Jenkins.

| Étape du cours | Stage Jenkins correspondant |
|---|---|
| 1. Commit & push | `Récupération du code` |
| 2. Notification (Jenkins est prévenu) | Aucun stage dédié : déclenchement configuré dans le job Jenkins |
| 3. Build | `Build` |
| 4. Feedback build | `Standard de code (lint)` puis statut du pipeline |
| 5. Tests automatiques | `Tests` |
| 6. Feedback tests | `post / success` ou `post / failure` |

Comment Jenkins est-il informé qu'un nouveau commit existe, dans votre
configuration (polling SCM, webhook, déclenchement manuel) ?

Dans la configuration locale fournie, le pipeline est lancé manuellement avec
**Build Now**. Jenkins récupère ensuite le commit via `checkout scm`. Avec un
dépôt distant, un webhook GitHub ou un polling SCM pourrait déclencher
automatiquement le même job.

## 2. Les prérequis d'une bonne CI (chapitre 4, partie 3)

| Prérequis | Statut sur SunuSanté | Détail |
|---|---|---|
| Dépôt avec versioning | OK | Dépôt Git local, sur la branche `corrections-tp04` ; il peut aussi être relié à un dépôt distant. |
| Standard de code vérifié | OK | `flake8 .` est exécuté dans le stage `Standard de code (lint)`. |
| Serveur d'intégration continue | OK | Jenkins local, avec un agent Docker basé sur `python:3.11-slim`. |

## 3. Pourquoi Jenkins, ici (chapitre 4, partie 4)

Le cours compare GitLab CI/CD, Jenkins et GitHub Actions. Remplissez ce
comparatif avec vos propres mots, puis justifiez en 2-3 phrases pourquoi
Jenkins convient (ou pas) à ce projet précis.

| Outil | Avantage principal | Inconvénient principal |
|---|---|---|
| GitLab CI/CD | CI/CD intégré à GitLab, avec une configuration centralisée | Dépend fortement de l'écosystème GitLab et de ses runners |
| Jenkins | Très extensible et compatible avec de nombreux SCM, langages et outils | Installation, plugins et maintenance à gérer soi-même |
| GitHub Actions | Très intégré à GitHub, avec des workflows faciles à versionner | Dépendance à GitHub et coût potentiel des minutes ou runners privés |

**Justification du choix pour SunuSanté :**

Jenkins convient à SunuSanté car le TP porte précisément sur l'intégration
continue et fournit déjà un `Jenkinsfile` versionné avec le projet. Son agent
Docker reproduit l'environnement Python et exécute de manière identique les
tests, le lint et les contrôles de sécurité.

## 4. CI, Continuous Delivery, déploiement continu

Sur les 3 périmètres vus en cours (CI : code source + tests + build ·
Continuous Delivery : + qualité + release manuelle · déploiement continu :
tout automatisé), lequel votre `Jenkinsfile` couvre-t-il aujourd'hui ?
Qu'est-ce qui manquerait pour passer au périmètre suivant ?

**Périmètre couvert :**

Le pipeline couvre la **CI** : récupération du code, installation des
dépendances, vérification du build Django, lint, tests automatiques et
contrôles de sécurité SAST/SCA. Il ne publie pas de release et ne déploie pas
l'application.

**Ce qui manquerait pour aller plus loin :**

Pour la Continuous Delivery, il faudrait ajouter une étape de packaging et
de publication d'un artefact ou d'une image, avec une validation ou un
déploiement manuel. Pour le déploiement continu, il faudrait automatiser le
déploiement vers un environnement cible, ainsi que sa configuration, ses
secrets, ses migrations et ses contrôles de santé.

## 5. Tests non fonctionnels hors scope

Le chapitre 4 liste aussi les tests capacitaires et de compatibilité,
absents de ce pipeline. Pourquoi, à l'échelle de ce TP, est-ce un choix
raisonnable plutôt qu'un oubli (indice : YAGNI, chapitre 2) ? Que
faudrait-il ajouter si SunuSanté grandissait réellement ?

Les tests capacitaires et de compatibilité sont raisonnablement hors scope
pour un petit TP : ils nécessitent plusieurs environnements, davantage de
données et des outils spécialisés, alors que l'objectif immédiat est de
valider la CI et la pyramide de tests avec un coût limité (YAGNI).

Si SunuSanté grandissait, il faudrait ajouter des scénarios de charge avec
Locust ou k6, mesurer les temps de réponse et les seuils de capacité, puis
exécuter une matrice de compatibilité sur les navigateurs, systèmes,
versions de Python et bases de données supportés.
