const express = require('express');
const session = require('express-session');
const mysql = require('mysql2');
const app = express();
const bcrypt = require('bcrypt');
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

// express-session 설정
app.use(session({
    secret: 'your_secret_key', // 세션 암호화에 사용되는 키
    resave: false, // 세션이 수정되지 않아도 다시 저장할지 여부
    saveUninitialized: false, // 초기화되지 않은 세션을 저장할지 여부
    cookie: { maxAge: 3600 * 1000 } // 쿠키의 유효 기간 설정 (밀리초 단위)
  }));

app.get('/', (req, res) => {
    connection.query(`SELECT no, title, reg_user_id, user.nickname, DATE_FORMAT(reg_dt, '%Y-%m-%d %H-%i:%s') as regdt
        FROM post
        JOIN user ON user.id = post.reg_user_id
        ORDER BY no DESC`, 
        function(err, posts) {
            res.render('index', { posts, user: req.session.user });
        })
    
});

app.get('/join', (req, res) => {
    res.render('join', {});
});

// 회원 등록
app.post('/join', async (req, res) => {

    const newData = req.body;

    const heshedPassword = await bcrypt.hash(req.body.pw, 10);

    const sql = 'INSERT INTO `db_comm`.`user` \
    (`id`,`pw`, `nickname`, `email`, `level`) VALUES (?, ?, ?, ?, 1)';

    const values = [newData.id, heshedPassword, newData.nickname, newData.email];

    connection.query(sql, values, (err, result) => {
        if (err) {
            console.error('데이터베이스 오류:', err);
            res.status(500).send('서버 오류');
            return;
        }

        const resultHtml = `<script>
        alert('회원 등록이 완료됨'); location.href = '/'; </script>`;
        res.send(resultHtml);
    });
});

// 로그인 페이지
app.get('/login', function(req, res) {
    res.render('login', {});
});

// 세션 로그인 구현
app.post('/login', function(req, res) {
    // id에 해당하는 유저 정보를 db에서 꺼내기
    const sql = `SELECT * FROM user WHERE id = ?`;
    const user = connection.query(sql, [req.body.id], function(err, user) {
        // db 쿼리 에러 처리
        if(err) {
            console.error('로그인 오류 :', err)
            return res.status(403).send('오류 발생');
        }

        // 없는 정보 에러 처리
        if (!user || user.length === 0) {
            return res.status(403).send(`<script>alert('사용자 정보를 찾을 수 없습니다.'); location.href='/login';</script>`);
        }

        user = user[0];

        // 로그인pw, 유저 정보의 hash된 pw 검증
        if (bcrypt.compareSync(req.body.pw, user.pw)) {
            req.session.user = user;
            res.redirect('/');
        } else {
            return res.status(403).send(`<script>alert('사용자 정보를 찾을 수 없습니다.'); location.href='/login';</script>`);
        }
    });

});

// 로그아웃
app.get('/logout', function(req, res) {
    req.session.destroy(function(){
        res.redirect('/');
    });
});

// 글 작성 페이지
app.get('/form', function(req, res) {
    res.render('form');
});

//글 작성 처리
app.post('/post', function(req, res) {
    // req.body.subject title content
    const newPost = req.body;

    const sql = 'INSERT INTO `db_comm`. `post` \
    (`subject`, `title`, `content`, `reg_dt`, `reg_user_id`) VALUES (?, ?, ?, now(), ?)';

    const values = [newPost.subject, newPost.title, newPost.connect, req.session.user.id];

    connection.query(sql, values, (err, result) => {
        if (err) {
            console.error('데이터베이스 오류:', err);
            res.status(500).send('서버 오류');
            return;
        }
        const resultHtml = `<script>
        alert('글 작성이 완료됨'); location.href = '/'; </script>`;
        res.send(resultHtml);
    });

});

//글 삭제 처리
app.post('/delete', function(req, res) {
    // session 유저 = 게시글 작성자 일 경우만 삭제하는 기능
    const userid = req.session.user.id;

    connection.query(`DELETE FROM post WHERE no = ? AND reg_user_id = ?`,
        [req.body.no], function(err, result) {
            res.redirect('/');
    })
})

// 게시글 조회
app.get('/posts/:no', function(req, res) {
    const no = req.params.no;
    connection.query(`SELECT * FROM post WHERE no = ?`, [no], function(err, post) {
        res.render('detail', {post: post[0]});
    });
});

app.listen(port, () => {
    console.log("서버 실행중");
});