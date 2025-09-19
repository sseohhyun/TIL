import requests
from bs4 import BeautifulSoup
import urllib3

# SSL 경고 비활성화
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. 웹페이지 가져오기
url = "https://topis.seoul.go.kr/"
response = requests.get(url, verify=False)  # SSL 인증서 검증 비활성화 후 가져오기
print("문제 1. 웹페이지 가져오기")
print("답: 상태 코드:", response.status_code)  # 응답의 상태 코드를 출력합니다.
print("설명: 상태 코드 200은 웹페이지가 성공적으로 로드되었음을 의미합니다.")

# 2. <title> 태그 내용 추출
soup = BeautifulSoup(response.text, 'html.parser')  # HTML 파서를 지정합니다.
title = soup.select('title')  # <title> 태그를 찾습니다.
print("\n문제 2. <title> 태그 내용 추출")
print("답: 웹페이지 제목:", title if title else "제목 없음")  # title의 텍스트를 출력합니다.
print("설명: BeautifulSoup을 사용하여 HTML에서 <title> 태그의 내용을 추출했습니다.")

# 3. <a> 태그 개수 세기
links = soup.select('a')  # 모든 <a> 태그를 찾습니다.
print("\n문제 3. <a> 태그 개수 세기")
print("답: 링크 개수:", len(links))  # links의 길이를 출력합니다.
print("설명: find_all() 메소드를 사용하여 모든 <a> 태그를 찾고, 그 개수를 계산했습니다.")

# 4. 외부 링크 필터링 후 첫 5개의 href 속성 출력
external_links = [link.get('href') for link in links 
                  if link.get('href') and 
                    ('http' in link.get('href') or 'https' in link.get('href'))]  # 외부 링크만 필터링합니다.
print("\n문제 4. 외부 링크 필터링 후 첫 5개의 href 속성 출력")
print("답:", external_links[0:5])  # 첫 5개의 외부 링크를 출력합니다.
print("설명: href 속성에 'http' 또는 'https'가 포함된 외부 링크를 필터링하여 출력했습니다.")

# 5. 'traffic' 또는 '교통'이 포함된 텍스트 찾기
traffic_texts = soup.find_all(string=lambda string: 
                              any(keyword in string.lower() for keyword in ['traffic', '교통']) 
                              if string else False)  # 'traffic' 또는 '교통'이 포함된 텍스트 찾기
filtered_texts = [text.strip() 
                  for text in traffic_texts 
                  # 만약 이 텍스트(text)를 감싸고 있는 부모 태그의 이름이 p, div, span, li, strong, 또는 a 리스트 안에 있다면...
                  if text.parent.name in ['p', 'div', 'span', 'li', 'strong', 'a']]  # 특정 태그 내에서 텍스트 추출
print("\n문제 5. 'traffic' 또는 '교통'이 포함된 텍스트 찾기")
print("답: 'traffic' 또는 '교통'이 포함된 텍스트:")
for text in filtered_texts:
    print("  -", text)  # 각 텍스트를 출력합니다.
print("설명: 'traffic' 또는 '교통'이라는 단어가 포함된 텍스트를 찾고, 지정된 태그에서만 추출하여 출력했습니다.")


