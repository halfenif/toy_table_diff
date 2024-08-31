from jinja2 import Environment, FileSystemLoader

import x_utils


# 템플릿 파일이 있는 디렉토리 설정
file_loader = FileSystemLoader('template_html')
env = Environment(loader=file_loader)

# 템플릿 파일 로드
template = env.get_template('test_template.html')

# 템플릿에 전달할 데이터
data = {
    'title': 'Jinja2 예제'
    ,'heading': 'Jinja2 템플릿 엔진'
    ,'content': '이것은 Jinja2 템플릿 엔진을 사용하는 예제입니다.'
    ,'rows' : [
         ['A','한글은 되나요?']
        ,['B','되기는 하겠지만']
        ,['C','감사합니다.']
    ]
}

# 템플릿 렌더링
output = template.render(data)

# 렌더링된 템플릿 출력
# print(output)
str_filename = x_utils.get_date_filename('data_report', 'test_report', 'html')
with open(str_filename, 'w', encoding="UTF-8") as f:
    f.writelines(output)