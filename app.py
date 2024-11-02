from flask import Flask, request, render_template
from calculate import Calculate

app = Flask(__name__)

def calculate(text):
    cal = Calculate(text)
    result = cal.perform_calculation()
    return result

@app.route("/", methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text_box_value = request.form.get('text_box')
        print("Value from text_box:", text_box_value)
        result = calculate(text_box_value)
    return render_template('index.html', result=str(result))

if __name__ == "__main__":
    app.run(debug=True)
