# -*- coding: utf-8 -*-
import re
import os

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import images

from cm.model.databaseModel import DocPost
from cm.model.databaseModel import DocComment
from cm.model.databaseModel import DocTag
from cm.model.databaseModel import ListYou
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
      modelDocPost.tags.append(vvv)
      modelDocPost.put()
    self.redirect("/")
    
class DocCommentReceive(CcdjhMarx):
  def post(self):
    commentIdc = self.request.get("commentIdc")
    commentIdcc=int(commentIdc)
    q=DocPost.get_by_id(commentIdcc)
    comment = DocComment(contact=q)
    comment.comment = self.request.get("content")
    comment.put()
    count=DocPost.all().filter('idc = ', commentIdcc).get()
    count.commentcount += 1
    count.put()
    self.redirect(self.request.referer)
    
class DocListReceive(CcdjhMarx):
  def post(self):
    modelListYou=ListYou()
    modelListYou.name = self.request.get("linkname")
    modelListYou.link = db.Link(self.request.get("link"))
    modelListYou.put()
    self.redirect(self.request.referer)
    
class AboutReceive(CcdjhMarx):
  def post(self):
    modelProfile=Profile()
    modelProfile.name = self.request.get("name")
    modelProfile.about = self.request.get("about")
    imgb = self.request.get("img")
    imgc=images.Image(imgb)
    imgd = imgc.im_feeling_lucky()
    modelProfile.avatar = db.Blob(imgd)
    modelProfile.put()
    self.redirect(self.request.referer)    