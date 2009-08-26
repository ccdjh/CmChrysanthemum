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
        greetings = memcache.get("greetings")
        if greetings is not None:
            return greetings
        else:
            greetings = self.render_profile()
            if not memcache.add("greetings", greetings, 10):
                logging.error("Memcache set failed.")
            return greetings

    def render_profile(self):
      results = Profile.all().get()
      return results
    
class  DocPostM():
    def get_docpost(self):
        greetings = memcache.get("greetings")
        if greetings is not None:
            return greetings
        else:
            greetings = self.render_docpost()
            if not memcache.add("greetings", greetings, 10):
                logging.error("Memcache set failed.")
            return greetings

    def render_docpost(self):
      results = DocPost.all().order('-date')
      return results