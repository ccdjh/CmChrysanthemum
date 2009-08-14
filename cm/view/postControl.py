# -*- coding: utf-8 -*-
import re
import os
import codecs

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import images

from cm.model.databaseModel import DocPost
from cm.model.databaseModel import DocComment
from cm.model.databaseModel import DocTag
from cm.model.databaseModel import ListYou
from cm.model.databaseModel import ListYouTwo
from cm.model.databaseModel import Profile



from cm.view.baseControl import CcdjhMarx


class DocPostReceive(CcdjhMarx):
  def post(self):
    modelDocPost=DocPost()
    modelDocTag=DocTag()
    if users.get_current_user():
      modelDocPost.author = users.get_current_user()
    modelDocPost.content = self.request.get("content")
    modelDocPost.title = self.request.get("title")
    modelDocPost.put()
    m=modelDocPost.key().id()
    modelDocPost.idc = m
    modelDocPost.put()
    
    v= self.request.get("tags")
    vv=re.split(',',v)
    for vvv in vv :
      ccc=vvv
      ccc=DocTag()
      bbb=DocTag()
      cccc=bbb.all().filter('tag = ', vvv).get()
      if cccc is not None:
        cccc.tagcount += 1
        cccc.put()
      else:
        ccc.tag=vvv
        ccc.put()
      vvvv=vvv
      modelDocPost.tags.append(vvvv)
      modelDocPost.put()
    self.redirect(self.request.referer)
    
class DocCommentReceive(CcdjhMarx):
  def post(self):
    c = self.request.get("commentIdc")
    cc=int(c)
    q=DocPost.get_by_id(cc)
    comment = DocComment(contact=q)
    comment.comment = self.request.get("content")
    gravatar = self.request.get("gravatar")
    comment.postid = cc
    if users.get_current_user():
      com= users.get_current_user()
      comm=com.email()
      comment.author = db.Email(comm)
    default = "/static/homsar.jpg"
    size=40
    if gravatar:
      comment.image=self.gravatarCM(comm,default,size)
    else:
      commm="yx0662@gmail.com"
      comment.image=self.gravatarCM(commm,default,size)
    comment.put()
    count=DocPost.all().filter('idc = ', cc).get()
    count.commentcount += 1
    m=comment.key().id()
    comment.idc = m
    comment.put()
    count.put()
    self.redirect(self.request.referer)
    
class DocListReceive(CcdjhMarx):
  def post(self):
    modelListYou=ListYou()
    modelListYou.name = self.request.get("linkname")
    modelListYou.put()
    m=modelListYou.key().id()
    modelListYou.idc = m
    modelListYou.put()
    self.redirect(self.request.referer)
    
class DocListReceiveTwo(CcdjhMarx):
  def post(self):
    from cm.model.databaseModel import ListYou
    from cm.model.databaseModel import ListYouTwo
    c = self.request.get("commentIdc")
    cc=int(c)
    q=ListYou.get_by_id(cc)
    ListYou = ListYouTwo(contact=q)
    ListYou.comment = self.request.get("linkname")
    ListYou.link = db.Link(self.request.get("link"))
    ListYou.put()
    m=ListYou.key().id()
    ListYou.idc = m
    ListYou.put()
    self.redirect(self.request.referer)
    
class AboutReceive(CcdjhMarx):
  def post(self):
    modelProfile=Profile.all().get()
    if modelProfile is not None:
    #modelProfile=Profile()
      modelProfile.name = self.request.get("name")
      modelProfile.about = self.request.get("about")
      modelProfile.title = self.request.get("title")
      modelProfile.description = self.request.get("description")
      imgb = self.request.get("img")
      modelProfile.avatar = db.Blob(imgb)
      modelProfile.put()
      m=modelProfile.key().id()
      modelProfile.idc = m
      modelProfile.put()
    else:
      modelProfileb=Profile()
      modelProfileb.name = self.request.get("name")
      modelProfileb.about = self.request.get("about")
      modelProfileb.title = self.request.get("title")
      modelProfileb.description = self.request.get("description")
      imgb = self.request.get("img")
      modelProfileb.avatar = db.Blob(imgb)
      modelProfileb.put()
      m=modelProfileb.key().id()
      modelProfileb.idc = m
      modelProfileb.put()
    self.redirect(self.request.referer)
    
class DocPutReceive(CcdjhMarx):
  def post(self):
    c = self.request.get("commentIdc")
    cc=int(c)
    modelDocPost=DocPost.get_by_id(cc)
    modelDocPost.content = self.request.get("content")
    modelDocPost.title = self.request.get("title")
    modelDocPost.put()
    self.redirect("/admin/doclist/")
    