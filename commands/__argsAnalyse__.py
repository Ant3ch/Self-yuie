import re
def argsAnalyse(self, infos: str, base_values: list[str, str], aliases: [str, str] = None) -> dict:
    dico = {}
    args = re.findall(' \{[^}]*\}', infos['content'])
    args = args[0].replace('}', '').replace('{', '')
    args = args.split(';')

    for arg in args:
        arg = arg.split('=')
        try:
            dico[arg[0].replace(' ', '')] = arg[1]

        except IndexError:
            continue

    args2 = {}
    for key in dico:
        for i, values in enumerate(base_values):
            for val in aliases[i]:
                if values == key or val == key:
                    args2[aliases[i][0]] = dico[key]
                    break

    return args2
