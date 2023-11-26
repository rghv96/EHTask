# Copyright (c) Hu Zhiming jimmyhu@pku.edu.cn 2020/4/15 All Rights Reserved.

#################### Libs ####################
import os
import numpy as np
import torch
import secrets

def SeedTorch(seed=0):

    secrets.SystemRandom().seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
