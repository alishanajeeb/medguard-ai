from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# ─── APP INITIALIZE ───
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'medguard-secret-key-2024')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'medguard.db')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ─── EXTENSIONS ───
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login to access this page.'

# ─── DATABASE MODELS ───
class User(UserMixin, db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(150), unique=True, nullable=False)
    password   = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    checks     = db.relationship('RiskCheck', backref='user', lazy=True)

class RiskCheck(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    input_text     = db.Column(db.String(500), nullable=False)
    medicine       = db.Column(db.String(200))
    condition      = db.Column(db.String(200))
    risk_level     = db.Column(db.String(20))
    risks          = db.Column(db.Text)
    recommendation = db.Column(db.Text)
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

# ─── LOGIN MANAGER ───
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'error': 'unauthorized', 'redirect': '/login'}), 401
    return redirect(url_for('login'))

# ─── THIS IS THE KEY FIX ───
@app.before_request
def create_tables():
    db.create_all()

# ─── ROUTES ───
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checker')
@login_required
def checker():
    return render_template('checker.html')

@app.route('/analyze', methods=['POST'])
@login_required
def analyze():
    from ai.classifier import analyze_input
    if not request.is_json:
        return jsonify({'error': 'Invalid request'}), 400
    data       = request.get_json()
    user_input = data.get('text', '').strip()
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400
    try:
        result = analyze_input(user_input)
        check  = RiskCheck(
            user_id        = current_user.id,
            input_text     = user_input,
            medicine       = result.get('medicine'),
            condition      = result.get('condition'),
            risk_level     = result.get('risk_level'),
            risks          = str(result.get('risks')),
            recommendation = result.get('recommendation')
        )
        db.session.add(check)
        db.session.commit()
        return jsonify(result)
    except Exception as e:
        print(f"Analyze error: {e}")
        return jsonify({
            'risk_level':     'UNKNOWN',
            'medicine':       'Error',
            'condition':      'Error',
            'risks':          ['Server error — please try again'],
            'recommendation': 'Please refresh and try again.',
            'source':         'local'
        }), 500

@app.route('/dashboard')
@login_required
def dashboard():
    checks = RiskCheck.query.filter_by(
        user_id=current_user.id
    ).order_by(RiskCheck.created_at.desc()).all()
    total  = len(checks)
    high   = sum(1 for c in checks if c.risk_level == 'HIGH')
    medium = sum(1 for c in checks if c.risk_level == 'MEDIUM')
    low    = sum(1 for c in checks if c.risk_level == 'LOW')
    return render_template('dashboard.html',
                           checks=checks, total=total,
                           high=high, medium=medium, low=low)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name     = request.form.get('name')
        email    = request.form.get('email')
        password = request.form.get('password')
        if not name or not email or not password:
            flash('All fields are required.', 'danger')
            return redirect(url_for('register'))
        existing = User.query.filter_by(email=email).first()
        if existing:
            flash('Email already registered. Please login.', 'danger')
            return redirect(url_for('register'))
        try:
            hashed   = generate_password_hash(password)
            new_user = User(name=name, email=email, password=hashed)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            print(f"Register error: {e}")
            flash('Something went wrong. Please try again.', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email    = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            flash('Email and password required.', 'danger')
            return redirect(url_for('login'))
        try:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            flash('Invalid email or password.', 'danger')
        except Exception as e:
            print(f"Login error: {e}")
            flash('Something went wrong. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/test-analyze', methods=['POST'])
def test_analyze():
    from ai.classifier import analyze_input
    data       = request.get_json()
    user_input = data.get('text', '')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400
    result = analyze_input(user_input)
    return jsonify(result)

# ─── RUN ───
if __name__ == '__main__':
    app.run(debug=False)