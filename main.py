from flask import Flask, render_template
from datetime import datetime
import os.path
import os

#if os.path.isfile('C:/Users/hbrain/PycharmProjects/pythonProject1/static/image/my_screenshot.png'):
    #os.remove('C:/Users/hbrain/PycharmProjects/pythonProject1/static/image/my_screenshot.png')
data2 = '0'
data3 = 0
tdata1 = datetime.now()
flag = 0
first_page = 'image/wait.png'
app = Flask(__name__)
@app.route("/")
def hello():

    global data2
    global data3
    global flag
    global first_page
    global tdata1
    data = str(datetime.now())

    file = 'C:/Users/hbrain/PycharmProjects/pythonProject1/static/image/my_screenshot.png'

    d1 = '2022-10-27 11:16:57.603188'
    d2 = '2022-10-27 11:14:56.024208'
    d3 = '0:00:01.346701'

    if flag==0:
        if os.path.isfile(file):
            create_time = os.path.getctime(file)
            ctime = datetime.fromtimestamp(create_time)
            tdata2 = datetime.now()
            data2 = str(datetime.fromtimestamp(create_time))
                #str(datetime.strptime(ctime,"%H:%M:%S"))
            data3 = str(tdata2 - ctime)
            first_page = 'image/my_screenshot.png'
            flag = 2


    tdata1 = datetime.now()

    return render_template('simple.html', d1 = data, name_url = first_page, d2 = data2, d3 = data3)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port="808")