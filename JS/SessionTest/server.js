const { render } = require('ejs');
const express = require('express');
const session = require('express-session'); // npm i express-session
const bcrypt = require('bcrypt');

const app = express();
const port = 3000;

const user_db = []

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true })); // FORM BODY 요청 받기

// express-session 설정
app.use(session({
  secret: 'your_secret_key', // 세션 암호화에 사용되는 키
  resave: false, // 세션이 수정되지 않아도 다시 저장할지 여부
  saveUninitialized: false, // 초기화되지 않은 세션을 저장할지 여부
  cookie: { maxAge: 60000 } // 쿠키의 유효 기간 설정 (밀리초 단위, 여기서는 1분)
}));

// 메인 화면
app.get('/', (req, res) => {
    const username = req.session.username;
    const loginUser = user_db.find(d => d.username == username)
    res.render('main', {loginUser});

})

// 로그인 로그아웃
app.get('/login', (req, res) => {
    res.render('join', {});
})

app.get('/logout', (req, res) => {
    req.session.destroy;
    res.redirect('/');
})

// 회원가입
app.get('/join', (req, res) => {
    res.render('join', {});
})

app.post('/join', async (req, res) => {
    const username = req.body.username;
    const pw = await bcrypt.hash(req.body.pw, 10);
    
    user_db.push({username, pw})

    res.redirect('/');
})

// 로그인 설정 예시
app.post('/login', async (req, res) => {
    
    const loginUser = user_db.find(d => d.username == req.body.username);
    const match = await bcrypt.compare(req.body.pw, loginUser.pw);

    if (match) {
        //로그인 성공
        res.session.username = req.body.username; 
        res.redirect('/');
    } else {
        //로그인 실패
        res.send('로그인 실패');
    }
})

// 세션 설정 예시
app.get('/set-session', (req, res) => {
  req.session.username = 'FirstCoding';
  res.send('세션 설정됨');
});

// 세션 읽기 예시
app.get('/get-session', (req, res) => {
  const username = req.session.username;
  if (username) {
    res.send(`저장된 세션: ${username}`);
  } else {
    res.send('설정된 세션 없음');
  }
});

// 세션 삭제 예시
app.get('/clear-session', (req, res) => {
  req.session.destroy(err => {
    if (err) {
      return res.send('세션 삭제 오류.');
    }
    res.send('세션 삭제됨.');
  });
});

app.listen(port, () => {
  console.log(`서버 실행 중: http://localhost:${port}`);
});
