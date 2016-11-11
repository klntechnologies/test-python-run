import pandas
from bottle import route, run, request

@route('/TestRun')
def gettest():
    return '''
<form action='/getrun' metohd='POST'>
<input type='text' name='inputtext' size=20 />
<input type='submit' name='submit' />
</form>
'''

@route('/getrun')
def getdata():
    inputvalue=request.forms.get('inputtext')
    return inputvalue

run(host='0.0.0.0', port=8080, debug=True)
