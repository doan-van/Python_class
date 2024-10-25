
import xarray as xr
ds = xr.open_dataset('input_data/SLP_DJF.nc')
x = ds.idata.values.reshape(ds.idata.shape[0], ds.lat2d.shape[0], ds.lat2d.shape[1])

do = xr.Dataset()
do['slp'] = (('time', 'lat', 'lon'), x)

for c in ['lon2d', 'lat2d', 'time']:
    do.coords[c] = ds.coords[c]

do.to_netcdf('input_data/SLP_DJF_2d.nc')
