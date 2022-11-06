import bottle
import json
import chat
import map

@bottle.route('/')
def send_HTML():
  return bottle.static_file('index.html',root='.')


@bottle.route('/chat.js')
def send_chat_js():
  return bottle.static_file('chat.js',root='.')

@bottle.route('/ajax.js')
def ajax():
  return bottle.static_file('ajax.js',root='.')


@bottle.route('/chat')
def send_chat():
  messages=chat.getchat()
  return json.dumps(messages)

@bottle.post('/send')
def receive_chat():
  content=bottle.request.body.read().decode()
  content=json.loads(content)
  chat.add_message(content['message'])
  return send_chat()


@bottle.post('/map')
def send_coords():
  coords = map.getcoords()
  return json.dumps(coords)
  
@bottle.post('/mapsend')
def receive_coords():
  content=bottle.request.body.read().decode()
  content=json.loads(content)
  
  map.add_coords(content['latlong'])
  return send_coords()

bottle.run(host="0.0.0.0", port=8080)



