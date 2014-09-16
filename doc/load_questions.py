
import sys, os
sys.path.append('/home/krother/mcquestions/')
from mcquestions import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcquestions.settings")

from multichoice.models import MCQuestion, Answer
from quiz.models import Quiz, Category, SubCategory

def create_category(name):
    print '\ncategory', name
    test = Category.objects.filter(category=name).exists()
    if test == False:
        category_object = Category(category=name)
        category_object.save()
    else:
        category_object = Category.objects.get(category=name)
    return category_object

def create_subcategory(name, category):
    print '\n\tsubcategory', name
    assert category != None
    test = SubCategory.objects.filter(sub_category=name).exists()
    if test == False:
        subcategory_object = SubCategory(sub_category=name, category=category)
        subcategory_object.save()
    else:
        subcategory_object = SubCategory.objects.get(sub_category=name)
    return subcategory_object

def create_question(category, sub_category, question, alt_answers):
    mc = MCQuestion(content=question, category=category, sub_category=sub_category)
    mc.save()
    for alt, correct in alt_answers:
        a = Answer(question=mc, content=alt, correct=correct)
        a.save()
    return mc

def create_quiz(category, subcategory, questions):
    url = subcategory.sub_category.lower().replace(' ', '_')
    print "\nCreating Quiz '%s' with %i questions" % (url, len(questions))
    quiz = Quiz(title=subcategory.sub_category, category=category, url=url)
    quiz.save()
    for q in questions:
        q.quiz.add(quiz)
        q.save()


category = None
subcategory = None
questions = []
question = ""
alt_answers = []
    
for line in open('sample_questions.md'):
    if line.startswith('# '):
        category = create_category(line[2:].strip())
    elif line.startswith('## '):
        if questions:
            create_quiz(category, subcategory, questions)
        subcategory = create_subcategory(line[3:].strip(), category)
        questions = []
    elif line.startswith('### '):
        if question:
            q = create_question(category, subcategory, question, alt_answers)
            questions.append(q)
        question = line[4:].strip()
        alt_answers = []
        print '\n\t\tnew question', question
        
    elif line.startswith('-['):
        alt = line[4:].strip()
        correct = line.startswith('-[x')
        alt_answers.append((alt, correct))
        print '\t\t\t', correct, alt


q = create_question(category, subcategory, question, alt_answers)
questions.append(q)
create_quiz(category, subcategory, questions)
