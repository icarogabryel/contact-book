from django.contrib import admin
from django.urls import path

from contact_book.app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('<int:pk>/update/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
]
