from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from project.quiz_information.easy_answers import question_answers
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/quiz', methods=["GET", "POST"])
@login_required
def quiz():
    if request.method == 'POST':
        score = 0
        if request.form['q1'] == question_answers.get("Q1"):
            score += 1
        if request.form['q2'] == question_answers.get("Q2"):
            score += 1
        if request.form['q3'] == question_answers.get("Q3"):
            score += 1
        if request.form['q4'] == question_answers.get("Q4"):
            score += 1
        # with open("project/templates/answers.html", 'a') as f:
        #     f.write(f"Good Work, You Scored {score} questions correctly!")
        return render_template('answers.html', score=score)
        # return redirect(url_for('main.answers', score=score))
    return render_template('quiz.html')


@main.route('/answers')
@login_required
def answers():
    return render_template("answers.html")
