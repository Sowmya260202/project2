from flask import Flask,render_template,request
import pymysql as sql

app = Flask(__name__)

my_connection=sql.connect(
    host = 'localhost',
    user = 'root',
    passwd='password#123',
    database='registration'
)
my_cursor = my_connection.cursor()

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/admissions',methods=['GET'])
def admissions():
    return render_template('admissions.html')

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register-form',methods=['POST'])
def register_form():
    sid = request.form['id']
    sname = request.form['sname']
    phone = request.form['phone']
    email = request.form['email']
    srank = request.form['srank']
    percentage = request.form['percentage']
    course = request.form['course']
    address = request.form['address']

    query = '''
        insert into students(sid,sname,phone,email,srank,percentage,course,address)
        values(%s,%s,%s,%s,%s,%s,%s,%s);
     '''

    values=(sid,sname,phone,email,srank,percentage,course,address)
    my_cursor.execute(query,values)
    my_connection.commit()
    return 'registration is successfully completed'

@app.route('/view',methods=['GET'])
def view():
    query = '''
     select * from students;
    '''
    my_cursor.execute(query)
    data = my_cursor.fetchall()
    return render_template('view.html',details=data)

@app.route('/update',methods=['GET'])
def update():
    return render_template('update.html')

@app.route('/update-form',methods=['POST'])
def update_form():
    sid = request.form['id']
    field = request.form['field']
    new_value = request.form['new_value']

    query = f'''
      update students
      set {field} = "{new_value}"
      where sid = {sid};
    '''
    my_cursor.execute(query)
    my_connection.commit()
    return 'updated successfully'

@app.route('/delete',methods=['GET'])
def delete():
    return render_template('delete.html')

@app.route('/delete-form',methods=['POST'])
def delete_form():
    sid= request.form['id']
    query = f'''
      delete from students
      where sid = {sid}
     '''
    my_cursor.execute(query)
    my_connection.commit()
    return f'user {sid} has been deleted'

@app.route('/query-form',methods=['POST'])
def query_form():
    qname=request.form['qname']
    email=request.form['email']
    phone=request.form['phone']
    course =request.form['course']

    query='''
        insert into queries(qname,email,phone,course)
        values(%s,%s,%s,%s)
    '''
    values =(qname,email,phone,course)

    my_cursor.execute(query,values)
    my_connection.commit()
    return render_template('index.html')



