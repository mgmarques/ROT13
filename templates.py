import os
import jinja2    # jinja.pocoo.org
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
				autoescape = True )

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):	
		self.render("rot13.html", rot="")

	def post(self):
		rot = ROT13(self.request.get("text"))
		self.render("rot13.html", rot = rot)


def ROT13 (s = ""):
    t  = ""
    
    for c in s:
        o = ord(c)
        if (o > 96 and o < 123):
            o += 13
            if (o > 122):
                o -= 26
        if (o > 64 and o < 91):
            o += 13
            if (o > 90):
                o -= 26
        t += chr(o)
                
    return t


app = webapp2.WSGIApplication([('/', MainPage),
			      ],
			     debug=True)
