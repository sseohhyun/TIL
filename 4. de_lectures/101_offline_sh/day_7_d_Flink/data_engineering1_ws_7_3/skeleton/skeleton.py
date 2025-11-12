import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 함수 호출

    # 병렬성 2로 설정
    env.set_parallelism(2)

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()  # 결측값 제거 후 리스트 변환

    # 데이터 스트림 생성
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())  # 데이터 스트림을 생성하는 메서드

    # WordCount 파이프라인 구성(2일차에 각각의 함수에 대한 내용 다룰 예정)
    word_count = (text_stream
                  .map(lambda text: [(word.lower(), 1) for word in text.split()], 
                       output_type=Types.LIST(Types.TUPLE([Types.STRING(), Types.INT()])))
                  .flat_map(lambda words: words, 
                            output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .reduce(lambda a, b: (a[0], a[1] + b[1])))

    # 결과 출력
    word_count.print()  # 스트림을 출력하는 메서드 호출

    # 실행
    env.execute("Finance News WordCount")  # Flink 실행을 시작하는 메서드 호출

if __name__ == "__main__":
    main()