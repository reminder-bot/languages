#: español

{
    '__maintainer__' : '@Giuh',

    'blacklisted' : ''':x: Este canal está en la blacklist :x:''',

    'admin_required' : 'Necesitas permisos de administrador para usar este comando.',

    'help' : '''Por favor visita https://reminder-bot.com/help?lang=ES''',

    'no_perms_webhook' : '''**AVISO**: Para colocar recordatorios necesito el permiso de `Administrar Webhooks`.''',

    'no_perms_general' : '''Acción imposible. Asegúrese que tengo los permisos correctos.''',

    'help_raw' : [
        ['Comandos de recordatorios', {
            '$natural' : 'Método más fácil para colocar recordatorios. Envía el comando para más información.',

            '$del' : 'Elimina recordatorios e intervalos en tu servidor. Si los recordatorios fueron colocados para un usuario específico, deberá enviar un mensaje directo al bot con el comando.',

            '$look' : 'Ver los recordatorios de un canal.',

            '$remind [usuario/canal] <tiempo-para-recordatorio> <mensaje>' : 'Considere utilizar el comando <code>$natural</code> en lugar de este. Coloca un recordatorio. El tiempo debe ponerse como [num][s/m/h/d], por ejemplo 10s para 10 segundos o 2s10m para 2 segundos 10 minutos. Un tiempo exacto puede ser colocado como <code>día/mes/año-hora:minuto:segundo</code>.',

            '$interval [usuario/canal] <tiempo-para-recordatorio> <intervalo> <mensaje>' : '<strong><a href="https://patreon.com/jellywx/">Patron Only.</a></strong> Considere utilizar el comando <code>$natural</code> en lugar de este. Coloca un recordatorio periódico iniciando desde el <code>tiempo-para-recordatorio</code> dado. El tiempo se coloca como dice arriba. Ej. `$interval 0s 20m ¡Hola Mundo!` enviará `¡Hola Mundo!` a tu canal cada 20 minutos.',

            '$todo' : 'Comandos relacionado a la lista TO-DO (lista de tareas). Utiliza <code>$todo help</code> para más información.',

            '$todos' : 'Idéntico a <code>$todo<code> pero para tareas a nivel de servidor.',

            '$timezone' : 'Configura la zona horaria del servidor, para facilitar los recordatorios basados en tiempo.',

            '$offset' : 'Ajustar o compensar la hora de todos los recordatorios del servidor por un determinado tiempo (por horarios de verano, etc.)', }],

        ['Comandos de administración', {
            '$restrict [roles]' : 'Añade/remueve permiso a ciertos roles mencionados para colocar recordatorios e intervalos.',

            '$blacklist [canal]' : 'Bloquea o desbloquea un canal de enviar comandos.' }],

        ['Otros comandos', {
            '$donate' : 'Muestra información sobre donaciones.',

            '$prefix <prefijo>' : 'Cambia el prefijo "$".',

            '$info' : 'Obtén información sobre el bot.',

            '$lang <nombre>' : 'Cambia el idioma.',

            '$clock' : 'Obtén la hora actual acorde a la zona horaria del servidor.',

            }
        ]
    ],


    'info' : '''
Prefijo por defecto: `$`
Prefijo seleccionado: `@{user} prefix $`
Ayuda: `{prefix}help`

**Bienvenido a RemindMe!**
Desarrollador: <@203532103185465344>
Un chico cool: <@174243954487853056>
Ícono: <@253202252821430272>
Encuéntrame en https://discord.gg/WQVaYmT y en https://github.com/JellyWX :)

Framework: `discord.py`
Proveedor de host: OVH

*Si tienes consultas sobre nuevas caracterísicas, por favor envíalas a nuestro servidor de Discord*
*Si tienes consultas sobre desarrollo de bot para tí y tu servidor, por favor envíame un mensaje directo*
''',

    'donate' : '''
¿Pensando en aportar una contribución mensual? Presiona abajo para mi Patreon y el servidor oficial del bot :D
https://www.patreon.com/jellywx

https://discord.gg/WQVaYmT

Aquí hay un poco más información:

Cuando donas, Patreon automáticamente te dará el rango en nuestro servidor de Discord, siempre y cuando hayas vinculado tu Patreon con Discord.
Con tu nuevo rango, podrás:
: usar el comando exclusivo `interval`
: colocar recordatorios más largos (2000 caracteres)
: colocar embeds con colores (disponible mediante el dashboard)

Para quienes estén en Patreon, muchas gracias :D Haces que este bot pueda sostenerse.

Ten en cuenta que debes estar conectado a nuestro servidor de Discord para recibir las recompenzas de Patreon.
''',

    'prefix' : {
        'no_argument' : '''
Por favor utiliza este comando como `mbprefix <prefijo>`
''',
        'success' : '''
Prefijo cambiado a {prefix}
''',

        'too_long' : '''Por favor selecciona un prefijo menor a 5 caracteres.'''
    },

    'timezone' : {

        'no_argument' : '''
Uso:
    ```{prefix}timezone <nombre>```
Ejemplo:
    ```{prefix}timezone Europe/London```
Todas las zonas horarias: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
Zona horaria actual: {timezone}''',

        'no_timezone' : '''Zona horaria no reconocida. Una lista está disponible en https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'success' : '''La zona horaria ha sido cambiada a {timezone}. Tu hora actual debería ser {time}'''
    },

    'restrict' : {

        'disabled' : '''Desactivados los permisos de recordatorios para el rol.''',

        'enabled' : '''Activados los permisos de recordatorios para el rol.''',

        'allowed' : '''Roles permitidos: {}''',

        'help' : '''Por favor menciona los roles a los cuales desees cambiarles los permisos de recordatorios.'''
    },

    'clear' : {

        'no_argument' : '''Por favor menciona los usuarios de los que deseas eliminar los mensajes.'''

    },

    'remind' : {
        'no_argument' : '''
Uso:
    ```{prefix}remind [canal o usuario] <tiempo para/tiempo exacto> <mensaje>```
Ejemplo:
    ```{prefix}remind #general 10s Hola mundo```
    ```{prefix}remind 10:30 Son las 10:30```''',

        'invalid_tag' : '''No es posible encontrar la localización de tu tag.''',

        'invalid_time' : '''Asegúrate que la hora que colocaste es en el formato [num][s/m/h/d][num][s/m/h/d] etc. o `día/mes/año-hora:minuto:segundo`.

        Asegúrate de que el tiempo colocado es menor a 50 años''',

        'invalid_count' : '''¡Demasiados recordatorios en el canal especificado! Utiliza `{prefix}del` para eliminar algunos, o utiliza `{prefix}donate` para aumentar el límite (tier de $5).''',

        'invalid_chars' : '''¡Recordatorio demasiado largo! (máx. 150, usaste {}). Utiliza `{prefix}donate` para aumentar el límite a 1900 caracteres (tier de $5).''',

        'invalid_chars_2000' : '''Discord no permite colocar recordatorios con 2000+ caracteres. Lo siento,''',

        'no_perms' : '''Necesitas `Administrar Mensajes` tener un rol con el cual puedas colocar recordaorios a ese canal. Contacta al admnistrador de tu servidor y dile que utilice el comando `{prefix}restrict` para especificar roles permitidos.''',

        'success' : '''Nuevo recordatorio registrado para <{}{}> en {} segundos. Ya no puedes editarlo, así que eres libre de eliminarlo.'''
    },

    'natural' : {
        'no_argument' : '''
**Nuevo** Procesamiento en lenguaje natural
Ejemplos:
    ```{prefix}natural en 10 minutos enviar ¡Hola Mundo! para #general```
    ```{prefix}natural a las 18:00 enviar ¡El gran evento ha comenzado!```
    ```{prefix}natural el 16 de julio a las 14:00 enviar ¡Hoy se reinician las subs! para #subs```
    ```{prefix}natural ahora enviar ¡Han pasado 10 minutos! cada 10 minutos para #timer```
Palabras clave:
    `enviar` : define el mensaje
    `cada` : define el intervalo
    `para` : define el destino del mensaje
Uso:
    ```{prefix}natural <tiempo para> enviar <mensaje> [cada intervalo] [para #canal/@usuario]```
    ''',

        'success' : '''Nuevo recordatorio registrado para {} en {} segundos. Si quieres eliminar este recordatorio, escribe `$del`.''',

        'bad_time' : '''Has fallado en colocar correctamente el tiempo. Por favor, colócalo claro, por ejemplo `16 de julio` o `en 20 minutos`''',

        'long_time' : '''¡Eso es un tiempo muy grande! Por favor, asegúrate que tu recordatorio es menor a 50 años.''',

        'send' : ''' enviar''',

        'to' : ''' para ''',

        'every' : ''' cada '''

    },

    'interval' : {
        'no_argument' : '''
Uso:
    ```{prefix}interval [canal o usuario] <tiempo para/tiempo exacto> <intervalo> <mensaje>```
Ejemplo:
    ```{prefix}interval #general 9:30 1d ¡Buen día!```
    ```{prefix}interval 0s 10s Esto será muy irritante```''',

        'invalid_interval' : '''Asegúrate que la hora que colocaste es en el formato [num][s/m/h/d][num][s/m/h/d] etc. sin espacios, ej. 10s para 10 segundos o 10s12m15h1d for 10 segundos, 12 minutos, 15 horas y 1 día.

        Asegúrate de que el tiempo del intervalo colocado es menor a 50 años''',

        '8_seconds' : '''Por favor asegúrate que tu intervalo es mayor a 8 segundos.''',

        'donor' : '''¡Necesitas ser un Patreon (dona 2$ o más) para acceder a este comando! Escribe `{prefix}donate` para más información.''',

        'success' : '''Nuevo intervalo registrado para <{}{}> en {} segundos . Ya no puedes editarlo, así que eres libre de eliminarlo.''',

        'removed' : '''Parece que no hay Patreons en tu servidor, por lo tanto el intervalo se ha eliminado.'''

    },

    'autoclear' : {
        'disable' : '''Autolimpieza desactivada en {}''',

        'enable' : '''Autolimpieza de {} segundos activada.''',
    },

    'del' : {
        'listing' : '''Listando recordatorios en este servidor... (puede haber un pequeño retraso, espera que el mensaje "Selecciona (1,2,3...)" aparezca).''',

        'listed' : '''Selecciona (1,2,3...) el recordaorio que quieres eliminar, o escribe cualquier otra cosa para cancelar.''',

        'count' : '''¡Se han eliminado {} recordatorios!'''
    },

    'look' : {
        'listing' : '''Listando los recordatorios del canal...''',
    },

    'todo' : {
        'server_only' : '''Por favor utiliza `{prefix}todo` para tu lista de tareas personal. `{prefix}todos` es para las tareas del servidor entero.''',

        'add' : '''*Pon `{prefix}{command} add <mensaje>` para añadir un ítem a tu TODO, o escribe `{prefix}{command} help` para más comandos*''',

        'too_long' : '''Disculpa, pero los ítems están limitados a 80 caracteres. Mantenlo conciso :)''',

        'too_long2' : '''Disculpa, pero la lista no puede excederse de los 800 caracteres. ¿Tal vez completar algunas tareas?''',

        'added' : '''¡Añadido \'{name}\' a la lista de tareas!''',

        'removed' : '''¡Eliminado \'{}\' de la lista de tareas!''',

        'error_value' : '''El ítem a remover ha de ser un número. Mira el número de las tareas usando `{prefix}{command}`''',

        'error_index' : '''No se pudo encontrar un ítem con ese número. ¿Estás en la lista correcta?''',

        'help' : '''Para usar comandos de la lista de tareas (TODO), pon `{prefix}{command} add <mensaje>`, `{prefix}{command} remove <número>`, `{prefix}{command} clear` y `{prefix}{command}` para añadir, remover, limpiar o mirar tu lista de tareas.''',

        'cleared' : '''¡Limpiada la lista de tareas!'''
    },

    'tags' : {

        'deleted' : '''Eliminado el tag {}''',

        'added' : '''Añadido el tag {}''',

        'invalid_count' : '''Lo siento, para usuarios normales hay un límite de 6 tags. Por favor elimina algunos o considera donar con `{prefix}donate` (tier de 5$).''',

        'invalid_chars' : '''Los tags están limitados a 80 caracteres. ¡Mantenlo conciso!''',

        'colon' : '''Por favor añade dos puntos para separar el nombre del tag con el cuerpo.''',

        'illegal' : '''Por favor no utilices palabras claves `add, new, remove, del` en el nombre de tus tags.''',

        'unfound' : '''No se pudo encontrar el tag con el nombre que has especificado.''',

        'help' : '''Utiliza `{prefix}tag add <nombre>: <mensaje>` para añadir nuevos tags. Utiliza `{prefix}tag remove <nombre>` para eliminar un tag. Utiliza `{prefix}tag <nombre>` para ver un tag. Utiliza `{prefix}tag` para ver todos los tags.'''
    },

    'blacklist' : {
        'removed_from' : '''Removidas las blacklists de los canales especificados.''',

        'added_from' : '''Añadido los canales especificados a la blacklist.''',

        'removed' : '''Removido el canal actual de la blacklist.''',

        'added' : '''Añadido el canal actual a la blacklist.'''

    },

    'lang' : {

        'invalid' : '''Idiomas:
{}''',

        'set' : '''Idioma cambiado a Español.''',
    },

    'clock' : {
        'time' : '''La hora actual es {}.''',
    }

}
