from flask import Flask,render_template,request,redirect,jsonify,session,flash
import device_manger as mgr

app = Flask(__name__)
app.secret_key ="digipodium iot workshops"

@app.route('/')
def hello():
    s1 = mgr.get_status('dev1')
    s2 = mgr.get_status('dev2')
    s3 = mgr.get_status('dev3')
    s4 = mgr.get_status('dev4')
    return render_template('index.html',s1=s1,s2=s2,s3=s3,s4=s4)

@app.route('/update', methods=['GET','POST'])
def process():
    device = request.args.get('device')
    action = request.args.get('state')
    status = 'on' if action=='1' else 'off'
    print(device,status)
    result = mgr.update_device(device,status)
    if result:
        return jsonify({'msg':f"device {device} switched {status}",'status':True})
    else:
        return jsonify({'msg':f"device {device} switched {status}",'status':False})

if __name__ == '__main__':
    app.run('192.168.43.203',debug=True)
