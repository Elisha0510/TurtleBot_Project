from DCLL import DCLinkedList

List = DCLinkedList()

def make_node():
    DCLinkedList.insertNodeBefore(List,1,1,1,5,401)
    DCLinkedList.insertNodeBefore(List,1,0,0,4,10)
    DCLinkedList.insertNodeBefore(List,1,0,0,4,9)
    DCLinkedList.insertNodeBefore(List,1,1,1,5,304)
    DCLinkedList.insertNodeBefore(List,1,0,0,3,8)
    DCLinkedList.insertNodeBefore(List,1,0,0,3,7)
    DCLinkedList.insertNodeBefore(List,1,0,0,3,6)
    DCLinkedList.insertNodeBefore(List,1,1,1,5,203)
    DCLinkedList.insertNodeBefore(List,1,0,0,2,5)
    DCLinkedList.insertNodeBefore(List,1,0,0,2,4)
    DCLinkedList.insertNodeBefore(List,1,1,1,5,102)
    DCLinkedList.insertNodeBefore(List,1,0,0,1,3)
    DCLinkedList.insertNodeBefore(List,1,0,0,1,2)
    DCLinkedList.insertNodeBefore(List,1,0,0,1,1)
    print("노드들을 모두 생성했습니다.")


def go_start(node_start):

    #출발노드로 경로 보내기
    if(node_start == 1):
        data = {1:'go:1', 2:'turn_left:1',3:'go:16'}
    elif(node_start == 2):
        data = {1:'go:1', 2:'turn_left:1',3:'go:26'}
    elif(node_start == 3):
        data = {1:'go:1', 2:'turn_left:1',3:'go:36'}
    elif(node_start == 102):
        data = {1:'go:1', 2:'turn_left:1',3:'go:47'}
    elif(node_start == 4):
        data = {1:'go:1', 2:'turn_left:1',3:'go:47', 4:'turn_right:1', 5:'go:7'}
    elif(node_start == 5):
        data = {1:'go:1', 2:'turn_left:1',3:'go:47', 4:'turn_right:1', 5:'go:14'}
    elif(node_start == 203):
        data = {1:'go:1', 2:'turn_left:1', 3:'go:6', 4:'turn_right:1',
            5:'go:21', 6:'turn_left:1',7:'go:41'}
    elif(node_start == 6):
        data = {1:'go:1', 2:'turn_left:1', 3:'go:6', 4:'turn_right:1',
            5:'go:21', 6:'turn_left:1',7:'go:30'}
    elif(node_start == 7):
        data = {1:'go:1', 2:'turn_left:1', 3:'go:6', 4:'turn_right:1',
            5:'go:21', 6:'turn_left:1',7:'go:20'}
    elif(node_start == 8):
        data = {1:'go:1', 2:'turn_left:1', 3:'go:6', 4:'turn_right:1',
            5:'go:21', 6:'turn_left:1',7:'go:10'}
    elif(node_start == 304):
        data = {1:'go:1', 2:'turn_left:1', 3:'go:6', 4:'turn_right:1', 5:'go:21'}
    elif(node_start == 9):   
        data = {1:'go:1', 2:'turn_left:1', 3:'go:6', 4:'turn_right:1', 5:'go:14'}
    elif(node_start == 10):
        data = {1:'go:1', 2:'turn_left:1', 3:'go:6', 4:'turn_right:1', 5:'go:7'}
    elif(node_start == 401):
        data = {1:'go:1', 2:'turn_left',3:'go:6'}
    return data

def go_end(node_start, node_end):
    # 만약 시작하는 노드가 꼭지점 노드가 아닐 때 
    zone_start = DCLinkedList.searchNodeBefore_zone(List,node_start) #출발노드의 구역
    zone_end = DCLinkedList.searchNodeBefore_zone(List, node_end) #도착노드의 구역

    # 5구역이 아니고 구역이 서로 같을 때
    if (zone_start == zone_end): 
        go_call = node_end - node_start
        if(zone_start == 3 or zone_start == 1): ## 1구역이거나 3구역일때
            if node_end > node_start:
                go_call = node_end - node_start
                #gocall 만큼 go 호출하기 오른쪽 방향 (방향 주의)
                data_node = {1:"go_410:%d" % go_call}
                print("오른쪽으로 %d번 go를 호출했습니다" % go_call)
                return data_node

            elif node_start > node_end:
                go_call = node_start - node_end
                #gocall 만큼 go 호출하기 왼쪽 방향 (방향 주의)
                data_node = {1:'turn_left:2', 2:'go_410:%d' %go_call}
                print("왼쪽으로 %d번 go를 호출했습니다" % go_call)
                return data_node
            
        elif(zone_start == 2 or zone_end == 4): ## 2구역이거나 4구역일때
            if node_end > node_start:
                go_call = node_end - node_start
                #gocall 만큼 go 호출하기 오른쪽 방향 (방향 주의)
                data_node = {1:"go_7:%d" % go_call}
                print("오른쪽으로 %d번 go를 호출했습니다" % go_call)
                return data_node

            elif node_start > node_end:
                go_call = node_start - node_end
                #gocall 만큼 go 호출하기 왼쪽 방향 (방향 주의)
                data_node = {1:'go_7:%d' %go_call}
                print("왼쪽으로 %d번 go를 호출했습니다" % go_call)
                return data_node
        
        elif(zone_start == 5):
            if(node_start == 401): # 출발하는 노드의 값이 401일 때
                if(node_end == 102): # 401 -> 102
                    data_node={1:'go_410:4'}
                    return data_node

                elif(node_end == 203): # 401 -> 203
                    data_node={1:'go_410:4', 2:'turn_right:1', 3:'go_7:3'}
                    return data_node

                elif(node_end == 304): # 401 -> 304
                    data_node={1:'turn_right:1', 2:'go_7:3'}
                    return data_node
            
            elif(node_start == 102): # 출발하는 노드의 값이 102일 때
                if(node_end == 203):
                    data_node={1:'turn_right:1', 2:'go_7:3'}
                    return data_node

                elif(node_end == 304):
                    data_node={1:'turn_right:1', 2:'go_7:3', 3:'go_410:4'}
                    return data_node

                elif(node_end == 401):
                    data_node-{1:'turn_left:2' , 2:'go_410:4'}
                    return data_node
            
            elif(node_start == 203): # 출발하는 노드의 값이 203일 때
                if(node_end == 304):
                    data_node={1:'turn_right:1', 2:'go_410:4'}
                    return data_node

                elif(node_end == 401):
                    data_node={1:'turn_right:1', 2:'go_410:4', 3:'turn_right:1', 4:'go_7:3'}
                    return data_node 

                elif(node_end == 102):
                    data_node-{1:'turn_left:2', 2:'go_7:3'}
                    return data_node
            
            elif(node_start == 304): # 출발하는 노드의 값이 304일 때
                if(node_end == 401):
                    data_node={1:'turn_right:2', 2:'go_7:3'}
                    return data_node

                elif(node_end == 102):
                    data_node={1:'turn_left:1', 2:'go_410:4', 3:'turn_left:1'}
                    return data_node

                elif(node_end  == 203):
                    data_node={1:'turn_left:1', 2:'go_410:4'}
                    return data_node
                
        
    else: # 서로 다른 구역일 때
        if (zone_start == 1): #출발구역이 1일 때
            if(zone_end == 2): #출발구역이 1이고 도착구역이 2일때
                zone_one = 3 - node_start +1
                print("%d번 go를 호출했습니다"% zone_one)
                #오른쪽으로 돌기
                print("오른쪽으로 90도 돌았습니다")
                zone_two = 2 - (5 - node_end)
                print("%d번 go를 호출했습니다"% zone_two)
                data_node = {1:'go_410:%d' %zone_one , 2:'turn_right:1', 3:'go_7:%d' %zone_two}
                return data_node
            
            # 더 짧은 거리 찾게 하기
            elif(zone_end == 3): #출발구역이 1이고 도착구역이 3일때
                #오른쪽으로 갈 때의 출발과 도착 사이의 노드 개수를 반환
                node_num_r = DCLinkedList.searchnodenumber_right(List, node_start, node_end)
                # 왼쪽으로 갈 때의 출발과 도착 사이의 노드 개수 반환
                node_num_l = 12 - node_num_r
                # 오른쪽 사이노드 < 왼쪽 사이노드 => 오른쪽으로 이동
                if(node_num_r <= node_num_l):
                    print("오른쪽 경로가 최단거리입니다.")
                    zone_one = 4 - node_start 
                    print("%d번 go를 호출했습니다"% zone_one)
                    #오른쪽으로 돌기 
                    print("오른쪽으로 90도 돌았습니다")
                    zone_two = 3
                    print("%d번 go를 호출했습니다"% zone_two)
                    #오른쪽으로 돌기
                    print("오른쪽으로 90도 돌았습니다")
                    zone_three = 3 - (8 - node_end)
                    print("%d번 go를 호출했습니다"% zone_three)
                    data_node = {1:'go_410:%d' %zone_one , 2:'turn_right:1', 3:'go_7:3', 
                                4:'turn_right:1', 5:'go_410:%d' %zone_three}
                    return data_node
                
                # 오른쪽 사이노드 > 왼쪽 사이노드 => 왼쪽으로 이동
                else:
                    print("왼쪽 경로가 최단거리입니다.")
                    #왼쪽 방향 보게 하기
                    zone_one = node_start
                    print("%d번 go를 호출했습니다"% zone_one)
                    #왼쪽으로 90도 돌기
                    print("왼쪽으로 90도 돌았습니다")
                    zone_two = 3
                    print("%d번 go를 호출했습니다"% zone_two)
                    #왼쪽으로 90도 돌기
                    print("왼쪽으로 90도 돌았습니다")
                    zone_three = 9 - node_end
                    print("%d번 go를 호출했습니다"% zone_three)
                    data_node={1:'go_410:%d' %zone_one, 2:'turn_left:1', 3:'go_7:3',
                            4:'turn_left:1', 5:'go_410:%d' %zone_three}
                    return data_node
                    
            elif(zone_end == 4):
                #왼쪽 방향 (뒤를 보기) 보게하기
                zone_one = node_start; #직진
                print("%d번 go를 호출했습니다"% zone_one)
                #좌회전
                print("왼쪽으로 90도 돌았습니다")
                zone_four = 11 - node_end
                print("%d번 go를 호출했습니다"% zone_four)
                data_node = {1:'go_410:%d' %zone_one , 2:'turn_left:1', 3:'go_7:%d' %zone_four}
                return data_node
    #------------------------------------------------------------------------
                
        elif(zone_start == 2): #출발구역이 2일 때
            if(zone_end == 1): #출발구역이 2이고 도착구역이 1일때
                # 뒤로 돌기 (180도 회전)
                print("뒤로 180도 돌았습니다")
                zone_two = 2 - (5-node_start)
                print("%d번 go를 호출했습니다"% zone_two)
                #좌회전으로 돌기
                print("왼쪽으로 90도 돌았습니다")
                zone_one = (3-node_end) + 1
                print("%d번 go를 호출했습니다"% zone_one)
                data_node={1:'turn_left:2', 2:'go_7:%d' %zone_two, 3:'turn_left:1', 
                        4:'go_410:%d' %zone_one}
                return data_node
                
            elif(zone_end == 3): #출발구역이 2이고 도착구역이 3일때
                zone_two = (5-node_start)+ 1
                print("%d번 go를 호출했습니다"% zone_two)
                #오른쪽으로 회전
                print("오른쪽으로 90도 돌았습니다")
                zone_three = 3 - ( 8 - node_end )
                print("%d번 go를 호출했습니다"% zone_three)
                data_node = {1:'go_7:%d' %zone_two , 2:'turn_right:1', 3:'go_410:%d' %zone_three}
                return data_node
                
            # 더 짧은 거리 찾게 하기
            elif(zone_end == 4): #출발구역이 2이고 도착구역이 4일때
                #오른쪽으로 갈 때의 출발과 도착 사이의 노드 개수를 반환
                node_num_r = DCLinkedList.searchnodenumber_right(List, node_start, node_end)
                # 왼쪽으로 갈 때의 출발과 도착 사이의 노드 개수 반환
                node_num_l = 12 - node_num_r
                # 오른쪽 사이노드 < 왼쪽 사이노드 => 오른쪽으로 이동
                if(node_num_r <= node_num_l):
                    print("오른쪽 경로가 최단거리입니다.")
                    zone_two = ( 5- node_start) + 1
                    print("%d번 go를 호출했습니다"% zone_two)
                    #오른쪽으로 회전
                    print("오른쪽으로 90도 돌았습니다")
                    zone_three = 4
                    print("%d번 go를 호출했습니다"% zone_three)
                    #오른쪽으로 회전
                    print("오른쪽으로 90도 돌았습니다")
                    zone_four = 2 - (10 - node_end)
                    print("%d번 go를 호출했습니다"% zone_four)
                    data_node = {1:'go_7:%d' %zone_two ,2:'turn_right:1',3:'go_410:4',4:'go_7:%d' %zone_four}
                    return data_node
                
                # 오른쪽 사이노드 > 왼쪽 사이노드 => 왼쪽으로 이동
                else:
                    print("왼쪽 경로가 최단거리입니다.")
                    #왼쪽 방향 보게 하기
                    zone_two = 2 - (5 - node_start)
                    print("%d번 go를 호출했습니다"% zone_two)
                    #왼쪽으로 90도 돌기
                    print("왼쪽으로 90도 돌았습니다")
                    zone_one = 4
                    print("%d번 go를 호출했습니다"% zone_one)
                    #왼쪽으로 90도 돌기
                    print("왼쪽으로 90도 돌았습니다")
                    zone_four = 1 + (10 - node_end)
                    print("%d번 go를 호출했습니다"% zone_four)
                    data_node = {1:'go_7:%d' %zone_two,2:'turn_left:1',3:'go_410:4', 4:'turn_left:1', 5:'go_7:%d' %zone_four}
                    return data_node
                
    #-----------------------------------------------------9-------------------

        elif(zone_start ==3): #출발구역이 3일때
            #더 짧은 거리 찾게하기
            if(zone_end == 1):# 출발구역이 3이고 도착구역이 1일때
                #왼쪽으로 갈 때의 출발과 도착 사이의 노드 개수를 반환
                node_num_l = DCLinkedList.searchnodenumber_left(List, node_start, node_end)
                # 오른쪽으로 갈 때의 출발과 도착 사이의 노드 개수 구하기
                node_num_r = 12 - node_num_l
                # 오른쪽 사이노드 < 왼쪽 사이노드 => 오른쪽으로 이동
                if(node_num_r <= node_num_l):
                    print("오른쪽 경로가 최단거리입니다.")
                    zone_three = 9 - node_start
                    print("%d번 go를 호출했습니다"% zone_three)
                    # 오른쪽으로 회전
                    print("오른쪽으로 90도 돌았습니다")
                    zone_four = 3
                    print("%d번 go를 호출했습니다"% zone_four)
                    # 오른쪽으로 회전
                    print("오른쪽으로 90도 돌았습니다")
                    zone_one = 3 - (3 - node_end)
                    print("%d번 go를 호출했습니다" % zone_one)
                    data_node = {1:'go_410:%d' %zone_three, 2:'turn_right:1', 3:'go_7:3',
                    4:'go_410:%d' %zone_one}
                    return data_node
                
                # 오른쪽 사이노드 > 왼쪽 사이노드 => 왼쪽으로 이동
                else:
                    print("왼쪽 경로가 최단거리입니다.")
                    #왼쪽 방향 보게 하기
                    zone_three = 3 - ( 8 - node_start)
                    print("%d번 go를 호출했습니다"% zone_three)
                    #왼쪽으로 90도 돌기
                    print("왼쪽으로 90도 돌았습니다")
                    zone_four = 3
                    print("%d번 go를 호출했습니다"% zone_four)
                    #왼쪽으로 90도 돌기
                    print("왼쪽으로 90도 돌았습니다")
                    zone_one = (3 - node_end) + 1
                    print("%d번 go를 호출했습니다"% zone_one)
                    data_node={1:'go_410:%d' %zone_three, 2:'turn_left:1', 3:'go_7:3',
                    4:'turn_left:1',5:'go_410:%d' %zone_one}
                    return data_node
                    
            elif(zone_end == 2): # 출발구역이 3이고 도착구역이 2일때
                zone_three = 3 - (8 - node_start)
                print("%d번 go를 호출했습니다"% zone_three)
                # 왼쪽으로 회전
                print("왼쪽으로 90도 돌았습니다")
                zone_two = 1 + (5-node_end)
                print("%d번 go를 호출했습니다"% zone_two)
                data_node ={1:'go_410:%d' %zone_three ,2:'turn_left:1',3:'go_7:%d' %zone_two}
                return data_node

            elif(zone_end == 4):
                zone_three = 9 - node_start
                print("%d번 go를 호출했습니다"% zone_three)
                # 오른쪽으로 회전
                print("오른쪽으로 90도 돌았습니다")
                zone_four = 2 - (10 - node_end)
                print("%d번 go를 호출했습니다"% zone_four)
                data_node={1:'go_410:%d' %zone_three ,2:'turn_right:1',3:'go_7:%d' %zone_four}
                return data_node

    #------------------------------------------------------------------------
        
        elif(zone_start == 4): # 출발구역이 4일때
            if(zone_end == 1):  # 출발구역이 4이고 도착구역이 1일때
                zone_four = 1 + (10 - node_start)
                print("%d번 go를 호출했습니다"% zone_four)
                # 오른쪽으로 회전
                print("오른쪽으로 90도 돌았습니다")
                zone_one = node_end
                print("%d번 go를 호출했습니다"% zone_one)
                data_node = {1:'go_7:%d' %zone_four, 2:'turn_right:1', 3:'go_410:%d' %zone_one}
                return data_node

                # 더 짧은 거리 찾게하기
            elif(zone_end ==2) : # 출발구역이 4이고 도착구역이 2일때
                node_num_l = DCLinkedList.searchnodenumber_left(List, node_start, node_end)
                # 오른쪽으로 갈 때의 출발과 도착 사이의 노드 개수 구하기
                node_num_r = 12 - node_num_l
                # 오른쪽 사이노드 < 왼쪽 사이노드 => 오른쪽으로 이동
                if(node_num_r <= node_num_l):
                    print("오른쪽 경로가 최단거리입니다.")
                    zone_four = 1 + (10 - node_start)
                    print("%d번 go를 호출했습니다"% zone_four)
                    # 오른쪽으로 회전
                    print("오른쪽으로 90도 돌았습니다")
                    zone_one = 4
                    print("%d번 go를 호출했습니다"% zone_one)
                    # 오른쪽으로 회전
                    print("오른쪽으로 90도 돌았습니다")
                    zone_two = 2 - (5-node_end)
                    print("%d번 go를 호출했습니다"% zone_two)
                    data_node = {1:'go_7:%d' %zone_four, 2:'turn_right:1',3:'go_410:4',
                    4:'turn_tight:1',5:'go_7:%d' %zone_two}
                    return data_node
                        
                    # 오른쪽 사이노드 > 왼쪽 사이노드 => 왼쪽으로 이동
                else:
                    print("왼쪽 경로가 최단거리입니다.")
                    zone_four = 2 - (10 - node_start)
                    print("%d번 go를 호출했습니다"% zone_four)
                    # 왼쪽으로 회전
                    print("왼쪽으로 90도 돌았습니다")
                    zone_one = 4
                    print("%d번 go를 호출했습니다"% zone_one)
                    zone_two = 1 + (5 - node_end)
                    print("%d번 go를 호출했습니다"% zone_two)
                    data_node={1:'go_7:%d' %zone_four, 2:'turn_left;1', 3:'go_410:4',
                    4:'turn_left:1', 5:'go_7:%d' %zone_two}
                    return data_node
                    
            elif(zone_end == 3): # 출발구역이 4이고 도착구역이 3일때
                zone_four = 2 - (10 - node_start)
                print("%d번 go를 호출했습니다"% zone_four)
                # 왼쪽으로 회전
                print("왼쪽으로 90도 돌았습니다")
                zone_three = 1 + (8 - node_end)
                print("%d번 go를 호출했습니다"% zone_three)
                data_node={1:'go_7:%d' %zone_four, 2:'turn_left:1', 3:'go_410:%d' %zone_three}
                return data_node

#------------------------------------------------------------------------
        elif(zone_start == 5): # 출발노드가 꼭지점일 경우
            if(node_start == 401): # 출발노드의 값이 401일 경우
                if(zone_end==1): # 도착노드 = 1구역
                    zone_one = 3 - ( 3 - node_end )
                    data_node={1:'turn_left:1', 2:'go_410:%d' %zone_one}
                    return data_node

                elif(zone_end == 2): # 도착노드 = 2구역
                    zone_two = 2 - (5 - node_end)
                    data_node={1:'turn_left:1', 2:'go_410:4', 3:'turn_right', 
                    4:'go_7:%d' %zone_two}
                    return data_node

                elif(zone_end == 3): # 도착노드 = 3구역
                    zone_three = 9 - node_end
                    data_node={1:'go_7:3', 2:'turn_left:1', 3:'go_410:%d' %zone_three}
                    return data_node
            
            elif(node_start == 102): # 출발노드의 값이 102인 경우
                if(zone_end == 1):
                    zone_one = 4 - node_end
                    data_node = {1:'turn_left:2', 2:'go_410:%d' %zone_one}
                    return data_node

                elif(zone_end == 2):
                    zone_two = 2 - (5 - node_end)
                    data_node={1:'turn_right:1', 2:'go_7:%d' %zone_two}
                    return data_node

                elif(zone_end == 3):
                    zone_three = 3 - (8-node_end)
                    data_node={1:'turn_right:1', 2:'go_7:3', 3:'turn_right:1', 4:'go_410: %d' %zone_three}
                    return data_node

                elif(zone_end == 4):
                    zone_four = 11 - node_end
                    data_node = {1:'turn_left:2', 2:'go_410:4', 3:'turn_left:1', 4:'go_7:%d' %zone_four}
                    return data_node

            elif(node_start == 203): #출발노드의 값이 203일 때
                if(zone_end == 1):
                    zone_one = 4 - node_end
                    data_node={1:'turn_left:1', 2:'go_7:3', 3:'turn_left:1', 4:'go_410:%d' %zone_one}
                    return data_node

                elif(zone_end ==2):
                    zone_two = 6 - node_end
                    data_node={1:'turn_left:1', 2:'go_7:%d' %zone_two}
                    return data_node

                elif(zone_end == 3):
                    zone_three = 3 - (8-node_end)
                    data_node={1:'turn_right:2', 2:'go_410:%d' %zone_three}
                    return data_node

                elif(zone_end == 4):
                    zone_four= 2 - (10 - node_end)
                    data_node = {1:'turn_right:2', 2:'go_410:4', 3:'turn_right:1', 4:'go_7:%d' %zone_four}
                    return data_node

            elif(node_start == 304): #출발노드의 값이 304일 때
                if(zone_end == 1): 
                    zone_one = 3 - (3 - node_end)
                    data_node={1:'turn_right:2', 2:'go_7:3', 3:'turn_right:1', 4:'go_410:%d' %zone_one}
                    return data_node

                elif(zone_end == 2):
                    zone_two = 6 - node_end
                    data_node={1:'turn_left:1', 2:'go_410:4', 3:'turn_left:1', 4:'go_7:%d' %zone_two}
                    return data_node
                    
                elif(zone_end == 3):
                    zone_three = 9 - node_end
                    data_node={1:'turn_left:1', 2:'go_410:%d' %zone_three}
                    return data_node

                elif(zone_end == 4):
                    zone_four = 2 - (10 - node_end)
                    data_node = {1:'turn_right:2', 2:'go_7:%d' %zone_four}
                    return data_node
            

