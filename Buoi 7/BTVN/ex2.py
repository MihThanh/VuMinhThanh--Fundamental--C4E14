from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<weight>/<height>')
def index(weight, height):
    bmi = (float(weight)/(float(height) * float(height)))

    if bmi < 16:
        return 'Your BMI: '+ str(bmi) + ' '  'Severely underweight'
    elif bmi >= 16 and bmi <= 18.5:
        return 'Your BMI: '+ str(bmi) + ' ' + 'Underweight'
    elif bmi >= 18.5 and bmi <25:
        return 'Your BMI: '+ str(bmi) + ' ' + 'Normal'
    elif bmi>= 25 and bmi < 30:
        return 'Your BMI: '+ str(bmi) + ' ' + 'Overweight'
    else:
        return 'Your BMI: '+ str(bmi) + ' ' + 'Obese'



if __name__ == '__main__':
  app.run(debug=True)
