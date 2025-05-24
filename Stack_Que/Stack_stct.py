class Stack:
    def __init__(self):
        self.items=[]

    def push(self,val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:          #IndexError발생 시, 리스트의 값을 지우거나 사용하거나 참조하는데 인덱스 값이 명확히 명시되지 않은 경우
            print("Stack is empty.")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty.")

    def __len__(self):
        return len(self.items)
    






