class Input:


    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

Search = Input('textsearch','input#search')


print(Search.loc)


class Button:


    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

home_button = Button('text','button#loc')
print(home_button.text,' ', home_button.loc)

class Title:


    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


home_title = Title('title_text', 'title#loc')
print(home_title.text, ' ', home_title.loc)


class Link:


    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
home_link = Link ('text_link', 'link#loc')
print(home_link.text, home_link.loc)


class Page:


    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)


home = Page('get_url')

home.get()