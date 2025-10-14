import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 그래픽 렌더링과 관련된 경고메시지가 뜰 수 있음 -> 문제없음
"""
[6516:8508:0315/183431.273:ERROR:direct_composition_support.cc(1122)] QueryInterface to IDCompositionDevice4 failed: 해당 인터페이스를 지원하지 않습니다. (0x80004002)
"""
def setup_driver():
    # 1. Chrome WebDriver 설정 및 실행
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # 보안 샌드박스 비활성화
    options.add_argument("--disable-dev-shm-usage")  # 공유 메모리 사용 비활성화
    driver = webdriver.Chrome(options=options)  # Chrome WebDriver를 실행합니다.
    return driver

def navigate_to_page(driver):
    # 2. 지정된 URL로 이동하고 페이지 로드 대기
    driver.get("https://topis.seoul.go.kr")  # URL을 지정하여 페이지를 엽니다.
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "contents-area"))  # 페이지의 특정 요소가 로드될 때까지 대기
    )

def search_keyword(driver, keyword):
    # 3. 검색창에 키워드를 입력하고 검색 버튼 클릭
    contents_area = driver.find_element(By.ID, "contents-area")  # 검색 영역을 찾습니다.
    search_box = contents_area.find_element(By.CSS_SELECTOR, "input.int-search")  # 검색창 찾기
    search_box.send_keys(keyword)  # 검색어를 입력합니다.
    search_button = contents_area.find_element(By.CSS_SELECTOR, "input.int-btn")  # 검색 버튼 찾기
    search_button.click()  # 검색 버튼을 클릭합니다.
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "asideContent"))  # 결과가 로드될 때까지 대기
    )

def scrape_results(driver):
    # 4. 검색 결과에서 데이터 추출
    aside_content = driver.find_element(By.CLASS_NAME, "asideContent")  # 결과 영역 찾기
    result_sections = {
        "도로": "resultListTraffic",
        "버스": "resultListBus",
        "정류소": "resultListBusStn",
        "따릉이": "resultListBic",
        "주차장": "resultListPark"
    }
    data = {section: [] for section in result_sections.keys()}
    for section_name, result_id in result_sections.items():
        results = aside_content.find_element(By.ID, result_id).find_elements(By.TAG_NAME, "li")  # 리스트 항목 찾기
        for result in results:
            item_text = result.text.strip().replace("\n", " | ")  # 줄바꿈을 제거하고 구분자를 추가
            data[section_name].append(item_text)
    return data

def save_data_to_csv(data):
    # 5. 데이터를 DataFrame으로 변환하여 CSV 파일로 저장
    all_data = [(category, item) for category, items in data.items() for item in items if item != "검색된 내역이 없습니다."]  # 유효한 데이터를 수집
    df = pd.DataFrame(all_data, columns=["Category", "Item"])  # DataFrame 생성
    df.to_csv("seoul_location_data.csv", index=False)  # CSV 파일로 저장
    print("1. 데이터가 seoul_location_data.csv 파일로 저장되었습니다.")

def load_data_from_csv():
    # 6. CSV 파일을 DataFrame으로 불러오기
    df = pd.read_csv("seoul_location_data.csv")  # CSV 파일 읽기
    print("\n2. 불러온 DataFrame:")
    print(df.head())  # DataFrame의 처음 5개 행 출력
    return df

def analyze_data(df):
    # 7. 각 카테고리별 데이터 개수 계산
    counts = df["Category"].value_counts()  # 카테고리별 개수 계산
    print("\n3. 각 카테고리별 데이터 개수:")
    print(counts)

    # 8. 가장 많은 데이터와 적은 데이터를 가진 카테고리 찾기
    max_category = counts.idxmax()  # 가장 많은 데이터가 있는 카테고리 찾기
    min_category = counts.idxmin()  # 가장 적은 데이터가 있는 카테고리 찾기
    print(f"\n4. 가장 많은 데이터가 있는 카테고리: {max_category} ({counts[max_category]}개)")
    print(f"   가장 적은 데이터가 있는 카테고리: {min_category} ({counts[min_category]}개)")

    # 9. 가장 긴 항목과 짧은 항목 이름 찾기
    df["Item"] = df["Item"].str.replace("\n", " ")  # 줄바꿈을 제거하여 깔끔하게 저장
    longest_name = max(df["Item"], key=len)  # 가장 긴 항목 이름 찾기
    shortest_name = min(df["Item"], key=len)  # 가장 짧은 항목 이름 찾기
    print(f"\n5. 가장 긴 이름: {longest_name} ({len(longest_name)}글자)")
    print(f"   가장 짧은 이름: {shortest_name} ({len(shortest_name)}글자)")

def main():
    driver = setup_driver()
    navigate_to_page(driver)
    search_keyword(driver, "관악구")  # 검색어를 사용하여 데이터 수집
    data = scrape_results(driver)
    driver.quit()  # 브라우저 종료

    save_data_to_csv(data)  # 수집된 데이터를 CSV 파일로 저장
    df = load_data_from_csv()  # 저장된 데이터를 불러오기
    analyze_data(df)  # 데이터 분석 수행

if __name__ == "__main__":
    main()