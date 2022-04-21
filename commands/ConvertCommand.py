from utils import BotUtils


async def on_command(event, args):

    if len(args) == 1:
        if not args[0].isnumeric():
            try:

                ticks = BotUtils.convert_to_ticks(args[0])

                if not ((ticks * 15) % 15) == 0:
                    newTicks = ticks
                    ticks = str(int(ticks)) + '*'
                    if (newTicks % 0.015) == 10:
                        newTicks = ((newTicks * 15) + 5) / 15
                    else if (newTicks % 0.015) == 5:
                        newTicks = ((newTicks * 15) - 5) / 15
                    await event.channel.send('Converted ticks `' + str(ticks) + "` Consider `" + BotUtils.convert_to_human_time(newTicks) + "`")
                else:
                    ticks = int(ticks)
                await event.channel.send('Converted ticks `' + str(ticks) + "`")

            except ValueError:
                await event.channel.send('Invalid time format given.')

        else:
            time = BotUtils.convert_to_human_time(args[0])
            await event.channel.send('Converted time `' + str(time) + '`')
