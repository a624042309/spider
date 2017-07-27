# date:2017-6-10
# version:Python 3.6.1
# 建议使用终端命令运行
# 替换headers中的Cookie、 User-Agent、 X-Xsrftoken
# 爬取知乎问题页头像 https://www.zhihu.com/question/22591304/followers
# 可以不使用requests库,仅使用urllib

from bs4 import BeautifulSoup
from urllib import request as urllib
from urllib import error
from time import sleep
import requests     
import re
import ssl
import random
import os

headers = {
	'Cookie':'_zap=2228213b-1890-4817-804b-71bee8aa3c04; d_c0="ABBC7LIcVwuPTjVYqE9gR-2gWxX-EZ8Da8E=|1487604555"; q_c1=a8d6539844464836a0cccac697d290f9|1495172985000|1495172985000; r_cap_id="ZjEzOGIzOGU3YzUxNDY5NDkyMDNkZjg1ZDhmMjc3ZTA=|1495914247|d663180f1d8b0cbb7836985d9b4812cae0d763c7"; cap_id="NzAxMjVkZjBmNDhhNGY4OWI5MDBmOWQ4NGU5YWQxYTM=|1495914247|8e1aa38e8c4ad0c104f59a04e50463b0e3b64ab8"; _zap=7ca00daa-9881-44b3-84fc-7f431950871a; aliyungf_tc=AQAAAH8602oUYAIAESDZ3T7B5sF53XSN; _xsrf=ff3132ee4530c4c2f46a1b36f06f8413; s-q=%E7%9F%A5%E4%B9%8E%E5%A4%B4%E5%83%8F%20%E7%88%AC; s-i=5; sid=sifgase8; z_c0=Mi4wQUFCQXJBeERBQUFBRUVMc3NoeFhDeGNBQUFCaEFsVk5EV1JSV1FBdnNyNkFjaXM3czU5d2pzVHkyYy0xTG5zTTFB|1496960427|68d58f196c431dbfc2f477163a997b007f55fe64; __utma=51854390.1144784705.1496960283.1496960283.1496960283.1; __utmb=51854390.0.10.1496960283; __utmc=51854390; __utmz=51854390.1496960283.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=51854390.100-1|2=registration_date=20141205=1^3=entry_date=20141205=1',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
	'X-Xsrftoken':'ff3132ee4530c4c2f46a1b36f06f8413'
}

# 下载网页
def getHTMLText(url,data):
	try:
		res = requests.post(url, headers=headers, data=data, timeout=10)
		res.raise_for_status()
		res.encoding = res.apparent_encoding
		return res.text
	except:
		return "产生异常"

# 找到所有头像的url,添加进list
def findImgs(html,imgList):
	soup = BeautifulSoup(html, "html.parser")
	imgs = soup.find_all('img',src=re.compile(r'_m\.jpg'))
	for img in imgs:
		# 去掉 \和" 字符，形成可下载的url
		img = (img.get('src')).replace('\\','').replace('\"','')
		# 发现特殊情况, url最后一个字符可能是 /
		if img[-1] == '/':
			img_list = list(img)
			img_list.pop()
			img = "".join(img_list)
		imgList.append(img)


# 下载保存到本地
def downloadImgs(imgList):
	print("找到%d个头像,开始下载..." % len(imgList))
	n = 0
	error_num = 0
	for imgUrl in imgList:
		try:
			# 存放路径
			urllib.urlretrieve(imgUrl, os.path.abspath('.') + '/jpg/%s.jpg' % n)
			n += 1
			# 终端运行会在当前行打印进度
			print('\r当前进度:{:.2f}%'.format(n*100/len(imgList)), end='')
			sleep(random.uniform(0.5,1))
                
		except error.URLError as e:
			error_num += 1
			print("\n第%d个%s" % (n,e.reason))
			continue
	print("\n下载完成,已下载%d个,失败%d个" % (len(imgList) - error_num, error_num))


def main():
	# 全局取消证书验证  （头像的图片地址是以https开头的，这里全局取消验证ssl）
	ssl._create_default_https_context = ssl._create_unverified_context

	url = "https://www.zhihu.com/question/22591304/followers"
	
	imgList = []
	
	print("正在查找所有用户头像,请稍候...")
	
	# 修改这里可以下载更多头像,ex: range(0,5000,20)
	for x in range(0,200,20):         
		# 生成post请求时用到的data
		data = {
			'start':'0',
			'offset':str(x)
		}
		html = getHTMLText(url,data)
		findImgs(html, imgList)
		# 睡眠函数用于防止爬取过快被封IP
		sleep(random.uniform(0.5,1))

	downloadImgs(imgList)

main()
