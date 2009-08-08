from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import images

from cm.view.baseControl import CcdjhMarx
from cm.model.databaseModel import DocPost
from cm.model.databaseModel import DocTag
from cm.model.databaseModel import Profile
from cm.model.databaseModel import ListYou

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
    modelDocOne=DocPost.all().filter('idc = ', idcc)
    modelDocOne.get()
    if modelDocOne is None:
      self.redirect("/error/")
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