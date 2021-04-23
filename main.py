
# 淘宝商品比价
import requests
import re


def getHtmlText(url):
    try:
        header = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'cookie': '',
        }  # 隐去了cookie信息和referer信息
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        return r.text
    except:
        print("爬取失败")
        return ""


def parsePage(ilist, html):
    try:
        plt = re.findall(r'\"view_price\":\"\d+\.\d*\"', html)
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        # print(tlt)
        print('【总数】:{}【总数】'.format(len(plt)))
        for i in range(len(plt)):
            price = eval(plt[i].split('\"')[3])
            title = tlt[i].split('\"')[3]
            ilist.append([title, price])
        # print(ilist)
    except:
        print("解析出错")


def printGoodsList(ilist, num):
    print("=====================================================================================================")
    tplt = "{0:<3}\t{1:<30}\t{2:>6}"
    print(tplt.format("序号", "商品名称", "价格"))
    count = 0
    for g in ilist:
        count += 1
        if count <= num:
            print(tplt.format(count, g[0], g[1]))
    print("=====================================================================================================")


def main():
    goods = "母婴"
    depth = 1
    start_url = "https://s.taobao.com/search?q="+goods
    infoList = []
    num = 20
    for i in range(depth):
        try:
            url = start_url + '$S=' + str(44*i)
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            continue

    printGoodsList(infoList, num)


main()
