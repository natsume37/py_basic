'''const
originalInterfaceList = [
    {"name": "纯净/B站", "category": 1, "url": "https://z1.m1907.cn/?jx=", "showType": 3},
    {"name": "高速接口", "category": 1, "url": "https://jsap.attakids.com/?url=", "showType": 3},
    {"name": "综合/B站", "category": 1, "url": "https://vip.parwix.com:4433/player/?url=", "showType": 3},
    {"name": "OK解析", "category": 1, "url": "https://okjx.cc/?url=", "showType": 3},
    {"name": "夜幕", "category": 1, "url": "https://www.yemu.xyz/?url=", "showType": 3},
    {"name": "乐多资源", "category": 1, "url": "https://api.leduotv.com/wp-api/ifr.php?isDp=1&vid=", "showType": 3},
    {"name": "爱豆", "category": 1, "url": "https://jx.aidouer.net/?url=", "showType": 1},
    {"name": "虾米", "category": 1, "url": "https://jx.xmflv.com/?url=", "showType": 1},
    {"name": "M3U8.TV", "category": 1, "url": "https://jx.m3u8.tv/jiexi/?url=", "showType": 3},
    {"name": "人人迷", "category": 1, "url": "https://jx.blbo.cc:4433/?url=", "showType": 3},
    {"name": "全民", "category": 1, "url": "https://jx.blbo.cc:4433/?url=", "showType": 3},
    {"name": "七哥", "category": 1, "url": "https://jx.mmkv.cn/tv.php?url=", "showType": 3},
    {"name": "冰豆", "category": 1, "url": "https://api.qianqi.net/vip/?url=", "showType": 3},
    {"name": "迪奥", "category": 1, "url": "https://123.1dior.cn/?url=", "showType": 1},
    {"name": "CK", "category": 1, "url": "https://www.ckplayer.vip/jiexi/?url=", "showType": 1},
    {"name": "游艺", "category": 1, "url": "https://api.u1o.net/?url=", "showType": 1},
    {"name": "LE", "category": 1, "url": "https://lecurl.cn/?url=", "showType": 1},
    {"name": "ckmov", "category": 1, "url": "https://www.ckmov.vip/api.php?url=", "showType": 1},
    {"name": "playerjy/B站", "category": 1, "url": "https://jx.playerjy.com/?url=", "showType": 3},
    {"name": "ccyjjd", "category": 1, "url": "https://ckmov.ccyjjd.com/ckmov/?url=", "showType": 1},
    {"name": "爱豆", "category": 1, "url": "https://jx.aidouer.net/?url=", "showType": 1},
    {"name": "诺诺", "category": 1, "url": "https://www.ckmov.com/?url=", "showType": 1},
    {"name": "H8", "category": 1, "url": "https://www.h8jx.com/jiexi.php?url=", "showType": 1},
    {"name": "BL", "category": 1, "url": "https://vip.bljiex.com/?v=", "showType": 1},
    {"name": "解析la", "category": 1, "url": "https://api.jiexi.la/?url=", "showType": 1},
    {"name": "MUTV", "category": 1, "url": "https://jiexi.janan.net/jiexi/?url=", "showType": 1},
    {"name": "MAO", "category": 1, "url": "https://www.mtosz.com/m3u8.php?url=", "showType": 1},
    {"name": "老板", "category": 1, "url": "https://vip.laobandq.com/jiexi.php?url=", "showType": 1},
    {"name": "盘古", "category": 1, "url": "https://www.pangujiexi.cc/jiexi.php?url=", "showType": 1},
    {"name": "盖世", "category": 1, "url": "https://www.gai4.com/?url=", "showType": 1},
    {"name": "小蒋", "category": 1, "url": "https://www.kpezp.cn/jlexi.php?url=", "showType": 1},
    {"name": "YiTV", "category": 1, "url": "https://jiexi.us/?url=", "showType": 1},
    {"name": "星空", "category": 1, "url": "http://60jx.com/?url=", "showType": 1},
    {"name": "0523", "category": 1, "url": "https://go.yh0523.cn/y.cy?url=", "showType": 1},
    {"name": "17云", "category": 1, "url": "https://www.1717yun.com/jx/ty.php?url=", "showType": 1},
    {"name": "4K", "category": 1, "url": "https://jx.4kdv.com/?url=", "showType": 1},
    {"name": "云析", "category": 1, "url": "https://jx.yparse.com/index.php?url=", "showType": 1},
    {"name": "8090", "category": 1, "url": "https://www.8090g.cn/?url=", "showType": 1},
    {"name": "江湖", "category": 1, "url": "https://api.jhdyw.vip/?url=", "showType": 1},
    {"name": "诺讯", "category": 1, "url": "https://www.nxflv.com/?url=", "showType": 1},
    {"name": "PM", "category": 1, "url": "https://www.playm3u8.cn/jiexi.php?url=", "showType": 1},
    {"name": "奇米", "category": 1, "url": "https://qimihe.com/?url=", "showType": 1},
    {"name": "思云", "category": 1, "url": "https://jx.ap2p.cn/?url=", "showType": 1},
    {"name": "听乐", "category": 1, "url": "https://jx.dj6u.com/?url=", "showType": 1},
    {"name": "aijx", "category": 1, "url": "https://jiexi.t7g.cn/?url=", "showType": 1},
    {"name": "52", "category": 1, "url": "https://vip.52jiexi.top/?url=", "showType": 1},
    {"name": "黑米", "category": 1, "url": "https://www.myxin.top/jx/api/?url=", "showType": 1},
    {"name": "豪华啦", "category": 1, "url": "https://api.lhh.la/vip/?url=", "showType": 1},
    {"name": "凉城", "category": 1, "url": "https://jx.mw0.cc/?url=", "showType": 1},
    {"name": "33t", "category": 1, "url": "https://www.33tn.cn/?url=", "showType": 1},
    {"name": "180", "category": 1, "url": "https://jx.000180.top/jx/?url=", "showType": 1},
    {"name": "无名", "category": 1, "url": "https://www.administratorw.com/video.php?url=", "showType": 1},
    {"name": "黑云", "category": 1, "url": "https://jiexi.380k.com/?url=", "showType": 1},
    {"name": "九八", "category": 1, "url": "https://jx.youyitv.com/?url=", "showType": 1},

    {"name": "综合线路解析", "category": 2, "url": "https://laisoyiba.com/mov/s/?sv=3&url=", "showType": 1},
    {"name": "纯净/B站", "category": 2, "url": "https://z1.m1907.cn/?jx=", "showType": 1},
    {"name": "高速接口", "category": 2, "url": "https://jsap.attakids.com/?url=", "showType": 1},
    {"name": "综合/B站1", "category": 2, "url": "https://vip.parwix.com:4433/player/?url=", "showType": 1},
    {"name": "OK解析", "category": 2, "url": "https://okjx.cc/?url=", "showType": 1},
    {"name": "夜幕", "category": 2, "url": "https://www.yemu.xyz/?url=", "showType": 1},
    {"name": "虾米", "category": 2, "url": "https://jx.xmflv.com/?url=", "showType": 1},
    {"name": "全民", "category": 2, "url": "https://jx.quanmingjiexi.com/?url=", "showType": 1}'''


url= "https://jiexi.380k.com/?url=", "showType"
print(url)