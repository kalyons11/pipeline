import os

from buzz import app

app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
