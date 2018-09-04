# WebHook Setup page using Flask App
# Given Token: 30270....
# A very simple Flask Hello World app for you to get started with...

import telepot
import urllib3
from flask import Flask, request
from nltk.chat.eliza import eliza_chatbot

from flask import render_template, redirect, url_for, session, send_from_directory

proxy_url = "http://proxy.server:1234"

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url,
                                    num_pools=3, maxsize=10, retries=False, timeout=30),
}

telepot.api._onetime_pool_spec = (urllib3.ProxyManager,
                                  dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                       retries=False, timeout=30)
                                  )

secret = "A_SECRET_NUMBER"
bot = telepot.Bot('302704...erased...')
bot.setWebhook(
    "https://webpage_url/{}".format(secret),
    max_connections=1)


# set the project root directory as the static folder, you can set others,

app = Flask(__name__, static_url_path='')


# [ WEB HOOK for TELEGRAM BOT ] -------------------------------------------------------------------
@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]

        # bot.sendMessage(chat_id, "This's Flask App: you said '{}', Thank you..".format(text))
        # Ln is changing like below

        if text == "/start":
            bot.sendMessage(
                chat_id, "Hello, I'm your Therapist. How can I help you?")
        elif text == "/stop":
            bot.sendMessage(
                chat_id, "Ok, it was pleasure to meet you. I hope see you soon, Bye~")
        else:
            bot.sendMessage(chat_id, eliza_chatbot.respond(text))
    return "OK"

# [ WEB PAGE ] --------------------------------------------------------------------


@app.route('/')
def index():
    return render_template('./index_flask.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/main')
def hello_workd():
    return '<h1>Hello FLASK World!</h1>'


@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username='default'):
    return 'USER : %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post #Num : %d' % post_id


@app.route('/logging')      # show logging message on console
def logging_test():         # logger message
    test = 1
    app.logger.debug('NEED : Debugging!')
    app.logger.warning(str(test) + ' Line')
    app.logger.error('*** ERROR!! ***')
    return "_EOL_ : End of Logging message is printed out at console : DONE!"


@app.route('/login_form')
def login_form():
    return render_template('./login_form.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if (request.form['username'] == 'Jamie' and request.form['password'] == '1234'):
            session['logged_in'] = True
            session['username'] = request.form['username']
        else:
            return '*** ERROR: Login Information are not valid!'
    else:
        return '*** ERROR: Wrong Acess (Access\'s denied)'


@app.route('/get_test', methods=['GET'])
def get_test():
    if request.method == 'GET':
        if (request.args.get('username') == 'Jamie' and request.args.get('password') == '1234'):
            return request.args.get('username') + "~!! , we welcome you...."
        else:
            return '*** ERROR: Login Information are not valid!'
    else:
        return '*** ERROR: Wrong Acess (Access\'s denied)'


@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/template')
@app.route('/template/<temp_id>')
def template_test(temp_id='Golf'):
    sports = ['Baseball', 'Soccer', 'Basketball',
              'Valleyball', 'Hokkey', 'Golf', 'Ping-pong', ]
    return render_template('template.html', temp_id=temp_id, sports=sports)


@app.route('/doraemon')
def doraemon():
    return render_template('./css_anim_doraemon_rolling_eyes2.html')


app.secret_key = '123?'
# session & request were used.
# app.secret_key = 'abc' --> should be added!
