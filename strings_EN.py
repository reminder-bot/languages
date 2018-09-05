#: english

{
    '__maintainer__' : '@JellyWX',

    'blacklisted' : ''':x: This channel is blacklisted :x:''',

    'admin_required' : 'You need to be an admin to run this command.',

    'help' : '''Please visit https://jellywx.co.uk/help?lang=EN''',

    'no_perms_webhook' : '''**WARNING**: To set reminders I need the `Manage Webhooks` permission.''',

    'no_perms_general' : '''Action forbidden. Please ensure I have the correct permissions.''',

    'help_raw' : [
        ['''Reminder Commands''', {
            '$natural' : 'Easier method to set reminders. Please run this command for more information.',

            '$del' : 'Delete reminders and intervals on your server. If the reminders are set up for DMs, direct message this command to the bot.',

            '$remind [user/channel] <time-to-reminder> <message>' : 'Please consider <code>$natural</code> rather than using this command. Set up a reminder. Takes times in the format of [num][s/m/h/d], for example 10s for 10 seconds or 2s10m for 2 seconds 10 minutes. An exact time can be provided as <code>day/month/year-hour:minute:second</code>.',

            '$interval [user/channel] <time-to-reminder> <interval> <message>' : 'Please consider <code>$natural</code> rather than using this command. Set a recurring reminder starting in the given <code>time-to-reminder</code>. Takes times in the normal formats, ex. <code>$interval 0s 20m Hello World!</code> will send \'Hello World!\' to your channel every 20 minutes.',

            '$todo' : 'TODO list related commands. Use <code>$todo help</code> for more information.',

            '$todos' : 'Identical to <code>$todo</code> but for server-wide task management.',

            '$timezone' : 'Set your server\'s timezone, for easier date-based reminders.' }],

        ['''Management Commands''', {
            '$autoclear [time/s] [channels]' : 'Enables/disables autoclearing, where messages sent to the channel (default your channel) will be automatically deleted after time (default 10 seconds).',

            '$clear <user mentions>' : 'Clears messages made by a user/s.',

            '$restrict [role mentions]' : 'add/remove roles from being allowed to send channel reminders and intervals.',

            '$blacklist [channel-name]' : 'Block or unblock a channel from sending commands.' }],

        ['''Other Commands''', {
            '$donate' : 'View information about donations.',

            'mbprefix <string>' : 'Change the prefix from $. This command does not use a prefix!',

            '$info' : 'Get info on the bot.',

            '$lang <name>' : 'Change the language.',

            '$clock' : 'Get current time in guild\'s timezone',

            '$clock show' : 'Get the current time.' }
        ]
    ],


    'info' : '''
Default prefix: `$`
Reset prefix: `@{user} prefix $`
Help: `{prefix}help`

**Welcome to RemindMe!**
Developer: <@203532103185465344>
Cool guy who knows what he's on about: <@174243954487853056>
Icon: <@253202252821430272>
Find me on https://discord.gg/WQVaYmT and on https://github.com/JellyWX :)

Framework: `discord.py`
Hosting provider: OVH

*If you have enquiries about new features, please send to the discord server*
*If you have enquiries about bot development for you or your server, please DM me*
''',

    'donate' : '''
Thinking of adding a monthly contribution? Press below for my patreon and official bot server :D
https://www.patreon.com/jellywx

https://discord.gg/WQVaYmT

Here's some more information:

When you donate, Patreon will automatically rank you up on our Discord server, supposing you have properly linked your Patreon and Discord accounts!
With your new rank, you'll be able to:
: use Patron-only commands like `interval`
: set more reminders (unlimited)
: set longer reminders (2000 chars)
: set more/longer tags

Anyone who is a Patron, thank you :D You make this bot sustainable

Please note, you must be connected to the Discord server to receive Patreon rewards.
''',

    'prefix' : {
        'no_argument' : '''
Please use this command as `mbprefix <prefix>`
''',
        'success' : '''
Prefix changed to {prefix}
''',

        'too_long' : '''Please select a prefix under 5 characters'''
    },

    'timezone' : {

        'no_argument' : '''
Usage:
    ```{prefix}timezone <Name>```
Example:
    ```{prefix}timezone Europe/London```
All timezones: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
Current timezone: {timezone}''',

        'no_timezone' : '''Timezone not recognized. A list is available at https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568''',

        'success' : '''Timezone has been set to {timezone}. Your current time should be {time}'''
    },

    'restrict' : {

        'disabled' : '''Disabled channel reminder permissions for roles.''',

        'enabled' : '''Enabled channel reminder permissions for roles.''',

        'allowed' : '''Allowed roles: {}''',

        'help' : '''Please mention roles you wish to change the reminder permissions for.'''
    },

    'clear' : {

        'no_argument' : '''Please mention users you wish to remove messages of.'''

    },

    'remind' : {
        'no_argument' : '''
Usage:
    ```{prefix}remind [channel mention or user mention] <time to or time at> <message>```
Example:
    ```{prefix}remind #general 10s Hello world```
    ```{prefix}remind 10:30 It\'s now 10:30```''',

        'invalid_tag' : '''Couldn't find a location by your tag present.''',

        'invalid_time' : '''Make sure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc. or `day/month/year-hour:minute:second`.

Make sure the time provided is less than 50 years in the future.''',

        'invalid_count' : '''Too many reminders in specified channel! Use `{prefix}del` to delete some of them, or use `{prefix}donate` to increase your maximum ($5 tier).''',

        'invalid_chars' : '''Reminder message too long! (max 150, you used {}). Use `{prefix}donate` to increase your character limit to 1900 ($5 tier).''',

        'invalid_chars_2000' : '''Discord restrictions mean we can\'t send reminders 2000+ characters. Sorry.''',

        'no_perms' : '''You must have `Manage Messages` or have a role capable of sending reminders to that channel. Please talk to your server admin, and tell her/him to use the `{prefix}restrict` command to specify allowed roles.''',

        'success' : '''New reminder registered for <{}{}> in {} seconds. If you want to delete this reminder, type `$del`.''',
    },

    'natural' : {
        'no_argument' : '''
**New** Natural language processing
Examples:
    ```{prefix}natural in 10 minutes send Hello World! to #general```
    ```{prefix}natural at 18:00 send The big event has started!```
    ```{prefix}natural on the 16th of july at 14:00 send Subs reset today! to #subs```
    ```{prefix}natural now send 10 minutes has passed! every 10 minutes to #timer```
Keywords:
    `send` : define the message
    `every` : define an interval
    `to` : define the location to send to
Usage:
    ```{prefix}natural <time statement> send <message> [every interval statement] [to #channel/@user]```
    ''',

        'success' : '''New reminder registered for {} in {} seconds. If you want to delete this reminder, type `$del`.''',

        'bad_time' : '''Your time failed to process. Please make it as clear as possible, for example `16th of july` or `in 20 minutes`''',

        'long_time' : '''That's a long time! Please ensure your reminder is younger than 50 years''',

        'send' : ''' send ''',

        'to' : ''' to ''',

        'every' : ''' every '''

    },

    'interval' : {
        'no_argument' : '''
Usage:
    ```{prefix}interval [channel mention or user mention] <time to or time at> <interval> <message>```
Example:
    ```{prefix}interval #general 9:30 1d Good morning!```
    ```{prefix}interval 0s 10s This will be really irritating```''',

        'invalid_interval' : '''Make sure the interval you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc. with no spaces, eg. 10s for 10 seconds or 10s12m15h1d for 10 seconds, 12 minutes, 15 hours and 1 day.

Make sure the interval provided is less than 50 years''',

        '8_seconds' : '''Please make sure your interval timer is longer than 8 seconds.''',

        'donor' : '''You need to be a Patron (donating 2$ or more) to access this command! Type `{prefix}donate` to find out more.''',

        'success' : '''New interval registered for <{}{}> in {} seconds . You can\'t edit the reminder now, so you are free to delete the message.''',

        'removed' : '''There appears to be no patrons on your server, so the interval has been removed.'''

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
