from django.db import models

class Question(models.Model):
    question_code = models.CharField(max_length=10, unique=True)  # Example: "1-1", "3-11"
    question_in_japanese = models.TextField()
    questions_in_english = models.TextField()
    possible_answers = models.JSONField()
    answer = models.TextField()
    notes = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self): #defines how instances of my model are represented as strings
        return self.question_code

class Vocabulary(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='vocabularies')
    japanese_word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    english_translation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.japanese_word} ({self.pronunciation}) - {self.english_translation}"
