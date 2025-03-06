from django.shortcuts import render, redirect
from .models import Question, Test, Answer
from random import sample


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')

        # Fetch available questions (from the Question model)
        available_questions = Question.objects.all()
        num_questions = min(10, available_questions.count())  # Ensure we don't request more questions than available

        # Randomly select 10 questions or fewer
        selected_questions = sample(list(available_questions), num_questions)

        # Create a new Test instance
        test = Test.objects.create(name=name)

        # Add selected questions to the test using ManyToManyField
        test.questions.set(selected_questions)  # Correctly set the questions using .set()

        return redirect(f'/test/{test.id}/question/1')  # Redirect to the first question
    return render(request, 'home.html')


def start_test(request, test_id, question_number):
    test = Test.objects.get(id=test_id)  # Get the test based on test_id

    # Fetch only the selected questions for this test
    questions = test.questions.all()  # Get the questions related to this test

    # Ensure question_number does not exceed available questions
    if question_number > len(questions):
        return redirect(f'/test/{test_id}/summary/')  # Redirect to summary if out of range

    current_question = questions[question_number - 1]  # Get the current question

    return render(request, '/Users/shanusinha/Documents/Django_practice/mcq_test/quiz/templates/test.html', {'test': test, 'question': current_question, 'question_number': question_number})


def submit_answer(request, test_id, question_number):
    if request.method == "POST":
        selected_option = request.POST.get('selected_option')
        question_id = request.POST.get('question_id')
        test = Test.objects.get(id=test_id)
        question = Question.objects.get(id=question_id)

        # Save the selected answer in the database
        Answer.objects.create(test=test, question=question, selected_option=selected_option)

        # If it's the last question, redirect to the summary page
        if question_number == 10:
            return redirect(f'/test/{test_id}/summary/')
        
        # Otherwise, go to the next question
        return redirect(f'/test/{test_id}/question/{question_number + 1}')


# Summary of the test showing marks
def test_summary(request, test_id):
    test = Test.objects.get(id=test_id)
    answers = Answer.objects.filter(test=test)
    correct_answers = 0
    total_questions = len(answers)

    # Calculate correct answers
    for answer in answers:
        if answer.selected_option == answer.question.correct_option:
            correct_answers += 1
    
    # Calculate the score (marks)
    marks = correct_answers

    return render(request, 'summary.html', {'test': test, 'answers': answers, 'marks': marks, 'total_questions': total_questions})