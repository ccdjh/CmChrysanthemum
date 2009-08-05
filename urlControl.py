# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from cm.view.getControl import Main
from cm.view.baseControl import Error
from cm.view.htmlConrtol import AdminPost
from cm.view.postControl import DocPostReceive

from cm.view.getControl import DocOneReceive
from cm.view.postControl import DocCommentReceive
from cm.view.getControl import DocTagReceive

application = webapp.WSGIApplication([
                                                        (r'/', Main),
                                                        (r'/admin/', AdminPost),
                                                        (r'/admin/docreceive/', DocPostReceive),
                                                        (r'/doc/(?P<idc>[0-9]{1,9})/', DocOneReceive),
                                                        (r'/comment/$', DocCommentReceive),
                                                        (r'/tag/(?P<tagc>[^/]+)/', DocTagReceive),
                                                        (r'/tag/(?P<tagc>[^/]+)/(?P<page>[0-9]+)/', DocTagReceive),
                                                        ('.*',Error)
], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
