# Customizing django_quiz

### Purpose of this document
Help to customize the look and feel of django_quiz 
if you are not a django pro.

### Customize templates
#### Problem
The **django_quiz** app is installed and works, but you want to change the page templates to match your website.

#### Solution

1. Copy the template files from **django_quiz/quiz/templates** to **your_django_project/templates/** . 
2. Edit the files.
3. add to **settings.py**: 

    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

4. Reload the page and see the effect.


### Import questions
#### Problem
You have a batch of Multiple Choice questions that you want to load into your database.

#### Solution
Try the script in **multichoice/load_questions.py** to load questions from a Markdown file. It is a straightforward approach that omits a lot of features, but could work as a starting point.

### Questions
Kristian Rother
krother@academis.eu
