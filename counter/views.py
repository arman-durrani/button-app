from django.shortcuts import render
from django.http import JsonResponse

def button_click(request):
    # Initialize the count or increment the count stored in the session
    count = request.session.get('button_press_count', 0)
    count += 1
    request.session['button_press_count'] = count

    # Return the updated count as a JSON response (for Ajax)
    return JsonResponse({'count': count})

def index(request):
    return render(request, 'button-counter/index.html')