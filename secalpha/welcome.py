# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, send_file
import sys
sys.path.append(os.getcwd())
sys.path.append('/home/vcap/tmp')
sys.path.append('/home/vcap/app')
sys.path.append('/home/vcap')
import corpcrawl
from corpcrawl.crawler import CorpCrawl 
from corpcrawl.backend import Backend
#import StringIO

class MyBackend(Backend):
#    strIO = StringIO.StringIO()
    workfile = os.getcwd() + '/workfile'
    f = open(workfile, 'w')
    def get_company(self, name):
        pass
    def add_company(self, comp):
        pass
#        self.strIO.write(str(comp))
        out1 = str(comp) + '\n' + '\n'
        self.f.write(out1)


app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/getsec')
def SayHello():
    my_backend = MyBackend() 
    crawler=CorpCrawl(cache_path=os.getcwd(), backend=my_backend)
    crawler.crawl([2010], [1])
    workfile = os.getcwd() + '/workfile'
    return send_file(workfile,
                     attachment_filename="testing.txt",
                     as_attachment=True)
#    return send_file(my_backend.strIO,
#                     attachment_filename="testing.txt",
#                     as_attachment=True)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
