import requests
from bs4 import BeautifulSoup
import traceback
import re
import sys

def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return "下载异常"

def getStockList(lst, stockURL):
    print('getStockList:\n')
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    print("正在获取股票列表...\n")
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

    print("获取股票列表完成\n")

def getStockInfo(lst, stockURL, fpath):
    print("正在写入文件...")
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            
            infoDict = {}
            soup = BeautifulSoup(html, "html.parser")
            stockInfo = soup.find('div', attrs = {'class':'stock-bets'})

            name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding = 'utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                #不换行进度展示请使用命令行运行本程序
                print('\r当前进度:{:.2f}%'.format(count*100/len(lst)), end='')                
        except:
               count += 1
               #不换行进度展示请使用命令行运行本程序
               print('\r当前进度:{:.2f}%'.format(count*100/len(lst)), end='')
               continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = sys.path[0]+'/BaiduStockInfo.txt' # 写入文件路径为当前程序文件所在位置
    slist = []

    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
    print("\n执行完毕!")

main() 
