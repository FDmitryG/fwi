from flask import Flask, request, render_template, abort, redirect
#import links_db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create_link():
    error = None
    message = None

    if request.method == 'POST':
        url = request.form['url']
        alias = request.form['alias']

        try:
            links_db.add_link(alias, url)
        except KeyError:
            error = 'Alias already exists'
        else:
            message = 'Link added'

    return render_template('help.html', error=error, success=message)


@app.route('/<alias>')
def goto(alias):
    try:
        url = links_db.get_link(alias)
    except KeyError:
        abort(404)

    return redirect(url)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)