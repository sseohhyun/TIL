import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경 가져오기
    
    # 병렬성 1로 설정
    env.set_parallelism(1)  

    # CSV 파일 로드
    df = pd.read_csv("../data/data.csv")  
    transactions = df[['stock_ticker', 'amount']].dropna().values.tolist()  # 주식 티커(상품)와 거래 금액 선택

    # 데이터 스트림 생성 (상품 ID, 거래 금액, 초기 거래 횟수(1) 추가)
    transaction_stream = env.from_collection(
        [(t[0], t[1], 1) for t in transactions],  # 거래 횟수(1) 추가
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.INT()])
    )

    # Keyby Reduce 연산: 상품별 총 거래 금액 및 거래 횟수 누적
    total_amount_stream = (transaction_stream
                           .key_by(lambda x: x[0])  # 특정 키 기준 그룹화 함수
                           .reduce(lambda a, b: (a[0], a[1] + b[1], a[2] + b[2])))  # 거래 금액 및 횟수 누적 함수

    # 평균 거래 금액 계산 (map 연산)
    average_transaction_stream = total_amount_stream.map(
        lambda x: (x[0], x[1], x[1] / x[2] if x[2] > 0 else 0),  # 평균 계산을 위한 map 연산 적용
        output_type=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.FLOAT()])
    )

    # 결과 출력 (상품별 총 거래 금액 및 평균 거래 금액)
    average_transaction_stream.print()  # 데이터 출력

    # Flink 실행
    env.execute("Stock Ticker Total and Average Transaction Amount")  # Flink 실행

if __name__ == "__main__":
    main()
