from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

# Create your views here.
def Index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "😊 Thank you for your feedback!")
            return redirect('Index')
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.order_by('-created_at')
    return render(request, 'index.html', {'form': form, 'feedbacks': feedbacks})

def Gallery(request):
    return render(request,'gallery.html')

def Anual(request):
    return render(request,'anual.html')

def Maintance(request):
    return render(request,'maintain.html')

def Acinstall(request):
   return render(request,'acrepair.html')

def Piduct(request):
   return render(request,'piinduc.html')


@staff_member_required
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.delete()
    return redirect('feedback')
