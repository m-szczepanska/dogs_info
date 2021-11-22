from django.urls import path

from dogs.views import dogs_list, dog_details


urlpatterns = [
    path('dogs', dogs_list, name='dogs_list'),
    path('dog/<int:dog_id>', dog_details, name='dog_details'),
]
