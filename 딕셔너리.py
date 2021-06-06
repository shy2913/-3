'''# 딕셔너리는 다음과 같이 선언할 수 있다=>ex1:a=dict(),ex2:a={'key1':'value1','key2':'value2'},* 추가 할 시에는 a['key3']='value3' 그리고 출력하면 됨!
리스트는 대괄호[], 딕셔너리는 {} 소괄호'''
a = {'key1': 'value1', 'key2': 'value2'}
a['key3'] = 'value3'
# print(a['key4'])  # key4값은 딕셔너리에 없는 값이므로 출력이 안됨!
''' for k, v in a.items():
    # 메소드를 사용하여 key와 value 값을 모두 꺼내올 수 있음! ## 딕셔너리 형태: a={key,value...}
    print(k, v) '''
del a['key1']
print(a)
