text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요.'.format(text))
    
def safe_pop_print(list, index):
    if index < len(list):
        print(list.pop(index))
    else:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))
        
safe_pop_print([1,2,3],5)

try:
    import pokemon_module
except ImportError:
    print("모듈이 없습니다.")