import sys
import Stabulous as stab
import utils
from flask import Flask
sys.path.append("Website_Stuff")
from views import views

sys

def startConverstion():
    mystatus=utils.Status()
    mystatus.setStatus("Starting")
    print(stab.main(r"D:\AIM_GAN_Model\PersonalTest\unstable\0.avi",mystatus))

app= Flask(__name__)

app.register_blueprint(views, url_prefix="/")

if __name__=='__main__':
    app.run(debug=True)