from django.shortcuts import render
from work.models import Chore, ChoreDebil


def random_chores(request):
    chores = Chore.objects.all()
    if request.method == 'POST':
        chore = Chore.objects.get(pk=request.POST.get("pk"))
        chosen_one = chore.pick_random_debil()

        return render(request, 'random-chores.html', {'chores': chores, 'chosen_one': chosen_one})
    # GET

    return render(request, 'random-chores.html', {'chores': chores})
