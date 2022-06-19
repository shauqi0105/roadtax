var mysql = require('mysql');
let con;
function connect() {
    con = mysql.createConnection({
        host: "localhost",
        user: "root",
        password: "root",
        database: "rakam"
    });

    con.connect(function (err) {
        if (err) throw err;
        console.log("Connected!");
    });
}

function login(username, password) {
    con.query(`SELECT username,password FROM login WHERE username="${username}" AND password="${password}"`, function (err, result, fields) {
        if (err) throw err;
        console.log(result);
        return result;
    });
}

module.exports = { connect, login }