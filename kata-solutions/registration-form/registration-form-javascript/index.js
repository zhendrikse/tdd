var express = require('express'),
    app     = express(),
    port    = parseInt(process.env.PORT, 10) || 8080;
const path = require('path');
const { validator } = require('./src/helpers');

// app.configure(function(){
//   app.use(express.bodyParser());
// });

app.use(express.static(__dirname));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.post('/submitform', (req, res) => {
  console.log("Hier");
  console.log(req);
  console.log(req.body);
  const messages = validator(req.body);

  if (Object.keys(messages).length > 0)
    return res.send('Thank you for subscribing');
  return res.statusCode(433).json(messages);
});

app.listen(PORT, (error) => {
  if (!error)
    console.log(
      'Server is Successfully Running, and App is listening on port ' + PORT
    );
  else console.log("Error occurred, server can't start", error);
});
