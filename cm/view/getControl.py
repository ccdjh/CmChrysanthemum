# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.ext import webapp

from cm.view.baseControl import CcdjhMarx
from cm.model.databaseModel import DocPost

class Main(CcdjhMarx):
  def get(self):
    modelDocPost_query = DocPost.all().order('-date')
    modelDocPost = modelDocPost_query.fetch(10)
    listNeed=self.listNeedCM()
    template_values = {'modelDocPost': modelDocPost,'listNeed': listNeed,}
    self.htmlRenderCM('../template/doc.html',template_values)
    
class DocOneReceive(CcdjhMarx):
  def get(self,idc):
    idcc=int(idc)
    modelDocOne=DocPost.all().filter('idc =', idcc)
    template_values = {'modelDocOne': modelDocOne,}
    self.htmlRenderCM('../template/one.html',template_values)      