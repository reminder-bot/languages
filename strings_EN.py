# noinspection PyStatementEffect
{
    '__full__': 'english',

    '__maintainer__': '@JellyWX',

    'flag': '🇬🇧',

    'blacklisted': ''':x: This channel is blacklisted :x:''',

    'no_perms_general': '''Please ensure the bot has the correct permissions:

✅     **Send Message**
{embed_links}     **Embed Links**
{manage_webhooks}     **Manage Webhooks**
    ''',

    'no_perms_managed': '''You must have `Manage Messages` or have a role capable of sending reminders to that channel. Please talk to your server admin, and ask them to use the `{prefix}restrict` command to specify allowed roles.''',

    'no_perms_restricted': '''You must have permission level `Manage Server` or greater to use this command.''',

    'help': {
        'desc': '''Type `{prefix}help command` to learn more about a command. Some commands are only available in servers''',

        'setup_title': 'Setup Commands',

        'mod_title': 'Moderator Commands',

        'reminder_title': 'Reminder Commands',

        'reminder_mod_title': 'Management Commands',

        'info_title': 'Info Commands',

        'todo_title': 'Todo Commands',

        'other_title': 'Other Commands',

        'lang': '''**Overview**
*Use this command to:*
• View available translations for the bot
• Change the language to see translated messages from the bot

**Arguments**
• `language` [optional] - the supported language you want to change the bot to

**Examples**
View all supported languages:
• `{prefix}lang`

Change the language to Spanish:
• `{prefix}lang ES`

Change the language to English:
• `{prefix}lang EN`''',

        'meridian': '''**Overview**
*Use this command to:*
• Change times to display in 12 hour format
• Revert times to display in 24 hour format

**Arguments**
• `12` - change to 12 hour format
• `24` - change to 24 hour format

**Examples**
Change to 12 hour format:
• `{prefix}meridian 12`

Revert to 24 hour format:        
• `{prefix}meridian 24`      
        ''',

        'timezone': '''**Overview**
*Use this command to:*
• View available timezones for the bot
• Change the timezone to your own timezone to ensure reminders are set correctly

**Arguments**
• `timezone` [optional] - the name of the timezone you want to change the bot to

**Examples**
View timezones:
• `{prefix}timezone`

Set the timezone if you're in the UK:
• `{prefix}timezone Europe/London`

Set the timezone if you're in Japan:
• `{prefix}timezone Asia/Tokyo`

Set the timezone if you're in East-coast America:
• `{prefix}timezone America/New_York`''',

        'prefix': '''**Overview**
*Use this command to:*
• Change your server's prefix when using the bot

**Arguments**
• `new prefix` - the new prefix to use (maximum 5 characters long)

**Examples**
Reset the prefix:
• `{prefix}prefix $`

Change the prefix to `r.`:
• `{prefix}prefix r.`''',

        'blacklist': '''**Overview**
*Use this command to:*
• Block channels from sending commands
• Unblock previously blocked channels from sending commands

**Arguments**
• `channel mention` [optional] - the mention of the channel to change the blacklist on. If not provided, will change the current channel

**Examples**
Blacklist/unblacklist `#general`:
• `{prefix}blacklist #general`''',

        'restrict': '''**Overview**
*Use this command to:*
• Allow users with certain roles to use specific commands
• Remove permissions from roles to use commands
• View role restrictions that are in place

**Arguments**
• `role mention` [optional] - the role that you wish to change permissions on
• `command names` [optional] - the commands to allow the role to use

**Examples**
View restrictions in place:
• `{prefix}restrict`

Allow users with the role `@Reminders` to use reminder commands:
• `{prefix}restrict @Reminders remind natural interval`

Reset the permissions on users with the role `@Reminders` to the default:
• `{prefix}restrict @Reminders`''',

        'alias': '''**Alias**
`a`
        
**Overview**
*Use this command to:*
• Save a long command to be reused quickly

**Usages**
• `{prefix}alias list` - view all saved commands and names
• `{prefix}alias remove name` - delete the alias named "name"
• `{prefix}alias name command..` - save `command` to "name"
• `{prefix}alias name` - run the command saved under "name" 

**Examples**
View all aliases on the server:
• `{prefix}alias list`

Save the command `{prefix}remind 10m Go for a walk!` to the name "walk":
• `{prefix}alias walk remind 10m Go for a walk!`

Recall the command saved in "walk", setting a reminder for 10 minutes' time:
• `{prefix}alias walk`

Remove the alias "walk":
• `{prefix}alias remove walk`''',

        'remind': '''**Alias**
`r`
        
**Overview**
*Use this command to:*
• Create a reminder quickly for one or more users or channels

**Arguments**
• `channel or user mentions` [optional] - mentions of channels or users to send the reminder to. Defaults to the current channel
• `time of reminder` - the time for the reminder, either in a displacement format (`A`s`B`m`C`h`D`d for `A` seconds, `B` minutes, `C` hours and `D` days) or a direct format (`DD/MM/YYYY-HH:MM:SS`)
• `message of reminder` - the message to send as the reminder

**Examples**
Set a reminder of "Finished" for 10 minutes' time:
• `{prefix}remind 10m Finished`

Set a reminder of "TV show starting!" for 6pm:
• `{prefix}remind 18:00 TV show starting!`

Set a reminder of "Raid beginning soon" for 9:30am on the 18th of October:
• `{prefix}remind 18/11-09:30 Raid beginning soon`

Set a reminder of "Check the logs" for 3 users in 1 hour:
• `{prefix}remind @JellyWX @kokobop @ENKeY 1h Check the logs`

**Extra Information**
• You can silent mention roles, users, everyone and here by using `<<everyone>>`, `<<here>>`, `<<role name>>` and `<<user id>>` in your reminder
• You can upload an attachment with the command as the caption to add an attachment to the reminder
• You can use `/tts` on the entire command to make the reminder TTS''',

        'interval': '''**Alias**
`i`

**Overview**
*Use this command to:*
• Create a repeating reminder quickly for one or more users or channels (Patreon only)

**Arguments**
• `channel or user mentions` [optional] - mentions of channels or users to send the reminder to. Defaults to the current channel
• `time of reminder` - the time for the reminder, either in a relative format (`A`s`B`m`C`h`D`d for `A` seconds, `B` minutes, `C` hours and `D` days) or a direct format (`DD/MM/YYYY-HH:MM:SS`)
• `repeat interval` - the time for the reminder, in a relative format (`A`s`B`m`C`h`D`d for `A` seconds, `B` minutes, `C` hours and `D` days)
• `message of reminder` - the message to send as the reminder

**Examples**
Set a reminder of "Refresh now!" every 10 minutes:
• `{prefix}interval 0s 10m Refresh now!`

Set a reminder of "TV show starting!" for 6pm every day:
• `{prefix}interval 18:00 1d TV show starting!`

Set a reminder of "Check the logs" for 3 users every hour:
• `{prefix}interval @JellyWX @kokobop @ENKeY 0s 1h Check the logs`

**Extra Information**
• You can silent mention roles, users, everyone and here by using `<<everyone>>`, `<<here>>`, `<<role name>>` and `<<user id>>` in your reminder
• You can upload an attachment with the command as the caption to add an attachment to the reminder
• You can use `/tts` on the entire command to make the reminder TTS''',

        'natural': '''**Alias**
`n`
        
**Overview**
*Use this command to:*
• Create normal or repeating reminders easily for one or more users or channels

**Usage**
• `{prefix}natural "time" send "message" every "repetition" to "channels/users"` - general structure of command. Please see examples below

**Examples**
Create a reminder saying "Make some food" for 10 minutes' time:
• `{prefix}natural in 10 minutes send Make some food`

Create a reminder saying "Shops reset" to `#notifs` for 6pm on Monday:
• `{prefix}natural at 6pm on monday send Shops reset to #notifs`

Create a reminder saying "The match starts in 15 minutes" for 7pm every Tuesday (Patreon only):
• `{prefix}natural at 7pm on Tuesday send The match starts in 15 minutes every 7 days`

Create a reminder saying "Subs reset today!" for 2pm on the 16th of July, sending to `#subs` and the users `@MrPleasant` and `@Giuh`   
• `{prefix}natural on the 16th of july at 14:00 send Subs reset today! to #subs @MrPleasant @Giuh`

**Extra Information**
• You can silent mention roles, users, everyone and here by using `<<everyone>>`, `<<here>>`, `<<role name>>` and `<<user id>>` in your reminder
• You can upload an attachment with the command as the caption to add an attachment to the reminder
• You can use `/tts` on the entire command to make the reminder TTS''',

        'countdown': '''**Overview**
*Use this command to:*
• Create an active countdown to a certain time, with periodic reminders

**Arguments**
• `time` - the time to countdown to (same format as `$remind`)
• `interval` - how often to send a countdown reminder
• `text` - what text to include with the countdown

**Examples**
Create a daily countdown for the 23rd of August, with event name "Reminder Bot's Birthday":
• `{prefix}countdown 2022/08/23-12:00 1d Reminder Bot's Birthday`

**Extra Information**
• Whilst the reminder content is automatically generated by this command, you can still modify it within the dashboard for more customization
        ''',

        'look': '''**Overview**
*Use this command to:*
• View reminders you have set

**Arguments**
• `number` [optional] - the number of reminders to view. Defaults to show all
• `channel` [optional] - the channel to view reminders from. Defaults to your current channel
• `time` [optional] - show reminders with their direct time rather than their relative time
• `enabled` [optional] - only show enabled reminders

**Examples**
View all reminders on the current channel:
• `{prefix}look`

View the next reminder on the current channel:
• `{prefix}look 1`

View all the reminders on `#general`:
• `{prefix}look #general`

View all reminders on `#general` with their direct times:
• `{prefix}look #general time`''',

        'del': '''**Overview**
*Use this command to:*
• Delete reminders
• View reminders on the entire server

**Usage**
• Type `{prefix}del` in any channel
• Wait for the bot to list the reminders on the server
• Reply with a number or a list of numbers for which reminders to delete

**Examples**
Delete the first reminder:
`>` `{prefix}del`
`<` Listing reminders on this server...
`>` `1`
`<` Deleted 1 reminders!

Delete 3 reminders:
`>` `{prefix}del`
`<` Listing reminders on this server...
`>` `1,2,3`
`<` Deleted 3 reminders!
''',

        'offset': '''**Overview**
*Use this command to:*
• Move all reminders by a certain time
• Account for daylight savings time

**Arguments**
• `time to move` - the relative time (`A`s`B`m`C`h`D`d for `A` seconds, `B` minutes, `C` hours and `D` days) to move the reminders by. Use a minus sign to move them backwards

**Examples**
Move all reminders forward by 1 hour:
• `{prefix}offset 1h`

Move all reminders backward by 1 hour:
• `{prefix}offset -1h`''',

        'pause': '''**Overview**
*Use this command to:*
• Silence any upcoming reminders for a certain amount of time
• Block reminders from sending in a channel
• Unsilence a previously silenced channel

**Arguments**
• `time to silence` [optional] - the relative time (`A`s`B`m`C`h`D`d for `A` seconds, `B` minutes, `C` hours and `D` days) or direct time (`DD/MM/YYYY-HH:MM:SS`) to silence reminders until. Defaults to forever

**Examples**
Block reminders forever/unblock reminders:
• `{prefix}pause`

Block reminders for 7 days:
• `{prefix}pause 7d`''',

        'nudge': '''**Overview**
*Use this command to:*
• Offset all future reminders on a channel by a certain amount when they are created
• Sync up the timings on a channel with the time in a game
• View if the current channel is nudged

**Arguments**
• `time to move` [optional] - the relative time (`A`s`B`m`C`h`D`d for `A` seconds, `B` minutes, `C` hours and `D` days) to move reminders by. Use a minus sign to move them backwards. If not provided, the current nudge will be displayed

**Examples**
Offset all future reminders by 2 seconds:
• `{prefix}nudge 2s`

Offset all future reminders backwards by 30 seconds:
• `{prefix}nudge -30s`
''',

        'info': '''**Alias**
`invite`
        
**Overview**
*Use this command to:*
• View more information about the bot
• Get an invite link to add the bot to more servers

**Examples**
View the info page:
• `{prefix}info`''',

        'help': '''**Overview**
*Use this command to:*
• View a list of commands
• Get help about specific commands

**Arguments**
• `command` [optional] - get help about a specific command

**Examples**
View all commands:
• `{prefix}help`

View help about the todo command:
• `{prefix}help todo`''',

        'donate': '''**Overview**
*Use this command to:*
• View information about subscribing to the bot
• Get a link to the Patreon page for the bot

**Examples**
View the Patreon info page:
• `{prefix}donate`''',

        'clock': '''**Overview**
*Use this command to:*
• View the time in the timezone you have set 

**Examples**
View the time in your timezone:
• `{prefix}clock`''',

        'todo': '''**Overview**
*Use this command to:*
• Manage your personal todo list

**Usages**
• `{prefix}todo` - view your todo list
• `{prefix}todo add item` - add "item" to your todo list
• `{prefix}todo remove n` - remove the `n`th item from your todo list
• `{prefix}todo clear` - remove all items from your todo list

**Examples**
View your todo list:
• `{prefix}todo`

Add "Do washing" to todo list:
• `{prefix}todo add Do washing`

Remove the first item on the todo list:
• `{prefix}todo remove 1`''',

        'todos': '''**Overview**
*Use this command to:*
• Manage the server's todo list

**Usages**
• `{prefix}todos` - view the server's todo list
• `{prefix}todos add item` - add "item" to the server's todo list
• `{prefix}todos remove n` - remove the `n`th item from the server's todo list
• `{prefix}todos clear` - remove all items from the server's todo list

**Examples**
View the server's todo list:
• `{prefix}todos`

Add "Update rules" to todo list:
• `{prefix}todos add Update rules`

Remove the first item on the todo list:
• `{prefix}todos remove 1`''',

        'todoc': '''**Overview**
*Use this command to:*
• Manage the channel's todo list

**Usages**
• `{prefix}todoc` - view the channel's todo list
• `{prefix}todoc add item` - add "item" to the channel's todo list
• `{prefix}todoc remove n` - remove the `n`th item from the channel's todo list
• `{prefix}todoc clear` - remove all items from the channel's todo list

**Examples**
View the channel's todo list:
• `{prefix}todoc`

Add "Collect redeemer" to todo list:
• `{prefix}todoc add Collect redeemer`

Remove the first item on the todo list:
• `{prefix}todoc remove 1`''',

        'timer': '''**Overview**
*Use this command to:*
• Create timers that count upwards
• Check on previously set timers
• Delete previously set timers

**Usages**
• `{prefix}timer start name` - start a new timer under the name "name"
• `{prefix}timer list` - view all timers on this server
• `{prefix}timer delete name` - delete a timer of the name "name"

**Examples**
Create a timer called 'Run started':
• `{prefix}timer start Run started`

Check how much time has passed since the timer was started:
• `{prefix}timer list`

Remove the timer:
• `{prefix}timer delete Run started`''',
    },

    'info': '''
Default prefix: `{default_prefix}`
Reset prefix: `@{user} prefix {default_prefix}`
Help: `{prefix}help`

**Welcome to Reminder Bot!**
Developer: <@203532103185465344>
Icon: <@253202252821430272>
Find me on https://discord.jellywx.com and on https://github.com/JellyWX :)

Invite the bot: https://invite.reminder-bot.com/
Use our dashboard: https://reminder-bot.com/

*If you have enquiries about new features, please send to the discord server*
''',

    'donate': '''
Thinking of adding a monthly contribution? Click below for my Patreon and official bot server :D

https://www.patreon.com/jellywx

https://discord.jellywx.com

Here's some more information:

When you donate, Patreon will automatically rank you up on our Discord server, supposing you have properly linked your Patreon and Discord accounts!
With your new rank, you'll be able to:
: set repeating reminders with `interval`, `natural` or the dashboard
: use unlimited uploads on SoundFX

Please note, you must be connected to the Discord server to receive Patreon rewards.
''',

    'prefix': {
        'no_argument': '''Please use this command as `@reminder-bot prefix <prefix>`''',

        'success': '''Prefix changed to {prefix}''',

        'too_long': '''Please select a prefix under 5 characters'''
    },

    'timezone': {
        'no_argument_title': '''Timezone Usage''',

        'no_argument': '''
**Usage:**
```{prefix}timezone <Name>```
**Example:**
```{prefix}timezone Europe/London```
You may want to use one of the popular timezones below, otherwise click [here](https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee):''',

        'no_timezone_title': '''Timezone Not Recognized''',

        'no_timezone': '''Possibly you meant one of the following timezones, otherwise click [here](https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee):''',

        'footer': '''Current timezone: {timezone}''',

        'set_p_title': '''Timezone Set''',

        'set_p': '''Timezone has been set to **{timezone}**. Your current time should be `{time}`''',
    },

    'meridian': {
        'title': '''Display Changed''',

        '12': '''Time display changed to **12 hour mode**''',

        '24': '''Time display changed to **24 hour mode**''',
    },

    'alias': {
        'invalid_command': '''Please use a command in the alias text. This command cannot be the alias command''',

        'not_found': '''No alias found with name `{name}`''',

        'created': '''New alias `{name}` created''',

        'removed': '''{count} alias deleted.'''
    },

    'restrict': {

        'disabled': '''Disabled restrictable command permissions for roles.''',

        'enabled': '''Enabled command permissions for roles.''',

        'title': '''Command Rules''',

        'failure': '''Failed to assign permissions for command `{command}`. This command either doesn't exist, or only works on preset restrictions''',
    },

    'remind': {
        'invalid_tag': '''Couldn't find a location by your tag. Your tag must be either a channel or a user (not a role)''',

        'invalid_time': '''Make sure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc. or `day/month/year-hour:minute:second`.''',

        'long_time': '''Make sure the time provided is less than {max_time} days in the future.''',

        'past_time': '''Please ensure the time provided is in the future. If the time *is* in the future, please be more specific with the definition.''',

        'success': '''Reminder for {location} set for {offset}''',

        'success_bulk': '''Reminders for {location} ({number}) set for {offset}''',

        'issue': '''Error occurred setting reminder for {location}:''',

        'issue_bulk': '''Errors occurred setting reminders for {location} ({number}):''',

        'title': '''{number} Reminders Set''',

        'attachment_too_large': '''Your attachment is too large to be sent. Please upload an attachment of 8MB or less''',

        'too_many_attachments': '''Too many attachments provided. Please only attach 1 file''',

        'attachment_download_failed': '''The attachment failed to download. Discord CDN could be down. Please retry later.''',

        'generic_error': '''A Discord error occurred: **{error}**''',
    },

    'interval': {
        'invalid_interval': '''Make sure the interval you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc. with no spaces, eg. 10s for 10 seconds or 10s12m15h1d for 10 seconds, 12 minutes, 15 hours and 1 day.''',

        'short_interval': '''Please ensure the interval provided is longer than {min_interval} seconds''',

        'invalid_expiration': '''Make sure the expiration time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc. or `day/month/year-hour:minute:second`.''',

        'long_interval': '''Please ensure the interval provided is less than {max_time} days''',

        'donor': '''You need to be subscribed to access this command! Type `{prefix}donate` to find out more.''',
    },

    'natural': {
        'invalid_time': '''Your time failed to process. Please make it as clear as possible, for example `16th of july` or `in 20 minutes`''',

        'long_time': '''Please ensure your reminder is younger than 50 years, or use a more specific time statement.''',

        'send': '''send''',

        'to': '''to''',

        'every': '''every''',
    },

    'del': {
        'listing': '''Listing reminders on this server... (there may be a small delay, please wait for the "List (1,2,3...)" message).''',

        'listed': '''List (1,2,3...) the reminders you wish to delete, or type anything else to cancel.''',

        'count': '''Deleted {} reminders!''',
    },

    'look': {
        'listing': '''Listing reminders on specified channel...''',

        'listing_limited': '''Listing the next {} reminders on specified channel...''',

        'inter': '''occurs next at''',

        'no_reminders': '''No reminders on specified channel.''',
    },

    'todo': {
        'add': '''*Do `{prefix}{command} add <message>` to add an item to your TODO, or type `{prefix}help {command}` for more commands!*''',

        'added': '''Added \'{name}\' to todo!''',

        'removed': '''Removed \'{}\' from todo!''',

        'error_value': '''Removal item must be a number. View the numbered TODOs using `{prefix}{command}`''',

        'error_index': '''Couldn\'t find item by that number. Are you in the correct todo list?''',

        'cleared': '''Cleared todo list!''',

        'confirm': '''You are about to delete **{} items** from your **{}** todo list. Are you sure? (type `yes` to confirm)''',

        'canceled': '''Clear canceled''',
    },

    'blacklist': {
        'removed_from': '''Removed blacklists from specified channels.''',

        'added_from': '''Added specified channels to blacklist.''',

        'removed': '''Removed current channel from blacklist.''',

        'added': '''Added current channel to blacklist.''',

    },

    'lang': {
        'select_title': '''Select Language''',

        'select': '''Use one of the commands or press a button below:''',

        'invalid_title': '''Invalid Language''',

        'invalid': '''Please select one from below:''',

        'set_p_title': '''Language Set''',

        'set_p': '''Language set to **English.**''',
    },

    'clock/time': '''Current time is **{}**''',

    'offset': {
        'invalid_time': '''Please ensure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d]''',

        'success': '''All reminders have been offset by {} seconds''',
    },

    'nudge': {
        'no_argument': '''Usage: `$nudge <time statement>`. Current nudge: {nudge}''',

        'invalid_time': '''Please ensure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d], and is less than 30'000 seconds''',

        'success': '''Future reminders will be nudged by {} seconds''',
    },

    'timer': {
        'limit': '''You already have 25 timers. Please delete some timers before creating a new one''',

        'name_length': '''Please name your timer something shorted (max. 32 characters, you used {})''',

        'unique': '''Please give your timer a unique name''',

        'success': '''Created a new timer''',

        'not_found': '''Could not find a timer by that name''',

        'deleted': '''Deleted a timer''',
    },

    'pause': {
        'invalid_time': '''Please ensure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc...''',

        'paused_until': '''Reminders in this channel have been silenced until **{}**''',

        'paused_indefinite': '''Reminders in this channel have been silenced indefinitely''',

        'unpaused': '''Reminders in this channel have been unsilenced''',
    },
}
