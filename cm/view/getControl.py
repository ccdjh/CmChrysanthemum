# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.ext import webapp

from cm.view.baseControl import CcdjhMarx
from cm.model.databaseModel import DocPost
from cm.model.databaseModel import DocTag

class Main(CcdjhMarx):
  def get(self,page=1):
    page=int(page)
    limit=2
    modelDocPost_query = DocPost.all().order('-date')
    count=modelDocPost_query.count()
    if (page-1)*limit>count:
      self.redirect("/error/")
    mm=self.navigationCM(page,count,limit)
    of=(mm['current']-1)*limit
    modelDocPost = modelDocPost_query.fetch(limit=limit, offset=of)
    listNeed=self.listNeedCM()
    tagList=DocTag.all()
    template_values = {'modelDocPost': modelDocPost,'listNeed': listNeed,'mm': mm,'tagList': tagList,}
    self.htmlRenderCM('../template/doc.html',template_values)

class DocOneReceive(CcdjhMarx):
  def get(self,idc):
    idcc=int(idc)
    modelDocOne=DocPost.all().filter('idc =', idcc)
    template_values = {'modelDocOne': modelDocOne,}
    self.htmlRenderCM('../template/one.html',template_values)
 
class DocTagReceive(CcdjhMarx):
  def get(self,tagc,page=1):
    page=int(page)
    tagText=tagc
    limit=2
    m=DocPost.all().filter('tags =', tagc)
    count=m.count()
    if (page-1)*limit>count:
      self.redirect("/error/")
    mm=self.navigationCM(page,count,limit)
    of=(mm['current']-1)*limit
    modelDocTag=m.fetch(limit=limit, offset=of)
    template_values = {'modelDocTag': modelDocTag,'tagText': tagText,'mm': mm,}
    self.htmlRenderCM('../template/tag.html',template_values)    