delete all
load ../data/2G5R.pdb, main
hide all
bg_color white
show cartoon, (chain A)
color white

set_color color1, [1.000,0.000,0.000]
create sector1, (resi 95,44,37,26,36,79,81,80,64,121) & (chain A)
color color1, sector1
show spheres, sector1
show surface, sector1

set_color color2, [0.000,1.000,0.000]
create sector2, (resi 65,46,106,48,39,45,124,105,126,63,99,30,132) & (chain A)
color color2, sector2
show spheres, sector2
show surface, sector2

set_color color3, [0.000,0.000,1.000]
create sector3, (resi 94,110,117,107,50,108,97,51,41,134,123,119,34) & (chain A)
color color3, sector3
show spheres, sector3
show surface, sector3

set_color color_ic1, [1.000,0.000,0.000]
create ic_1, (resi 95,44,37,26,36,79,81,80,64,121) & (chain A)
color color_ic1, ic_1
show spheres, ic_1
show surface, ic_1

set_color color_ic2, [0.800,1.000,0.000]
create ic_2, (resi 65,46,106,48,39,45,124,105) & (chain A)
color color_ic2, ic_2
show spheres, ic_2
show surface, ic_2

set_color color_ic3, [0.000,1.000,0.400]
create ic_3, (resi 94,110,117,107,50,108,97,51) & (chain A)
color color_ic3, ic_3
show spheres, ic_3
show surface, ic_3

set_color color_ic4, [0.000,0.400,1.000]
create ic_4, (resi 126,63,99,30,132) & (chain A)
color color_ic4, ic_4
show spheres, ic_4
show surface, ic_4

set_color color_ic5, [0.800,0.000,1.000]
create ic_5, (resi 41,134,123,119,34) & (chain A)
color color_ic5, ic_5
show spheres, ic_5
show surface, ic_5

zoom
set transparency, 0.4
ray
png linsi
