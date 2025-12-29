from flask import Flask, render_template, request
from crew_logic import run_pdf_crew
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        topic = request.form.get('topic')
        result = run_pdf_crew(topic)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)