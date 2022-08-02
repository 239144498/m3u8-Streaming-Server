#!/usr/bin python3
# -*- coding: utf-8 -*-
import random
from typing import Any, Union
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, Query, Response, Request
from starlette.middleware.sessions import SessionMiddleware

from .utile import *

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key=b'\xbaL%\xc0\x9a\xbe\xa5r\xbb\x7f \xd2\xd6\xb1\x9bU\x15\xb0\x0e\x05?\x91-\xcf'
)


@app.get('/')
def abc():
    return Response("A", status_code=200)


@app.get('/stream/{seq}.ts')
async def bitstream(seq: int,
                    host: Any = Query(None),
                    fid: Any = Query(...),
                    hd: Any = Query(None)) -> StreamingResponse | None:

    now = now_time()
    t = solve(os.environ['code2'].format(seq))
    if abs(now - t) > random.randint(300, 600):  # 截止时间
        return
    begin, seq, token, deadline = generpara(t).pop()
    url = generate_url(fid, host, hd, begin, seq, token, deadline, "gene")
    return StreamingResponse(fake_video_streamer(url), 200, headers, media_type='video/MP2T')


@app.get('/channel.m3u8')
def generate_file(
        host: Any = Query(None),
        fid: Any = Query(...),
        hd: Any = Query(None)) -> Union[Response, StreamingResponse] | None:
    return StreamingResponse(generate_m3u8(now_time(), host, fid, hd, "gene3"), 200, {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Content-Type': 'application/vnd.apple.mpegurl',
        'Expires': '-1',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Credentials': 'true',
    })


@app.get('/channel2.m3u8')
def generate_file(host: Any = Query(None),
                  fid: Any = Query(...),
                  hd: Any = Query(None)) -> Union[Response, StreamingResponse] | None:

    return StreamingResponse(generate_m3u8(now_time(), host, fid, hd, "gene"), 200, {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Content-Type': 'application/vnd.apple.mpegurl',
        'Expires': '-1',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Credentials': 'true',
    })


@app.get('/file.m3u')
def generate_file(hd: Any = Query(None)) -> StreamingResponse:
    if not hd:
        hd = "720"

    return StreamingResponse(generate_m3u(hd), 200, {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Content-Type': 'application/vnd.apple.mpegurl',
        'Expires': '-1',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Credentials': 'true',
    })


@app.get("/{file_path:path}")
def download(file_path: str) -> Response | StreamingResponse:
    if "live/pool/" not in file_path:
        return Response(status_code=404)

    url = os.environ['host'] + '/' + file_path
    return StreamingResponse(fake_video_streamer(url), 200, headers, media_type='video/MP2T')
