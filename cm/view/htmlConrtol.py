# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import memcache

from cm.view.baseControl import CcdjhMarx
from cm.model.databaseModel import ListYou
from cm.model.databaseModel import Profile
from cm.model.databaseModel import DocPost
from cm.model.databaseModel import DocComment
from cm.model.databaseModel import Theme
from cm.model.databaseModel import ThemeTwo

from cm.view.memcacheControl import ProfileM


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
    #p=ProfileM()
    #about = p.get_profile() 
    about=Profile.all()
    template_values = {'listNeed': listNeed,'about': about,}
    self.htmlRenderCM('../template/about.html',template_values)
    
class Feed(CcdjhMarx):
  def get(self):
    feed=DocPost.all().order('-date')
    myurl=self.request.host_url
    pro=Profile.all()
    template_values = {'feed': feed,'myurl': myurl,'pro': pro,}
    self.htmlRenderCM('../template/feed.xml',template_values)
    
class DocPut(CcdjhMarx):
  def get(self,idc):
    g =int(idc)
    y=DocPost.all().filter('idc = ', g)
    template_values = {'y': y,}
    self.htmlRenderCM('../template/put.html',template_values)
    
class DocTheme(CcdjhMarx):
  def get(self):
    y=Theme.all()
    template_values = {'y': y,}
    self.htmlRenderCM('../template/theme.html',template_values)    