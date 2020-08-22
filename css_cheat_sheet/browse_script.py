import ui,os
from urllib.parse import urljoin
#file_path = 'index.html'
#file_path = urljoin('file://', os.path.abspath(file_path))
file_path = os.path.abspath('index.html')
w = ui.WebView()
w.load_url(file_path)
w.present()

