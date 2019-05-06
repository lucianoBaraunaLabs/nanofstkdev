# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations
from database_setup import Base, Restaurant, Menuitem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Objetivo 3 - Criar novos restaurantes.
# Objetivo 4 - Renomear restaurantes.
# Objetivo 5 - Deletar restaurantes.
class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Objetivo 1 - Listar todos os restaurantes.
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"

                # Objetivo 3 - Criar novos restaurantes - Criando link para página.
                output += '''<a href='/restaurants/new'>Make new restaurant</a>'''
                # Objetivo 2 - Adicionar botões para editar e deletar links.
                for restaurant in restaurants:
                    output += "<p>"
                    output += restaurant.name
                    output += '<br />'
                    # Objetivo 4 - Editar dados - criando links para editar
                    output += "<a href ='/restaurants/%s/edit' >Edit&nbsp;&nbsp;</a> " % restaurant.id
                    # Objetivo 5 - Deletar dados - criando links para deletar
                    output += "<a href ='/restaurants/%s/delete'> Delete </a>" % restaurant.id
                    output += "</p>"
                    output += "<hr />"

                output += "</body></html>"
                self.wfile.write(output)
                return

            # Objetivo 3 - Criar novos restaurantes.
            if self.path.endswith("/restaurants/new"):
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name'> "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                output += "<a href='/restaurants'>Go back</a>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                 # Objetivo 4 - Editar restaurantes.
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                # Se retornar algo
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += myRestaurantQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/restaurants/%s/edit' >" % restaurantIDPath
                    output += "<input name = 'newRestaurantName' type='text' placeholder = '%s' >" % myRestaurantQuery.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
            # Objetivo 5 - Delete
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?" % myRestaurantQuery.name
                    output += "<form method='POST' enctype = 'multipart/form-data' action = '/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<input type = 'submit' value = 'Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)



        except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path)
    

    def do_POST(self):
        try:
            # Objetivo 5 - Deletar restaurante
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()

                if myRestaurantQuery:
                    session.delete(myRestaurantQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            # Objetivo 4 - Editando restaurante
            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]

                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    
                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = messagecontent[0]
                        session.add(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()
             
            # Objetivo 2 - Criar novos restaurantes.
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant
                    newRestaurante = Restaurant(name = messagecontent[0])
                    session.add(newRestaurante)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
        except:
            pass


def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()