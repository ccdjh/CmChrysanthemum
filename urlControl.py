# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from cm.view.getControl import Main
from cm.view.baseControl import Error
from cm.view.htmlConrtol import AdminPost

application = webapp.WSGIApplication([
                                                        ('/', Main),
                                                        ('/admin/', AdminPost),
                                                        ('.*',Error)
], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()