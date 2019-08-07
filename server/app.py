# run.py
import os
from apis import create_app

if __name__ == '__main__':
    print(os.path.abspath('./settings.py'))
    app = create_app(config_file=os.path.abspath('./settings.py'))
    app.run(debug=True)