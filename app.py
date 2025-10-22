from flask import Flask, render_template, request

app = Flask(__name__)

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Wordsworth", "William Shakespeare", "Leo Tolstoy", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is 9 + 10?",
        "options": ["17", "18", "19", "21"],
        "answer": "19"
    }
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_answers = []
        score = 0
        for i, q in enumerate(quiz):
            selected = request.form.get(f"q{i}")
            correct = q["answer"]
            is_correct = selected == correct
            if is_correct:
                score += 1
            user_answers.append({
                "question": q["question"],
                "selected": selected,
                "correct": correct,
                "is_correct": is_correct,
                "options": q["options"]
            })
        return render_template("index.html", submitted=True, quiz=user_answers, score=score, total=len(quiz))
    
    return render_template("index.html", submitted=False, quiz=list(enumerate(quiz)))

if __name__ == "__main__":
    app.run(debug=True)
