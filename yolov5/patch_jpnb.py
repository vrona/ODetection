import torch
from IPython.display import Image, clear_output  # to display images
from utils.google_utils import gdrive_download  # to download models/datasets
from tensorboard import program


clear_output()
print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

tb = program.TensorBoard()
tb.configure(argv=[None, '--logdir', '/runs'])
url = tb.launch()
