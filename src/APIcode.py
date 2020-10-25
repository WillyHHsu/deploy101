import pickle
import xgboost as xgb
from flask import Flask, request, json
import numpy as np

app = Flask(__name__)
#model =  pickle.load(open("model/creditas.pickle", "rb"))
bst = xgb.Booster({'nthread': 4})
model = bst.load_model('model/model.bst') 

@app.route('/')
def alive():
    return print('alive')

@app.route('/predict', methods = ['POST'])
def predict():
    
    data = request.get_json(force=True)
	
	#TODO pensar em uma forma de parsear 
    a = data['age']
    b=data['monthly_income']
    c=data['collateral_value']
    d=data['loan_amount']
    e=data['collateral_debt']
    f=data['verified_restriction']
    g=data['dishonored_checks']
    h=data['banking_debts']
    i=data['commercial_debts']
    j=data['form_completed']
    k=data['landing_page_bins_/emprestimo/garantia-veiculo']
    l=data['landing_page_bins_/emprestimos/solicitar']
    m=data['ratio_colaretal_loan']
    n=data['ratio_loan_income']
    o=data['ratio_payment_income']
    p=data['channel_affiliates']
    q=data['channel_direct']
    r=data['channel_display']
    s=data['channel_emailaffiliates']
    t=data['channel_search']
    
    params_list = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
    _ = np.array(params_list).reshape(1,20)
    result =  model.predict_proba(_)

    return json.dumps({'nao':float(result[0][0]),'sim': float(result[0][1])}, sort_keys=False)
    	
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
