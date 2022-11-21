async def analyse(self,infos):
    message = infos['content']
    if len(message) == 0:
        return
    if message[0] not in self.prefixes:
        return

    message = message.replace(message[0], "").split(' ')

    while '' in message:
        message.remove('')

    command = message[0]
    args = message[1:len(message)]
    for key in self.COMMANDS.keys():
        if key == command:
            await self.COMMANDS.get(key)(self, infos=infos, args=args)
            print(self.colorings.MAGENTA +
                  infos['author'].name + "#" + infos['author'].discriminator
                  + self.colorings.RESET + self.colorings.THISTLE +
                  f': issued a command -> {infos["content"].replace(infos["content"][0], "")}'
                  + self.colorings.RESET
                  )