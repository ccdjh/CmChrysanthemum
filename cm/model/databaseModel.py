from google.appengine.ext import db

class DocPost(db.Model):
    title = db.StringProperty()
    content = db.TextProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    author = db.UserProperty()
    idc = db.IntegerProperty()
    tags = db.ListProperty(db.Category)
    commentcount = db.IntegerProperty(default=0)
    
class DocComment(db.Model):
      contact = db.ReferenceProperty(DocPost,collection_name='post_comment')
      comment = db.TextProperty()
      date = db.DateTimeProperty(auto_now_add=True)
      idc = db.IntegerProperty()
      author = db.EmailProperty()
      postid = db.IntegerProperty()
      image = db.StringProperty()

class DocTag(db.Model):
    tag = db.StringProperty(multiline=False)
    tagcount = db.IntegerProperty(default=1)
    
class Profile(db.Model):
    name = db.StringProperty()
    about = db.TextProperty()
    avatar = db.BlobProperty()
    idc = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty()
    description = db.StringProperty()
    
class ListYou(db.Model):
    name = db.StringProperty(multiline=False)
    link = db.LinkProperty()
    idc = db.IntegerProperty()