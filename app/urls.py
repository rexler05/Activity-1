from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView,
                    AboutPageView,
                    ContactPageView,
                    BlogListView,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView,
                    RegisterView,
                    LoginView,
                    logout_view,
                    ProfileView,
                    ProfileUpdateView,
                    ProfilePageView,
                    PetCreateView,
                    PetListView,
                    PetDetailView,
                    PetUpdateView,
                    PetDeleteView,
                    ShelterListView,
                    ShelterDetailView,
                    ShelterCreateView,
                    ShelterUpdateView,
                    ShelterDeleteView)

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('account_settings/', ProfileView.as_view(), name='account_settings'),
    path('account_settings/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('shelters/', ShelterListView.as_view(), name='shelter_list'),
    path('shelters/<int:pk>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('shelters/create/', ShelterCreateView.as_view(), name='shelter_form'),
    path('shelters/<int:pk>/edit/', ShelterUpdateView.as_view(), name='shelter_edit'),
    path('shelters/<int:pk>/delete', ShelterDeleteView.as_view(), name='shelter_delete'),
    # Pet URLs
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('pets/create/', PetCreateView.as_view(), name='pet_form'),
    path('pets/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),
    path('pets/<int:pk>/delete', PetDeleteView.as_view(), name='pet_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)