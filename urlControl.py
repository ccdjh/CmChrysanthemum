# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
#       Chrysanthemum Tea
#       
#       Copyright 2009 Ccdjh.Marx <Ccdjh.Marx@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from cm.view.getControl import Main
from cm.view.baseControl import Error
from cm.view.htmlControl import AdminPost
from cm.view.postControl import DocPostReceive
from cm.view.getControl import DelDocReceive
from cm.view.htmlControl import DocPut
from cm.view.postControl import DocPutReceive

from cm.view.getControl import DocOneReceive
from cm.view.postControl import DocCommentReceive
from cm.view.getControl import DelCommentReceive
from cm.view.getControl import DocTagReceive

from cm.view.postControl import DocListReceive
from cm.view.htmlControl import DocList
from cm.view.getControl import DelListReceive
from cm.view.postControl import DocListReceiveTwo
from cm.view.getControl import DelListTwoReceive

from cm.view.postControl import AboutReceive
from cm.view.htmlControl import About
from cm.view.getControl import AboutImageReceive

from cm.view.htmlControl import DocTheme
from cm.view.postControl import DocThemeReceive 
from cm.view.getControl import ThemeImageReceive
from cm.view.postControl import ThemeReceive

from cm.view.htmlControl import ErrorAll
from cm.view.htmlControl import Feed

application = webapp.WSGIApplication([
                                        (r'/', Main),
                                        (r'/feed/', Feed),
                                        (r'/p/(?P<page>[0-9]{1,9})/', Main),
                                        (r'/admin/', AdminPost),
                                        (r'/admin/doctheme/', DocTheme),
                                        (r'/admin/docthemereceive/', DocThemeReceive ),
                                        (r'/admin/themereceive/', ThemeReceive ),
                                        (r'/admin/docreceive/', DocPostReceive),
                                        (r'/admin/doclist/', DocList),
                                        (r'/admin/doclist/p/(?P<page>[0-9]{1,9})/', DocList),
                                        (r'/admin/deldoclist/(?P<idc>[0-9]{1,9})/', DelListReceive),
                                        (r'/admin/deldoclisttwo/(?P<idc>[0-9]{1,9})/', DelListTwoReceive),
                                        (r'/admin/doclistreceivetwo/', DocListReceiveTwo),
                                        (r'/admin/aboutreceive/', AboutReceive),
                                        (r'/admin/about/', About),
                                        (r'/image/(?P<idc>[0-9]{1,9})/', AboutImageReceive),
                                        (r'/imagetheme/(?P<idc>[0-9]{1,9})/', ThemeImageReceive),
                                        (r'/admin/doclistreceive/', DocListReceive),
                                        (r'/doc/(?P<idc>[0-9]{1,9})/(?P<title>[^/]+)/', DocOneReceive),
                                        (r'/admin/deldoc/(?P<idc>[0-9]{1,9})/', DelDocReceive),
                                        (r'/admin/putdoc/(?P<idc>[0-9]{1,9})/', DocPut),
                                        (r'/admin/putdocreceive/', DocPutReceive),
                                        (r'/admin/delcomment/(?P<idc>[0-9]{1,9})/(?P<idd>[0-9]{1,9})/', DelCommentReceive),
                                        (r'/comment/$', DocCommentReceive),
                                        (r'/tag/(?P<tagc>[^/]+)/', DocTagReceive),
                                        (r'/tag/(?P<tagc>[^/]+)/(?P<page>[0-9]+)/', DocTagReceive),
                                        (r'/error/', ErrorAll),
                                        ('.*',ErrorAll)
], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
