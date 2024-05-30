const express = require('express');
const app = express();
const port = 5000;

var count = 0;

app.set('view engine', 'ejs');

app.listen(port, () => {
    console.log(`서버 실행중: http://localhost:{port}`);
});

app.get('/', (req, res) => {
    res.render('index', { count })
});

// countup API
app.put('/count', (req, res) => {
    req.json({count})
    count += 1;
    res.json({count});
});

// change API
const { id } = req.params;
const { value } = req.body;

if (parseInt(id, 10) === data.id) {
  data.value = value;
  res.status(200).json({ message: 'Data updated successfully', data });
} else {
  res.status(404).json({ message: 'Data not found' });
}

// reset API
app.delete('/reset', (req, res) => {
    count = 0;
    res.json({"result":"OK"});
});