
def get_web(url):
    """URL을 넣으면 페이지 내용을 올려주는 함수"""
    import urllib.request
    request = urllib.request.urlopen(url)
    data = request.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹 페이지 주소? ')
content = get_web(url)
print(content)