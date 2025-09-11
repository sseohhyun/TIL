# GIT 분산 버전 관리 시스템

# 원격 저장소

## 복습
- 변화를 기록하고 추적하는 것
- 분산 버전 관리 시스템

    |중앙 집중식 | 분산식|
    |---|---|
    |버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드|버전을 여러 개의 복제된 저장소에 저장 및 관리|
    |합치는 과정에서 충돌 발생, 중앙 서버가 손실되면 복구할 수 없음| 숨김폴더 `.git` 파일 내에 버전 별로 변동사항을 기록해 둠. 해당 파일을 내려받아 연결해서 업무 가능|

## GIT의 영역
### 1. Working Directory (현재 작업중인 영역)
실제 작업중인 파일들이 위치하는 영역
```bash
git add 00_startcamp/01_git/markdown.md
```
- 특정 md만 추가하여 staging area에 추가

### 2. Staging Area (기록 대상 모아두는 영역)
Working Directory에서 변경된 파일들 중에 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
```bash
git status
```
- 현재 staging area에 있는 파일을 확인할 수 있음
- Changes to be comitted -> 내가 추가한 파일을 확인
- Untracked files -> 변동사항이 생겼지만, 내가 추가하지 않았다는 파일, git이 신경쓰지 않는 파일

- Repository로 이동
    ```bash
    git commit -m "버전에 대한 설명"
    ```
- 로그 확인
    ```bash
    git log
    ```


### 3. Repository (저장소)
**버전(commit)** 이력과 파일들이 영구적으로 저장되는 영역, **모든 버전(commit)** 과 변경 이력이 기록됨


### 4. COMMIT
변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 'SNAPSHOT'이라고도 함
- commit을 위한 config 설정
    ```bash
    git config --global user.email "katie1426@naver.com"
    git config --global user.name "김서현"
    ```

## Remote Repository
1. GITLAB
- Private이 특징: 초대된 사람만 볼 수 있음, 자신이 만든 것은 자신만 볼 수 있음
2. GITHUB
- Public이 특징: 포트폴리오, 실력 증빙용  

### Remote Repository 설정
``` bash
git remote add origin https://github.com/hwi-min/TIL.git
```
- 해당 링크의 repository를 origin으로 부르겠다
- origin 제외 다른 이름으로 저장도 가능

### Push
``` bash
git push -u origin master
```