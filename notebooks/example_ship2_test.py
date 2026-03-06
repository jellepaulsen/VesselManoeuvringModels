import matplotlib.pyplot as plt
plt.style.use('grayscale')
from pylab import rcParams
rcParams['figure.figsize'] = 10, 5

import numpy as np
from vessel_manoeuvring_models.models.vmm_linear import vmm_linear as vmm
from vessel_manoeuvring_models.models.vmm import ModelSimulator

import pandas as pd
import numpy as np
import vessel_manoeuvring_models.prime_system
from vessel_manoeuvring_models.models import brix_coefficients
from vessel_manoeuvring_models.prime_system import PrimeSystem
import os.path
import pytest
from vessel_manoeuvring_models.visualization.plot import track_plot, track_plots




from vessel_manoeuvring_models.parameters import df_parameters
from vessel_manoeuvring_models.substitute_dynamic_symbols import run
from vessel_manoeuvring_models import prime_system

ship_parameters = {
    "T": 0.2063106796116504,
    "L": 5.014563106796117,
    "CB": 0.45034232324249973,
    "B": 0.9466019417475728,
    "rho": 1000,
    "x_G": 0,
    "m": 441.0267843660858,
    "I_z": 693.124396594905,
    "volume": 0.4410267843660858,
}


def calculate_prime(row, ship_parameters):
    return run(function=row["brix_lambda"], **ship_parameters)


def test_model_simulator(vmm, ship_parameters, df_parameters, prime_system, speed):

    ## Define a model simulator:
    # This is a simulator with freezed parameters and ship_parameters:
    parameters = df_parameters['prime']
    model = ModelSimulator(simulator=vmm, 
                           parameters=parameters, 
                           ship_parameters=ship_parameters, 
                           control_keys=['delta'], 
                           primed_parameters=True, 
                           prime_system=prime_system)


    t = np.linspace(0,45,1000)
    df_ = pd.DataFrame(index=t)
    df_['u'] = speed*1.852/3.6
    df_['v'] = 0
    df_['r'] = 0
    df_['x0' ] = 0
    df_['y0' ] = 0
    df_['psi'] = 0
    df_['delta'] = np.deg2rad(20)
    df_['U'] = np.sqrt(df_['u']**2 + df_['v']**2)

    result = model.simulate(df_=df_)
    return result

mask = df_parameters["brix_lambda"].notnull()
df_parameters.loc[mask, "brix_prime"] = df_parameters.loc[mask].apply(
    calculate_prime, ship_parameters=ship_parameters, axis=1
)

df_parameters["prime"] = df_parameters["brix_prime"]

df_parameters.loc["Ydelta", "prime"] = 0.003  # Just guessing
df_parameters.loc["Ndelta", "prime"] = (
    -df_parameters.loc["Ydelta", "prime"] / 2
)  # Just guessing

df_parameters.loc["Nu", "prime"] = 0
df_parameters.loc["Nur", "prime"] = 0
df_parameters.loc["Xdelta", "prime"] = -0.001
df_parameters.loc["Xr", "prime"] = 0
df_parameters.loc["Xrr", "prime"] = 0.007
df_parameters.loc["Xu", "prime"] = -0.003
df_parameters.loc["Xuu", "prime"] = 0
df_parameters.loc["Xv", "prime"] = 0
df_parameters.loc["Xvr", "prime"] = -0.006
df_parameters.loc["Yu", "prime"] = 0
df_parameters.loc["Yur", "prime"] = 0.001

df_parameters.loc["Nuv", "prime"] = 0.0
df_parameters.loc["Xthrust", "prime"] = 1.0
df_parameters.loc["Yrdeltadelta", "prime"] = 0.0
df_parameters.loc["Xvdelta", "prime"] = 0.0
df_parameters.loc["Xdeltadelta", "prime"] = 0.0
df_parameters.loc["Yvdeltadelta", "prime"] = 0.0
df_parameters.loc["Nrdeltadelta", "prime"] = 0.0
df_parameters.loc["Yuv", "prime"] = 0.0
df_parameters.loc["Nvdeltadelta", "prime"] = 0.0

prime_system_1 = prime_system.PrimeSystem(**ship_parameters)  # model

df_ship_parameters = prime_system_1.prime(ship_parameters)
# print(f"df_ship_parameters: \n {df_ship_parameters.keys()} ")



results = test_model_simulator(vmm=vmm, ship_parameters=ship_parameters, df_parameters=df_parameters, prime_system=prime_system_1, speed=4).result.copy()
print(results)

with plt.xkcd(randomness=0.5):
    # This figure will be in XKCD-style
    fig,ax = plt.subplots()
    
    
    results.plot(x='y0', y='x0', ax=ax, label="Titanic")
    ax.axis('equal')
    
    plt.show()