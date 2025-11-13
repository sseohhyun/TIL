import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FileSink
from pyflink.common.serialization import Encoder
from pyflink.common.typeinfo import Types
from pyflink.java_gateway import get_gateway

def main():
    # 실행 환경 생성
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 함수 호출

    # 데이터 소스 생성
    data = ["Hello", "Flink", "World"]
    data_stream = env.from_collection(data, type_info=Types.STRING())  # 데이터를 스트림으로 변환하는 메서드 호출

    # Java 인코더 생성
    gateway = get_gateway()
    j_string_encoder = gateway.jvm.org.apache.flink.api.common.serialization.SimpleStringEncoder()  # Java 엔코더 객체 생성

    # Python Encoder 생성
    encoder = Encoder(j_string_encoder)

    # 출력 디렉터리 설정
    output_dir = "./output/result"
    os.makedirs(output_dir, exist_ok=True)  # 디렉터리 없으면 생성

    # FileSink 설정
    file_sink = FileSink.for_row_format(output_dir, encoder).build()  # FileSink 설정(빌드)

    # Sink에 데이터 연결
    data_stream.sink_to(file_sink)  # 데이터 스트림을 Sink에 연결

    # Flink 작업 실행
    env.execute("File Sink Example")  # Flink 실행 시작

if __name__ == "__main__":
    main()
