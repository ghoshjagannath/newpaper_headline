from bs4 import BeautifulSoup as soup
import requests 

# step-1 
# Search such website which enable use for web scrapping 
websites=["https://asiatimes.com/south-asia/india/"]



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

res=requests.get(websites[0],headers)
data=soup(res.text,'html.parser')


print(data.select('ul.menu-item-423205 li'))

for website in websites:

    try:
        res=requests.get(website)
        if res.status_code==200:
            print('Connection has been established')
            some=soup(res.text,'html.parser')
            news=some.find_all('h2')
            print("Printing Headlines of this website")
            for i in news:
                print(i.get_text())
                print(i.find('a')['href'])
            print("\n"*10)

        else:
            print('Connection has been jambed')
    except :
        pass

