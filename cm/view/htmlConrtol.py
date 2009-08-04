# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.ext import webapp

from cm.view.baseControl import CcdjhMarx

class AdminPost(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    template_values = {'listNeed': listNeed,}
    self.htmlRenderCM('../template/admin.html',template_values)