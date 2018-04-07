#!/usr/bin/env python
import os


def push():
    push_movie = 'ffmpeg -re -i /home/movie/shendechuanshuo.mp4 -c copy -f flv rtmp://127.0.0.1:1935/hls/movie'
    os.system(push_movie)


if __name__ == '__main__':
    for i in range(0, 1000):
        push()

#nohup python -u ffmpeg_push.py > out.log 2>&1 &