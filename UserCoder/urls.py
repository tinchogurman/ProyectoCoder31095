from django.contrib.auth.views import LogoutView
from django.urls import path

from UserCoder.views import login_request, register, editar_usuario, upload_avatar

urlpatterns = [
    path('login/', login_request, name='UserCoderLogin'),
    path('registro/', register, name='UserCoderRegister'),
    path('logout/', LogoutView.as_view(template_name='UserCoder/logout.html'), name='UserCoderLogout'),
    path('editar/', editar_usuario, name='UserCoderEditar'),
    path('avatar/', upload_avatar, name='UserCoderAvatar'),
]
