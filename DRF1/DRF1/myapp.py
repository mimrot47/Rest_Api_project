import requests 
import json 
#Get Request 
# BASE_URL='http://127.0.0.1:8000/api'
# def get_req(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     res=requests.get(BASE_URL,data=json.dumps(data))
#     print(res.json())
#     print(res.status_code)
# get_req()


##create Resource 
# BASE_URL='http://127.0.0.1:8000/api'
# def psot_req():
#     data={
#         'eno':3,
#         'ename':'gokul',
#         'esal':1400,
#         'eaddr':'Sanli'
#        }
#     res=requests.post(BASE_URL,data=json.dumps(data))
#     print(res.status_code)
#     print(res.json())
# psot_req()

# update data with put method
# BASE_URL='http://127.0.0.1:8000/api'
# def put_req(id):
#     data={
#         'id':id,
#         'ename':'okul',
#         'esal':8020,
#         'eaddr':'Aurangabad'
#     }
#     url=requests.put(BASE_URL,data=json.dumps(data))
#     print(url.status_code)
#     print(url.json())
# put_req(1)