from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 인증과 관련된 테이블을 설정할 때 
    # 장고가 기본적을 제공해주는 필드를 (username, password, email 등)을
    # 수정 없이 그대로 사용한다고 하더라도,
    # 장고는 user 모델을 custom 해서 등록하기를 강력히 권장함
        # 이때, 단순히 acounts 앱에 user 모델을 만들기만 한다고 해서
        # 기존의 django가 제공해주는 그 인증, 권한, auth 모델과의 
        # 복잡한 연관 관계가 모두 한번에 수정되는 것은 아님
    
    # 우리는 django에게, 이 class가 기존의 auth class를 대체할 것임을 설정함
    # 설정 -> settings.py
    pass