from django.contrib import admin
from django.urls import path, include
from mainapp.views import Index, About, Contact, Login, Logout_admin, View_Doctor, View_Patient, Add_Doctor, Delete_Doctor, Delete_Patient, Add_Patient, Profile
from accounts.views import register, signin
#from root.mainapp import views
#from _ast import Index
urlpatterns = [
    path('', View_Patient, name='home'),
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('delete_doctor(?P<int:did>)', Delete_Doctor, name='delete_doctor'),
    #path('edit_doctor/', Edit_Doctor, name='edit_doctor'),
    #path('edit_patient/', Edit_Patient, name='edit_patient'),
    path('delete_patient(?P<int:pid>)', Delete_Patient, name='delete_patient'),
    path('accounts/', include('accounts.urls')),
    path('profile/', Profile, name='profile'),
    path('admin_login/accounts/register', register, name='register'),
    path('admin_login/accounts/signin', signin, name='signin')

]