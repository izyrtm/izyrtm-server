# izyrtm-server

izyrtm은 RTM 자동화를 위한 봇을 손쉽게 생성/운영 할 수 있도록 도와주는 솔루션입니다. 

## What's Better

## Architecture
![arch.png](./img/arch.png)

- 구성 : zulip + prometheus + grafana + rtm daemon

## How To Use
### Install & Build

1) zulip 설치

https://zulip.readthedocs.io/en/stable/production/install.html

2) prometheus + grafana + smtp 설치
- 파일 다운 : docker-compose.yml, prometheus.yml
- 빌드/설치/실행 : docker-compose up -d
- 삭제시 : docker-compose rm -s

3) rtm daemon 설치
- 파일 다운 : rtmBot 폴더 다운

### Run

- start izyrtmDaemon -> python3 izyrtm.py start  
- stop izyrtmDaemon -> python3 izyrtm.py stop
- status izyrtmDaemon ->python3 izyrtm.py status

- rtm daemon 구성

![file.png](./img/file.png)

- izyrtm 실행

![izyrtm.png](./img/izyrtm.png)

- izyrtm 노드 start

![start.png](./img/start.png)

- izyrtm 노드 status

![status2.png](./img/status2.png)

- izyrtm 노드 stop

![stop.png](./img/stop.png)


## License
MIT License

Copyright (c) 2019 izyrtm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
