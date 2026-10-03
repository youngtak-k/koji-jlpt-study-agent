# Koji — JLPT Study Agent

Préparez le JLPT N5–N1 avec votre propre manuel, dans votre langue. Résolvez une question difficile, choisissez un travail adapté au temps disponible et reprenez là où vous en étiez.

## Commencez par une question

**Dans un chat avec une IA que vous utilisez déjà :** importez ou collez le [guide Koji](../agent/COACH.md), puis posez votre question. Ajoutez, si nécessaire, la phrase concernée, les choix et votre réponse. Utilisez un court extrait ou une photo lisible que le chat peut traiter.

> Suis ce guide Koji. Explique-moi en français. J’ai choisi B, mais le corrigé indique C. Voici le passage et mon raisonnement. Pourquoi C convient-il mieux ?

**Dans Codex ou Claude Code avec accès aux fichiers :** [téléchargez ce dépôt](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), décompressez-le et ouvrez le dossier. Demandez :

> Lis AGENTS.md et aide-moi à étudier avec Koji. Explique-moi en français et rédige mes notes en français. Voici ma question sur le manuel.

Vous pouvez formuler ces demandes dans votre langue. Aucun serveur Koji, application distincte, installation de Python ou clé API du projet n’est nécessaire. Il faut avoir accès à un assistant IA capable de lire le guide ; ses limites et ses tarifs continuent de s’appliquer.

## Ou choisissez le travail du jour

Indiquez à Koji la section du manuel ouverte et le temps dont vous disposez. Ajoutez votre niveau JLPT visé s’il n’est pas encore connu.

> Je prépare le N3. Je commence cette section de grammaire et j’ai 25 minutes. Aide-moi à choisir le travail d’aujourd’hui.

Koji propose un point de départ, un point d’arrêt et un budget de temps comprenant révision, questions et bref bilan. Le titre d’un livre ne permet pas d’en déduire les pages ou le contenu. Vous pouvez commencer par une section avant d’établir un plan pour tout l’examen.

## Terminez en un message

> J’ai terminé les questions 1 à 4 en 18 minutes. J’ai eu besoin d’un indice pour la question 3. La prochaine est la 5.

Koji résume le travail réellement effectué, les incertitudes restantes et le point de reprise. Poser une question ne compte pas automatiquement comme une erreur ; une réponse obtenue avec un indice reste distincte d’une réponse autonome.

Si l’accès aux fichiers fonctionne, Koji enregistre et vérifie votre état actuel dans `local/CURRENT.md`, avec des notes de séance complémentaires. Dans un chat ordinaire, il fournit une note d’étude compacte et actualisée à enregistrer vous-même. Générer une note ne signifie pas l’enregistrer automatiquement en local.

## Revenez et poursuivez

> Continuons. J’ai 15 minutes aujourd’hui.

Conservez le même dossier d’étude ou fournissez votre dernière note enregistrée dans le nouveau chat. Koji utilise les éléments antérieurs pertinents pour proposer une courte révision et le prochain travail dans le manuel. Par exemple, une distinction comprise grâce à un indice peut faire l’objet d’une brève vérification sans aide avant de continuer.

Après une pause, dites-le :

> Je n’ai pas étudié pendant une semaine. J’ai 10 minutes aujourd’hui.

Koji repart des progrès confirmés et réduit la tâche en fonction du temps. Les jours manqués ne deviennent pas des heures supplémentaires de rattrapage obligatoire. Vous pouvez aussi demander un bilan hebdomadaire, corriger un enregistrement, exporter votre note actuelle ou dire « n’enregistre pas cette séance ».

## Vos notes grandissent avec votre apprentissage

Le guide est le ferment de départ ; votre étude fournit la matière. Les explications utiles qui reviennent peuvent devenir des pages de connaissances liées entre elles, distinctes des preuves de ce que vous savez répondre. Vous n’avez pas à organiser les dossiers ni à tenir un second carnet vous-même.

Vos fichiers d’étude restent dans `local/`, exclu de Git par défaut. Conservez ce dossier lorsque vous mettez Koji à jour : remplacez les fichiers du guide partagé, pas vos données d’apprentissage. Le stockage local ne signifie pas que l’IA traite les données hors ligne. Koji travaille pendant vos conversations, sans rappels en arrière-plan ni synchronisation automatique entre copies.

Les explications et notes suivent vos préférences linguistiques, avec des exemples japonais et les lectures des kanji. Le guide est rédigé en anglais. Les traductions du README sont produites par IA et n’ont pas fait l’objet d’une révision indépendante par des locuteurs natifs ; l’édition anglaise fait référence.

## Langues du README

- [English](../README.md)
- [한국어](README.ko.md)
- [日本語](README.ja.md)
- [Español](README.es.md)
- [Français](README.fr.md)
- [Deutsch](README.de.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)
- [Português (Brasil)](README.pt-BR.md)
- [Italiano](README.it.md)
- [Русский](README.ru.md)
- [Українська](README.uk.md)
- [Polski](README.pl.md)
- [Nederlands](README.nl.md)
- [Svenska](README.sv.md)
- [Dansk](README.da.md)
- [Norsk (bokmål)](README.no.md)
- [Suomi](README.fi.md)
- [Čeština](README.cs.md)
- [Türkçe](README.tr.md)
- [Bahasa Indonesia](README.id.md)
- [Tiếng Việt](README.vi.md)
- [ไทย](README.th.md)
- [हिन्दी](README.hi.md)
- [বাংলা](README.bn.md)
- [العربية](README.ar.md)
- [فارسی](README.fa.md)
- [עברית](README.he.md)
- [Bahasa Melayu](README.ms.md)
- [Filipino](README.tl.md)
