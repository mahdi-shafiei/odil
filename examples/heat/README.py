#!/usr/bin/env python3

import os

text = """<!--- DO NOT EDIT THIS FILE. Generated by [[GEN]]-->
# Inferring conductivity from temperature

"""


def add_subdir(subdir, title, cmd, img=True):
    global text
    text += f"""
### {title}

```
{cmd}
```

Output directory `{subdir}`:

* [`train.log`]([[EXAMPLES]]/[[OUTDIR]]/{subdir}/train.log)
"""
    if img:
        text += f"""
* [`u_00010.png`]([[EXAMPLES]]/[[OUTDIR]]/{subdir}/u_00010.png)  
  <img src="[[EXAMPLES]]/[[OUTDIR]]/{subdir}/u_00010.png" height=200>
* [`k_00010.png`]([[EXAMPLES]]/[[OUTDIR]]/{subdir}/k_00010.png)  
  <img src="[[EXAMPLES]]/[[OUTDIR]]/{subdir}/k_00010.png" height=150>

"""


add_subdir("out_ref", "Reference solution", "case=0 outdir=out_ref ./run", img=0)
add_subdir("out_odiln", "ODIL Newton", "case=2n outdir=out_odiln ./run")
add_subdir("out_odil", "ODIL Adam", "case=2 outdir=out_odil ./run")
add_subdir("out_pinn", "PINN Adam", "case=2p gpus=0 outdir=out_pinn ./run")

text += f"""### Training history

```
./plot_train.py
```

* [`heat_train_u.png`]([[EXAMPLES]]/[[OUTDIR]]/heat_train_u.png)  
  <img src="[[EXAMPLES]]/[[OUTDIR]]/heat_train_u.png" height=200>
* [`heat_train_k.png`]([[EXAMPLES]]/[[OUTDIR]]/heat_train_k.png)  
  <img src="[[EXAMPLES]]/[[OUTDIR]]/heat_train_k.png" height=200>
"""

outdir = "heat"
gen = text
gen = gen.replace("[[GEN]]", os.path.basename(__file__))
gen = gen.replace("[[EXAMPLES]]", "https://cselab.github.io/odil/examples")
gen = gen.replace("[[OUTDIR]]", outdir)
with open("README.md", "w") as f:
    f.write(gen)
