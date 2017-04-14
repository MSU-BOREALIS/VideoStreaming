const http = require('http'),
      express = require('express')

const app = express()

require('./routes').forEach(routes => app.use(routes))

http.createServer(app).listen(8080, '0.0.0.0', () => {
  console.log('[eclipse-pi-http] Running on port 8080')
})
