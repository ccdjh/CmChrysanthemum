# -*- coding: utf-8 -*-
import urllib

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import images
from google.appengine.api import users

from cm.view.baseControl import CcdjhMarx
from cm.model.databaseModel import DocPost
from cm.model.databaseModel import DocTag
from cm.model.databaseModel import Profile
from cm.model.databaseModel import ListYou
from cm.model.databaseModel import DocComment

class Main(CcdjhMarx):
  def get(self,page=1):
    page=int(page)
    limit=4
    modelDocPost_query = DocPost.all().order('-date')
    count=modelDocPost_query.count()
    if (page-1)*limit>count:
      self.redirect("/error/")
    mm=self.navigationCM(page,count,limit)
    of=(mm['current']-1)*limit
    modelDocPost = modelDocPost_query.fetch(limit=limit, offset=of)
    listNeed=self.listNeedCM()
    tagList=DocTag.all()
    link=ListYou.all()
    pro=Profile.all()
    template_values = {'modelDocPost': modelDocPost,'listNeed': listNeed,'mm': mm,'tagList': tagList,'link': link,'pro': pro,}
    self.htmlRenderCM('../template/doc.html',template_values)

class DocOneReceive(CcdjhMarx):
  def get(self,idc):
    idcc=int(idc)
    modelDocOne=DocPost.all().filter('idc = ', idcc)
    modelDocOne.get()
    if modelDocOne is None:
      self.redirect("/error/")
    u=users.get_current_user()
    listNeed=self.listNeedCM()
    template_values = {'modelDocOne': modelDocOne,'u': u,'listNeed': listNeed,}
    self.htmlRenderCM('../template/one.html',template_values)
 
class DocTagReceive(CcdjhMarx):
  def get(self,tagc,page=1):
    page=int(page)
    tagText=urllib.unquote(tagc).decode("utf-8")
    limit=2
    m=DocPost.all().filter('tags =', tagText)
    count=m.count()
    if (page-1)*limit>count:
      self.redirect("/error/")
    mm=self.navigationCM(page,count,limit)
    of=(mm['current']-1)*limit
    modelDocTag=m.fetch(limit=limit, offset=of)
    template_values = {'modelDocTag': modelDocTag,'tagText': tagText,'mm': mm,}
    self.htmlRenderCM('../template/tag.html',template_values)
    
class AboutImageReceive(CcdjhMarx):
  def get(self,idc):    
    g =int(idc)
    photo=Profile.get_by_id(g)
    self.response.headers['Content-Type'] = 'image/jpeg'
    self.response.out.write(photo.avatar)
    
class DelListReceive(CcdjhMarx):
  def get(self,idc):    
    g =int(idc)
    y=ListYou.get_by_id(g)
    db.delete(y)
    self.redirect(self.request.referer)
    
class DelDocReceive(CcdjhMarx):
  def get(self,idc):    
    g =int(idc)
    y=DocPost.get_by_id(g)
    for tt in y.tags:
      ttt=tt
      ttt=DocTag.all().filter('tag =', tt).get()
      if ttt.tagcount>1:
        ttt.tagcount=ttt.tagcount-1
        ttt.put()
      else:
        db.delete(ttt)
    db.delete(y)
    self.redirect(self.request.referer)
    
class DelCommentReceive(CcdjhMarx):
  def get(self,idc,idd):    
    g =int(idc)
    y=DocComment.get_by_id(g)
    db.delete(y)
    gg =int(idd)
    yy=DocPost.get_by_id(gg)
    yy.commentcount=yy.commentcount-1
    yy.put()
    self.redirect(self.request.referer)    