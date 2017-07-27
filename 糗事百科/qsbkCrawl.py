from bs4 import BeautifulSoup
import requests
import re

def getHTMLText(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        #res.encoding = res.apparent_encoding
        return res.text
    except:
        return "下载网页异常"

def extContent(html, contList):
    soup = BeautifulSoup(html, "html.parser")
    divList = soup.find_all('div', class_=r'content')

    for i in range(len(divList)):
        span = divList[i].find('span').get_text()
        contList.append(span)
 
def writeFile(contList):
    # 此处要设定encoding参数
    file = open('qsbk.html', 'w', encoding='utf-8')
    file.write("<html>")
    file.write("<body>")
    num = 1
    for i in contList:
        file.write("<p>【%d】%s</p>" % (num, i))
        num += 1
    file.write("</body>")
    file.write("<html>")
    file.close()
    
def main():
    ''' 8hr      热门
        hot      24小时
        imgrank  热图
        text     文字
        history  穿越
        pic      糗图
        textnew  新鲜
        每个标签下都有35个page
    '''
    page = 35
    start_url = "https://www.qiushibaike.com/8hr/page/"
    contList = []
    for i in range(1,page + 1):
        try:
            url = start_url + str(i)
            print(url)
            html = getHTMLText(url)
            extContent(html, contList)
        except:
            url = start_url + str(i)
            print(url+"出错")
            continue
    writeFile(contList)

main()
