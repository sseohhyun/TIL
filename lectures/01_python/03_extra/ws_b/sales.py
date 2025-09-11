# sales.txt 파일 생성
with open('sales.txt', 'w') as file:
    pass

# sales.py 파일 작성
def record_sale(coffee, quantity):
    with open('sales.txt', 'a') as file:
        file.write(f"{coffee}, {quantity}\n")

