
from django.contrib.auth import views as auth_views
from django.urls import path, include


from .views import google_login, signup, login_function, logout_view, loginpage, signuppage,Verification

urlpatterns = [



    path('login', login_function, name='login'),
    path('logout', logout_view, name='logout'),
    path('sign-up', signup, name='signup'),
    path('loginpage/', loginpage, name='loginpage'),


    path('register.html', signuppage, name='signuppage'),


    path('google_login', google_login, name='google_login'),


    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
 path('activate/<uidb64>/<token>',Verification.as_view(),name='activate')





]
