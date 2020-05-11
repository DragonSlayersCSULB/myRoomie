from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, BillListView, BillDetailView, BillCreateView, BillUpdateView, BillDeleteView
from . import views

urlpatterns = [
    #path('', views.mainLoginScreen, name='main-login'), #this is what the previous main screen was linked to.
    path('', auth_views.LoginView.as_view(template_name='main/mainLoginScreen.html'), name='login'),
    path('home', views.home, name='main-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='main-about'),
    # -- Bills
    path('bill/', views.bills, name='main-bill'),
    #path('bills/new', PostCreateView.as_view(), name='new-bill'),
    path('bill/<int:pk>', BillDetailView.as_view(), name='bill-detail'), # allows to view a specific bill via pk
    path('bill/new', BillCreateView.as_view(), name='bill-create'),
    # -----
    path('roommates/', views.roommates, name='main-roommates'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('crowdfund/', views.crowdfund, name='main-crowdfund'),
    path('repairs/', views.repairs, name='main-repairs'),
    path('calendar/', views.calendar, name='main-calendar'),
    path('grocery', views.grocery, name='main-grocery'),
    path('crowdfund/', views.crowdfund, name='main-crowdfund'),
    
    #path('login/', views.mainLoginScreen, name='mainLoginScreen'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    
    path('tasks/', include('tasks.urls'), name='tasks'),
]
