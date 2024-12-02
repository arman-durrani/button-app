from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def button_click(request):
    count = request.session.get('button_press_count', 0)
    if request.method == 'POST' : 
        # Initialize the count or increment the count stored in the session
        count += 1
    request.session['button_press_count'] = count
    # Return the updated count as a JSON response (for Ajax)
    return JsonResponse({'count': count})

def index(request):
    return render(request, 'button-counter/index.html')