# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# Common Gateway Interface
import cgi 

class WebServerHandler(BaseHTTPRequestHandler):
    # manipulado todos os gets do servidor.
    def do_GET(self):
        # rota hello
        if self.path.endswith("/hello"):
             # sucess
            self.send_response(200)
            # enviando um cabeçalho dizendo que é um conteúdo html
            self.send_header('Content-type', 'text/html')
            # indica o fim do nosso cabeçalho de resposta
            self.end_headers()
            # Escrevendo a mensagem
            output = ""
            output += "<html><body>"
            output += "<h1>Hello!</h1>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
            return
        # rota ola
        if self.path.endswith("/hola"):
             # sucess
            self.send_response(200)
            # enviando um cabeçalho dizendo que é um conteúdo html
            self.send_header('Content-type', 'text/html')
            # indica o fim do nosso cabeçalho de resposta
            self.end_headers()
            # Escrevendo a mensagem
            output = ""
            output += "<html><body>"
            output += "<h1>&#161 Hola !</h1>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
            return
        else:
            # Caso nada seja encontrado.
            self.send_error(404, 'File Not Found: %s' % self.path)
    # Requisições posts
    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # cgi.parse_header - Analisa um cabeçalho do formulário HTML, tal 
            # como o tipo do conteúdo.
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                # le todos os campos
                fields = cgi.parse_multipart(self.rfile, pdict)
                # pega o conteúdo do campo message
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s" % port)
        # mantém o server conectado até que seja interrompido. 
        server.serve_forever() 
        # KeyboardInterrupt é o atalho para encerrar o terminal em python. ctrl + c
    except KeyboardInterrupt: 
        print(" ^C entered, stopping web server....")
        # desliga o servidor.
        server.socket.close() 

# Arqui executa o método principal quando é chamada a classe
if __name__ == '__main__':
    main()