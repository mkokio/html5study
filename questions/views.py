from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Vocabulary

def index(request):
    question_list = Question.objects.all()
    context = {"question_list": question_list}
    #render() function takes the request object as its first argument, a template name 
    #as its second argument and a dictionary as its optional third argument
    return render(request, "questions/index.html", context)

def detail(request, question_code):
    question = get_object_or_404(Question, question_code=question_code) 
    vocab_list = question.vocabularies.all()  # Get related vocabulary entries
    context = {
        "question": question,
        "vocab_list": vocab_list,
    }
    return render(request, "questions/detail.html", context)

def add(request):
    if request.method == "POST":
        question_code = request.POST.get("question_code")
        question_in_japanese = request.POST.get("question_in_japanese")
        question_in_english = request.POST.get("question_in_english")
        possible_answers = [
            request.POST.get("choice_a"),
            request.POST.get("choice_b"),
            request.POST.get("choice_c"),
            request.POST.get("choice_d"),
            request.POST.get("choice_e"),
            request.POST.get("choice_f"),
        ]
        answer = request.POST.get("answer")
        notes = request.POST.get("notes")
        link = request.POST.get("link")

        newly_created_question = Question.objects.create(
            question_code=question_code,
            question_in_japanese=question_in_japanese,
            questions_in_english=question_in_english,
            possible_answers=possible_answers,
            answer=answer,
            notes=notes,
            link=link,
        )

        # Create related Vocabulary entries
        for i in range(1, 6):
            japanese_word = request.POST.get(f"j{i}")
            pronunciation = request.POST.get(f"p{i}")
            english_translation = request.POST.get(f"e{i}")
            if japanese_word and pronunciation and english_translation:
                Vocabulary.objects.create(
                    question=newly_created_question,
                    japanese_word=japanese_word,
                    pronunciation=pronunciation,
                    english_translation=english_translation
                )
        
        return HttpResponseRedirect(reverse("questions:success"))
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return render(request, "questions/add.html")

def success(request):
    return render(request, "questions/success.html")

def allvocab(request):
    vocab_list = Vocabulary.objects.all()  # Get related vocabulary entries
    context = {
        "vocab_list": vocab_list,
    }
    return render(request, "questions/allvocab.html", context)