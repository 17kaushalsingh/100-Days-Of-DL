## Download dataset locally
- Run in terminal
    - `mkdir -p ~/.kaggle`
    - `cp ../kaggle.json ~/.kaggle/`
- Run in notebook
    - `!kaggle datasets download -d salader/dogs-vs-cats`
- Unzip the downloaded file

## Download dataset in Colab
- Upload the kaggle.json in root content directory
- Run in notebook
    - `!mkdir -p ~/.kaggle`
    - `!cp kaggle.json ~/.kaggle/`
    - `!kaggle datasets download -d salader/dogs-vs-cats`
- Unzip the downloaded 
```python
import zipfile
Zipref = zipfile.ZipFile('/content/dogs-vs-cats.zip', 'r')
Zipref.extractall('/content')
Zipref.close