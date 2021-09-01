from flask import render_template, request, Blueprint, redirect, url_for, Blueprint
from forum.models import Post
from flask_login import current_user
main = Blueprint('main', __name__)

@main.route('/')


@main.route('/guest_home', methods=['GET', 'POST'])
def guest_home():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
       return render_template("guest_home.html")


@main.route('/home')
def home():
    if current_user.is_authenticated:
      page = request.args.get('page', 1, type=int)
      posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=5)

      return render_template("home.html", posts=posts)
    else:
        return redirect(url_for('main.guest_home'))
