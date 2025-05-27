from mobius import MobiusStrip  # make sure both mobius.py and test.py python scripts are in the same folder

strip = MobiusStrip(R=1.0, w=0.4, n=150)
strip.plot()  # accept 87 diff gradient color scheme thorugh color parameter, refer the readme.md
print("Surface Area:", strip.compute_surface_area())  # use fix parameter to fix the decimals count, for example fix=6 => result {x.xxxxxx}
print("Edge Length:", strip.compute_edge_length())  # use fix parameter to round the decimal, for example fix=4 => result {x.xxxx}
# by default fix is 14 and color is Greys
