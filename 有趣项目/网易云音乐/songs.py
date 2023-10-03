# coding : utf-8
# 夏目&青一
# @name:songs
# @time: 2023/2/18  14:49

# coding : utf-8
# 夏目&青一
# @name:网易云_hotsongs
# @time: 2023/2/18  9:40
import time
import requests
import re
from selenium import webdriver

cookie = '_ntes_nnid=009e2e729245a62cf441644733b3f07b,1676592171791; _ntes_nuid=009e2e729245a62cf441644733b3f07b; NMTID=00OUhG-gqWR5wdYlk2UjisCNId_y6cAAAGGXK5KVQ; WEVNSM=1.0.0; WNMCID=dricnq.1676592172039.01.0; WM_TID=U%2FUw7q64sFtABVVRRQLUfWfgyegltSA5; JSESSIONID-WYYY=B7HbOszuRYI%5CQYK%5CYbm1PSSbzPMa78C4Y%5CzPVH399yTY08uuKan2lGkN715uafWRQzkPWfxcemH6Z3zUeAIElewvjGyIsT5xY16zeYfEvdWTw%2BXhRgExwMReUhr3ACK2CIT8dsj22T1G5agw%5CqHdCSkx07z%5CUGBl6cglaJHB4bTy9tcW%3A1676686206229; _iuqxldmzr_=33; WM_NI=msKM47htFn9pKsAe0YzNgoMtqw1pv8KANaZM7%2FA4SythQpMIk95R%2FxjjDxd%2F3cBw1B%2Bt1mpK5vb8UaMIqvFJDREhF2ckQffzoL9%2BaGIf1RwTaSXph2yhmxg7VWnhnJKnS3Y%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb7ef54a6bba7acb45ab7a88ab7c84a929f9b86c86b8cb483a5ca6a8eb2a1a9ae2af0fea7c3b92aafad85aeb73dacac8a8fbc7c89ad8f86b353ba92a990d080b3a9ff91f534899f8282d947f5f18fd5d273b8b89f91d043a9e7fbb3ae74aab68c99e725f1bd8e98b44ae9acff8ef341f7aaaed9d86b8f97bf97c542888e8b89c53aa1b59f87e572ad94f7cce44d8bbaffb3f660a38d9891eb3abbb8a399e63d9689a289ed4289b29dd4dc37e2a3'
headers = {
    'cookie': cookie,
    'referer': 'https://music.163.com/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

urls_dic = {
    '热歌榜': 'https://music.163.com/discover/toplist?id=3778678',
    '飙升榜': 'https://music.163.com/discover/toplist',
    '新歌榜': 'https://music.163.com/discover/toplist?id=3779629',
    '原创榜': 'https://music.163.com/discover/toplist?id=2884035',
}


# 歌单获取
def songs(name=list(urls_dic.keys())[0], url=urls_dic['热歌榜']):
    global num
    num = 1
    res = session.get(url, headers=headers)
    print(f'{name}'.center(40, '-'))
    print(f'状态码：{res.status_code}')
    # print(res.text)
    res = re.findall(u'<a href="/song\?id=([\d]*)">([\u4e00-\u9fa5]{1,})</a></li>', res.text)[1:31]
    a = list(range(1,31))
    r = zip(res, a)
    res = list(r)
    # [('1997438791', '乌梅子酱'), ...]
    for song in res:
        print(f'\033[32m{num}    {song[0][1].center(20)}\033[0m')
        num += 1
    print(f'{name}'.center(40, '-'))
    return res


def web_music(vlues):
    # 拼接链接
    # http://music.163.com/song/media/outer/url?id=281951.mp3
    list = input('请输入要听歌曲的序列号-->>>').strip()
    # values = [((2, 4), 1), ((2, 4), 2), ((2, 4), 3), ((2, 4), 4)]
    for i in vlues:
        if i[1] == int(list):
            link = f'http://music.163.com/song/media/outer/url?id={i[0][0]}.mp3'
            # 静默模式
            # 初始化配置
            # options = webdriver.ChromeOptions()
            # # headless 为静默模式
            # # # 将配置传入浏览器
            # driver = webdriver.Chrome(options=options)
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_experimental_option('excludeSwitches', ['enable-automation'])
            option.add_experimental_option('useAutomationExtension', False)
            driver = webdriver.Chrome(options=option)
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': 'Object.defineProperty(navigator, "webdriver", {get:()=>undefined})'
            })
            object_existed = False
            try:
                print(f'{i[0][1]} 正在播放'.center(15, '+'))
                driver.get(link)
                if driver is not None:
                    try:
                        driver.execute_script('javascript:void(0);')
                        object_existed = True
                    except:
                        # webdriver要求浏览器执行Javascript出现异常
                        try:
                            driver.quit()
                        finally:
                            driver = None
                    finally:
                        # time.sleep(2)
                        input('按任意键取消播放-->>')
                        print(f'{i[0][1]}   播放结束！'.center(15, '-'))
                        driver.quit()
                if not object_existed:
                    pass
            except:
                driver.quit()
                print('歌曲播放失败')


# 主函数
def main():
    global c, music_link
    while True:
        print('默认为热歌榜'.center(30, '-'))
        for key in func_dic:
            print(key, func_dic[key][0])
        opt = input('请输入功能编码 >>>').strip()
        if opt == 'q' or opt == 'Q':
            break
        if opt == '5':
            if c != 0:
                print('正在调用歌曲链接')
                web_music(music_link)
            continue
        if opt == '':
            music_link = songs()
            c += 1

        elif opt not in func_dic:
            print('\033[33m输入有误，请重新输入！\033[0m')  # 输出黄色文字
            continue

        else:
            # 调用songs函数
            music_link = func_dic[opt][1](name=func_dic[opt][0], url=urls_dic[func_dic[opt][0]])
            c += 1


func_dic = {
    '1': ('热歌榜', songs),
    '2': ('飙升榜', songs),
    '3': ('新歌榜', songs),
    '4': ('原创榜', songs),
    '5': ('听歌模式', web_music),
    'q': ('退出',)
}

if __name__ == '__main__':
    session = requests.Session()
    session.headers.update(headers)
    num = 1
    c = 0
    print(
        ''' 
  __     __                __  __  
 |  \/\ /  \/\ /   |\/|  |/__`/  ` 
 |__/~~\|__/~~\    |  \__/.__/\__, 
'''
    )
    main()
    print('欢迎下次光临'.center(20, '-'))
