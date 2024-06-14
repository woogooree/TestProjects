const express = require('express');
const mysql = require('mysql2');
const app = express();
const port = 80;

// EJS 사용 설정
app.set('view engine', 'ejs');

// FORM POST 사용
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


// MySQL 연결 설정
const connection = mysql.createConnection({
    host: 'localhost', //DB 돌아가는 서버(PC) IP 주소
    user: 'root', // MySQL 사용자 이름
    password: '', // MySQL 비밀번호
    database: 'db_comm', // 사용할 데이터베이스 이름
    port: 4306,
});

// MySQL 연결
connection.connect((err) => {
    if (err) {
        console.error('MySQL 연결 실패:', err);
        return;
    }
    console.log('MySQL 연결 성공');
});

app.get('/', (req, res) => {
    posts = []; // todo : post목록 데이터를 조회해야함
    res.render('index', { posts });
});

app.get('/join', (req, res) => {
    res.render('join', {});
});

app.post('/join', (req, res) => {

    const newData = req.body;

    const sql = 'INSERT INTO `db_comm`.`user` \
    (`id`,`pw`, `nickname`, `email`, `level`) VALUES (?, ?, ?, ?, 1)';

    const values = [newData.id, newData.pw, newData.nickname, newData.email];

    connection.query(sql, values, (err, result) => {
        if (err) {
            console.error('데이터베이스 오류:', err);
            return res.status(500).send('서버 오류');
        }

        const resultHtml = `<script>
        alert('회원 등록이 완료됨');
        location.href = '/'; </script>`;
        res.send(resultHtml);
        res.status(201).send('Data added successfully');
    });
});

app.listen(port, () => {
    console.log("서버 실행중");
});
