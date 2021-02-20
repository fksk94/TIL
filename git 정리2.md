# GIT 정리

* `git init`
  * 현재 폴더에서 git 명령어를 쓸 수 있게 해준다.
  * `.git` 파일이 생기고 이 파일에 지금부터 쓰는 git 명령어들과 history가 저장된다.
* `git log`
  * 현재 repository의 history를 보여준다.
  * option: `git log -p`는 변경된 history의 내용을 보여준다.
* `git diff`
  * 마지막 버전과 변경된 파일의 차이점을 보여준다.
* `git status`
  * working tree의 상태를 보여준다.
* `git add .`
  * 현재 폴더의 모든 파일을 staging area로 올려준다.
  * `.` 대신 각각의 파일을 지정해줘도 된다.
  * 예를 들면, `git add hello.txt`
* `git commit`
  * 버전을 만든다.
  * repository에 저장된다. 
    * 저장된다고 해서 원격과 동기화가 되는 것은 아니다.
    * repository에 저장된 데이터는 `push`로 원격 git과 동기화 시켜줘야 한다.
  * `git commit -m "message"` 는 우리가 커밋할 때, 쓸 메세지를 쓸 수 있게 만든다.
  * `-a`
    * 이 옵션은 이미 커밋이 한 번이라도 된 파일에서 변경된 부분만 add 및 커밋해준다.
* `git push`
  * 원격 git과 동기화 시킨다.
  * 현재 로컬 git에서 수정한 파일들을 원격 git으로 올리는 것이다.
  * `git push origin master` 이렇게 하면 master 브랜치로 올릴 수 있다.
  * `git push -u origin master` 
    * 이렇게 하면 다음부터 `git push`만 써도 `git push origin master`가 실행된다.
* `git reset --hard`
  * 마지막 버전으로 working tree를 돌린다.
  * add나 commit을 하지 않았을 때, 사용 가능
  * 했을 때도 사용가능한지 모르겠음 -- 다음에 알아볼 예정
  * 버전이 원격에 올라갔을 때, 말고 로컬에선 지지고 볶는 것은 가능.
  * 하지만.. 원격을 올라갔을 때는 얽히는 문제 발생... (이걸 어떻게 해결해야할지는 모르겠다.)
* `git log -p`
  * 이 명령어를 통해 각 커밋의 해시 값을 알 수 있다.
  * 그 해시 값을 통해 각 커밋 버전으로 돌아갈 수 있다.
* `branch`
  * 브랜치는 develop에서만 움직이며, 버전을 확실히 할 때(오류없이 기능이 잘 수행될 때) master 브랜치로 버전을 명시하며 커밋한다.
  * develop에서 커밋하는 것이 아니다.
  * develop은 가만히 머지만 하며, feature 브랜치에서 기능을 만들고 develop으로 하나씩 merge해 준다.
  * 그렇게 완성된 develop을 위의 문장처럼 `master`로 옮겨준다.
  * 음.. 적어도 3개의 브랜치가 있어야하는데, 4개정도 만들어주는 것이 좋을 것 같다.

* untracked files
  * git에서 관리하지 않고 있는 파일
* tracked files
  * git에서 관리하고 있는 파일
* Working Tree
  * 작업하고 있는 공간
  * add를 하면 Stage Area로 갱신한다.
* Stage Area
  * commit을 하면 Local Repository로 갱신한다.
* Local Repository
  * push를 하면 이제 원격 저장소에 갱신 및 저장된다.

![Image for post](https://miro.medium.com/max/686/1*diRLm1S5hkVoh5qeArND0Q.png)