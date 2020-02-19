import bz2
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import pysam
import requests
import seaborn as sns
import umap
import vcf

from plotly.offline import init_notebook_mode, iplot
from MulticoreTSNE import MulticoreTSNE as mTSNE
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from pandas import DataFrame


import warnings
warnings.filterwarnings('ignore')
init_notebook_mode(connected=True) #plotly

def vcf2df(vcf_fname):
    """Convert a subsetted vcf file to pandas DataFrame"""
    vcf_reader = vcf.Reader(filename=vcf_fname)
    
    df = pd.DataFrame(index=vcf_reader.samples)
    for variant in vcf_reader:
        df[variant.ID] = [call.gt_type if call.gt_type is not None else 3 for call in variant.samples]

    return df

 