# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:20:05 2026

@author: Eben
"""



# Set the input file path for the model to use
model = KoekenBak.KoekenBak('/home/eben/KoekenBak/input/Parameter_testing/20220202-dust-gas-porosity-5e12-2.dat')

# Start the model calculations
model.startSession()

# Plot the species abundance for different outflow types
for istar,star in enumerate(model.star_grid):
   folder = os.path.join(path.cout,'models',star['LAST_CHEMISTRY_MODEL'])+'/'
   #- Smooth outflow
   if star['CLUMPMODE'] == 'SMOOTH':
     radius = np.array(CodeIO.getChemistryPhysPar(folder+'csphyspar_smooth.out','RADIUS'))
     fracs = CodeIO.getChemistryAbundances(folder+'csfrac_smooth.out')
     p.loglog(radius,fracs[mol]*2.,color=colours[istar],linestyle='dashed')
 
   #- One-component outflow (void interclump)
   elif star['CLUMPMODE'] == 'POROSITY' and star['FIC'] == 0:
     radius = np.array(CodeIO.getChemistryPhysPar(folder+'csphyspar_clump.out','RADIUS'))
     fracs = CodeIO.getChemistryAbundances(folder+'csfrac_clump.out')
     p.loglog(radius,fracs[mol]*2.,color=colours2[istar],linestyle='dashdot')
 
   #- Two-component outflow (Eq. 23 from Van de Sande et al. 2018b)  
   elif star['CLUMPMODE'] == 'POROSITY' and star['FIC'] > 0:
     fracs_clump = CodeIO.getChemistryAbundances(folder+'csfrac_clump.out')
     fracs_ic = CodeIO.getChemistryAbundances(folder+'csfrac_interclump.out')
     fr = (fracs_clump[mol]+(1-star['FVOL'])*star['FIC']*(fracs_ic[mol]-fracs_clump[mol]))*2.
     p.loglog(radius,fr,color=colours7[istar],linestyle=linest[istar])
