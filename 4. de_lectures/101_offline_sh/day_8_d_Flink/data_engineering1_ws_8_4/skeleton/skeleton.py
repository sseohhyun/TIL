import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def process_transactions(input_stream):
    """
    거래 데이터를 반복 처리하는 함수
    - 최대 10회 반복 후 종료
    - 거래 금액을 10% 증가시키면서 5000 미만 데이터만 유지
    """
    max_iterations = 10  # 최대 반복 횟수
    iteration = 0

    while iteration < max_iterations:
        updated_stream = (input_stream
                          .map(lambda x: (x[0], x[1] * 1.1), output_type=Types.TUPLE([Types.STRING(), Types.FLOAT()]))  
                          .filter(lambda x: x[1] < 5000))  # 5000 미만 값만 유지

        if updated_stream is None or iteration == max_iterations - 1:  
            break  

        input_stream = updated_stream  # 업데이트된 데이터를 사용
        iteration += 1  

    return input_stream  # 최종 처리된 스트림 반환

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    transactions = df[['stock_ticker', 'amount']].dropna().values.tolist()  

    # 데이터 스트림 생성
    transaction_stream = env.from_collection(
        transactions, 
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()])
    )

    # 거래 금액 기준 데이터 분할
    high_value_stream = transaction_stream.filter(lambda x: x[1] >= 5000)  # 5000 이상인 거래만 선택하는 람다 함수
    low_value_stream = transaction_stream.filter(lambda x: x[1] < 5000 )  # 5000 미만 거래만 선택하는 람다 함수 작성

    # 반복 연산 적용
    processed_stream = process_transactions(low_value_stream)  # 반복 적용할 데이터 스트림 지정

    # 최종 결과 스트림 병합
    final_stream = high_value_stream.union(processed_stream)  # 두 개의 데이터 스트림을 병합

    # 결과 출력
    final_stream.print()

    # 실행
    env.execute("Transaction Processing with Split & Iteration")

if __name__ == "__main__":
    main()
