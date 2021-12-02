from blogs import app, conn
from flask import render_template, request, redirect, url_for, flash

global session, pengguna
session = False
pengguna = ''


@app.route("/home")
def home_page():
    sql = "SELECT * FROM post ORDER BY idpost DESC"

    cursor = conn.cursor()
    cursor.execute(sql)

    artikel = cursor.fetchall()

    return render_template('index.html', artikel=artikel, session=session, pengguna=pengguna)


# @app.route('/session')
# def session_check():
#     if session != True:
#         return redirect(url_for('login_page'))


@app.route('/blog', methods=['GET', 'POST'])
def blog_page():
    # Mengubah data
    _idTemp = request.values.get('temp_id')
    _judul = request.values.get('judul')
    _isi = request.values.get('isi')
    _keyword = request.values.get('keyword')

    sql_ubah = "UPDATE post SET judul=%s, isi=%s, keyword=%s WHERE idpost=%s"
    data_ubah = (_judul, _isi, _keyword, _idTemp)
    cursor_ubah = conn.cursor()
    cursor_ubah.execute(sql_ubah, data_ubah)
    conn.commit()

    redirect('/blog')

    # Menampilkan data
    sql_tampil = "SELECT * FROM post ORDER BY idpost DESC"

    cursor_tampil = conn.cursor()
    cursor_tampil.execute(sql_tampil)

    artikel = cursor_tampil.fetchall()

    if session != True:
        return redirect(url_for('login_page'))

    else:
        return render_template('blog.html', artikel=artikel, session=session, pengguna=pengguna)


@app.route('/blog/hapus/<_id>')
def hapus_data(_id):
    sql = "DELETE FROM post WHERE idpost = %s"
    data = (_id)
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()

    return redirect('/blog')


@app.route('/blog/tambah', methods=['POST'])
def tambah_data():
    if request.method == 'POST':
        # Menambah data
        _judul = request.values.get('judul_post')
        _isi = request.values.get('isi_post')
        _keyword = request.values.get('keyword_post')

        sql = "INSERT INTO post VALUES (null, %s, %s, %s)"
        data = (_judul, _isi, _keyword)

        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()

        return redirect('/blog')
    else:
        return render_template('blog.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    _username = request.values.get('username')
    _password = request.values.get('password')

    if request.method == 'POST':
        sql = 'SELECT * FROM pengguna WHERE username=%s'

        cursor = conn.cursor()
        cursor.execute(sql, _username)
        hasil = cursor.fetchone()

        if _username == hasil[2] and _password == hasil[3]:
            global session, pengguna
            session = True
            pengguna = hasil[1]

            flash(f'Anda login sebagai {pengguna}', category='success')
            return redirect(url_for("home_page"))
        else:
            return 'Gagal'
    else:
        return render_template('login.html')


@app.route('/user')
def user_page():
    if session != True:
        return redirect(url_for('login_page'))

    else:
        return render_template('user.html', session=session, pengguna=pengguna)



@app.route('/logout')
def logout_session():
    global session
    session = False
    return redirect(url_for("home_page"))
