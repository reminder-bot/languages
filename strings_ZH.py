#: chinese simplified

{
    '__maintainer__' : '@Gourdyu',

    'blacklisted' : ''':x: 此频道已被禁止使用指令 :x:''',

    'admin_required' : '你需要管理员权限才能使用此指令。',

    'help' : '''请查看 https://jellywx.co.uk/help?lang=ZH''',

    'help_raw' : [
        ['''提醒事项指令''', {
            '$del' : '删除服务器上的提醒事项或周期重复提醒。如果是私信提醒，请给bot私信发送这个指令。',

            '$remind [用户/频道] <提醒时间> <内容>' : '设置一个提醒。将时间设置成[数字][s/m/h/d]的格式，比如 10s 即10秒， 2s10m 即10分钟2秒。也可用 `日`/`月`/`年`-`时`:`分`:`秒` 的格式设置精确时间。',

            '$interval [用户/频道] <提醒时间> <重复周期> <内容>' : '设置一个周期重复提醒，给出的`内容`将从`提醒时间`开始，每隔`重复周期`被重复提醒一次。将时间设置成如上格式。例如`$interval 0s 20m Hello World!`就会每20分钟向该频道发送一次`Hello World!`。',

            '$todo' : '与待办事项列表有关的指令。使用`$todo help`来获取更多信息。',

            '$todos' : '与`$todo`相似，用来设置全服务器的待办事项列表。',

            '$timezone' : '设置服务器的时区，从而更容易地设置提醒。' }],

        ['''管理指令''', {
            '$autoclear [时间/秒] [频道]' : '开启/关闭自动清除功能，在指定频道（默认为该频道）发送的信息将在发出后指定时间（默认10秒）被自动清除。',

            '$clear <指定用户>' : '清除指定用户发送的信息。',

            '$restrict [指定身份组]' : '允许/禁止指定身份组设置频道提醒事项和周期重复提醒。',

            '$tag' : '标签指令。使用`$tag help`来获取更多信息。',

            '$blacklist [频道名称]' : '允许/禁止在指定频道发送指令。' }],

        ['''其他指令''', {
            '$donate' : '查看有关捐赠的信息。',

            'mbprefix <前缀符号>' : '更改前缀。此指令不需要添加前缀！',

            '$info' : '获取此bot的相关信息。',

            '$lang <语言名称>' : '更改语言。',

            '$clock [12]' : '显示现在的时间，附加选项则显示十二小时制的时间。' }
        ]
    ],

    'web_foot_title' : '更多信息',
    'web_foot' : '在输入指令时不要输入括号！比如， mbprefix ! ，而不是 mbprefix <!>',
    'web_foot2' : '如果你需要更多帮助，请加入我们的Discord服务器：',

    'about' : {'关于' : ['bot制作者：Jude Southworth', 'Github：<a href=https://github.com/JellyWX>https://github.com/JellyWX</a>', '想要制作bot？请在Discord上联系我。', '程序架构：OVH']},

    'join' : '加入我们的Discord服务器',
    'invite' : '邀请此bot到你的服务器',

    'info' : '''
默认前缀：`$`
重设前缀：`@{user} prefix $`
帮助：`{prefix}help`

**欢迎来到RemindMe！**
开发者：<@203532103185465344>
这个人超屌的：<@174243954487853056>
图标：<@253202252821430272>
在 https://discord.gg/WQVaYmT 或 https://github.com/JellyWX 可以找到我 :)

程序架构：`discord.py`
主机提供：OVH

我的其他bot（仅限Patron）:
https://discordapp.com/oauth2/authorize?client_id=411224415863570434&scope=bot&permissions=35840

*如果你需要询问有关新功能的问题，请发往Discord服务器*
*如果你需要为你或你的服务器询问有关bot开发的问题，请私信我*
''',

    'donate' : '''
想要每个月贡献些什么？请点击下面的Patreon和官方bot服务器链接:D
https://www.patreon.com/jellywx

https://discord.gg/WQVaYmT

更多信息：

如果你将你的Patreon和Discord账号连接，当你捐赠的时候，Patreon会自动将你列在我们的Discord服务器的排名上！
有了这个新的排名，你就可以：
: 使用仅限Patron的指令，如`interval`
: 设置更多提醒事项（无限制）
: 设置更长的提醒事项（2000字符）
: 设置更多/更长的标签

感谢所有已经成为Patron的人 :D 是你们让这个bot可以继续维护下去。

请注意，务必将你的Patreon和Discord账号连接，这样才能获得Patreon的特权。
''',

    'prefix' : {
        'no_argument' : '''
请像这样使用这个指令 `mbprefix <前缀>`
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
时区列表： https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
当前时区：{timezone}''',

        'no_timezone' : '''未知时区。可用的时区列表在 https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568''',

        'success' : '''成功设置时区为{timezone}。您当前时间应为{time}'''
    },

    'restrict' : {

        'disabled' : '''成功禁止该身份组使用频道提醒。''',

        'enabled' : '''成功允许该身份组使用频道提醒。''',

        'allowed' : '''允许使用指令的身份组：{}''',

        'help' : '''请指定身份组来更改其提醒事项指令的使用权限。'''
    },

    'clear' : {

        'no_argument' : '''请指定用户来清除他发送的信息。'''

    },

    'remind' : {
        'no_argument' : '''
用法:
    ```{prefix}remind [发往的频道或用户] <剩余时间或时间点> <内容>```
例子:
    ```{prefix}remind #general 10s Hello world```
    ```{prefix}remind 10:30 现在是10:30```''',

        'invalid_tag' : '''无法找到你给出的发送对象。''',

        'invalid_time' : '''确保你给出的时间是以 [数字][s/m/h/d][数字][s/m/h/d]... 的格式，或 `日/月/年-时:分:秒` 的格式。

给出的时间不能超过未来50年。''',

        'invalid_count' : '''这个频道里的待提醒事项太多了！用`{prefix}del`来删掉一些，或者用`{prefix}donate`来扩大最大量（5美元档）''',

        'invalid_chars' : '''提醒内容太长了！（最大150字符，你输入了{}字符）。用`{prefix}donate`来增加最大长度到1900字符（5美元档）。''',

        'invalid_chars_2000' : '''Discord限制一条信息不能超过2000字符。抱歉。''',

        'no_perms' : '''你必须拥有`管理信息`权限或可以向该频道发送提醒事项的身份组。请联系服务器的管理员，让他使用`{prefix}restrict`指令来指定允许使用指令的身份组。''',

        'success' : '''成功给 <{}{}> 设置{}秒钟后的提醒。如果你想删除这条提醒，输入`$del`。''',

        'success_new' : '''成功给 {} 设置{}秒钟后的提醒。如果你想删除这条提醒，输入`$del`。'''
    },

    'interval' : {
        'no_argument' : '''
用法：
    ```{prefix}interval [指定频道或用户] <剩余时间或时间点> <重复周期> <内容>```
举例：
    ```{prefix}interval #general 9:30 1d 早上好！```
    ```{prefix}interval 0s 10s 这能烦死人```''',

        'invalid_interval' : '''确保你给出的重复周期是以[num][s/m/h/d][num][s/m/h/d]...的格式，不要空格，比如 10s 即10秒，或 10s12m15h1d 即1天15小时12分钟10秒。

给出的时间不能超过未来50年。''',

        '8_seconds' : '''请让重复周期大于8秒。''',

        'donor' : '''你必须成为Patron（捐赠2美元或更多）才能使用这个指令！输入`{prefix}donate`来了解更多。''',

        'success' : '''成功给<{}{}>设置在{}秒钟后开始的周期重复提醒。你还不能编辑提醒的内容，但你可以删除它。''',

        'removed' : '''这个服务器上现在没有Patron了，所以设置的周期重复提醒已被删除。'''

    },

    'autoclear' : {
        'disable' : '''成功取消 {} 的自动清除。''',

        'enable' : '''成功开启 {} 的自动清除。''',
    },

    'del' : {
        'listing' : '''正在列出此服务器上的待提醒事项。（可能会有延迟，请等待"列出 (1,2,3...)"这条信息被发出。）''',

        'listed' : '''列出你想要删除的提醒事项的编号(1,2,3...)，或者发送随便其他的内容来取消。''',

        'count' : '''成功删除{}条提醒！'''
    },

    'todo' : {
        'server_only' : '''请用`{prefix}todo`来使用你的个人待办事项列表。`{prefix}todos`只能在服务器中使用。''',

        'add' : '''*用`{prefix}{command} add <内容>`来向你的待办事项列表里添加事项，或输入`{prefix}{command} help`来查看更多指令！*''',

        'too_long' : '''抱歉，待办事项的内容限制在80字符以下。简短些 :)''',

        'too_long2' : '''抱歉，待办事项列表一共不能超过800字符。或许可以先去完成其中的一些？''',

        'added' : '''成功向待办事项列表中加入“{name}”！''',

        'removed' : '''成功从待办事项列表中移除“{name}”！''',

        'error_value' : '''输入待移除事项的编号。用`{prefix}{command}`来查看待办事项列表。''',

        'error_index' : '''无法找到该数字对应的事项。你不会是迷路了吧？''',

        'help' : '''使用待办事项列表，用`{prefix}{command} add <内容>`来增加待办事项，用`{prefix}{command} remove <编号>`来移除待办事项，用`{prefix}{command} clear`来清空待办事项列表，以及用`{prefix}{command}`来查看待办事项列表。''',

        'cleared' : '''已清空待办事项列表！'''
    },

    'tags' : {

        'deleted' : '''已删除标签 {}''',

        'added' : '''已添加标签 {}''',

        'invalid_count' : '''抱歉，普通用户至多可设置6条标签。请删除一些标签，或者考虑使用`{prefix}donate`捐赠（5美元档）。''',

        'invalid_chars' : '''标签至多可容纳80字符。简短些！''',

        'colon' : '''请用冒号将标签的名称和内容分开。''',

        'illegal' : '''标签名称中请不要出现`add`、`new`、`remove`或`del`。''',

        'unfound' : '''无法找到你给出的名称的标签。''',

        'help' : '''使用`{prefix}tag add <名称>: <内容>` 来创建一个新标签。使用`{prefix}tag remove <名称>`来删除一个标签。使用`{prefix}tag <名称>`来查看标签内容。使用`{prefix}tag`来查看所有标签的列表。'''
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

        'set' : '''语言已被设为中文。''',
    },

    'clock' : {
        'clock' : '''现在时间为 {}。''',
    }

}
