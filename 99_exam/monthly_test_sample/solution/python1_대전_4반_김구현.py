def clean_name(name):
    """
    이름의 앞뒤 공백을 제거하고, 첫 글자만 대문자로 바꿉니다.
    (예: "  heLLo " -> "Hello")
    """
    # strip()으로 공백을 제거하고, capitalize()로 첫 글자를 대문자화합니다.
    return name.strip().capitalize()

def make_greeting(name):
    """
    정리된 이름을 받아 "안녕하세요, [이름]님!" 형식의 문자열로 만듭니다.
    (예: "홍길동" -> "안녕하세요, 홍길동님!")
    """
    # f-string을 사용하여 간단하게 문자열을 조합합니다.
    return f"안녕하세요, {name}님!"

def process_namelist(name_list):
    """
    전체 이름 리스트를 받아, 비어있지 않은 이름만 골라 인사말로 만들어
    리스트로 반환합니다.
    (이름이 공백으로만 이뤄진 경우는 무시합니다.)
    위에 작성한 함수들을 적절히 활용해야 합니다.
    """
    processed_list = []
    for name in name_list:
        # 1. 이름을 정리합니다.
        cleaned = clean_name(name)

        # 2. 정리된 이름이 비어있지 않은 경우에만 처리합니다.
        if cleaned:  # 빈 문자열은 False로 취급됩니다.
            # 3. 인사말을 만들어 리스트에 추가합니다.
            greeting = make_greeting(cleaned)
            processed_list.append(greeting)

    return processed_list

# ----------------------------------------------------
# 아래 코드는 절대 수정하지 마시오.
# ----------------------------------------------------
raw_names = [
    "  홍길동",
    "김싸피 ",
    "   ",
    "lee sunsin"
]

result = process_namelist(raw_names)
print(result)