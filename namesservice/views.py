from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from .forms import NameForm
from .models import SimpleName


def home_page_view(request):
    form = NameForm(request.POST or None)
    if request.method == 'POST' and request.accepts("application/json"):
        if form.is_valid():
            name_data = form.cleaned_data['name']
            form.save()
            return JsonResponse(
                {"name": name_data, "accepted": True},
                status=200
                )
        else:
            return JsonResponse({"name": form.data['name']}, status=200)
    return render(request, 'nameservice/home.html', {'form': form})


class NamesListView(ListView):
    template_name = 'nameservice/name_list.html'
    model = SimpleName
    context_object_name = 'names_list'
    paginate_by = 5
