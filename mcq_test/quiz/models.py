from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)  # A, B, C, or D

    def __str__(self):
        return self.question_text

class Test(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    questions = models.ManyToManyField(Question)  # Many-to-Many relation to Question

    def __str__(self):
        return self.name

class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)

    def __str__(self):
        return f"Answer for {self.question} in Test {self.test.name}"