class tools:
    HIDECHARACTER = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| "

    @staticmethod
    def embed(title: str = "", description: str = "", img_url: str = "", redirect_url: str = "", author_text: str = "",
              color: tuple or list = (0, 0, 0), show=False) -> str:
        to_put = []

        if author_text:
            author_text = f"author={author_text.replace(' ', '%2520')}&"
            to_put.append(author_text)

        if title:
            title = f"title={title.replace(' ', '%2520')}&"
            to_put.append(title)
        if description:
            description = f"description={description.replace(' ', '%2520')}&"
            to_put.append(description)
        if color:
            color = f"color={tools.__rgbhex__(color)}&"
            to_put.append(color)
        if img_url:
            image_url = f"image={img_url.replace(' ', '%2520').replace(':', '%253A').replace('/', '%252F')}&"
            to_put.append(image_url)
        if redirect_url:
            redirect = f"redirect={redirect_url.replace(' ', '%2520').replace(':', '%253A').replace('/', '%252F')}"
            to_put.append(redirect)

        embed = "https://embed.rauf.wtf/embed/?" + "".join(to_put)

        return tools.HIDECHARACTER + " " + embed if not show else embed

    @staticmethod
    def __rgbhex__(rgb: tuple or list):
        if len(rgb) < 3:
            raise Exception("INVALID RGB CODE")
        elif len(rgb) > 3:
            raise Exception("INVALID RGB CODE")
        hexadeciaml = []
        for digit in rgb:
            hexdigit = hex(digit).split('x')[-1]

            if len(hexdigit) == 1:
                hexdigit = "0" + hexdigit
            hexadeciaml.append(hexdigit)
        return "".join(hexadeciaml)



