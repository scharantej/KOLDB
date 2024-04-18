
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///koldb.sqlite'
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)

class KOL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    expertise = db.Column(db.String(120))
    contact = db.Column(db.String(120))

@app.route('/kol/profile/<int:kol_id>')
def kol_profile(kol_id):
    kol = KOL.query.get_or_404(kol_id)
    return render_template('kol_profile.html', kol=kol)

@app.route('/kol/list')
def kol_list():
    kols = KOL.query.all()
    return render_template('kol_list.html', kols=kols)

@app.route('/kol/create', methods=['GET', 'POST'])
def kol_create():
    if request.method == 'POST':
        name = request.form['name']
        expertise = request.form['expertise']
        contact = request.form['contact']
        new_kol = KOL(name=name, expertise=expertise, contact=contact)
        db.session.add(new_kol)
        db.session.commit()
        flash('New KOL created successfully.')
        return redirect(url_for('kol_list'))
    return render_template('kol_create.html')

@app.route('/kol/edit/<int:kol_id>', methods=['GET', 'POST'])
def kol_edit(kol_id):
    kol = KOL.query.get_or_404(kol_id)
    if request.method == 'POST':
        kol.name = request.form['name']
        kol.expertise = request.form['expertise']
        kol.contact = request.form['contact']
        db.session.commit()
        flash('KOL updated successfully.')
        return redirect(url_for('kol_profile', kol_id=kol_id))
    return render_template('kol_edit.html', kol=kol)

@app.route('/kol/delete/<int:kol_id>')
def kol_delete(kol_id):
    kol = KOL.query.get_or_404(kol_id)
    db.session.delete(kol)
    db.session.commit()
    flash('KOL deleted successfully.')
    return redirect(url_for('kol_list'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
