# run.py
import os
from apis import create_app
# for >flask run
if __name__ == '__main__':
    #print(os.path.abspath('./settings.py'))
    app = create_app()
    app.run(debug=True)