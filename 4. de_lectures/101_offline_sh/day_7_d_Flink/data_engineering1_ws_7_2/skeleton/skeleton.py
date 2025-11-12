from pyflink.datastream import StreamExecutionEnvironment  # Flink의 실행 환경을 가져오는 모듈 임포트

def main():
    # Flink 실행 환경 생성
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 생성하는 코드

    # 데이터 스트림 생성 코드
    data_stream = env.from_collection(["Hello", "Flink", "World"])

    # 스트림 데이터 출력
    data_stream.print()  # 데이터 스트림의 내용을 출력하는 코드

    # Flink 프로그램 실행
    env.execute("Flink Installation Test")  # Flink 프로그램 실행 코드

if __name__ == "__main__":
    main()
