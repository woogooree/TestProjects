const express = require('express');
const mysql = require('mysql2');
const app = express();
const port = 4000;


// ejs 렌더링 엔진 사용
app.set('view engine', 'ejs');
//html form 데이터 처리에 사용
app.use(express.urlencoded({extended : true}));

// MySQL 연결 설정
const connection = mysql.createConnection({
    host: 'localhost',
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


app.listen(port, () => {
    console.log(`Server running on port ${port}`);
})

// 메인 페이지
app.get('/', (요청, 응답) => {
    응답.sendFile(__dirname + '/index.html');
})

// 댓글 페이지 로드
app.get('/comments', (요청, 응답) => {
    // 응답.sendFile(__dirname + '/comments.html');
    const sql = 'SELECT * FROM comment order by no desc';

    connection.query(sql, (err, results) => {
        if (err) {
            console.error('데이터베이스 오류:', err);
            return 응답.status(500).send('서버 오류');
        }
        응답.render('comments', {comments : results })
    });
})

// 댓글 수정 화면 (GET)
app.get('/comments/:id', (요청, 응답) => {
    const sql = 'SELECT * FROM comment WHERE no = ?';
    const id = [요청.params.id];

    connection.query(sql, id, (err, results) => {
        if (err) {
            console.error('데이터베이스 오류:', err);
            return 응답.status(500).send('서버 오류');
        }
        응답.render('edit', { comments : results })
    });
})

// 댓글 수정 API (PUT, JSON으로 받기)
app.put('/api/comments/:no', express.json(), (요청, 응답) => {
    console.log(요청.body);

    응답.send('ok');
})

// 댓글 페이지 API
app.get('/api/comments', (요청, 응답) => {
    const sql = 'SELECT * FROM comment order by no desc';

    connection.query(sql, (err, results) => {
        if (err) {
            console.error('데이터베이스 오류:', err);
            return 응답.status(500).send('서버 오류');
        }
        응답.json({ comments : results });
    });
})

// 댓글 등록 데이터 처리
app.post('/comments', (요청, 응답) => {

    // mysql insert
    const sql = 'INSERT INTO comment (nickname, comment) VALUES (?, ?)';
    const values = [요청.body.nickname, 요청.body.comment];

    connection.query(sql, values, (err, result) => {
        if (err) {
            console.error('데이터베이스 오류:', err);
            return 응답.status(500).send('서버 오류');
        }
        응답.redirect('/comments');
    });
})

// 댓글 삭제 API

app.delete('/api/comments/:id', (요청, 응답) => {
    const sql = 'DELETE FROM comment WHERE no = ?';
    const id = [요청.params.id];
    
    connection.query(sql, id, (err, results) => {
        if (results.affectedRows == 0) {
            응답.status(500).json({"result":"FAIL"})
        }
        if (err) {
            console.error('데이터베이스 오류:', err);
            return 응답.status(500).send('서버 오류');
        }
        응답.json({"result" : "OK"});
    });
})

