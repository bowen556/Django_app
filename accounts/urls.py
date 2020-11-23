from django.urls import path
from . import views

# Defines each page's urls and their names
urlpatterns = [
    path('', views.home, name="home"),
    path('locations/', views.locations, name="locations"),
    path('viewlocations/<str:pk>/', views.viewlocations, name="viewlocations"),
    path('users/', views.users, name="users"),
    path('admin/auth/user/add/', views.createUsers, name="create_users"),
    path('admin/accounts/entry/add/', views.createLocations, name="create_locations"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user_profile/', views.userProfile, name="profile"),
    path('region/<str:cats>/', views.Region, name="region"),
    path('allregions/', views.allRegions, name="allregions"),
    path('auditlogs/', views.AuditLogsView, name="auditlogs"),
    path('pdf_auditlogs/', views.Download_auditlogsPDF.as_view(), name="pdf_auditlogs"),
    path('pdf_viewlocations/<str:pk>/', views.DownloadviewlocationsPDF.as_view(), name="pdf_viewlocations"),
    path('faq/', views.faq, name="faq"),
    path('faqadmin/', views.faqadmin, name="faqadmin")
]
