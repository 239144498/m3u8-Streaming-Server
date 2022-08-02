#!/usr/bin python3
# -*- coding: utf-8 -*-
import time
import requests

from opencc import OpenCC  # pip install opencc-python-reimplemented
from .settings import *

requests.packages.urllib3.disable_warnings()
request = requests.session()


async def fake_video_streamer(url):
    """
    下载url数据
    :param url:
    :return:
    """
    header = {
        'User-Agent': '(Windows NT 10.0; Win64; x64) PotPlayer/22.7.6',
        'Host': os.environ['host3'],
        'Cache-Control': 'no-cache',
    }
    s = now_time()
    with request.get(url=url, headers=header, verify=False, stream=True) as res:
        e = now_time()
        print(e - s)
        yield res.content


def generpara(now):
    """
    构造关键参数
    :param now:
    :return:
    """
    para = []
    exec(os.environ['code'])
    return para


def solve(eq, var='x'):
    """
    解未知数x
    :param eq:
    :param var:
    :return:
    """
    c = eval(eq, {var: 1j})
    return -c.real / c.imag


def generate_url(fid, host, hd, begin, seq, token, deadline, gene):
    """
    不同请求方式 url 不同
    :param fid:
    :param host:
    :param hd:
    :param begin:
    :param seq:
    :param token:
    :param deadline:
    :param gene:
    :return:
    """
    _ = os.environ[gene]
    HD = eval(os.environ['hd'])
    if gene == "gene3":
        if not host:
            host = os.environ['local']
        if hd:
            _ += f"&hd={hd}"
        return _.format(host, fid, fid, hd, begin, seq, token,
                        deadline)
    else:
        if not host:
            host = os.environ['local']
        if not hd:
            hd = HD['720']
        return _.format(host, fid, fid, hd, begin, seq, token,
                        deadline)


def generate_m3u8(now, host, fid, hd, gene):
    """
    构造 m3u8 数据
    :param now:
    :param host:
    :param fid:
    :param hd:
    :param gene:
    :return:
    """
    begin, seq, token, deadline = generpara(now).pop()
    yield f"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:4
#EXT-X-MEDIA-SEQUENCE:{seq}
#EXT-X-INDEPENDENT-SEGMENTS\n"""
    for num1, num2 in enumerate(range(0, 40, 4)):
        yield "#EXTINF:4,\n" + generate_url(fid, host, hd, begin + num2, seq + num1, token, deadline, gene) + "\n"
    # print("final:", now, seq, begin)


def generate_m3u(hd):
    """
    构造 m3u 数据
    :param para:
    :param now:
    :param hd:
    :return:
    """
    host = eval(os.environ['hosts'])[6]
    yield "#EXTM3U\n"
    for i in gdata()['Data']:
        # tvg-ID="" 频道id匹配epg   fsLOGO_MOBILE
        yield '#EXTINF:{} tvg-chno="{}" tvg-id="{}" tvg-name="{}" tvg-logo="{}" group-title="{}",{}\n'.format(-1, i[
            'fnCHANNEL_NO'], i['fnID'], i['fsNAME'], i['fsHEAD_FRAME'], i['fsTYPE_NAME'], i['fsNAME'])
        if hd == "720":
            yield host + f"/channel?fid={i['fs4GTV_ID']}\n"
        else:
            yield host + f"/channel?fid={i['fs4GTV_ID']}&hd={hd}\n"


def gdata():
    url = os.environ["url"] + "1"
    header = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,im1age/webp,*/*;q=0.8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    }
    with requests.get(url=url, headers=header, verify=False) as res:
        return res.json()


def t2s(para):
    """
    用于繁体转简体
    :param para:
    :return:
    """
    return OpenCC('t2s').convert(para)


def now_time():
    return int(time.time())
