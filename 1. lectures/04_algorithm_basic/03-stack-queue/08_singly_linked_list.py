class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.next = None  # 다음 노드를 가리키는 포인터


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # 링크드 리스트의 헤드 초기화

    # 특정 위치에 노드를 삽입하는 메서드
    def insert(self, data, position):
        new_node = Node(data)  # 삽입할 새로운 노드 생성
        if position == 0:  # 위치가 0인 경우
            new_node.next = self.head  # 새로운 노드의 다음을 헤드로 설정
            self.head = new_node  # 헤드를 새로운 노드로 변경
        else:
            current = self.head
            for _ in range(position - 1):  # 삽입 위치 이전까지 이동
                if current is None:  # 범위를 벗어난 경우
                    print("범위를 벗어난 삽입입니다.")
                    return
                current = current.next
            new_node.next = current.next  # 새로운 노드의 다음을 현재 노드의 다음으로 설정
            current.next = new_node  # 현재 노드의 다음을 새로운 노드로 설정

    # 리스트의 끝에 노드를 추가하는 메서드
    def append(self, data):
        new_node = Node(data)  # 추가할 새로운 노드 생성
        if self.is_empty():  # 리스트가 비어있는 경우
            self.head = new_node  # 헤드를 새로운 노드로 설정
        else:
            current = self.head
            while current.next:  # 마지막 노드까지 이동
                current = current.next
            current.next = new_node  # 마지막 노드의 다음을 새로운 노드로 설정

    # 리스트가 비어있는지 확인하는 메서드
    def is_empty(self):
        return self.head is None  # 헤드가 None인지 확인

    # 특정 위치의 노드를 삭제하는 메서드
    def delete(self, position):
        if self.is_empty():  # 리스트가 비어있는 경우
            print("싱글 링크드 리스트가 비었습니다.")
            return

        if position == 0:  # 첫 번째 노드를 삭제하는 경우
            deleted_data = self.head.data  # 삭제할 데이터 저장
            self.head = self.head.next  # 헤드를 다음 노드로 변경
        else:
            current = self.head
            for _ in range(position - 1):  # 삭제할 노드의 이전까지 이동
                if current is None or current.next is None:  # 범위를 벗어난 경우
                    print("범위를 벗어났습니다.")
                    return
                current = current.next
            deleted_node = current.next  # 삭제할 노드 저장
            deleted_data = deleted_node.data  # 삭제할 데이터 저장
            current.next = current.next.next  # 이전 노드의 다음을 삭제할 노드의 다음으로 변경
        return deleted_data  # 삭제한 데이터 반환

    # 특정 데이터를 가진 노드의 위치를 찾는 메서드
    def search(self, data):
        current = self.head
        position = 0
        while current:  # 리스트를 순회하며 데이터 찾기
            if current.data == data:
                return position  # 데이터가 있는 위치 반환
            current = current.next
            position += 1
        return -1  # 데이터를 찾지 못한 경우 -1 반환

    # 리스트를 문자열로 변환하는 메서드
    def __str__(self):
        result = []
        current = self.head
        while current:  # 리스트를 순회하며 데이터를 결과 리스트에 추가
            result.append(current.data)
            current = current.next
        return str(result)  # 결과 리스트를 문자열로 변환하여 반환


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print(sll)  # [1, 2, 3]

deleted_item = sll.delete(1)
print(f"Deleted item: {deleted_item}")  # 2
print(sll)  # [1, 2, 3]