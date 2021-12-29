from flask import Flask,render_template,request,url_for,redirect
import random
random_num = random.randint(0,100)
count = 10
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():

 print(random_num)
 return render_template('htmlform.html',rand = random_num,count = count)
@app.route('/checkrand',methods=['POST','GET'])
def rand():
 message = ''
 data = int(request.args.get('input'))
 counter = int(request.args.get('count'))
 print('inputed data is '+str(data))
 counter = counter-1
 print(random_num)
 print(data == random_num)
 if data == random_num:
    counter = 0
    return render_template('htmlform.html',msg = 'you have won the game',count = counter)
 elif data < random_num and counter > 0:
     return render_template('htmlform.html',msg = 'Small num',count = counter)
 elif data > random_num and counter > 0:
     return render_template('htmlform.html',msg = 'Large num',count = counter)
 return render_template('htmlform.html',msg = 'you lose the game',result = random_num,count = counter,rand = random_num)
if __name__ == '__main__':
    app.run(debug=True)