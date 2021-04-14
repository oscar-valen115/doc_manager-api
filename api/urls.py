from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.doctor_views import Doctors, DoctorDetail
from .views.patient_views import Patients, PatientDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('doctors/', Doctors.as_view(), name='doctors'),
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor_detail'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient_detail'),
    path('patients/', Patients.as_view(), name='patient'),
]
