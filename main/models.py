from django.db import models
from typing import cast
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )
    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.IntegerField( choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title


class Updated(models.Model):
    
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField('*', max_length=15, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer(Updated):
    
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Test(models.Model):
    question = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    true_answer = models.PositiveIntegerField('true answer')
    false_answer = models.PositiveIntegerField('false answer')
    all_answer = models.PositiveIntegerField()

    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.question.title