# 로컬 WSL SSH 설정 및 비밀번호 없는 접속 구성 실습

## 1. OpenSSH 서버 설치
```bash
# OpenSSH 서버 설치
sudo apt install -y openssh-server
```

## 2. SSH 키 페어 생성
```bash
# RSA 키 페어 생성 (빈 비밀번호로)
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
```

## 3. 공개키를 자신의 authorized_keys에 등록
```bash
# 공개키를 authorized_keys에 추가
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

## 4. 권한 설정 (권한이 너무 넓으면 접속이 차단됨)
```bash
# - 600: 소유자만 읽기/쓰기 가능
chmod 0600 ~/.ssh/authorized_keys
```

## 5. SSH 접속 테스트 (localhost로 자기 자신에게 접속)
```bash
# SSH 접속 성공 시, 다음 메시지처럼 표시됩니다:
# Welcome to Ubuntu 22.04 LTS ...
ssh localhost
```
