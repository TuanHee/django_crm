from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
    path('records/create', views.record_create, name='records.create'),
    path('records/<int:id>', views.records_show, name='records.show'),
    path('records/<int:id>/update', views.records_update, name='records.update'),
    path('records/<int:id>/delete', views.records_delete, name='records.delete'),
]
