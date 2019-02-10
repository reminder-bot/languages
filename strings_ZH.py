#: simplified chinese

{
    '__full__': 'simplified chinese',

    '__maintainer__' : '@Gourdyu',

    'blacklisted' : ''':x: 此频道已被禁止使用指令 :x:''',

    'admin_required' : '你需要管理员权限才能使用此指令。',

    'help' : '''请查看 https://reminder-bot.com/help?lang=ZH''',

    'no_perms_webhook' : '''**警告**：我需要`管理Webhooks`权限才能设置提醒事项。''',

    'no_perms_general' : '''指令被拒绝执行。请确保已正确设置我的权限。''',

    'help_raw' : [
        ['''提醒事项指令''', {
            '$natural' : '一种更简单的设置提醒的方式。请运行这个指令来获取更多信息。',

            '$del' : '删除服务器上的提醒事项或周期重复提醒。如果是私信提醒，请给bot私信发送这个指令。',

            '$look [频道]' : '查看频道中的提醒事项',

            '$remind [用户/频道] <提醒时间> <内容>' : '请优先考虑使用<code>$natural</code>而不是用这个指令。设置一个提醒。将时间设置成 [数字][s/m/h/d] 的格式，比如 10s 即10秒， 2s10m 即10分钟2秒。也可用<code>日/月/年-时:分:秒</code>的格式设置精确时间。',

            '$interval [用户/频道] <提醒时间> <重复周期> <内容>' : '<strong><a href="https://patreon.com/jellywx/">仅限Patron。</a></strong> 请优先考虑使用<code>$natural</code>而不是用这个指令。设置一个从<code>提醒时间</code>开始的周期重复提醒。将时间设置成普通的格式，例如<code>$interval 0s 20m Hello World!</code>就会每20分钟向该频道发送一次\'Hello World!\'。',

            '$todo' : '与待办事项列表有关的指令。使用<code>$todo help</code>来获取更多信息。',

            '$todos' : '和<code>$todo</code>一样，用于全服务器的任务管理。',

            '$timezone' : '设置服务器的时区，来让设置提醒更加容易。',

            '$offset' : '将服务器内的所有提醒事项全部平移指定时长（来应对夏令时）' }],

        ['''管理指令''', {
            '$restrict [指定身份组]' : '允许/禁止指定身份组设置频道提醒事项和周期重复提醒。',

            '$blacklist [频道名称]' : '允许/禁止在指定频道发送指令。' }],

        ['''其他指令''', {
            '$donate' : '查看有关捐赠的信息。',

            '$prefix <前缀符号>' : '更改前缀。',

            '$info' : '获取此bot的相关信息。',

            '$lang <语言名称>' : '更改语言。',

            '$clock' : '显示集体所在的时区当前的时间。',

            }
        ]
    ],


    'info' : '''
默认前缀：`$`
重设前缀：`@{user} prefix $`
帮助：`{prefix}help`

**欢迎来到Reminder Bot！**
开发者：<@203532103185465344>
图标：<@253202252821430272>
可以在 https://discord.gg/WQVaYmT 或 https://github.com/JellyWX 找到我 :)

邀请此bot： https://discordapp.com/oauth2/authorize?client_id=349920059549941761&scope=bot&permissions=8
使用控制台： https://reminder-bot.com/

*如果你需要询问有关新功能的问题，请发往Discord服务器*
''',

    'donate' : '''
想要每个月贡献些什么？请点击下方我的Patreon页面和官方bot服务器链接:D
https://www.patreon.com/jellywx

https://discord.gg/WQVaYmT

更多信息：

请将你的Patreon和Discord账号连接，这样当你捐赠的时候，Patreon就会自动将你从我们的Discord服务器上标识出来！
然后，你就可以：
: 使用仅限Patron的指令`interval`
: 设置带颜色嵌入块的提醒事项（可以在控制台中设置）
: 使用自定义头像的提醒事项（可以在控制台中设置，限$5档）

感谢所有已经成为Patron的人 :D 是你们让这个bot得以维护。

请注意，务必将你的Patreon和Discord账号连接，这样才能获得Patreon的权限。
''',

    'prefix' : {
        'no_argument' : '''
请像这样使用这个指令 `@reminder-bot prefix <前缀>`
''',
        'success' : '''
前缀已更改为{prefix}
''',

        'too_long' : '''请将前缀控制在5字符以下'''
    },

    'timezone' : {

        'no_argument' : '''
用法：
    ```{prefix}timezone <时区名>```
举例：
    ```{prefix}timezone Europe/London```
时区列表： https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
当前时区：{timezone}''',

        'no_timezone' : '''未知时区。可用的时区列表： https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'success' : '''时区已被设置为{timezone}。您当前的时间应为{time}'''
    },

    'restrict' : {

        'disabled' : '''成功禁止该身份组设置频道提醒。''',

        'enabled' : '''成功允许该身份组设置频道提醒。''',

        'allowed' : '''允许设置提醒的身份组：{}''',

        'help' : '''请指定身份组来更改其使用提醒指令的权限。'''
    },

    'remind' : {
        'no_argument' : '''
用法:
    ```{prefix}remind [发往的频道或用户] <剩余时间或时间点> <内容>```
举例:
    ```{prefix}remind #general 10s Hello world```
    ```{prefix}remind 10:30 现在是10:30```''',

        'invalid_tag' : '''无法定位你给出的发送对象。''',

        'invalid_time' : '''请以 [数字][s/m/h/d][数字][s/m/h/d]... 的格式，或 `日/月/年-时:分:秒` 的格式给出时间。

给出的时间不能超过未来50年。''',

        'invalid_chars' : '''提醒内容太长了！（最大150字符，你输入了{}字符。）用`{prefix}donate`来把最大长度扩大到1900字符（5美元档）。''',

        'invalid_chars_2000' : '''Discord限制一条信息不能超过2000字符。抱歉。''',

        'no_perms' : '''你必须拥有`管理信息`权限或可以向该频道发送提醒的身份组。请联系服务器的管理员，让他们使用`{prefix}restrict`指令来指定允许设置提醒的身份组。''',

        'success' : '''发往 <{}{}> 的提醒将在{}秒后发出。如果你想删除这条提醒，输入`$del`。''',
    },

    'natural' : {
        'no_argument' : '''
**新** 自然语言处理
举例：
    ```{prefix}natural in 10 minutes send Hello World! to #general```
    ```{prefix}natural at 18:00 send 搞一波大操作！```
    ```{prefix}natural on the 16th of july at 14:00 send 该交订阅费了！ to #subs```
    ```{prefix}natural now send 10分钟过去了！ every 10 minutes to #timer```
关键词：
    `send`：给出提醒内容
    `every`：给出重复周期（仅限Patreon）
    `to`：给出发往的对象
用法：
    ```{prefix}natural <时间短语> send <内容> [every 重复周期短语] [to #频道/@用户]```
    ''',

        'success' : '''发往 {} 的提醒将在{}秒后发出。如果你想删除这条提醒，输入`$del`。''',

        'bad_time' : '''未能成功处理给出的时间。请尽可能清楚地表述，比如`16th of july`或是`in 20 minutes`''',

        'long_time' : '''时间太长了！不要让提醒的时间超过未来50年''',

        'send' : ''' send ''',

        'to' : ''' to ''',

        'every' : ''' every '''

    },

    'interval' : {
        'no_argument' : '''
用法：
    ```{prefix}interval [指定频道或用户] <剩余时间或时间点> <重复周期> <内容>```
举例：
    ```{prefix}interval #general 9:30 1d 早上好！```
    ```{prefix}interval 0s 10s 这能烦死人```''',

        'invalid_interval' : '''请以 [数字][s/m/h/d][数字][s/m/h/d]... 的格式给出重复周期，不要空格，比如 10s 即10秒，或 10s12m15h1d 即1天15小时12分钟10秒。

给出的时间不能超过未来50年。''',

        '8_seconds' : '''请让重复周期大于8秒。''',

        'donor' : '''你必须成为Patron（捐赠2美元或更多）才能使用这个指令！输入`{prefix}donate`来了解更多。''',

        'success' : '''发往 <{}{}> 的周期重复提醒将在{}秒后开始。你还不能编辑提醒的内容，但你可以删除它。''',

        'removed' : '''这个服务器上没有Patron，所以设置的周期重复提醒已被删除。'''

    },

    'del' : {
        'listing' : '''正在列出此服务器上的提醒事项。（可能会有延迟，请等待“列出 (1,2,3...)”这条信息被发出。）''',

        'listed' : '''列出事项的编号(1,2,3...)来删除提醒，或者发送任意其他内容来取消。''',

        'count' : '''删除了{}条提醒！'''
    },

    'look' : {
        'listing' : '''正在列出指定频道上的提醒事项……''',

        'inter' : '''在''',
        
        'no_reminders' : '''指定频道上没有提醒事项。''',
    },

    'todo' : {
        'server_only' : '''请用`{prefix}todo`来使用你的个人待办事项列表。`{prefix}todos`只能在服务器中使用。''',

        'add' : '''*用`{prefix}{command} add <内容>`来向你的待办事项列表里添加事项，或输入`{prefix}{command} help`来查看更多指令！*''',

        'too_long' : '''抱歉，待办事项的内容限制在80字符以下。简短些 :)''',

        'too_long2' : '''抱歉，待办事项列表总计不能超过800字符。或许可以先去完成一些？''',

        'added' : '''成功将“{name}”加入待办事项列表！''',

        'removed' : '''“{name}”已从待办事项列表中移除！''',

        'error_value' : '''输入待移除事项的编号。用`{prefix}{command}`来查看待办事项列表。''',

        'error_index' : '''没有找到该数字对应的事项。你不会是迷路了吧？''',

        'help' : '''待办事项列表指令有：用`{prefix}{command} add <内容>`来增加待办事项，用`{prefix}{command} remove <编号>`来移除待办事项，用`{prefix}{command} clear`来清空待办事项列表，用`{prefix}{command}`来查看待办事项列表。''',

        'cleared' : '''待办事项列表已被清空！'''
    },

    'blacklist' : {
        'removed_from' : '''成功允许在该频道使用指令。''',

        'added_from' : '''成功禁止在该频道使用指令。''',

        'removed' : '''成功允许在此频道使用指令。''',

        'added' : '''成功禁止在此频道使用指令。'''

    },

    'lang' : {

        'invalid' : '''语言：
{}''',

        'set' : '''语言已设置为中文。''',
    },

    'clock' : {

        'time' : '''当前时间为{}。''',

    },

    'offset' : {

        'invalid_time' : '''请以 [num][s/m/h/d][num][s/m/h/d] 的格式给出时间''',

        'success' : '''已将所有提醒事项平移{}秒''',

    },
}
