from django.urls import path
from .views import emp_add_data, show_data, delete_data, update_data_form, updated_data_save
urlpatterns = [
    path('emp/', emp_add_data),
    path('emp/show_data/', show_data),
    path('emp/delete_data/<int:pk>/', delete_data),
    path('emp/update_data/<int:ud>/', update_data_form),
    path('emp/updated_data_save/<int:data_update>/', updated_data_save),
]
