# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from cm.view.getControl import Main
from cm.view.baseControl import Error
from cm.view.htmlConrtol import AdminPost
from cm.view.postControl import DocPostReceive
from cm.view.getControl import DelDocReceive
from cm.view.htmlConrtol import DocPut
from cm.view.postControl import DocPutReceive

from cm.view.getControl import DocOneReceive
from cm.view.postControl import DocCommentReceive
from cm.view.getControl import DelCommentReceive
from cm.view.getControl import DocTagReceive

from cm.view.postControl import DocListReceive
from cm.view.htmlConrtol import DocList
from cm.view.getControl import DelListReceive
from cm.view.postControl import DocListReceiveTwo

from cm.view.postControl import AboutReceive
from cm.view.htmlConrtol import About
from cm.view.getControl import AboutImageReceive

from cm.view.htmlConrtol import Feed

application = webapp.WSGIApplication([
                                        (r'/', Main),
                                        (r'/feed/', Feed),
                                        (r'/p/(?P<page>[0-9]{1,9})/', Main),
                                        (r'/admin/', AdminPost),
                                        (r'/admin/docreceive/', DocPostReceive),
                                        (r'/admin/doclist/', DocList),
                                        (r'/admin/deldoclist/(?P<idc>[0-9]{1,9})/', DelListReceive),
                                        (r'/admin/doclistreceivetwo/', DocListReceiveTwo),
                                        (r'/admin/aboutreceive/', AboutReceive),
                                        (r'/admin/about/', About),
                                        (r'/image/(?P<idc>[0-9]{1,9})/', AboutImageReceive),
                                        (r'/admin/doclistreceive/', DocListReceive),
                                        (r'/doc/(?P<idc>[0-9]{1,9})/(?P<title>[^/]+)/', DocOneReceive),
                                        (r'/admin/deldoc/(?P<idc>[0-9]{1,9})/', DelDocReceive),
                                        (r'/admin/putdoc/(?P<idc>[0-9]{1,9})/', DocPut),
                                        (r'/admin/putdocreceive/', DocPutReceive),
                                        (r'/admin/delcomment/(?P<idc>[0-9]{1,9})/(?P<idd>[0-9]{1,9})/', DelCommentReceive),
                                        (r'/comment/$', DocCommentReceive),
                                        (r'/tag/(?P<tagc>[^/]+)/', DocTagReceive),
                                        (r'/tag/(?P<tagc>[^/]+)/(?P<page>[0-9]+)/', DocTagReceive),
                                        (r'/error/', Error),
                                        ('.*',Error)
], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
