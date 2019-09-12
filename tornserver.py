#!/usr/bin/python
import os
import tornado.ioloop
import tornado.web
import config_write
from config_write import sec1,sec2
conobj = config_write.config_writer()

class config_write(tornado.web.RequestHandler):

    	def get(self):

		action = self.get_argument('action')
        	website_hostname = self.get_argument('website_hostname')
        	website_ip = self.get_argument('website_ip')
		website_port = self.get_argument('website_port')
		waf_port = self.get_argument('waf_port')
		is_ssl_enabled = self.get_argument('is_ssl_enabled')
		server_pem = self.get_argument('server_pem')
		
		if action == "add":
			res = conobj.add(website_hostname,website_ip,website_port,waf_port,is_ssl_enabled,server_pem)

		self.write(res)
        	#self.write(website_hostname + "Added Successfully")

def make_app():
	return tornado.web.Application([(r"/config_write.py?", config_write),])

if __name__ == "__main__":
    app = make_app()
    app.listen(58080)
    tornado.ioloop.IOLoop.current().start()
