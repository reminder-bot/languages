# noinspection PyStatementEffect
{
    '__full__': 'français',

    '__maintainer__': '@Matheo_33',

    'flag': '🇫🇷',

    'blacklisted': ''': x: Cette chaîne est blacklistée: x:''',

    'help': '''Veuillez visiter https://reminder-bot.com/help?lang=FR''',

    'no_perms_webhook': '''** AVERTISSEMENT **: Pour définir des rappels, j'ai besoin de l'autorisation `Gérer les webhooks`.''',

    'no_perms_embed_links': '''** AVERTISSEMENT **: Pour fonctionner, j'ai besoin de l'autorisation `Embed Links`.''',

    'no_perms_general': '''Action interdite. Veuillez vous assurer que j'ai les autorisations appropriées. ''',

    'no_perms_managed': '''Vous devez avoir `Manage Messages` ou avoir un rôle capable d'envoyer des rappels à ce canal. Veuillez parler à l'administrateur de votre serveur et demandez-lui d'utiliser la commande `{prefix} restrict` pour spécifier les rôles autorisés. ''',

    'no_perms_restricted': '''Vous devez avoir le niveau d'autorisation `Gérer le serveur` ou supérieur pour utiliser cette commande.''',

    'help_raw': [
        ['''Commandes de rappel''', {
            '$natural': '''Méthode plus simple pour définir des rappels. Veuillez exécuter cette commande pour plus d'informations.''',

            '$del': 'Supprimez les rappels et les intervalles sur votre serveur. Si les rappels sont configurés pour les DM, envoyez cette commande au bot. ',

            '$look [n] [channel] [enabled] [time]': '''Afficher les rappels dans une chaîne. S'il est fourni, <code> n </code> se limitera à l'affichage des n prochains rappels. Si <code> enabled </code> est écrit, seuls les rappels activés seront affichés. Si <code> time </code> est écrit, l'heure exacte sera affichée plutôt que le décalage''',

            '$rappelle [utilisateur / canal] <time-to-reminder> <message>': '''Commande obsolète. Utilisez <code> $ natural </code> au lieu de cette commande. Créez un rappel. Prend des temps au format [num][s/m/h/d], par exemple 10s pendant 10 secondes ou 2s10m pendant 2 secondes 10 minutes. Une heure exacte peut être fournie sous la forme <code>jour/mois/année-heure:minute:seconde</code>.''',

            '$interval [user/channel] <time-to-reminder> <interval> <message>': '''<strong><a href="https://patreon.com/jellywx/">Patron uniquement.</a> </strong> Commande obsolète. Utilisez <code>$natural</code> au lieu de cette commande. Définissez un rappel récurrent à partir de l '<code>heure de rappel</code> donnée. Prend des temps dans les formats normaux, ex. <code> $ intervalle 0s 20m Hello World! </code> enverra \ ' Hello World! \ ' sur votre chaîne toutes les 20 minutes.''',

            '$offset': '''Décaler les rappels d'un serveur entier d'une heure définie (aide à tenir compte de l'heure d'été)''',
        }],

        ['''Commandes de gestion''', {
            '$timezone': '''Définir votre serveur, fuseau horaire de, pour les rappels à base de date plus facile.''',

            '$lang <nom>': '''Changez la langue.''',

            '$nudge <time>': '''Activer le nudging sur le canal actuel. Cela vous permet de synchroniser tous les futurs rappels à la seconde avec des choses comme dans les horloges de jeu''',

            '$pause [time]': '''Silence les rappels sur la chaîne actuelle. Un délai d'attente pour cela peut être fourni en option, sinon les rappels sont désactivés indéfiniment. Peut être désactivé avec la même commande''',

            '$restrict [role mention] [commands]': '''Changer quelles commandes peuvent être utilisées par quels rôles''',

            '$blacklist [channel-name]': '''Bloquer ou débloquer un canal de l'envoi de commandes.''',
        }],

        ['''Autres commandes''', {
            '$donation': 'Afficher des informations sur les dons.',

            '$prefix <string>': 'Changer le préfixe de $.',

            '$info': 'Obtenez des informations sur le bot.',

            '$clock': '''Obtenir l'heure actuelle dans le fuseau horaire de la guilde''',

            '$todo user': '''Commandes liées à la liste TODO. Utilisez <code> $ todo help </code> pour plus d'informations. ''',

            '$todo channel': '''Identique au <code>$todo server</code> mais pour la gestion des tâches basée sur le canal.''',

            '$todo server': '''Identique à <code>$todo channel</code> mais pour la gestion des tâches basée sur le serveur.''',

            '$alias': '''Enregistre une commande sous un nom réutilisable plus court. Utilisez <code>$alias name command</code> pour configurer, par exemple <code>$alias rem natural en 10 minutes send hello</code>, puis utilisez <code>$alias name</code> pour rappeler''',

            '$timer': '''Règle une minuterie qui marque l'heure actuelle. Faites `$timer` pour plus d'informations.''',

        }]
    ],

    'info': '''
Préfixe par défaut: `{default_prefix}`
Réinitialiser le préfixe: `@{user} prefix {default_prefix}`
Aide: `{prefix}help`

**Bienvenue dans Reminder Bot!**
Développeur: <@203532103185465344>
Icône: <@253202252821430272>

Retrouvez-moi sur https://discord.jellywx.com et sur https://github.com/JellyWX :)
Invitez le bot: https://invite.reminder-bot.com/
Utilisez notre tableau de bord: https://reminder-bot.com/

*Si vous avez des questions sur les nouvelles fonctionnalités, veuillez les envoyer au serveur Discord *
''',

    'donate': '''
Vous envisagez d'ajouter une cotisation mensuelle? Cliquez ci-dessous pour mon serveur patreon et bot officiel: 
https://www.patreon.com/jellywx/
https://discord.jellywx.com/

Voici quelques informations supplémentaires:
Lorsque vous faites un don, Patreon vous classera automatiquement sur notre serveur Discord, en supposant que vous ayez correctement lié vos comptes Patreon et Discord!

Avec votre nouveau rang, vous pourrez:
: définir des rappels répétés avec `interval`,`natural` ou le tableau de bord
: utilisez des téléchargements illimités sur SoundFX

Quiconque est un partisan de Patreon, merci: D Vous rendez ce bot durable
Veuillez noter que vous devez être connecté au serveur Discord pour recevoir des récompenses Patreon.
''',

    'prefix': {

        'no_argument': '''
Veuillez utiliser cette commande comme `@ reminder-bot prefix <prefix>`
''',
        'succès': '''
Le préfixe a été remplacé par {prefix}
''',

        'too_long': '''Veuillez sélectionner un préfixe de moins de 5 caractères'''
    },

    'timezone': {

        'no_argument': '''
Usage:
```{prefix}timezone <Nom>```
Exemple:
```{prefix}timezone Europe/Paris```
Tous les fuseaux horaires: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'no_timezone': '''Fuseau horaire non reconnu. Une liste est disponible sur https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'footer': '''Fuseau horaire actuel: {timezone}''',

        'set_p': '''Le fuseau horaire personnel a été défini sur {timezone}. Votre heure actuelle devrait être {time} ''',
    },

    'alias': {

        'help': '''Utilisation:
`{prefix}alias <name> <command>`: attache un alias à une commande
`{prefix}alias <name>`: rappelle une commande attachée à un alias
`{prefix}alias list`: liste des alias
`{prefix}alias remove <name>`: remove an existing alias ''',

        'invalid_command': '''Veuillez utiliser une commande dans le texte de l'alias. Cette commande ne peut pas être la commande alias ''',

        'not_found': '''Aucun alias trouvé avec le nom `{nom}` `''',

        'created': '''Nouvel alias `{name}` created''',

        'supprimé': '''{count} alias supprimé.'''
    },

    'restrict': {

        'disabled': '''Désactivation des autorisations de commande restrictives pour les rôles.''',

        'enabled': '''Autorisations de commande activées pour les rôles.''',

        'allowed': '''Règles: {}''',

        'failure': '''Impossible d'attribuer les autorisations pour la commande `{commande}`. Cette commande n'existe pas ou ne fonctionne que sur les restrictions prédéfinies ''',

        'help': '''Utilisation:
**Réinitialiser les restrictions de rôle**
`$restrict @RoleName`

**Permit Command (par exemple `natural` et son alias `n`)**
`$restrict @RoleName natural`

**Afficher les restrictions**
`$restrict`
'''
    },

    'remind': {

        'no_argument': '''
Usage:
    ```{prefix}remind [mention de la chaîne ou mention de l'utilisateur] <heure ou heure à> <message>` `` `
    
Exemple:
    ```{prefix}remind #general 10s Hello world```
    ```{prefix}remind 10:30 Il \ ' est maintenant 10: 30``` ''',

        'invalid_tag': '''Impossible de trouver un emplacement à côté de votre balise présente.''',

        'invalid_time': '''Assurez-vous que l'heure que vous avez fournie est au format [num][s/m/h/d][num][s/m/h/d] etc. ou `jour/mois/année-heure:minute:seconde`. ''',

        'long_time': '''Assurez-vous que l'heure fournie est inférieure à {max_time} jours dans le futur.''',

        'past_time': '''Veuillez vous assurer que l'heure indiquée est dans le futur. Si l'heure * est * dans le futur, veuillez être plus précis avec la définition. ''',

        'success': '''Nouveau rappel enregistré pour {location} dans {offset}.''',
    },

    'interval': {

        'no_argument': '''
Usage:
    ```{prefix}interval [channel mention or user mention] <time to or time at> <interval> <message>```
Exemple:
    ```{prefix}interval #general 9:30 1d Bonjour!```
    ```{prefix}interval 0s 10s Ce sera vraiment irritant```''',

        'invalid_interval': '''Assurez-vous que l'intervalle que vous avez fourni est au format [num][s/m/h/d][num][s/m/h/d] etc. sans espaces, par exemple . 10s pendant 10 secondes ou 10s12m15h1d pendant 10 secondes, 12 minutes, 15 heures et 1 jour. ''',

        'short_interval': '''Veuillez vous assurer que l'intervalle fourni est supérieur à {min_interval} secondes''',

        'long_interval': '''Veuillez vous assurer que l'intervalle fourni est inférieur à {max_time} jours''',

        'donateur': '''Vous devez être un mécène (don de 2$ ou plus) pour accéder à cette commande! Tapez `{prefix}donate` pour en savoir plus. ''',

    },

    'naturel': {

        'no_argument': '''
Traitement du langage naturel
Exemples:
    ```{prefix}natural en 10 minutes, envoyez Hello World! à #general```
    ```{prefix}natural à 18h00 envoyer Le grand événement a commencé!```
    ```{prefix}natural le 16 juillet à 14h00, envoyez les abonnés réinitialisés aujourd'hui! à #subs @Sub1 @Sub2```
    ```{prefix}natural maintenant envoyer 10 minutes s'est écoulé! toutes les 10 minutes à #timer```
Mots clés:
    `send`: définir le message
    `every`: définir un intervalle (Patreon uniquement)
    `to`: définit l'emplacement vers lequel envoyer (peut définir plusieurs emplacements, comme` @JellyWX #general @ SomeUser` à envoyer aux trois)
Usage:
    ```{prefix}natural <time statement> envoyer <message> [chaque intervalle] [à # channel / @ user]```
    ''',

        'invalid_time': '''Votre temps n'a pas pu être traité. Veuillez le rendre aussi clair que possible, par exemple "16 juillet" ou "dans 20 minutes''',

        'long_time': '''Veuillez vous assurer que votre rappel date de moins de 50 ans, ou utilisez un relevé de temps plus précis.''',

        'send': '''envoyer''',

        'to': '''à''',

        'every': '''chaque''',

        'bulk_set': '''{} rappels définis avec succès''',

    },

    'del': {

        'listing': '''Liste des rappels sur ce serveur ... (il peut y avoir un petit retard, veuillez attendre le message "Liste (1,2,3 ...)").''',

        'listed': '''Répertoriez (1,2,3 ...) les rappels que vous souhaitez supprimer, ou saisissez autre chose pour annuler.''',

        'count': '''{} rappels supprimés!''',
    },

    'look': {

        'listing': '''Répertorier les rappels sur le canal spécifié ...''',

        'listing_limited': '''Liste des {} prochains rappels sur la chaîne spécifiée ...''',

        'inter': '''survient ensuite à''',

        'no_reminders': '''Aucun rappel sur le canal spécifié.''',
    },

    'todo': {

        'add': '''*Faites `{prefix}{command} add <message>` pour ajouter un élément à votre TODO, ou tapez `{prefix}{command} help` pour plus de commandes!*''',

        'added': '''Ajouté '{name}' todo!''',

        'removed': '''Supprimé '{}' de todo!''',

        'error_value': '''L'élément de suppression doit être un nombre. Visualisez les TODO numérotés à l'aide de `{prefix}{command}`''',

        'error_index': '''Impossible de trouver l'élément par ce numéro. Êtes-vous dans la bonne liste de choses à faire? ''',

        'help': '''Pour utiliser les commandes TODO, faites `{prefix} {command} add <message>`, `{prefix}{command} remove <number>`, `{prefix} {command} clear` et `{prefix}{command}` pour ajouter, supprimer, effacer ou afficher votre liste de tâches. ''',

        'cleared': '''Effacer la liste de tâches!''',

        'confirm': '''Vous êtes sur le point de supprimer **{} éléments** de votre **{}** liste de tâches. Êtes-vous sûr? (tapez `yes` pour confirmer) ''',

        'canceled': '''Effacer annulé''',
    },

    'blacklist': {
        'removed_from': '''Suppression des listes noires des chaînes spécifiées.''',

        'added_from': '''Ajout des chaînes spécifiées à la liste noire.''',

        'removed': '''La chaîne actuelle a été supprimée de la liste noire.''',

        'added': '''Ajout de la chaîne actuelle à la liste noire.''',

    },

    'lang': {

        'invalid': '''Langues:
{} ''',

        'set_p': '''Langue personnelle définie sur le français.''',
    },

    'clock': {

        'time': '''L'heure actuelle est {}.''',

    },

    'offset': {

        'help': '''Utilisation: `{prefix}offset <time/s>`''',

        'invalid_time': '''Veuillez vous assurer que l'heure que vous avez fournie est au format [num][s/m/h/d][num][s/m/h/d]...''',

        'success': '''Tous les rappels ont été décalés de {} secondes''',

    },

    'nudge': {

        'invalid_time': '''Veuillez vous assurer que l'heure que vous avez fournie est au format [num] [s / m / h / d] [num] [s / m / h / d] et est inférieure à 30' 000 secondes ''',

        'success': '''Les prochains rappels seront avancés de {} secondes''',

    },

    'timer': {

        'limit': '''Vous avez déjà 25 minuteries. Veuillez supprimer quelques minuteurs avant d'en créer un nouveau ''',

        'name_length': '''Veuillez nommer votre minuterie quelque chose de court-circuité (max. 32 caractères, vous avez utilisé {})''',

        'unique': '''Veuillez donner à votre minuterie un nom unique''',

        'success': '''Création d'une nouvelle minuterie''',

        'not_found': '''Impossible de trouver une minuterie de ce nom''',

        'deleted': '''Suppression d'une minuterie''',

        'help': '''**Aide du minuteur**
`timer list` - Afficher toutes les minuteries actuelles de votre serveur / utilisateur
`timer start [nom]` - Démarre une nouvelle minuterie (compte indéfiniment)
`timer delete <nom>` - Supprimer une minuterie par nom
        ''',

    },

    'pause': {

        'invalid_time': '''Veuillez vous assurer que l'heure que vous avez fournie est au format [num][s/m/h/d][num][s/m/h/d]...''',

        'paused_until': '''Les rappels de cette chaîne ont été réduits au silence jusqu'au ** {} **''',

        'paused_indefinite': '''Les rappels de cette chaîne ont été supprimés indéfiniment''',

        'unpaused': '''Les rappels de cette chaîne n'ont pas été mis sous silence''',
    },
}
