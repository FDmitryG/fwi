from flask import Flask, render_template, request, url_for, redirect
from firewall_api import FireWall

app = Flask(__name__)

action = FireWall()


@app.route("/")
def home():
    list_of_chains = action.get_chains()
    return render_template("home.html", list_of_chains=list_of_chains)


@app.route("/chain", methods=['GET', 'POST'])
def chain_page():
    chain = None
    list_of_chains = action.get_chains()
    if request.method == 'GET':
        chain = request.args.get('chain')

    full_output = action.get_chain_data(chain)
    chain_name = full_output[0]
    row = full_output[1]
    return render_template("chain.html", list_of_chains=list_of_chains, chain_name=chain_name,
                           row=row, chain=chain)


@app.route("/add_rule", methods=['GET', 'POST'])
def add_rule():
    chain = request.form['chain']
    new_rule_rs = request.form['new_rule_rs']
    new_rule_prot = request.form['new_rule_prot']
    new_rule_dport = request.form['new_rule_dport']
    new_rule_address = request.form['new_rule_address']
    new_rule_action = request.form['new_rule_action']

    action.add_rule(chain, new_rule_rs, new_rule_prot, new_rule_dport, new_rule_address, new_rule_action)
    return redirect(url_for('chain_page', chain=chain))


@app.route("/delete_rule", methods=['GET'])
def delete_rule():
    rul_number = request.args.get('rul_number')
    chain = request.args.get('chain')

    action.del_rule(chain, rul_number)
    return redirect(url_for('chain_page', chain=chain))


@app.route("/create_chain", methods=['GET', 'POST'])
def create_chain():
    if request.method == 'POST':
        new_chain_name = request.form['new_chain_name']
        action.add_chain(new_chain_name)
        return redirect(url_for('home'))

    list_of_chains = action.get_chains()
    return render_template("create_chain.html", list_of_chains=list_of_chains)

@app.route("/delete_chain", methods=['GET', 'POST'])
def delete_chain():
    del_chain_name = request.form['del_chain_name']
    action.del_chain(del_chain_name)
    return redirect(url_for('home'))


@app.route("/help")
def help_page():
    list_of_chains = action.get_chains()
    ipt_help = action.get_help
    return render_template("help.html", list_of_chains=list_of_chains, help=ipt_help)


@app.route("/export")
def export():
    action.export_conf()
    return redirect("#")



if __name__ == "__main__":
    app.run(debug=True)
