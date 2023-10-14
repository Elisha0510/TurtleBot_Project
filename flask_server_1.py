import node_path
from flask import Flask, request, render_template, json
import requests
app = Flask(__name__)

@app.route('/')
def gui():
    return render_template('first.html')

@app.route('/6_floor') 
def floor():
    return render_template('6_floor.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/method', methods = ['POST'])
def method():
    if request.method == 'POST':
        room = int(request.form["room"])
        print("전달된 데이터 = ({})".format(room))

        if room == 604: #남윤영 교수님
            data = {1:'turn_right:1', 2:'go:6', 3:'turn_left:1', 
                    4:'go:17', 5:'turn_right:1', 6:'go:1'}
        
        elif room == 605: #이상정 교수님
            data = {1:'turn_right:1', 2:'go:6', 3:'turn_left:1', 
                    4:'go:9', 5:'turn_right:1', 6:'go:1'}
        
        elif room == 607:  #홍인식 교수님
            data = {1:'turn_right:1', 2:'go:6', 3:'turn_right:1', 
                    4:'go:6', 5:'turn_left:1', 6:'go:2'}
        
        elif room == 609: #과사무실
            data = {1:'turn_left:1', 2:'go:18', 3:'turn_left:1', 
                    4:'go:1'}
        
        elif room == 610: 
            data = {1:'turn_left:1', 2:'go:30', 3:'turn_left:1', 
                    4:'go:1'}
        
        elif room == 618:
            #최단 경로
            data = {1:'turn_left:1', 2:'go:6', 3:'turn_right:1', 
                    4:'go:22',5:'turn_left:1',6:'go:41',7:'turn_right:1',8:'go:1'}
        
        elif room == 619:
            #최단 경로
            data = {1:'turn_left:1', 2:'go:6', 3:'turn_right:1', 
                    4:'go:22',5:'turn_left:1',6:'go:37',7:'turn_right:1',8:'go:1'}
        
        elif room == 620:
            data = {1:'turn_left:1', 2:'go:5', 3:'turn_right:1', 
                    4:'go:22',5:'turn_left:1',6:'go:16',7:'turn_right:1',8:'go:1'}
        
        elif room == 1:
            pass
        
        url = "http://192.168.50.140:5000/move"
        headers = {'Content-type': 'application/json'}
        requests.post(url, data=json.dumps(data), headers=headers)
            
    return ''

@app.route('/node' , methods = ['POST'])
def node():
    if request.method == 'POST':
        node_start = int(request.form["depart"])
        node_finish = int(request.form["arrive"])
        print("출발 데이터 = (%d)" %node_start)
        print("도착 데이터 = (%d)" %node_finish)
        node_path.make_node()
        data_start = {}
        data_finish = {}
        print(data_start)
        print(data_finish)
        # 출발 노드로 가는 경로 반환
        data_start = node_path.go_start(node_start)
        print('data_start 반환')

        url = "http://192.168.50.140:5000/node"
        headers = {'Content-type': 'application/json'}
        requests.post(url, data=json.dumps(data_start), headers=headers)

        # 도착 노드로 가는 경로 반환
        # data_finish = node_path.go_end(node_start, node_finish)
        # print('data_start 반환')
        # requests.post(url, data=json.dumps(data_finish), headers=headers)
        # print("보냈습니다")

        
    return ''  
        
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5500, debug=True)