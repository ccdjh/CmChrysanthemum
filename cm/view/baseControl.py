# -*- coding: utf-8 -*-
import re
import os

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class CcdjhMarx(webapp.RequestHandler):
    def htmlRenderCM(self, template_file, template_value):
        path = os.path.join(os.path.dirname(__file__), template_file)
        self.response.out.write(template.render(path, template_value))
    def errorRenderCM(self,code):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!40444444')
    def navigationCM(self,offset,total_count,limit=10):
      if offset:
        try:
          offset = int(offset)
        except:
          offset = 1
        else:
          offset = max(1, offset)
      else:
        offset = 1
      if offset>1:
        previous_list = range(1,offset)
        previous = offset -1
      else:
        previous_list = None
        previous = None
      last=((total_count-1)/limit)+1
      if last>offset:
        next_list = range(offset+1,last+1)
        next = offset + 1
      else:
        next_list = None
        next = None
      response = {'previous_list' : previous_list,
                'previous':previous,
                'current': offset,
                'next': next,
                'next_list': next_list,
                'last': last }
      return response

    def listNeedCM(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            urlLinktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            urlLinktext = 'Login'
        
        listNeed = {'url' : url,
                        'urlLinktext': urlLinktext }
        return listNeed
    
class Error(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!404')
