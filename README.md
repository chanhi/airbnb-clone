# Airbnb Clone

### with nomad coder


## Setting
python: 3.8.10
pip: 22.1.2
django: 2.2.5

#### pipenv
- npm 같이 관리 해주는 python 도구
- 생성된 가상환경에 들어가기 위해서 terminal에서 `pipenv shell`을 입력해야한다.
- django-admin을 쳐서 확인가능 (아마 가상환경에서만 적용되는 명령어 인듯)

#### linting
- python은 runtime 언어이기 때문에 이를 보완하기 위해서 실행전에 오류나 관습 check를 해준다
- flake8 사용
#### formatting
- 관습에 따라 저장시 자동으로 format 해준다.
- black 사용
- 관습: python PEP8 참고

## Useage Django
- `django-admin startapp [app_name]` -> application 생성, 이름은 복수형
- application은 funtion의 집합

### config
- #### config/settings
    - 다른 부분에서도 적용되는 것이지만 대부분의 Django에서 제공하는 변수의 이름은 변경하면 안된다.
- #### config/urls
    - 이곳에서 원하는 경로로 url을 지정할 수 있다.

### Migration
- django에서 sql을 사용할 때 migration을 통해 설정 할 수 있다.
- 변경사항이 생기면 `python manage.py makemigration`을 통해 migration을 생성한다.
- `python manage.py migrate` 을 통해 migration을 반영하여 db 업데이트

### Fields
- `models.py`에 따로 커스텀해서 만들 수 있다.
- 기본적으로 django에서 제공하는 Field를 사용할 수 있다.
- `models.ImageField` `models.CharField` `models.TextField` `models.DateField` `models.BooleanField` 등의 Field가 있다.
- `def __str__()`
- ForeignKeyField , on_delete
- ManyToManyField
- search_fields([App]) :default로 부분 일치 -> ^app: 앞부분만 일치, =app: 정확히 일치

### core
- 베이스가 되는 folder로, 중복되는 부분을 core로 부터 확장을 한다.
- `class Meta:  abstract = True` -> 추상(abstract) 모델로 설정, db에 등록되지 않는다.

### manage python commands
- `from django.core.management.base import BaseCommand` 로 `BaseCommand` import
- class에 argument로 BaseCommand를 전달해준다.
- `def add_arguments(self, parser):`로 추가하고자 하는 command 추가
```python
def add_arguments(self, parser):
    parser.add_argument(
        "--times", help="How many times do you want me work"
    )
```
- `add_arguments`는 `def handle(self, *args, **options):`를 가져야하기 때문에 추가한다.
    -BaseCommand의 하위class들은 handle을 가져야함

```python
def handle(self, *args, **options):
    times = options.get("times")
    for t in range(0, int(times)):
        self.stdout.write(self.style.SUCCESS("I love you"))
```
```
#Terminer
>python manage.py [filename] --times 50
I love you *50
```

### seed
- test db를 만들기 위해 사용

### views
- views, url
- templates

* Managers, QuerySets
- QuerySets (modelsName)_set
chanhi
1234