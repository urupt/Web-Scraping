import requests
from bs4 import BeautifulSoup

result = requests.get('https://twilog.org/uryo1112')
soup = BeautifulSoup(result.text, 'html.parser')
Ryoukun_html_list = soup.find_all('p', class_='tl-text')

print('place | shop | food | reason')
print('---------- | ---------- | ---------- | ----------')
for Ryoukun_html in Ryoukun_html_list:
    Ryoukun_text = Ryoukun_html.get_text()

    element = Ryoukun_text.replace('まじでこの世の全ての', '')
    element2 = element.replace('好きに教えてあげたいんだが', '')
    element3 = element2.replace('には全ての人間を虜にする禁断の', '')
    element4 = element3.replace('がある', '')
    element5 = element4.replace('これが', '')
    element6 = element5.replace('超絶美味いからぜひ全国の', '')
    element7 = element6.replace('好き、', '')
    element8 = element7.replace('を愛する者たち、', '')
    element9 = element8.replace('を憎む者たち、全ての', '')
    element10 = element9.replace('関係者に伝われ', '')

    if 'っ！' in Ryoukun_text:
        element10 = Ryoukun_text.replace('っ！', '')

    if '超絶可愛いからぜひ全国の' in Ryoukun_text:
        element10 = Ryoukun_text.replace('超絶可愛いからぜひ全国の', '')

    if 'を見つけてしまったんだが、' in Ryoukun_text:
        element10 = Ryoukun_text.replace('を見つけてしまったんだが、', '')

    if 'まじでうますぎる' in Ryoukun_text:
        element10 = Ryoukun_text.replace('まじでうますぎる', '')

    print(element10)




