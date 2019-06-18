from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

# 회원정보수정을 커스터마이징 하기 위해
class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')