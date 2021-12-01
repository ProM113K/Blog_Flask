from blogs import app, conn
from flask import render_template, request, redirect


@app.route("/home")
def home_page():
    sql = "SELECT * FROM post ORDER BY idpost DESC"

    cursor = conn.cursor()
    cursor.execute(sql)

    artikel = cursor.fetchall()

    return render_template('index.html', artikel=artikel)

@app.route('/home/kategori/<_category>')
def category(_category):
    sql = "SELECT * FROM post WHERE keyword=%s"
    data = _category
    cursor = conn.cursor()
    cursor.execute(sql, data)

    artikel_cat = cursor.fetchall()

    return render_template('index.html', artikel=artikel_cat)


@app.route('/blog', methods=['GET', 'POST'])
def blog_page():
    # Mengubah data
    _idTemp = request.values.get('temp_id')
    _judul = request.values.get('judul')
    _isi = request.values.get('isi')
    _keyword = request.values.get('keyword')

    sql_ubah = "UPDATE post SET judul=%s, isi=%s, keyword=%s WHERE idpost=%s"
    data_ubah = (_judul,_isi, _keyword, _idTemp)
    cursor_ubah = conn.cursor()
    cursor_ubah.execute(sql_ubah, data_ubah)
    conn.commit()

    redirect('/blog')

    # Menampilkan data
    sql_tampil = "SELECT * FROM post ORDER BY idpost DESC"

    cursor_tampil = conn.cursor()
    cursor_tampil.execute(sql_tampil)

    artikel = cursor_tampil.fetchall()

    return render_template('blog.html', artikel=artikel)


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

        print(data)

        return redirect('/blog')
    else:
        return render_template('blog.html')
