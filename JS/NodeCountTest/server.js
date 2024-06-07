const express = require('express');
const app = express();
const port = 5000;

var count = 0;

app.set('view engine', 'ejs');
app.use(express.json());

app.listen(port, () => {
    console.log(`서버 실행중: http://localhost:${port}`);
});

app.get('/', (req, res) => {
    res.render('index', { count })
});

// countup API
app.put('/count', (req, res) => {
    count += 1;
    res.json({ count });
});

// change API
app.put('/change', (req, res) => {
    count = parseInt(req.body.count, 10);
    res.json({ count });
})

// reset API
app.delete('/reset', (req, res) => {
    count = 0;
    res.json({"result":"OK"});
});