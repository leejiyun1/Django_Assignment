from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path, include
from todo.views import todo_list, todo_info, todo_create, todo_update, todo_delete
from users import views as user_views

urlpatterns = [
    path('todo/', todo_list, name='cbv_todo_list'),  # ❌ 이름이 잘못된 부분도 있음
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),

    path('cbv/', include('todo.urls')),  # ✅ CBV용 URL 추가

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]
