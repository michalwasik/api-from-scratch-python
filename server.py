from flask import render_template, request, Flask
from model import Track, Data, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()
app=Flask(__name__)

def show_track(track):
    item = session.query(Track).filter_by(slugname=track).first()
    return render_template('track_data.html', track_name=item.name, data=sorted(item.stuff, key=lambda d: d.time))


@app.route('/track/<slug_name>', methods=['GET', 'POST'])
def track(slug_name):
    if request.method == 'POST':
        track_id = session.query(Track).filter_by(slugname=slug_name).first().id
        ride = Data(driver=request.form['driver'], time=request.form['time'].replace(',', '.'), car=request.form['car'], track_id=track_id, added = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        session.add(ride)
        session.commit()
    return show_track(slug_name)


@app.route('/')
def index():
    alldata=session.query(Track).all()
    return render_template('index.html', data=alldata)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)