var express = require('express'),
    bodyParser = require('body-parser'),
    app     = express();
const path = require('path');
const PORT = 3000;
const { validator } = require('./src/helpers');
const setRateLimit = require("express-rate-limit");

var app = express();

// Rate limit middleware
const rateLimitMiddleware = setRateLimit({
  windowMs: 60 * 1000,
  max: 5,
  message: "You have exceeded your 5 requests per minute limit.",
  headers: true,
});

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())

app.use(express.static(__dirname));

app.get('/', rateLimitMiddleware, (request, response) => {
  response.sendFile(path.join(__dirname + '/index.html'));
});
app.set('trust proxy', 1)

app.post('/submitform', rateLimitMiddleware, (request, response) => {
  const messages = validator(request.body);

  if (Object.keys(messages).length > 0)
    return response.status(433).send(messages);
  return response.send('Thank you for subscribing');
});

app.listen(PORT, (error) => {
  if (!error)
    console.log(
      'Server is Successfully Running, and App is listening on port ' + PORT
    );
  else console.log("Error occurred, server can't start", error);
});
