# 0713


git init(버전 관리를 시작할 디렉토리에서 진행) -> working directory

git add -> staging Area

git commit -m "" -> repository 순으로 작성

master --> git의 저장소(branch 이름)

branch -> 가지/ 실사용, 테스트용 으로 따로 개발할때, master branch test branch로 따로 개발

---
원격 저장소 - gitlab

git remote add origin https://lab.ssafy.com/markrla/kbs.git / 명령어


git remote add origin https://github.com/markrla/TIL.git

git push -u origin master

git pull

.gitignore 파일 생성하고 이 파일에 파일 이름 넣기 ex) 0713.md

-> 파일이 무시됨

이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음

https://www.toptal.com/developers/gitignore/

control A 후 .gitignore 파일에 붙여넣기