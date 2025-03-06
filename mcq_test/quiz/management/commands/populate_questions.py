# quiz/management/commands/populate_questions.py

from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Populates the Question model with 200 questions'

    def handle(self, *args, **kwargs):
        questions_data =[
        {
            "question_text": "What is the capital of France?",
            "option_a": "Berlin",
            "option_b": "Madrid",
            "option_c": "Paris",
            "option_d": "Rome",
            "correct_option": "C"
        },
        {
            "question_text": "Which planet is known as the Red Planet?",
            "option_a": "Earth",
            "option_b": "Mars",
            "option_c": "Jupiter",
            "option_d": "Venus",
            "correct_option": "B"
        },
        {
            "question_text": "Who developed the theory of relativity?",
            "option_a": "Isaac Newton",
            "option_b": "Albert Einstein",
            "option_c": "Nikola Tesla",
            "option_d": "Marie Curie",
            "correct_option": "B"
        },
        {
            "question_text": "What is the largest ocean on Earth?",
            "option_a": "Atlantic Ocean",
            "option_b": "Indian Ocean",
            "option_c": "Pacific Ocean",
            "option_d": "Arctic Ocean",
            "correct_option": "C"
        },
        {
            "question_text": "Which element has the chemical symbol 'O'?",
            "option_a": "Oxygen",
            "option_b": "Osmium",
            "option_c": "Ozone",
            "option_d": "Oganesson",
            "correct_option": "A"
        },
        {
            "question_text": "What is the square root of 64?",
            "option_a": "8",
            "option_b": "6",
            "option_c": "7",
            "option_d": "9",
            "correct_option": "A"
        },
        {
            "question_text": "Which of these is a primary color?",
            "option_a": "Purple",
            "option_b": "Green",
            "option_c": "Red",
            "option_d": "Orange",
            "correct_option": "C"
        },
        {
            "question_text": "In which year did the Titanic sink?",
            "option_a": "1905",
            "option_b": "1912",
            "option_c": "1920",
            "option_d": "1930",
            "correct_option": "B"
        },
        {
            "question_text": "Who was the first president of the United States?",
            "option_a": "George Washington",
            "option_b": "Thomas Jefferson",
            "option_c": "Abraham Lincoln",
            "option_d": "John Adams",
            "correct_option": "A"
        },
        {
            "question_text": "What is the smallest planet in our solar system?",
            "option_a": "Earth",
            "option_b": "Venus",
            "option_c": "Mercury",
            "option_d": "Mars",
            "correct_option": "C"
        },
        {
            "question_text": "Who painted the Mona Lisa?",
            "option_a": "Vincent van Gogh",
            "option_b": "Pablo Picasso",
            "option_c": "Leonardo da Vinci",
            "option_d": "Claude Monet",
            "correct_option": "C"
        },
        {
            "question_text": "Which animal is known as the King of the Jungle?",
            "option_a": "Elephant",
            "option_b": "Lion",
            "option_c": "Tiger",
            "option_d": "Giraffe",
            "correct_option": "B"
        },
        {
            "question_text": "What is the longest river in the world?",
            "option_a": "Amazon",
            "option_b": "Nile",
            "option_c": "Yangtze",
            "option_d": "Mississippi",
            "correct_option": "B"
        },
        {
            "question_text": "What is the largest planet in our solar system?",
            "option_a": "Earth",
            "option_b": "Jupiter",
            "option_c": "Saturn",
            "option_d": "Neptune",
            "correct_option": "B"
        },
        {
            "question_text": "Which of these is a mammal?",
            "option_a": "Shark",
            "option_b": "Dolphin",
            "option_c": "Lizard",
            "option_d": "Snake",
            "correct_option": "B"
        },
        {
            "question_text": "What is the boiling point of water?",
            "option_a": "90°C",
            "option_b": "95°C",
            "option_c": "100°C",
            "option_d": "110°C",
            "correct_option": "C"
        },
        {
            "question_text": "What is the capital of Japan?",
            "option_a": "Seoul",
            "option_b": "Beijing",
            "option_c": "Tokyo",
            "option_d": "Kyoto",
            "correct_option": "C"
        },
        {
            "question_text": "Which country is famous for the Eiffel Tower?",
            "option_a": "Germany",
            "option_b": "Italy",
            "option_c": "France",
            "option_d": "England",
            "correct_option": "C"
        },
        {
            "question_text": "Which sport is known as 'The Beautiful Game'?",
            "option_a": "Basketball",
            "option_b": "Baseball",
            "option_c": "Football",
            "option_d": "Tennis",
            "correct_option": "C"
        },
        {
            "question_text": "Who wrote 'Romeo and Juliet'?",
            "option_a": "Jane Austen",
            "option_b": "William Shakespeare",
            "option_c": "Charles Dickens",
            "option_d": "Mark Twain",
            "correct_option": "B"
        },
        {
            "question_text": "What is the tallest mountain in the world?",
            "option_a": "Mount Kilimanjaro",
            "option_b": "Mount Everest",
            "option_c": "K2",
            "option_d": "Mont Blanc",
            "correct_option": "B"
        },
        {
            "question_text": "Which gas do plants absorb from the air during photosynthesis?",
            "option_a": "Oxygen",
            "option_b": "Carbon Dioxide",
            "option_c": "Nitrogen",
            "option_d": "Helium",
            "correct_option": "B"
        },
        {
            "question_text": "Which country is the largest by land area?",
            "option_a": "United States",
            "option_b": "China",
            "option_c": "Canada",
            "option_d": "Russia",
            "correct_option": "D"
        },
        {
            "question_text": "What is the national currency of the United Kingdom?",
            "option_a": "Euro",
            "option_b": "Pound Sterling",
            "option_c": "Dollar",
            "option_d": "Yen",
            "correct_option": "B"
        },
        {
            "question_text": "Which bird is known for its ability to mimic human speech?",
            "option_a": "Parrot",
            "option_b": "Sparrow",
            "option_c": "Eagle",
            "option_d": "Penguin",
            "correct_option": "A"
        },
        {
            "question_text": "What is the output of the following code: print(type(3.14))?",
            "option_a": "<class 'int'>",
            "option_b": "<class 'float'>",
            "option_c": "<class 'str'>",
            "option_d": "<class 'list'>",
            "correct_option": "B"
        },
        {
            "question_text": "Which of the following data types is immutable in Python?",
            "option_a": "list",
            "option_b": "dict",
            "option_c": "set",
            "option_d": "tuple",
            "correct_option": "D"
        },
        {
            "question_text": "What is the default database used by Django?",
            "option_a": "MySQL",
            "option_b": "PostgreSQL",
            "option_c": "SQLite",
            "option_d": "MongoDB",
            "correct_option": "C"
        },
        {
            "question_text": "What command is used to start a Django project?",
            "option_a": "django-admin startproject",
            "option_b": "python manage.py startproject",
            "option_c": "django startproject",
            "option_d": "python startproject",
            "correct_option": "B"
        },
        {
            "question_text": "What is the file used for database migrations in Django?",
            "option_a": "models.py",
            "option_b": "migrations.py",
            "option_c": "migrate.py",
            "option_d": "admin.py",
            "correct_option": "B"
        },
        {
            "question_text": "What does the Django ORM do?",
            "option_a": "Generates HTML",
            "option_b": "Handles database operations",
            "option_c": "Runs the server",
            "option_d": "Manages URLs",
            "correct_option": "B"
        },
        {
            "question_text": "Which function is used to create a new instance of a Django model?",
            "option_a": "create()",
            "option_b": "new()",
            "option_c": "save()",
            "option_d": "add()",
            "correct_option": "A"
        },
        {
            "question_text": "In Django, what is the function of the 'urls.py' file?",
            "option_a": "Defines models",
            "option_b": "Manages database connections",
            "option_c": "Maps URLs to views",
            "option_d": "Manages static files",
            "correct_option": "C"
        },
        {
            "question_text": "What is the default template engine used by Django?",
            "option_a": "Jinja2",
            "option_b": "Mako",
            "option_c": "Django Template Language",
            "option_d": "Mustache",
            "correct_option": "C"
        },
        {
            "question_text": "What command is used to apply migrations in Django?",
            "option_a": "python manage.py migrate",
            "option_b": "django-admin migrate",
            "option_c": "python migrate",
            "option_d": "python db migrate",
            "correct_option": "A"
        },
        {
            "question_text": "What is a Django 'view'?",
            "option_a": "A database table",
            "option_b": "A template",
            "option_c": "A function that returns a response",
            "option_d": "A URL pattern",
            "correct_option": "C"
        },
        {
            "question_text": "Which method is used to delete a model instance in Django?",
            "option_a": "remove()",
            "option_b": "delete()",
            "option_c": "erase()",
            "option_d": "destroy()",
            "correct_option": "B"
        },
        {
            "question_text": "What is the purpose of the 'self' keyword in Python?",
            "option_a": "It refers to the class itself.",
            "option_b": "It refers to the instance of the class.",
            "option_c": "It is used to define the constructor.",
            "option_d": "It is used to inherit methods from other classes.",
            "correct_option": "B"
        },
        {
            "question_text": "What will be the output of the following code: print(2 ** 3)?",
            "option_a": "5",
            "option_b": "6",
            "option_c": "8",
            "option_d": "None of the above",
            "correct_option": "C"
        },
        {
            "question_text": "Which of the following functions is used to get the length of a list in Python?",
            "option_a": "get_length()",
            "option_b": "len()",
            "option_c": "length()",
            "option_d": "size()",
            "correct_option": "B"
        },
        {
            "question_text": "What does the 'continue' statement do in a loop?",
            "option_a": "Exits the loop",
            "option_b": "Starts a new loop",
            "option_c": "Skips the current iteration of the loop",
            "option_d": "None of the above",
            "correct_option": "C"
        },
        {
            "question_text": "Which of the following is the correct way to create a set in Python?",
            "option_a": "{1, 2, 3}",
            "option_b": "[1, 2, 3]",
            "option_c": "(1, 2, 3)",
            "option_d": "set(1, 2, 3)",
            "correct_option": "A"
        },
        {
            "question_text": "What is the correct syntax for defining a function in Python?",
            "option_a": "def function_name[]:",
            "option_b": "function function_name():",
            "option_c": "function_name{}:",
            "option_d": "def function_name():",
            "correct_option": "D"
        },
        {
            "question_text": "What will the following code output: 'Hello, world!'.lower()?",
            "option_a": "'hello, world!'",
            "option_b": "'Hello, World!'",
            "option_c": "'hello, WORLD!'",
            "option_d": "'HELLO, WORLD!'",
            "correct_option": "A"
        },
        {
            "question_text": "Which module in Python is used to work with regular expressions?",
            "option_a": "regex",
            "option_b": "re",
            "option_c": "regexp",
            "option_d": "pattern",
            "correct_option": "B"
        }
        ]
        
        # Loop through the list and create Question objects
        for data in questions_data:
            Question.objects.create(
                question_text=data['question_text'],
                option_a=data['option_a'],
                option_b=data['option_b'],
                option_c=data['option_c'],
                option_d=data['option_d'],
                correct_option=data['correct_option']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated 200 questions'))