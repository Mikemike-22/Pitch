from flask import render_template
from . import main
from ..models import Pitch
from .forms import PitchForm

# Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/pitches',methods= ['GET','POST'])
@login_required
def pitches_list():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.pitch_category.data 

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.pitches_list'))

        all_pitches = Pitch.get_all_pitches()

        title = 'Pitches Page'
        return render_template('Pitches.html',title = title, pitch_form = pitch_form, pitches = all_pitches)