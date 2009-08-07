# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.ext import webapp

from cm.view.baseControl import CcdjhMarx
from cm.model.databaseModel import ListYou
from cm.model.databaseModel import Profile

class AdminPost(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    template_values = {'listNeed': listNeed,}
    self.htmlRenderCM('../template/admin.html',template_values)
    
class DocList(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    link=ListYou.all()
    template_values = {'listNeed': listNeed,'link': link,}
    self.htmlRenderCM('../template/list.html',template_values)
    
class About(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    about=Profile.all()
    template_values = {'listNeed': listNeed,'about': about,}
    self.htmlRenderCM('../template/about.html',template_values)        