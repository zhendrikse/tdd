var express = require('express'),
    bodyParser = require('body-parser'),
    app     = express();
const path = require('path');
const PORT = 3000;
const { validator } = require('./src/helpers');

var app = express();

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())

app.use(express.static(__dirname));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.post('/submitform', (req, res) => {
  const messages = validator(req.body);

  if (Object.keys(messages).length > 0)
    return res.status(433).send(messages);
  return res.send('Thank you for subscribing');
});

app.listen(PORT, (error) => {
  if (!error)
    console.log(
      'Server is Successfully Running, and App is listening on port ' + PORT
    );
  else console.log("Error occurred, server can't start", error);
});
