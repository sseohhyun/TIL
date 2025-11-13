import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # 실행 환경 가져오기
    # 병렬성 2로 설정
    env.set_parallelism(2)  

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()  # 결측값 제거 후 리스트 변환

    # 데이터 스트림 생성
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())  # 데이터 스트림 생성

    # FlatMap 및 Filter 연산 적용
    finance_keywords = {"stock", "market", "investment", "economy"}
    processed_stream = (text_stream
                        .flat_map(lambda text: [(word.lower(), 1) for word in text.split()], 
                              output_type=Types.TUPLE([Types.STRING(), Types.INT()]))  # FlatMap 연산 적용
                        .filter(lambda x: x[0] in finance_keywords))  # 특정 금융 키워드만 필터링하는 함수

    # 키워드 별로 갯수 집계
    aggregated_stream = processed_stream.key_by(lambda x: x[0]).sum(1)
    # 결과 출력
    aggregated_stream.print()

    # 실행
    env.execute("FlatMap and Filter Example")  # Flink 실행

if __name__ == "__main__":
    main()
