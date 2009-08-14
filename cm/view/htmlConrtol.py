# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.ext import webapp

from cm.view.baseControl import CcdjhMarx
from cm.model.databaseModel import ListYou
from cm.model.databaseModel import Profile
from cm.model.databaseModel import DocPost
from cm.model.databaseModel import DocComment


class AdminPost(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    doc=DocPost.all()
    template_values = {'listNeed': listNeed,'doc': doc,}
    self.htmlRenderCM('../template/admin.html',template_values)
    
class DocList(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    link=ListYou.all()
    comment=DocPost.all()
    template_values = {'listNeed': listNeed,'link': link,'comment': comment,}
    self.htmlRenderCM('../template/list.html',template_values)
    
class About(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    about=Profile.all()
    template_values = {'listNeed': listNeed,'about': about,}
    self.htmlRenderCM('../template/about.html',template_values)
    
class Feed(CcdjhMarx):
  def get(self):
    feed=DocPost.all().fetch(limit=2)
    template_values = {'feed': feed,}
    self.htmlRenderCM('../template/feed.xml',template_values)
    
class DocPut(CcdjhMarx):
  def get(self,idc):
    g =int(idc)
    y=DocPost.all().filter('idc = ', g)
    template_values = {'y': y,}
    self.htmlRenderCM('../template/put.html',template_values)