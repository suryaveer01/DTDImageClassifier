import subprocess


runs_dir = 'runs'
subprocess.call(['tensorboard', '--logdir',runs_dir])