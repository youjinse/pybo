from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from app.forms import UserCreateForm
from app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        dup_user = User.query.filter_by(username=form.username.data).first()
        dup_email = User.query.filter_by(email=form.email.data).first()
        if dup_user or dup_email:
            if dup_user:
                flash('이미 존재하는 사용자입니다.')
            if dup_email:
                flash('이미 존재하는 email 입니다.')
        else:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
    return render_template('auth/signup.html', form=form)
