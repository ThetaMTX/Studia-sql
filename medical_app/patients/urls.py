from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import patient_list, edit_patient, edit_examination
from .views import delete_patient_confirmation, delete_patient

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),  # Redirect root URL to login page
    path('patients/', views.patient_list, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('patient/<int:pk>/delete/', delete_patient_confirmation, name='delete_patient_confirmation'),
    path('patient/<int:pk>/delete/confirm/', delete_patient, name='delete_patient'),
    path('<int:pk>/examinations/', views.examination_list, name='examination_list'),
    path('<int:pk>/examinations/add/', views.add_examination, name='add_examination'),
    path('<int:patient_pk>/examinations/<int:exam_pk>/delete/', views.delete_examination, name='delete_examination'),
    path('login/', auth_views.LoginView.as_view(template_name='patients/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', edit_patient, name='edit_patient'),
    path('examinations/<int:examination_pk>/edit/<int:patient_pk>/', edit_examination, name='edit_examination'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

