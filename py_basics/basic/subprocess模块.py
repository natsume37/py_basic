# coding : utf-8
# 夏目&青一
# @name:subprocess模块
# @time: 2023/1/27  18:05

import subprocess

while True:
    cmd = input('请输入系统命令')
    obj = subprocess.Popen(cmd,
                           shell=True,  # 通过终端执行
                           stdout=subprocess.PIPE,  # 命令正常执行的代码存放管道
                           stderr=subprocess.PIPE
                           )  # 命令出错结果保存到管道
    res = obj.stdout.read()  # 读取正确管道的内容（二进制数据）
    print(res.decode('utf-8'))  # 因为是系统命令，所以根据系统编码方式解码

    err_res = obj.stderr.read()
    print(err_res)
