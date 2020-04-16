import os
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import StringField, SelectField, RadioField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Optional, Email
from wtforms.widgets import TextArea
from apprun import Category


base_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = base_path+'\\static\\img\\uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=20)], render_kw={'placeholder': 'Enter ferret category'})
    image = FileField('Select images', validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS, 'Only png, jgep & jpg files allowed')], render_kw={'multiple': False},)


class AdoptionForm(FlaskForm):
    shelter_name = StringField('ShelterName', validators=[DataRequired(), Length(min=3, max=20)], render_kw={'placeholder': 'Enter shelter name'})
    zip_code = StringField('ZipCode', validators=[DataRequired(), Length(min=3, max=20)], render_kw={'placeholder': 'Enter zip code of shelter'})
    ferret_name = StringField('Ferret Name', validators=[DataRequired(), Length(min=3, max=20)], render_kw={'placeholder': 'Enter ferret name'})
    ferret_category = SelectField('Ferret Category', coerce=int, choices=[(cat.id, cat.name) for cat in Category.query.all()])
    bonded = RadioField('Bonded', choices=[('single', 'Single'), ('pair', 'Pair')], default='single')
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')], default='male')
    age = IntegerField('Age', validators=[DataRequired()], render_kw={'placeholder': 'Enter ferret age in years'})
    health = RadioField('Health Knowledge', choices=[('yes', 'Yes'), ('no', 'No')], default='yes')
    health_details = StringField('Health Details', validators=[Optional()], render_kw={'placeholder': 'Enter health details'})
    image = FileField('Select images', validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS, 'Only png, jgep & jpg files allowed')], render_kw={'multiple': True},)
    about_ferret = StringField('AboutFerret', widget=TextArea(), validators=[DataRequired(), Length(min=10, max=500)], render_kw={'placeholder': 'About the Ferret'})
    vaccinated = RadioField('Vaccinated', choices=[('yes', 'Yes'), ('no', 'No')], default='yes')
    shelter_email = EmailField('ShelterEmail', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Enter shelter Email Address'})
    shelter_phone_no = IntegerField('ShelterPhone', validators=[Optional()], render_kw={'placeholder': 'Enter phone number of shelter (optional)'})
    ferret_things = StringField('FerretThing', validators=[DataRequired(), Length(min=5, max=120)], render_kw={'placeholder': 'Things that come with the ferret'})


class SurrenderForm(FlaskForm):
    ferret_name = StringField('Ferret Name', validators=[DataRequired(), Length(min=3, max=20)], render_kw={'placeholder': 'Enter ferret name'})
    ferret_category = SelectField('Ferret Category', coerce=int, choices=[(catery.id, catery.name) for catery in Category.query.all()])
    bonded = RadioField('Bonded', choices=[('single', 'Single'), ('pair', 'Pair')], default='single')
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')], default='male')
    age = IntegerField('Age', validators=[DataRequired()], render_kw={'placeholder': 'Enter ferret age in years'})
    health = RadioField('Health Knowledge', choices=[('yes', 'Yes'), ('no', 'No')], default='yes')
    health_details = StringField('Health Details', validators=[Optional()], render_kw={'placeholder': 'Enter health details'})
    image = FileField('Select images', validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS, 'Only png, jgep & jpg files allowed')], render_kw={'multiple': True},)
    about_ferret = StringField('AboutFerret', widget=TextArea(), validators=[DataRequired(), Length(min=10, max=500)], render_kw={'placeholder': 'About the Ferret'})
    vaccinated = RadioField('Vaccinated', choices=[('yes', 'Yes'), ('no', 'No')], default='yes')
    owner_email = EmailField('OwnerEmail', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Enter your Email Address'})
    owner_phone_no = IntegerField('OwnerPhone', validators=[Optional()], render_kw={'placeholder': 'Enter your phone number (optional)'})
    surrender_in = SelectField('Surrender In (days)', coerce=int, choices=[(d, d) for d in range(1, 31)])
    ferret_things = StringField('FerretThing', validators=[DataRequired(), Length(min=5, max=120)], render_kw={'placeholder': 'Things that come with the ferret'})
