import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FileSink
from pyflink.common.serialization import Encoder
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 메서드 호출
    
    # 병렬성 2로 설정
    env.set_parallelism(2)

    # 직접 만든 데이터 스트림
    manual_data = [("Manual1", 1000.0), ("Manual2", 2000.0)]
    manual_stream = env.from_collection(manual_data, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    # 파일에서 읽어온 데이터 스트림
    df = pd.read_csv("../data/data.csv")
    file_data = df[['transaction_id', 'amount']].dropna().values.tolist()
    file_stream = env.from_collection(file_data, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    # 두 개의 데이터 스트림 결합
    combined_stream = manual_stream.union(file_stream)  # 두 개의 스트림을 결합하는 연산

    # 데이터 변환 (금액을 1.2배 증가)
    processed_stream = combined_stream.map(lambda x: (x[0], x[1] * 1.2))

    # 튜플을 문자열로 변환 → "Manual1,1200.0"
    string_stream = processed_stream.map(
        lambda x: f"{x[0]},{x[1]}",
        output_type=Types.STRING()
    )

    # PrintSink를 활용한 출력
    string_stream.print()

    # FileSink 설정 (문자열 저장용)
    file_sink = FileSink.for_row_format(
        "./output/transactions_result",
        Encoder.simple_string_encoder()
    ).build()

    # FileSink 연결
    string_stream.sink_to(file_sink)

    # Flink 실행
    env.execute("Custom Source and Sink Example")


if __name__ == "__main__":
    main()
