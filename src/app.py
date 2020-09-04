from flask import Flask, render_template, request
from core import HHData


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def get_page():
    if request.method == 'POST':
        a = HHData(request.form['tag'])
        return render_template(
            'index.html',
            gist_titile_msk=['Город'] + list(a.moscow_ds.keys()),
            gist_val_msk=['Москва'] + list(a.moscow_ds.items()),
            gist_titile_reg=['Город'] + list(a.region_ds.keys()),
            gist_val_reg=['Регионы'] + list(a.region_ds.items())
        )

    return render_template(
        'get_req.html'
    )


app.run(port=8822, debug=True, host="0.0.0.0")
