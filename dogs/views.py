from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from dogs.models import Dog


@require_http_methods(['GET'])
def dogs_list(request):
    context = {'dogs': Dog.objects.all()}
    return render(
        request,
        'dogs/dogs_list.html',
        context=context
    )


@require_http_methods(['GET'])
def dog_details(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    context = {'dog': dog}
    return render(
        request,
        'dogs/dog_details.html',
        context=context
    )