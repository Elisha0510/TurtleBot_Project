# 원형 이중 링크드 리스트
class DCLinkedList:
    # D_C_L_List에서 쓸 노드
    class Node:
        def __init__(self, go , right , left , zone , num, n=None, p=None):
            self.go = go
            self.right = right
            self.left = left
            self.zone = zone
            self.num = num # 저장된 데이터
            self.next = n  # 다음 노드 가리키는 변수
            self.prev = p  # 이전 노드 가리키는 변수

    # D_C_L_List에서 필요한 변수
    def __init__(self):
        self.head = None  # 첫 생성시 내부에는 노드가 없음
        self.tail = None

    # head로 삽입. v : 데이터
    def insertNodeBefore(self, go , right , left , zone , num):
        # 없을 경우
        if self.head is None:
            self.head = self.Node(go , right , left , zone , num)
            self.tail = self.head  # 같은 노드를 가리킴
        else:
            # 기존 head.prev를 새 노드로 지정(새 노드의 prev는 tail, next는 head로 지정)
            self.head.prev = self.Node(go , right , left , zone , num, n=self.head, p=self.tail)
            self.head = self.head.prev  #head를 새 노드로 변경
            self.tail.next = self.head   #tail.next를 새 head로 업데이트

    # tail로 삽입. v : 데이터
    def insertNodeAfter(self, go , right , left , zone , num):
        # 없을 경우
        if self.tail is None:
            self.tail = self.Node(go , right , left , zone , num)
            self.head = self.tail  # 같은 노드를 가리킴
        else:
            # 기존 tail.next를 새 노드로 지정(새 노드의 prev는 tail, next는 head로 지정)
            self.tail.next = self.Node(go , right , left , zone , num, p=self.tail, n=self.head)
            self.tail = self.tail.next  #tail을 새 노드로 변경
            self.head.prev = self.tail #head.prev를 새 tail로 업데이트

    def printNodeBefore(self): ##프린트 하는 함수 다시 고려하기
        # 데이터가 없을 때
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            link = self.head  # 처음은 head를 지정. 이후부터는 현 노드의 next를 지정

            # link가 가리키는 노드가 없을 때까지 반복
            # None,0,""는 조건판단에서 False 처리, 그 외는 True로 처리
            while link:
                print(link.num, '<->', end=' ')
                if link == self.tail: #link가 tail일 경우 멈추기
                    break
                link = link.next  # link를 현 위치 노드의 next로 변경
            print()  # 줄바꿈 용

    def printNodeAfter(self):  ##프린트 하는 함수 다시 고려하기
        # 데이터가 없을 때
        if self.tail is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            link = self.tail

            while link:
                print(link.num, '<->', end=' ')
                if link == self.head: #link가 head일 경우 멈추기
                    break
                link = link.prev  # link를 현 위치 노드의 next로 변경
            print()  # 줄바꿈 용

    # head로 삭제
    def deleteNodeBefore(self):
        # 없을 경우 - > 스킵
        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return
        else:
            #현재 head가 가리키는 노드의 next를 새로운 head로 지정
            self.head = self.head.next
            self.head.prev = self.tail  #새로운 head.prev를 tail로 지정
            self.tail.next = self.head  #tail.next를 head로 지정

    # tail로 삭제
    def deleteNodeAfter(self):
        # 없을 경우 - > 스킵
        if self.tail is None:
            print("삭제할 노드가 없습니다.")
            return
        else:
            #현재 tail이 가리키는 노드의 prev를 새로운 tail로 지정
            self.tail = self.tail.prev
            self.tail.next = self.head #새로운 tail.next를 head로 지정
            self.head.prev = self.tail #head.prev를 tail로 지정

    # head로 조회(탐색) , 구역번호를 반환
    def searchNodeBefore_zone(self, num):
        # 데이터가 없을 때
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head  # 처음은 head를 지정. 이후부터는 현 노드의 next를 지정
            index = 0  # 몇 번째 노드인지 기록
            while link:
                # 내가 찾는 노드인지 확인
                if num == link.num:
                    print('노드를 찾았습니다.')
                    return link.zone  # 위치를 반환
                else:
                    link = link.next  # link를 현 위치 노드의 next로 변경
                    index += 1  # 위치값 1 증가
                    if link == self.tail: #link가 tail일 경우 멈추기
                        break
            # 여기까지 왔다 == 해당 v값을 가진 노드가 없다.
            
    #노드 개수 반환
    def searchnodenumber_right(self, node_start , node_end):
        # 데이터가 없을 때
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head  # 처음은 head를 지정. 이후부터는 현 노드의 next를 지정
            node_num = 0  # 노드의 수
            while link:
                # 시작노드를 찾았다면
                if node_start == link.num:
                    print('시작노드를 찾았습니다.')
                    link = link.next
                    while link != self.head:
                        if(node_end == link.num):
                            print("도착노드를 찾았습니다")
                            print("오른쪽으로는 %d개의 노드가 사이에 있습니다" %node_num)
                            return node_num
                        else:
                            link = link.next  # link를 현 위치 노드의 next로 변경
                            node_num += 1  # 노드의 수 1씩 증가
                            if link == self.tail: #link가 tail일 경우 멈추기
                                break
                else:
                    link = link.next
    def searchnodenumber_left(self, node_start , node_end):
        # 데이터가 없을 때
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head  # 처음은 head를 지정. 이후부터는 현 노드의 next를 지정
            node_num = 0  # 노드의 수
            while link:
                # 시작노드를 찾았다면
                if node_start == link.num:
                    print('시작노드를 찾았습니다.')
                    link = link.prev
                    while link != self.tail:
                        if(node_end == link.num):
                            print("도착노드를 찾았습니다")
                            print("오른쪽으로는 %d개의 노드가 사이에 있습니다" %node_num)
                            return node_num
                        else:
                            link = link.prev  # link를 현 위치 노드의 next로 변경
                            node_num += 1  # 노드의 수 1씩 증가
                            if link == self.tail: #link가 tail일 경우 멈추기
                                break
                else:
                    link = link.next


    # tail로 조회(탐색)
    def searchNodeAfter(self, num):
        # 데이터가 없을 때
        if self.tail is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.tail
            index = -1  # 몇 번째 노드인지 기록
            while link:
                # 내가 찾는 노드인지 확인
                if num == link.num:
                    return index  # 위치를 반환
                else:
                    link = link.prev  # link를 현 위치 노드의 prev로 변경
                    index -= 1  # 위치값 1 감소
                    if link == self.head: #link가 head일 경우 멈추기
                        break
            # 여기까지 왔다 == 해당 v값을 가진 노드가 없다.
            