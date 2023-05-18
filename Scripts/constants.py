import os
import sys
if getattr(sys, 'frozen', False):
    root_dir = os.path.dirname(sys.executable)
else:
    root_dir = os.path.dirname(os.path.dirname(__file__))
resources_dir = os.path.join(root_dir, 'Resources')
img_dir = os.path.join(resources_dir, 'logo.png')
qres_dir = os.path.join(root_dir, 'qres')