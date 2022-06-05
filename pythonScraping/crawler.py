import requests

from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles/page
    """

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output

        """
        print('URL: {}'.format(self.url))
        print('TITLE:{}'.format(self.title))
        print('BODY:\n{}'.format(self.body))


class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        Utilty function used to get a content string from
        a Beautiful Soup object and a selector. Return an empty
        string if no object is found for the given selector
        """

        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()


crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'https://www.oreilly.com', 'h1', 'section#product-description'],
    ['Reuters', 'https://www.reuters.com/', 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'https://www.brookings.edu/', 'h1', 'div.post-body'],
    ['Zn', 'https://zn.ua/', 'h1', 'div.StoryBodyCompanionColumn div p']
]

websites = []
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(
    websites[0],
    'https://www.oreilly.com/library/view/learning-python-5th/9781449355722/')
crawler.parse(
    websites[1],
    'https://www.reuters.com/world/europe/explosions-rock-ukrainian-capital-kyiv-mayor-says-2022-06-05/')
crawler.parse(
    websites[2],
    'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(
    websites[3],
    'https://zn.ua/macrolevel/kompensatsija-za-razrushennoe-zhile-chto-s-nej-ne-tak.html')
