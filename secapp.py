from flask import Flask,render_template
from collections.abc import Container
app=Flask(__name__)
@app.route('/')
def  index():
    return render_template('index.html')
try:
    # 👇️ using Python 3.10+
    from collections.abc import Container
except ImportError:
    # 👇️ using Python 3.10-
    from collections import Container
if __name__=='__main__':
    app.run(debug=True)
