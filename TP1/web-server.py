import sys
import BaseHTTPServer
import SimpleHTTPServer
import socket
import time
import psycopg2


from urlparse import urlparse

ip = sys.argv[1]

def SplitParam(param):
        split_param = param.split('=')
        if len(split_param) != 2:
          return ['', '']
        return split_param

class MyServer(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(self):
    record = ""
    try:
      connection = psycopg2.connect(user="postgres",
                                    password="mypass",
                                    host=ip,
                                    port="5432",
                                    database="inf8480")
      cursor = connection.cursor()
      # Print PostgreSQL Connection properties
      print (connection.get_dsn_parameters(), "\n")
      # Print PostgreSQL version
      cursor.execute("SELECT matricule, name FROM etudiants;")
      record = cursor.fetchone()
      print("You are connected to - ", record, "\n")
    except (Exception, psycopg2.Error) as error:
      print ("Error while connecting to PostgreSQL", error)
    finally:
      # closing database connection.
      if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    query = urlparse(self.path).query
    query_params = dict(SplitParam(param) for param in query.split('&'))

    if 'nom' not in query_params:
      query_params['nom'] = 'Inconnu'
    nom = query_params['nom']

    time.sleep(0.5)

    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write('<h1> It Works ! </h1>  <p style="font-family: sans-serif;"> Vous venez de reussir a installer un serveur web : ' + socket.gethostname() + '.<br>')

    self.wfile.write('Et de le connecter a une base de donnee dont voici un enregistrement : ' + str(record) + "</p>")

    self.wfile.write('<img src="https://www.polymtl.ca/profiles/portail/themes/custom/bueno/logo.png"> ')

    return

server = BaseHTTPServer.HTTPServer
server_address = ('', 8080)

MyServer.protocol_version = 'HTTP/1.0'
httpd = server(server_address, MyServer)

sa = httpd.socket.getsockname()
print('Serveur actif a ', sa[0], 'port', sa[1])
httpd.serve_forever()
