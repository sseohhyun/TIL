import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment  # Flink 스트리밍 실행 환경을 가져오는 모듈
from pyflink.common.typeinfo import Types  # 데이터 타입을 정의하는 모듈

def main():
    # Flink 스트리밍 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경 생성

    # 병렬성 2로 설정
    env.set_parallelism(2)

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()  # 리스트 변환을 위한 메서드 호출

    # 스트리밍 데이터 스트림 생성
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())  # 데이터 스트림을 생성하는 메서드

    # WordCount 파이프라인 구성
    word_count = (text_stream
                  .flat_map(lambda text: [(word.lower(), 1) for word in text.split()], 
                            output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .sum(1))  # 실시간 합산을 위한 덧셈 함수

    # 결과 실시간 출력
    word_count.print()  # 스트림을 출력하는 메서드 호출

    # 실행
    env.execute("Streaming Finance News WordCount")  # Flink 실행을 시작하는 메서드 호출

if __name__ == "__main__":
    main()
