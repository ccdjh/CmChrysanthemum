# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from ccdjh.view.getControl import Main
from ccdjh.view.htmlControl import DocPostTemplate
from ccdjh.view.postControl import DocPostReceive
from ccdjh.view.getControl import DocOneReceive
from ccdjh.view.postControl import DocCommentReceive
from ccdjh.view.errorControl import Error
from ccdjh.view.getControl import DocTagReceive

application = webapp.WSGIApplication([
                                                        ('/', Main),
                                                        (r'/docpost/$', DocPostTemplate),
                                                        (r'/docreceive/$', DocPostReceive),
                                                        ('/docone/(?P<idc>[0-9]{1,9})/', DocOneReceive),
                                                        (r'/tag/(?P<tagc>[^/]+)/', DocTagReceive),
                                                        (r'/tag/(?P<tagc>[^/]+)/(?P<page>[0-9]+)/', DocTagReceive),
                                                        (r'/comment/$', DocCommentReceive),
                                                        ('.*',Error)
], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
