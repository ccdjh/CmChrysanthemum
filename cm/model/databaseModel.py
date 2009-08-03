from google.appengine.ext import db

class DocPost(db.Model):
    title = db.StringProperty()
    content = db.TextProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    author = db.UserProperty()
    idc = db.IntegerProperty()
    tags = db.StringListProperty()
    commentcount = db.IntegerProperty(default=0)
    
class DocComment(db.Model):
      contact = db.ReferenceProperty(DocPost,collection_name='post_comment')
      comment = db.TextProperty()
      date = db.DateTimeProperty(auto_now_add=True)

class DocTag(db.Model):
    tag = db.StringProperty(multiline=False)
    tagcount = db.IntegerProperty(default=1)