#: Dutch | STILL A WORK IN PROGRESS!

{
    '__maintainer__' : '@Mr Pleasant',

    'blacklisted' : ''':x: Dit kanaal is op de zwarte lijst :x:''',

    'admin_required' : 'Je moet een admin zijn om dit commando te gebruiken.',

    'help' : '''Ga voor meer informatie naar https://jellywx.co.uk/help?lang=EN''', #:<------------ WIP

    'help_raw' : [
        ['''Herinnering Commando`s''', {
            '$del' : 'verwijder de herinneringen en intervals op je server. Stuur een direct commando naar de bot als de herinneringen via DM`s zijn.',

            '$remind [gebruiker/kanaal] <tijd-tot-herinnering> <bericht>' : 'stel een herinnering in. Neemt de tijd in het formaat van [num][s/m/h/d], bijvoorbeeld 10s voor 10 seconden of 2s10m for 2 seconden en 10 minuten. Een precieze tijd kan gegeven worden als `dag`/`maand`/`jaar`-`uur`:`minuut`:`seconden`.',

            '$interval [gebruiker/kanaal] <tijd-tot-herinnering> <interval> <bericht>' : 'stel een interval in, waar het gegeven `bericht` elk `interval` verzonden wordt in elk gegeven `tijd-tot-herinnering` tijd. Neemt de tijd in het formaat hierboven. Voorbeeld: `$interval 0s 20m Hello World!` verstuurt `Hello World!` elke 20 minuten naar het kanaal.',

            '$todo' : 'commando voor het stellen van een to do lijst. Gebruik `$todo help` voor meer informatie.',

            '$todos' : 'hetzelfde als `$todo` maar voor server breed taakbeheer.',

            '$timezone' : 'Zet de tijdszone voor je server, voor makkelijkere setup in de database.' }],

        ['''Management Commando`s''', {
            '$autoclear [tijd/s] [kanaal]' : 'Schakelt automatisch verwijderein in/uit, elk bericht in het kanaal (Standaard het kanaal waar het commando wordt geplaatst) wordt automatisch verwijderd na een tijd (standaard 10 seconden).',

            '$clear <gebruiker>' : 'Verwijdert berichten verstuurt door gebruiker(s).',

            '$restrict [roles]' : 'toevoegen / verwijderen van rollen om kanaalherinneringen en -intervallen te kunnen verzenden.',

            '$tag' : 'Aliasing commando`s. Gebruik `$tag help` voor meer informatie.',

            '$blacklist [kanaal-naam]' : 'Blokkeer of deblokkeer de mogelijkheid voor commando`s in een specifiek kanaal.' }],

        ['''Andere Commando`s''', {
            '$donate' : 'toon informatie voor donaties.',

            'mbprefix <string>' : 'verander de prefix van de bot, standaard is dit $. Dit commando gebruikt geen prefix!!',

            '$info' : 'krijg informatie over de bot.',

            '$lang <name>' : 'verander de taal.',

            '$clock [12]' : 'krijg de tijd op dit moment, optioneel als een 12-uurs klok.' }
        ]
    ],

    'web_foot_title' : 'Extra informatie',
    'web_foot' : 'Typ de brackets niet wanneer je een commando typt!Bijvoorbeeld: mbprefix !, niet mbprefix <!>',
    'web_foot2' : 'Je benkt welkom in onze Discord Suppot Server (Engels) als je meer hulp nodig hebt!',

    'about' : {'Ovef de bot' : ['Bot gemaakt door: Jude Southworth', 'Github: <a href=https://github.com/JellyWX>https://github.com/JellyWX</a>', 'Zou je graag een bot willen? Neem contact met JellyWX op via Discord, in het Engels.', 'Hosting provider: OVH']},

    'join' : 'Word lid van de Discord server',
    'invite' : 'nodig de Bot uit in jouw server',

    'info' : '''
Standaard prefix: `$`
Reset prefix: `@{user} prefix $`
Help: `{prefix}help`

**Welkom bij RemindMe!**
Developer: <@203532103185465344>
Coole gast die weet waar hij het over heeft: <@174243954487853056>
Icon: <@253202252821430272>
Vind me op  https://discord.gg/WQVaYmT en op https://github.com/JellyWX :)
Framework: `discord.py`
Hosting provider: OVH
Mijn andere bot (alleen voor Patreons):
https://discordapp.com/oauth2/authorize?client_id=411224415863570434&scope=bot&permissions=35840
*Als je vragen hebt over nieuwe functies, graag een bericht in de discord server!r*
*Als je een vraag hebt over de ontwikkeling van de bot voor jou op je server, stuur mij een privé bericht!*
''',

    'donate' : '''
Zit je er over te denken om een maandelijkse bijdrage te doen? Klik op het adres hierbeneden voor mijn patreon en voor mijn discord server :D
https://www.patreon.com/jellywx

https://discord.gg/WQVaYmT

Hier is wat meer informatie:

Wanneer je een donatie doet zal Patreon jou automatisch een rankup geven in onze Discord server, als je je Discord en Patreon account al met elkaar gelinkt hebt.
Met je nieuwe rank kan je:
: Patreon-exclusieve commando`s gebruiken zoals `interval`
: Mogelijkheid om meer reminders in te stellen (ongelimiteerd)
: Mogelijkheid om langere reminders in te stellen (2000 chars)
: Mogelijkheid om meer & langere tags in te stellen

Aan iedereen die een Patron is: Bedankt :D Jullie zorgen er voor dat deze bot kan blijven voortbestaan.

Let er op dat je met de Discord server verbonden moet zijn om de Patreon rewards te krijgen.
''',

    'prefix' : {
        'no_argument' : '''
Gebruik dit commando als `mbprefix <prefix>`
''',
        'success' : '''
Prefix veranderd naar {prefix}
''',

        'too_long' : '''Kies alstublieft een prefix uit die korter is dan 5 karakters.'''
    },

    'timezone' : {

        'no_argument' : '''
Gebruik:
    ```{prefix}timezone <naam>```
Example:
    ```{prefix}timezone Europe/London```
Alle ondersteunde tijdszones: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
Huidige tijdszone: {timezone}''',

        'no_timezone' : '''Tijdszone is niet herkend. Een volledige lijst is beschikbaar op https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568''',

        'success' : '''Tijdszone is veranderd naar {timezone}. De huidige tijd zou {time} moeten zijn.'''
    },

    'restrict' : {

        'disabled' : ''''De herinnering toestemmingen voor de rollen zijn verwijderd.'''',

        'enabled' : ''''De herinnering toestemmingen voor de rollen zijn toegevoegd.''',

        'allowed' : '''Toegestane rollen: {}''',

        'help' : '''Vermeld alstublieft de rollen waaarvan je de toestemmingen aan wil passen.'''
    },

    'clear' : {

        'no_argument' : '''Vermeld alstublieft de gebruikers van wie je de berichten wilt verwijderen.'''

    },

    'remind' : {
        'no_argument' : '''
Gebruik:
    ```{prefix}remind [kanaal/gebruiker] <tijd tot of tijd wanneer> <bericht>```
Voorbeeld:
    ```{prefix}remind #general 10s Hello world```
    ```{prefix}remind 10:30 It`s now 10:30```''',

        'invalid_tag' : '''De locatie van de tag is niet gevonden.''',

        'invalid_time' : '''Zorg dat de tijd in het bericht als vorm heeft [num][s/m/h/d][num][s/m/h/d] etc. danwel `dag/maand/jaar-uur:minuut:seconde`.

        Zorg dat de tijd niet verder dan 50 jaar in de toekomst is!''',

        'invalid_count' : '''Te veel herinneringen in het specifieke kanaal! Gebruik  `{prefix}del` om een aantal te verwijderen, of gebruik `{prefix}donate` om de maximale herinneringen te verhogen ($5 tier).''',

        'invalid_chars' : '''Herinnering bericht is te lang! (max 150, jij hebt er  {} gebruikt). Gebruik `{prefix}donate` om je karakter limiet te verhogen naar 1900 ($5 tier).''',

        'invalid_chars_2000' : '''Discord staat geen berichten toe die langer dan 2000 karakters zijn. Sorry.''',

        'no_perms' : '''Je moet de `Manage Messages`/`Berichten Beheren` hebben, ofwel een rol die reminders naar dat kanaal kan zenden. Bespreek dit met je server admin, en overleg met hem/haar om het `{prefix}restrict` commando te gebruiken om bepaalde rollen toe te staan.''',

        'success' : '''Nieuwe herinnering geregistreerd voor <{}{}> in {} seconden. Als je deze herinnering wilt verwijderen, gebruik dan `$del`.'''
    },

    'interval' : {
        'no_argument' : '''
Gebruik:
    ```{prefix}interval [kanaal/gebruiker] <tijd tot of tijd wanneer> <interval> <bericht>```
Voorbeeld:
    ```{prefix}interval #general 9:30 1d Goede morgen!```
    ```{prefix}interval 0s 10s Dit zal aardig vervelend worden!```''',

        'invalid_interval' : '''Zorg dat het interval wat je gegeven hebt als vorm heeft [num][s/m/h/d][num][s/m/h/d] etc. met geen spaties, bijvoorbeeld 10s voor 10 seconden of 10s12m15h1d voor 10 seconden, 12 minuten, 15 uur en 1 dag.

        Zorg dat het interval gegeven niet langer is dan 50 jaar!''',

        '8_seconds' : '''Zorg dat je interval tijd langer is dan 8 seconden.''',

        'donor' : '''Je moet een Patron zijn (donating 2$ of meer) om toegang tot dit commando te krijgen! Typ `{prefix}donate` om meer informatie te krijgen.''',

        'success' : '''Nieuw interval geregistreerd voor <{}{}> in {} seconden. Je kan het interval nu niet meer veranderen, dus je kan dit bericht nu verwijderen.''',

        'success_new' : '''Nieuw interval geregistreerd voor {} in {} seconden. Als je dit interval wilt verwijderen, typ `$del`.'''
        
        'removed' : '''Het lijkt dat er geen patrons in je server zitten, dus het interval is gestopt.'''

    },

    'autoclear' : {
        'disable' : '''Autoclearing disabled on {}''',

        'enable' : '''{} second autoclearing enabled.''',
    },

    'del' : {
        'listing' : '''Listing reminders on this server... (there may be a small delay, please wait for the "List (1,2,3...)" message).''',

        'listed' : '''List (1,2,3...) the reminders you wish to delete, or type anything else to cancel.''',

        'count' : '''Deleted {} reminders!'''
    },

    'todo' : {
        'server_only' : '''Please use `{prefix}todo` for your personal TODO list. `{prefix}todos` is only for server use.''',

        'add' : '''*Do `{prefix}{command} add <message>` to add an item to your TODO, or type `{prefix}{command} help` for more commands!*''',

        'too_long' : '''Sorry, but TODO message sizes are limited to 80 characters. Keep it concise :)''',

        'too_long2' : '''Sorry, but TODO lists are capped at 800 characters. Maybe, get some things done?''',

        'added' : '''Added \'{name}\' to todo!''',

        'removed' : '''Removed \'{}\' from todo!''',

        'error_value' : '''Removal item must be a number. View the numbered TODOs using `{prefix}{command}`''',

        'error_index' : '''Couldn\'t find item by that number. Are you in the correct todo list?''',

        'help' : '''To use the TODO commands, do `{prefix}{command} add <message>`, `{prefix}{command} remove <number>`, `{prefix}{command} clear` and `{prefix}{command}` to add to, remove from, clear or view your todo list.''',

        'cleared' : '''Cleared todo list!'''
    },

    'tags' : {

        'deleted' : '''Deleted tag {}''',

        'added' : '''Added tag {}''',

        'invalid_count' : '''Sorry, but for normal users tags are capped at 6 tags. Please remove some or consider donating with `{prefix}donate` ($5 tier).''',

        'invalid_chars' : '''Tags are capped at 80 characters. Keep it concise!''',

        'colon' : '''Please add a colon to split the name of the tag from the body.''',

        'illegal' : '''Please don\'t use keywords `add, new, remove, del` in the names of your tags.''',

        'unfound' : '''Couldn\'t find the tag by the name you specified.''',

        'help' : '''Use `{prefix}tag add <name>: <message>` to add new tags. Use `{prefix}tag remove <name>` to delete a tag. Use `{prefix}tag <name>` to view a tag. Use `{prefix}tag` to list all tags'''
    },

    'blacklist' : {
        'removed_from' : '''Removed blacklists from specified channels.''',

        'added_from' : '''Added specified channels to blacklist.''',

        'removed' : '''Removed current channel from blacklist.''',

        'added' : '''Added current channel to blacklist.'''

    },

    'lang' : {

        'invalid' : '''Languages:
{}''',

        'set' : '''Language set to English.''',
    },

    'clock' : {
        'time' : '''Current time is {}.''',
    }

}
