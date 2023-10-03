# coding : utf-8
# 夏目&青一
# @name:异步IO
# @time: 2023/5/28  15:11
import asyncio


async def test():
    await asyncio.sleep(2)
    print("任务完成")


if __name__ == '__main__':
    asyncio.get_event_loop()