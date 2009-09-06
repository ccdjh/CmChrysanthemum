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
from cm.view.memcacheControl import DocPostM

class AdminPost(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    docc=DocPost.all().order('-date')
    doc = docc.fetch(limit=10, offset=0)
    template_values = {'listNeed': listNeed,'doc': doc,}
    self.htmlRenderCM('../template/admin.html',template_values)
    
class DocList(CcdjhMarx):
  def get(self,page=1):
    listNeed=self.listNeedCM()
    link=ListYou.all()
    #comment=DocPost.all()
    page=int(page)
    limit=5
    comment_query = DocPost.all().order('-date')
    count=comment_query.count()
    if (page-1)*limit>count:
      self.redirect("/error/")
    mm=self.navigationCM(page,count,limit)
    of=(mm['current']-1)*limit
    comment = comment_query.fetch(limit=limit, offset=of)
    template_values = {'listNeed': listNeed,'link': link,'comment': comment,'mm': mm,}
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
    p=DocPostM()
    feed = p.get_docpost() 
    #feed=DocPost.all().order('-date')
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
    
class ErrorAll(CcdjhMarx):
  def get(self):
    listNeed=self.listNeedCM()
    template_values = {'listNeed': listNeed,}
    self.htmlRenderCM('../template/error.html',template_values) 