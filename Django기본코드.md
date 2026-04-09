# 가상환경 생성
python -m venv venv
source venv/scripts/activate
pip install django
pip freeze > requirments.txt
pip install -r requirments.txt
deactivate

# 프로젝트 생성
django-admin startproject 프로젝트명 .
# 서버실행
python manage.py runserver
# 앱 생성
python manage.py startapp 앱명(복수형권장)
settings.py 에서 앱명 등록하기
# 요청과 응답
- urls.py 에서
from 앱명 import 모듈명(예:views)
path('주소끝에내용/', 모듈명.모듈내함수이름)
- 모듈명.py 에서
  - def 함수이름(request):
    - return render(request, '앱이름/index.html')
- 앱폴더 안에 templates 폴더 만들고 그 안에 또 앱이름폴더 만듬. 그 안에 index.html넣기.
- 