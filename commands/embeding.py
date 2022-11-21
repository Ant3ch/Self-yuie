async def embeding(self,infos,args):
    if self.config['share']['selfing']:
        await infos['message'].delete()
    if len(args) == 0:
        return

    args = self.__argAnalyse__(infos, ['title', 'color', 'description', 'image', 'url', 'author', ],
                               [['t'], ['c'], ['d'], ['i'], ['u'], ['a']])
    if args.get('c') is None:
        args.__setitem__('c', '0,0,0')
    if args.get('u') is None:
        args.__setitem__('u', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    await infos['channel'].send(content=self.tools.embed(
        title=args.get('t'),
        color=[int(val) for val in args.get('c').split(",") if val is not None],
        description=args.get('d'),
        img_url=args.get('i'),
        redirect_url=args.get('u'),
        author_text=args.get('a')
    ))