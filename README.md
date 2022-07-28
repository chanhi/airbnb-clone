# Airbnb Clone

### with nomad coder


## Setting

pipenv
- npm 같이 관리 해주는 python 도구
- 생성된 가상환경에 들어가기 위해서 terminal에서 `pipenv shell`을 입력해야한다.
- django-admin을 쳐서 확인가능 (아마 가상환경에서만 적용되는 명령어 인듯)

linting: python은 runtime 언어이기 때문에 이를 보완하기 위해서 실행전에 오류나 관습 check를 해준다
* flake8 사용
* 관습: python PEP8 참고
formatting: 관습에 따라 저장시 자동으로 format 해준다.
* black 사용

## Migration
- django에서 sql을 사용할 때 migration을 통해 설정 할 수 있다.
- `python manage.py makemigration`을 통해 models.py의 변경사항을 확인하고 migrate를 통해 업데이트 한다.

`django-admin startapp [app_name]` -> application 생성, 이름은 복수형

chanhi
1q2w3e4r!