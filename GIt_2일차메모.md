## 협업을 통해 나의 코드를 공유하고 싶습니다.
## Remote Repository (원격저장소)
코드의 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
WorkingDirectory / StagingArea / Repository

다양한 원격 저장소 "서비스": GitLab, GitHub, Bitbucket
Git이란 "프로그램" 이다. 

## Remote
Github Repository ---(remote)--- Local Repository
git remote add origin remote_repo_url
origin은 url을 저장하는 변수(추가하는 원격 저장소 별칭)
remote_repo_url 은 github에서 주소

## push / pull & clone
push: 로컬에서 깃허브로ㅓ
pull or clone: 깃허브에서 로컬로
git push origin master : git아 push해줘 origin 이라는 이름의 원격 저장소에 master 라는 이름의 브랜치를

git config 에서의 이메일과 사용자네임은 그냥 누가만들었는지를 알려주는 것일뿐
git push origin master에서 로그인하라는 창: 너가 여기에 올 권한이 있느냐? (뭔말인지모르겟다)

## push결론: 원격저장소에는 commit이 올라가는 것. commit이력이 없다면 push불가능.

git pull origin master : 원격 저장소의 변경사항만을 받아옴(업데이트)
git clone remote_repo_url : 원격 저장소 전체를 복제 (다운로드)
clone받은 프로젝트는 이미 git init이 되어 있습니다.

git remote rm <remote_name>: 현재 로컬 저장소에 등록된 원격 저장소 삭제




## 지금까지 GIT정리
(자동저장설정후) 최상위폴더에서 git init > 수정 > git add a.txt > (git status) > git commit -m "first_commit" > (git log) 

깃허브에 올리기: git remote add origin githubURL > (git remote -v) > git push origin master
깃허브에서 내컴퓨터에받기: 복제:git clone URL 수정사항반영:git pull origin master

## gitignore
Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일
프로젝트에 따라 공유하지 않아야 하는 것들도 존재하기 때문
# 이해x

## Git revert
특정 commit을 없었던 일로 만드는 작업
git revert <commit id> 
git log 치면 commit뒤에 나오는 긴문자=commit id
작동원리: 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit 생성
git revert commit_id

:wq

## Git reset
:특정 commit으로 되돌아가는 작업
git reset [옵션] <commit_id>
옵션3가지: --soft / --mixed / --hard
삭제되는 commit들의 기록을 어떤 영역에 남겨둘 것인지 옵션을 활용해 조정가능
--soft: 삭제된 commit들의 기록을 staging area에 남김
--mixed(기본값이라 생략가능): 삭제된 '' working directory에 남김 - add commit으로 다시업로드가능
--hard: 삭제된 commit들의 기록을 남기지 않음

# ?: github에 올라간자료 reset외않되

## TIL : Today I Learned

git commit --amend : commit 메세지 수정

git restore : add하기 전에 수정내용 되돌리기.(복원절대불가)

git restore --staged : staging area에서 working directory로 되돌리기.
git rm --cached :  