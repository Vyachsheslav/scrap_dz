import bs4
import requests
from fake_headers import Headers


# HEADERS = {
# 'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
# 'Accept-Language': 'ru-RU,ru;q=0.9',
# 'Sec-Fetch-Dest': 'document',
# 'Sec-Fetch-Mode': 'navigate',
# 'Sec-Fetch-Site': 'same-origin',
# 'Sec-Fetch-User': '?1',
# 'Cache-Control': 'max-age=0',
# 'If-None-Match': 'W/“37433-+qZyNZhUgblOQJvD5vdmtE4BN6w”',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
# 'sec-ch-ua-mobile': '?0'}

URL = "https://habr.com/ru/all/"

#ключевые слова в новостях меняются, брал это для проверки что ищет по всем статьям
HUBS = ['мобильное','Максим']

list_news = []

def get_url_info(URL):
    response = requests.get(URL, headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    return soup

def get_articles():
    articles = get_url_info(URL).find_all('article')
    for article in articles:
        previews = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        previews = [article.find('p').text for preview in previews]    
        for preview in previews:
            if set(HUBS) & set(preview.split()):
                time = article.find(class_="tm-article-snippet__datetime-published").find('time').text
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                title = article.find("h2").find('span').text
                result = f"{time}: {title} ==> https://habr.com{href}"
                list_news.append(result)
    return     
                
    

if __name__ == "__main__":
    headers = Headers(os="mac", headers=True).generate()

    get_url_info(URL)
    get_articles()
    print(list_news)




