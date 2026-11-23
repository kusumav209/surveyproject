
from django.shortcuts import render
from .models import Survey, Response


def home(request):

    survey = Survey.objects.first()

    if request.method == "POST":

        if survey is None:
            return render(request, 'home.html', {
                'survey': None,
                'error': 'Please add a survey question first.'
            })

        survey_id = request.POST.get('survey_id')

        survey = Survey.objects.filter(id=survey_id).first()

        if survey is None:
            return render(request, 'home.html', {
                'survey': Survey.objects.first(),
                'error': 'Survey not found. Please try again.'
            })

        name = request.POST.get('name')
        email = request.POST.get('email')
        selected_option = request.POST.get('selected_option')
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')

        options = [
            survey.option1,
            survey.option2,
            survey.option3,
            survey.option4
        ]

        if selected_option not in options:
            return render(request, 'home.html', {
                'survey': survey,
                'error': 'Please select a valid option.'
            })

        if not rating or not rating.isdigit() or not 1 <= int(rating) <= 5:
            return render(request, 'home.html', {
                'survey': survey,
                'error': 'Please select a rating between 1 and 5.'
            })

        Response.objects.create(
            name=name,
            email=email,
            survey=survey,
            selected_option=selected_option,
            rating=int(rating),
            feedback=feedback
        )

        return render(request, 'thankyou.html')

    return render(request, 'home.html', {
        'survey': survey
    })
