from django.shortcuts import render, redirect
from .models import StudentFeedback


def home(request):
    return render(request, 'feedback/home.html')


def feedback_form(request):

    if request.method == 'POST':

        student_name = request.POST.get('student_name')
        roll_number = request.POST.get('roll_number')
        subject = request.POST.get('subject')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        StudentFeedback.objects.create(
            student_name=student_name,
            roll_number=roll_number,
            subject=subject,
            rating=rating,
            comments=comments
        )

        return redirect('success')

    return render(request, 'feedback/feedback.html')


def success(request):
    return render(request, 'feedback/success.html')