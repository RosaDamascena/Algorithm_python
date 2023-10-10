# stack class 직접 구현

class Stack :
    # Stack 자료구조를 생성하는 순간, 기입해야 하는 정보들
    # 지금 생성한 stack의 크기
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        # 최초 생성시의 top
        self.top = -1

    def is_empty(self):
        # stack이 비었을 때 pop 메서드가 실행되면
        # 현재 stack이 비어있음을 알려줄 수 있어야 한다.
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        # stack이 가득 찼을 때 push 메서드가 실행되면
        # 현재 stack이 가득 찼음을 알려줄 수 있어야 한다.
        if self.top + 1 == self.size:
            return True
        else:
            return False

    def push(self, item):
        if self.is_full():
            raise Exception('Stack is full!')
        else:
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return value

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        else:
            return self.items[self.top]

    # 1. stack이 비었는지
    # 2. stack이 가득 찼는지
    # 3. 값 삽입
    # 4. 값 제거
    # 5. top 위치의 값 출력

s1 = Stack(3)
print(s1.items)
print(s1.top)
print(s1.is_empty())
print(s1.is_full())
s1.push('A')
print(s1.items)
print(s1.top)
print(s1.peek())
print(s1.pop())
print(s1.items)
print(s1.top)