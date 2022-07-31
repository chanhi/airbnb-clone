# Airbnb Clone

### with nomad coder


## Setting
python: 3.8.10
pip: 22.1.2
django: 2.2.5

pipenv
- npm 같이 관리 해주는 python 도구
- 생성된 가상환경에 들어가기 위해서 terminal에서 `pipenv shell`을 입력해야한다.
- django-admin을 쳐서 확인가능 (아마 가상환경에서만 적용되는 명령어 인듯)

linting: python은 runtime 언어이기 때문에 이를 보완하기 위해서 실행전에 오류나 관습 check를 해준다
* flake8 사용
* 관습: python PEP8 참고
formatting: 관습에 따라 저장시 자동으로 format 해준다.
* black 사용

# Useage Django
- `django-admin startapp [app_name]` -> application 생성, 이름은 복수형
- application은 funtion의 집합

## Migration
- django에서 sql을 사용할 때 migration을 통해 설정 할 수 있다.
- 변경사항이 생기면 `python manage.py makemigration`을 통해 migration을 생성한다.
- `python manage.py migrate` 을 통해 migration을 반영하여 db 업데이트

## Fields
- `models.py`에 따로 커스텀해서 만들 수 있다.
- 기본적으로 django에서 제공하는 Field를 사용할 수 있다.
- `models.ImageField` `models.CharField` `models.TextField` `models.DateField` `models.BooleanField` 등의 Field가 있다.
- `def __str__()`
- ForeignKeyField , on_delete
- ManyToManyField

## core
- 베이스가 되는 folder로, 중복되는 부분을 core로 부터 확장을 한다.
- `class Meta:  abstract = True` -> 추상(abstract) 모델로 설정, db에 등록되지 않는다.



chanhi
1q2w3e4r!