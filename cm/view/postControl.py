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
from cm.model.databaseModel import Theme
from cm.model.databaseModel import ThemeTwo

from cm.view.memcacheControl import ProfileM
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
    if v=="":
      v="chrysanthemum"
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
    #gravatar = self.request.get("gravatar")
    comment.postid = cc
    if users.get_current_user():
      com= users.get_current_user()
      comm=com.email()
      comment.author = db.Email(comm)
      comment.googleauthor= users.get_current_user()
    #myurl=self.request.host_url
    default = self.request.host_url+"/static/image/gravatars.jpg"
    size=40
    comment.image=self.gravatarCM(comm,default,size)
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
    n=self.request.get("linkname")
    if n=="":
      n="ccdjh"
    l=self.request.get("link")
    if l=="":
      l="http://www.ccdjh.cn"
    else:
        from google.appengine.ext.db import BadValueError
        try:
            l = db.Link(l)
        except BadValueError:
            l="http://www.ccdjh.com"
            
    ListYou.comment = n
    ListYou.link = db.Link(l)
    ListYou.lidc=cc
    ListYou.put()
    m=ListYou.key().id()
    ListYou.idc = m
    ListYou.put()
    self.redirect(self.request.referer)
    
class AboutReceive(CcdjhMarx):
  def post(self):
    modelProfile=Profile.all().get()
    #img=self.request.get("img")
    #if img =="":
     #   self.redirect("/error/")
    if modelProfile is not None:
      modelProfile.name = self.request.get("name")
      modelProfile.about = self.request.get("about")
      modelProfile.title = self.request.get("title")
      modelProfile.description = self.request.get("description")
      #imgb =  images.resize(self.request.get("img"),46,46)
      modelProfile.avatar = db.Blob(self.request.get("img"))
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
      #imgb = images.resize(self.request.get("img"),46,46)
      modelProfileb.avatar = db.Blob(self.request.get("img"))
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
    
class DocThemeReceive(CcdjhMarx):
  def post(self):
    c=Theme()
    c.link = self.request.get("link")
    c.name = self.request.get("name")
    c.author = self.request.get("author")
    i = self.request.get("img")
    c.avatar = db.Blob(i)
    c.put()
    m=c.key().id()
    c.idc = m
    c.put()
    self.redirect(self.request.referer)
    
class ThemeReceive(CcdjhMarx):
  def post(self):
    g = self.request.get("th")
    o=ThemeTwo.all().get()
    if o is not None:
      if g=="white":
        o.link=db.Link("http://www.v2ex.com/")
        o.name="white"
        o.author="livid"
        o.put()
      elif g=="purple":
        o.link=db.Link("http://www.v2ex.com/")
        o.name="purple"
        o.author="livid"
        o.put()
      elif g=="orange":
        o.link=db.Link("http://www.v2ex.com/")
        o.name="orange"
        o.author="livid"
        o.put()
      elif g=="night":
        o.link=db.Link("http://www.v2ex.com/")
        o.name="night"
        o.author="livid"
        o.put()
      elif g=="dust":
        o.link=db.Link("http://www.v2ex.com/")
        o.name="dust"
        o.author="livid"
        o.put()
      elif g=="mour":
        o.link=db.Link("http://blog.kf25.cn/romoo")
        o.name="mour"
        o.author="Romoo"
        o.put()
      elif g=="light":
        o.link=db.Link("http://www.v2ex.com/")
        o.name="light"
        o.author="livid"
        o.put()
      elif g=="grid":
        o.link=db.Link("http://www.singrun.com/")
        o.name="grid"
        o.author="singrun"
        o.put()
      elif g=="cloud":
        o.link=db.Link("http://www.saicn.com/")
        o.name="cloud"
        o.author="sai"
        o.put()
      elif g=="flamingo":
        o.link=db.Link("http://www.ccdjh.com/")
        o.name="flamingo"
        o.author="livid"
        o.put()
      elif g=="tropical":
        o.link=db.Link("http://www.ccdjh.com/")
        o.name="tropical"
        o.author="ccdjh"
        o.put()
      elif g=="ivory":
        o.link=db.Link("http://www.ccdjh.com/")
        o.name="ivory"
        o.author="ccdjh"
        o.put()
      elif g=="cerulean":
        o.link=db.Link("http://www.ccdjh.com/")
        o.name="cerulean"
        o.author="ccdjh"
        o.put()
      elif g=="cobalt":
        o.link=db.Link("http://www.ccdjh.com/")
        o.name="cobalt"
        o.author="ccdjh"
        o.put()
      else:
        i=int(g)
        c=Theme.get_by_id(i)
        o.link=c.link
        o.name=c.name
        o.author=c.author
        o.put()
    else:
      m=ThemeTwo()
      if g=="white":
        m.link=db.Link("http://www.v2ex.com/")
        m.name="white"
        m.author="livid"
        m.put()
      elif g=="purple":
        m.link=db.Link("http://www.v2ex.com/")
        m.name="purple"
        m.author="livid"
        m.put()
      elif g=="orange":
        m.link=db.Link("http://www.v2ex.com/")
        m.name="orange"
        m.author="livid"
        m.put()
      elif g=="night":
        m.link=db.Link("http://www.v2ex.com/")
        m.name="night"
        m.author="livid"
        m.put()
      elif g=="dust":
        m.link=db.Link("http://www.v2ex.com/")
        m.name="dust"
        m.author="livid"
        m.put()
      elif g=="mour":
        m.link=db.Link("http://blog.kf25.cn/romoo")
        m.name="mour"
        m.author="romoo"
        m.put()
      elif g=="light":
        m.link=db.Link("http://www.v2ex.com/")
        m.name="light"
        m.author="livid"
        m.put()
      elif g=="grid":
        m.link=db.Link("http://www.singrun.com/")
        m.name="grid"
        m.author="singrun"
        m.put()
      elif g=="cloud":
        m.link=db.Link("http://www.saicn.com/")
        m.name="cloud"
        m.author="sai"
        m.put()
      elif g=="flamingo":
        m.link=db.Link("http://www.ccdjh.com/")
        m.name="flamingo"
        m.author="ccdjh"
        m.put()
      elif g=="tropical":
        m.link=db.Link("http://www.ccdjh.com/")
        m.name="tropical"
        m.author="ccdjh"
        m.put()
      elif g=="ivory":
        m.link=db.Link("http://www.ccdjh.com/")
        m.name="ivory"
        m.author="ccdjh"
        m.put()
      elif g=="cerulean":
        m.link=db.Link("http://www.ccdjh.com/")
        m.name="cerulean"
        m.author="ccdjh"
        m.put()
      elif g=="cobalt":
        m.link=db.Link("http://www.ccdjh.com/")
        m.name="cobalt"
        m.author="ccdjh"
        m.put()
      else:
        i=int(g)
        c=Theme.get_by_id(i)
        m.link=c.link
        m.name=c.name
        m.author=c.author
        m.put()
    self.redirect(self.request.referer)
    
class ThemeReceiveb(CcdjhMarx): #old
  def post(self):
    g = self.request.get("th")
    i=int(g)
    c=Theme.get_by_id(i)
    o=ThemeTwo.all().get()
    if o is not None:
      o.link=c.link
      o.name=c.name
      o.author=c.author
      o.put()
    else:  
      m=ThemeTwo()
      m.link=c.link
      m.name=c.name
      m.author=c.author
      m.put()
    self.redirect(self.request.referer)
