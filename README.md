# 0713

### 로컬 저장소 설정

1. git init(버전 관리를 시작할 디렉토리에서 진행) -> working directory

2. git add -> staging Area

3. git commit -m "" -> repository 순으로 작성

master --> git의 저장소(branch 이름)

branch -> 가지/ 실사용, 테스트용 으로 따로 개발할때, master branch test branch로 따로 개발

.git 이라는 파일을 만들어 개인 컴퓨터나 노트북에서 로컬 저장소로 설정하고 이후 작업물을 원격 저장소(github) 에 올릴 수 있다.

4. git remote add origin https://lab.ssafy.com/markrla/kbs.git / 명령어

git remote add origin(원격 저장소 이름) https://github.com/markrla/TIL.git  --> origin은 닉네임으로 origin1이나 다른 이름으로 바꿀 수 있다.

로컬 저장소에서 원격저장소의 주소 등록하기 -- 원격저장소 이름(기본 origin) 바꾸면 여러개 등록 가능

---
### 원격 저장소 설정 - gitlab , lab.ssafy

1. gitlab이나 lab.ssafy에서 new , new project 로 프로젝트 파일 생성 (ex TIL, 개인프로젝트) 

-lab.ssafy의 경우 Project URL에서 Groups이 아니라 Users로 만들기

-Initialize repository ... 로 README.MD 파일 생성할 것인가 선택 


---
### 로컬 저장소 -> 원격 저장소

commit 되어 있는 파일만 원격 저장소로 올릴 수 있음 

1. git push -u origin master  --> origin의 원격저장소에 master(로컬저장소)에서 작업한 작업물을 등록한다


---
### 원격 저장소 -> 로컬 저장소

1. git clone https://github.com/markrla/TIL.git  -> 원격저장소에서 로컬저장소로 옮기기 (github의 올려진 작업물을 노트북이나 개인컴퓨터로 가져올 수 있다.)

2. git pull --> 클론으로 모든 작업물을 가져온 이후, commit 이후의 작업물만 로컬저장소로 가져오기

.gitignore 파일 생성하고 이 파일에 파일 이름 넣기 ex) 0713.md

-> 파일이 무시됨

이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음

https://www.toptal.com/developers/gitignore/

control A 후 .gitignore 파일에 붙여넣기



