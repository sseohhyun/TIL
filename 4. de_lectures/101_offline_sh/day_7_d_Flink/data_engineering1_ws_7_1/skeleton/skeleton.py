from pyflink.datastream import StreamExecutionEnvironment

def main():
    # Flink 실행 환경을 생성하세요.
    env = StreamExecutionEnvironment.get_execution_environment()

    # 병렬성을 2로 설정하세요.
    env.set_parallelism(2)

    # 간단한 데이터 스트림 생성
    data_stream = env.from_collection(["Hello", "Flink", "World"])

    # 스트림 데이터 출력
    data_stream.print()

    # Flink 프로그램을 실행하세요.
    env.execute("Flink Installation Test")

if __name__ == "__main__":
    main()
