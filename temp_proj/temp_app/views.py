from django.shortcuts import render

def info_views(request):
    context = {
        'name': 'mariam',
        'surname': 'koberidze',
        'age': 17,
        'height': 180,
    }

    return render(request, 'info.html', context)

def hobbies_views(request):
    hobbies = ['coding', 'art', 'volleball', 'music']
    grade = 12
    context = {
        'hobbies': hobbies,
        'grade': grade,
    }
    return render(request, 'hobbies.html', context)