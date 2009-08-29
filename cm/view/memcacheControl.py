 #-*- coding: utf-8 -*-
import cgi
import datetime
import logging
import StringIO
from google.appengine.api import memcache

from cm.model.databaseModel import Profile
from cm.model.databaseModel import DocPost
logging.getLogger().setLevel(logging.DEBUG)
class  ProfileM():
    def get_profile(self):
        profiles = memcache.get("profiles")
        if profiles is not None:
            return profiles
        else:
            profiles = self.render_profile()
            if not memcache.add("profiles", profiles):
                logging.error("Memcache set failed.")
            return profiles

    def render_profile(self):
      results = Profile.all().get()
      return results
    
class  DocPostM():
    def get_docpost(self):
        docposts = memcache.get("docposts")
        if docposts is not None:
            return docposts
        else:
            docposts = self.render_docpost()
            if not memcache.add("docposts", docposts):
                logging.error("Memcache set failed.")
            return docposts

    def render_docpost(self):
      results = DocPost.all().order('-date')
      return results