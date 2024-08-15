
from fruitipediaApp.fruits import views
from django.urls import path, include

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.CreateFruitView.as_view(), name='create fruit'),
    path('create-category/', views.create_category, name='create category'),
    path('<int:fruit_id>/', include([
        path('edit-fruit/', views.edit_fruit, name='edit fruit'),
        path('delete-fruit/', views.delete_fruit, name='delete fruit'),
        path('details-fruit/', views.details_fruit, name='details fruit'),
    ]))
)
