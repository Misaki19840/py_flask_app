from flask import Flask, request,render_template
import argparse
import sys

app = Flask(__name__)

# login処理です
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        return render_template('form.html')
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        return render_template('form.html')

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='put arg')
    parser.add_argument('--host',default='0.0.0.0')
    parser.add_argument('--port',default='8000')
    parser.add_argument('--debug',default='True')
    args = parser.parse_args()
    print(args.host)
    print(args.port)
    print(args.debug)
    app.run(host = args.host,port = int(args.port), debug=args.debug)