import os

from flask import Flask, render_template, flash, request, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename, redirect
from forms import *

base_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = base_path+'\\static\\img\\uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/ferret_isms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'DontTellAnyone'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'ferret.isms@gmail.com',
    "MAIL_PASSWORD": 'P@55w0rd1'
}

app.config.update(mail_settings)
mail = Mail(app)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    image_name = db.Column(db.String(50))
    adopt = db.relationship('AdoptionList', backref='cat')
    adopl = db.relationship('AdoptList', backref='catery')
    foster = db.relationship('FosterList', backref='catry')
    adoplc = db.relationship('AdoptListConfirm', backref='catery1')
    fosterc = db.relationship('FosterListConfirm', backref='catry1')


class AdoptionList(db.Model):
    __tablename__ = 'adoption'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shelter_ferret_name = db.Column(db.String(240), unique=True)
    shelter_name = db.Column(db.String(120))
    zip_code = db.Column(db.String(20))
    ferret_name = db.Column(db.String(120))
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # cat = relationship(Category, backref=backref("categories", uselist=False))
    Bonded = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    health_knowledge = db.Column(db.String(10))
    health_knowledge_status = db.Column(db.String(100))
    images = db.Column(db.String(500))
    about = db.Column(db.String(500))
    vaccinated = db.Column(db.String(10))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    things = db.Column(db.String(120))


class AdoptList(db.Model):
    __tablename__ = 'adopt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ferret_owner_name = db.Column(db.String(240), unique=True)
    ferret_name = db.Column(db.String(120))
    catery_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # cat = relationship(Category, backref=backref("categories", uselist=False))
    bonded = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    health_knowledge = db.Column(db.String(10))
    health_knowledge_status = db.Column(db.String(100))
    images = db.Column(db.String(500))
    about = db.Column(db.String(500))
    vaccinated = db.Column(db.String(10))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    surrender_in = db.Column(db.Integer)
    things = db.Column(db.String(120))


class FosterList(db.Model):
    __tablename__ = 'foster'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ferret_owner_name = db.Column(db.String(240), unique=True)
    ferret_name = db.Column(db.String(120))
    catery_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # cat = relationship(Category, backref=backref("categories", uselist=False))
    bonded = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    health_knowledge = db.Column(db.String(10))
    health_knowledge_status = db.Column(db.String(100))
    images = db.Column(db.String(500))
    about = db.Column(db.String(500))
    vaccinated = db.Column(db.String(10))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    surrender_in = db.Column(db.Integer)
    things = db.Column(db.String(120))


class AdoptListConfirm(db.Model):
    __tablename__ = 'adopt_confirm'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ferret_owner_name = db.Column(db.String(240), unique=True)
    ferret_name = db.Column(db.String(120))
    catery_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # cat = relationship(Category, backref=backref("categories", uselist=False))
    bonded = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    health_knowledge = db.Column(db.String(10))
    health_knowledge_status = db.Column(db.String(100))
    images = db.Column(db.String(500))
    about = db.Column(db.String(500))
    vaccinated = db.Column(db.String(10))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    surrender_in = db.Column(db.Integer)
    things = db.Column(db.String(120))


class FosterListConfirm(db.Model):
    __tablename__ = 'foster_confirm'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ferret_owner_name = db.Column(db.String(240), unique=True)
    ferret_name = db.Column(db.String(120))
    catery_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # cat = relationship(Category, backref=backref("categories", uselist=False))
    bonded = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    health_knowledge = db.Column(db.String(10))
    health_knowledge_status = db.Column(db.String(100))
    images = db.Column(db.String(500))
    about = db.Column(db.String(500))
    vaccinated = db.Column(db.String(10))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    surrender_in = db.Column(db.Integer)
    things = db.Column(db.String(120))


@app.route("/")
def home():
    return render_template('index.html')


@app.before_first_request
def setup_all():
    db.create_all()


@app.route("/available_for_adopt")
def available_for_adopt():
    data = []
    data1 = []
    dat = AdoptList.query.order_by('surrender_in').all()
    for da in dat:
        nam = da.images
        nam = nam.replace("[", '')
        nam = nam.replace("]", '')
        nam = nam.replace("'", '')
        nam = nam.replace(" ", '')
        img_name = nam.split(",")
        f_cat = Category.query.filter_by(id=da.catery_id).first()
        dic = {'images': img_name, 'ferret_category': f_cat.name, 'ferret_owner_name': da.ferret_owner_name,
               'health_knowledge': da.health_knowledge, 'ferret_name': da.ferret_name, 'gender': da.gender,
               'age': da.age, 'email': da.email, 'about': da.about}
        data.append(dic)
    dat1 = AdoptionList.query.all()
    for da1 in dat1:
        nam = da1.images
        nam = nam.replace("[", '')
        nam = nam.replace("]", '')
        nam = nam.replace("'", '')
        nam = nam.replace(" ", '')
        img_name = nam.split(",")
        f_cat = Category.query.filter_by(id=da1.cat_id).first()
        dic1 = {'images': img_name, 'ferret_category': f_cat.name, 'shelter_ferret_name': da1.shelter_ferret_name,
               'health_knowledge': da1.health_knowledge, 'ferret_name': da1.ferret_name, 'gender': da1.gender,
               'age': da1.age, 'email': da1.email, 'about': da1.about}
        data1.append(dic1)
    return render_template('available_for_adopt.html', data=data, data1=data1, act='afa')


@app.route("/adopt_detail")
def adopt_detail():
    id_get = request.args.get('v')
    data = AdoptList.query.filter_by(ferret_owner_name=id_get).first()
    f_cat = Category.query.filter_by(id=data.catery_id).first()
    ferret_category = f_cat.name
    nam = data.images
    nam = nam.replace("[", '')
    nam = nam.replace("]", '')
    nam = nam.replace("'", '')
    nam = nam.replace(" ", '')
    img_name = nam.split(",")
    return render_template('adopt_detailed.html', data=data, ferret_category=ferret_category, images=img_name, act='afa')


@app.route("/foster_detail")
def foster_detail():
    id_get = request.args.get('v')
    data = FosterList.query.filter_by(ferret_owner_name=id_get).first()
    f_cat = Category.query.filter_by(id=data.catery_id).first()
    ferret_category = f_cat.name
    nam = data.images
    nam = nam.replace("[", '')
    nam = nam.replace("]", '')
    nam = nam.replace("'", '')
    nam = nam.replace(" ", '')
    img_name = nam.split(",")
    return render_template('foster_detailed.html', data=data, ferret_category=ferret_category, images=img_name, act='aff')


@app.route("/available_for_foster")
def available_for_foster():
    data = []
    data1 = []
    dat = FosterList.query.order_by('surrender_in').all()
    for da in dat:
        nam = da.images
        nam = nam.replace("[", '')
        nam = nam.replace("]", '')
        nam = nam.replace("'", '')
        nam = nam.replace(" ", '')
        img_name = nam.split(",")
        f_cat = Category.query.filter_by(id=da.catery_id).first()
        dic = {'images': img_name, 'ferret_category': f_cat.name, 'ferret_owner_name': da.ferret_owner_name,
               'health_knowledge': da.health_knowledge, 'ferret_name': da.ferret_name, 'gender': da.gender,
               'age': da.age, 'email': da.email, 'about': da.about}
        data.append(dic)
    dat1 = AdoptionList.query.all()
    for da1 in dat1:
        nam = da1.images
        nam = nam.replace("[", '')
        nam = nam.replace("]", '')
        nam = nam.replace("'", '')
        nam = nam.replace(" ", '')
        img_name = nam.split(",")
        f_cat = Category.query.filter_by(id=da1.cat_id).first()
        dic1 = {'images': img_name, 'ferret_category': f_cat.name, 'shelter_ferret_name': da1.shelter_ferret_name,
                'health_knowledge': da1.health_knowledge, 'ferret_name': da1.ferret_name, 'gender': da1.gender,
                'age': da1.age, 'email': da1.email, 'about': da1.about}
        data1.append(dic1)
    return render_template('available_for_foster.html', data=data, data1=data1, act='aff')


@app.route("/form", methods=['GET', 'POST'])
def form():
    data = Category.query.filter_by(id=5).first()


@app.route("/confirm_foster", methods=['GET', 'POST'])
def confirm_foster():
    id_get = request.args.get('v')
    data = FosterList.query.filter_by(ferret_owner_name=id_get).first()
    check_data = FosterListConfirm.query.filter_by(ferret_owner_name=id_get).first()
    if check_data:
        flash("This request is already sent to admin please wait for response")
    else:
        data1 = FosterListConfirm(ferret_owner_name=data.ferret_owner_name, ferret_name=data.ferret_name, catery_id=data.catery_id, bonded=data.bonded, gender=data.gender,
                                  age=data.age, health_knowledge=data.health_knowledge, health_knowledge_status=data.health_knowledge_status, images=data.images, about=data.about,
                                  vaccinated=data.vaccinated, email=data.email, phone=data.phone, surrender_in=data.surrender_in, things=data.things)
        db.session.add(data1)
        db.session.commit()
        msg = Message(subject="Order Confirmation",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[data.email],
                      body="Some one is interesting to foster a ferret, please see your email and let's confirm.")
        mail.send(msg)
    return redirect(url_for('available_for_foster'))


@app.route("/confirm_adopt", methods=['GET', 'POST'])
def confirm_adopt():
    id_get = request.args.get('v')
    data = AdoptList.query.filter_by(ferret_owner_name=id_get).first()
    check_data = AdoptListConfirm.query.filter_by(ferret_owner_name=id_get).first()
    if check_data:
        flash("This request is already sent to admin please wait for response")
    else:
        data1 = AdoptListConfirm(ferret_owner_name=data.ferret_owner_name, ferret_name=data.ferret_name, catery_id=data.catery_id, bonded=data.bonded, gender=data.gender,
                                 age=data.age, health_knowledge=data.health_knowledge, health_knowledge_status=data.health_knowledge_status, images=data.images, about=data.about,
                                 vaccinated=data.vaccinated, email=data.email, phone=data.phone, surrender_in=data.surrender_in, things=data.things)
        db.session.add(data1)
        db.session.commit()
        msg = Message(subject="Order Confirmation",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[data.email],
                      body="Some one is interesting to adopt a ferret, please see your email let's confirm us with sending email of interested person to update the record.")
        mail.send(msg)
    return redirect(url_for('available_for_adopt'))


@app.route("/up_for_adoptions", methods=['GET', 'POST'])
def up_for_adoptions():
    adop_form = AdoptionForm()
    if request.method == 'POST':
        if adop_form.validate_on_submit():
            shelter_ferret_name = adop_form.shelter_name.data + '_' + adop_form.ferret_name.data
            f = request.files.getlist("image")
            image_array = []
            for file in f:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_array.append(filename)
            data = AdoptionList(shelter_ferret_name=shelter_ferret_name, shelter_name=adop_form.shelter_name.data, zip_code=adop_form.zip_code.data,
                                ferret_name=adop_form.ferret_name.data, cat_id=adop_form.ferret_category.data, Bonded=adop_form.bonded.data,
                                gender=adop_form.gender.data, age=adop_form.age.data, health_knowledge=adop_form.health.data, health_knowledge_status=adop_form.health_details.data,
                                images=str(image_array), about=adop_form.about_ferret.data, vaccinated=adop_form.vaccinated.data, email=adop_form.shelter_email.data,
                                phone=adop_form.shelter_phone_no.data, things=adop_form.ferret_things.data)
            db.session.add(data)
            db.session.commit()
            flash('Shelter data insert successfully')
            return redirect(url_for('up_for_adoptions'))
        else:
            flash('Some thing went wrong')
    return render_template('up_for_adoptions.html', form=adop_form, act='ufa')


@app.route("/surrendering_ferret", methods=['GET', 'POST'])
def surrendering_ferret():
    sur_form = SurrenderForm()
    if request.method == 'POST':
        if sur_form.validate_on_submit():
            ferret_owner_name = sur_form.ferret_name.data + '_' + sur_form.owner_email.data
            f = request.files.getlist("image")
            image_array = []
            for file in f:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_array.append(filename)
            data1 = FosterList(ferret_owner_name=ferret_owner_name, ferret_name=sur_form.ferret_name.data, catery_id=sur_form.ferret_category.data,
                               bonded=sur_form.bonded.data, gender=sur_form.gender.data, age=sur_form.age.data, health_knowledge=sur_form.health.data,
                               health_knowledge_status=sur_form.health_details.data, images=str(image_array), about=sur_form.about_ferret.data, vaccinated=sur_form.vaccinated.data,
                               email=sur_form.owner_email.data, phone=sur_form.owner_phone_no.data, surrender_in=sur_form.surrender_in.data, things=sur_form.ferret_things.data)

            data2 = AdoptList(ferret_owner_name=ferret_owner_name, ferret_name=sur_form.ferret_name.data, catery_id=sur_form.ferret_category.data,
                              bonded=sur_form.bonded.data, gender=sur_form.gender.data, age=sur_form.age.data, health_knowledge=sur_form.health.data,
                              health_knowledge_status=sur_form.health_details.data, images=str(image_array), about=sur_form.about_ferret.data, vaccinated=sur_form.vaccinated.data,
                              email=sur_form.owner_email.data, phone=sur_form.owner_phone_no.data, surrender_in=sur_form.surrender_in.data, things=sur_form.ferret_things.data)
            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()
            flash('Surrendering data insert successfully')
            return redirect(url_for('surrendering_ferret'))
        else:
            flash('Some thing went wrong')
    return render_template('surrendering_ferrert.html', form=sur_form, act='sur')


@app.route("/about_ferret", methods=['GET', 'POST'])
def about_ferret():
    cat = Category.query.all()
    return render_template('about_ferret.html', data=cat)


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route("/admin_dashboard", methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if (email == 'admin@ferretsystem.com') and (password == 'Admin123'):
            return render_template('admin_dashboard.html')
        else:
            flash('Please enter valid login details')
            return redirect(url_for('login'))
    else:
        return render_template('admin_dashboard.html')


@app.route("/add_category", methods=['GET', 'POST'])
def add_category():
    caty = Category.query.all()
    cat_form = CategoryForm()
    if cat_form.validate_on_submit():
        file = cat_form.image.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data = Category(name=cat_form.name.data.encode('utf-8'), image_name=file.filename)
        db.session.add(data)
        db.session.commit()
        flash('Categories data insert successfully')
    else:
        flash('Something went wrong with modal form please check')
    return render_template('admin_add_category.html', form=cat_form, ca=caty)


@app.route("/update_cat", methods=['GET', 'POST'])
def update_cat():
    if request.method == 'POST':
        c_id = request.form['id_cat']
        c_name = request.form['category']
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        update_this = Category.query.filter_by(id=c_id).first()
        update_this.name = c_name
        update_this.image_name = filename
        db.session.commit()
        flash('Data updated successfully')
        return redirect(url_for('add_category'))


@app.route("/delete_cat/<string:id_data>", methods=['GET', 'POST'])
def delete_cat(id_data):
    delete_this = Category.query.filter_by(id=id_data).first()
    db.session.delete(delete_this)
    db.session.commit()
    flash('Data deleted successfully')
    return redirect(url_for('add_category'))


@app.route("/manage_adopt")
def manage_adopt():
    adopt = AdoptListConfirm.query.all()
    return render_template('admin_adopt.html', fos=adopt)


@app.route("/update_adopt<string:id_data>", methods=['GET', 'POST'])
def update_adopt(id_data):
    if request.method == 'POST':
        f_ferret = request.form['ferret_name']
        f_email = request.form['email']
        f_phone = request.form['phone']
        f_things = request.form['things']
        f_surrender_in = request.form['surrender_in']
        ferret_owner_name = f_ferret + '_' + id_data
        update_this = AdoptList.query.filter_by(ferret_owner_name=ferret_owner_name).first()
        ferret_owner_name_update = f_ferret + '_' + f_email
        update_this.ferret_owner_name = ferret_owner_name_update
        update_this.email = f_email
        if f_phone:
            update_this.phone = f_phone
        else:
            update_this.phone = None
        update_this.things = f_things
        update_this.surrender_in = f_surrender_in
        db.session.commit()
        delete_this = AdoptListConfirm.query.filter_by(ferret_owner_name=ferret_owner_name).first()
        db.session.delete(delete_this)
        db.session.commit()
        msg = Message(subject="Order Confirmation",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[f_email],
                      body="Thank you for showing interest in adoption of ferret, we approve your request and updated record.")
        mail.send(msg)
        flash('Data updated successfully')
        return redirect(url_for('manage_adopt'))


@app.route("/delete_adopt/<string:id_data>", methods=['GET', 'POST'])
def delete_adopt(id_data):
    delete_this = AdoptListConfirm.query.filter_by(id=id_data).first()
    db.session.delete(delete_this)
    db.session.commit()
    flash('Data deleted successfully')
    return redirect(url_for('manage_adopt'))


@app.route("/manage_foster")
def manage_foster():
    foster = FosterListConfirm.query.all()
    return render_template('admin_foster.html', fos=foster)


@app.route("/update_foster<string:id_data>", methods=['GET', 'POST'])
def update_foster(id_data):
    if request.method == 'POST':
        f_ferret = request.form['ferret_name']
        f_email = request.form['email']
        f_phone = request.form['phone']
        f_things = request.form['things']
        f_surrender_in = request.form['surrender_in']
        ferret_owner_name = f_ferret + '_' + id_data
        update_this = FosterList.query.filter_by(ferret_owner_name=ferret_owner_name).first()
        ferret_owner_name_update = f_ferret + '_' + f_email
        update_this.ferret_owner_name = ferret_owner_name_update
        update_this.email = f_email
        if f_phone:
            update_this.phone = f_phone
        else:
            update_this.phone = None
        update_this.things = f_things
        update_this.surrender_in = f_surrender_in
        db.session.commit()
        delete_this = FosterListConfirm.query.filter_by(ferret_owner_name=ferret_owner_name).first()
        db.session.delete(delete_this)
        db.session.commit()
        msg = Message(subject="Order Confirmation",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[f_email],
                      body="Thank you for showing interest in foster a ferret, we approve your request and updated record.")
        mail.send(msg)
        flash('Data updated successfully')
        return redirect(url_for('manage_foster'))


@app.route("/delete_foster/<string:id_data>", methods=['GET', 'POST'])
def delete_foster(id_data):
    delete_this = FosterListConfirm.query.filter_by(id=id_data).first()
    db.session.delete(delete_this)
    db.session.commit()
    flash('Data deleted successfully')
    return redirect(url_for('manage_foster'))


@app.route("/send_details", methods=['GET', 'POST'])
def send_details():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        msg = Message(subject="Ferret-Isms Contact Us",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[app.config.get("MAIL_USERNAME")],
                      body="Name : " + name + "\nEmail Address : " + email + "\nMessage : " + message)
        mail.send(msg)
        flash('Email send successfully')
    return redirect(url_for('contact_us'))


@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html')


@app.route("/ferret_fact", methods=['GET', 'POST'])
def ferret_fact():
    return render_template('fact_ferret.html')


if __name__ == "__main__":
   app.run(debug=True, port=8080)
#app.run((host='0.0.0.0', port=<8049>, debug=False)
