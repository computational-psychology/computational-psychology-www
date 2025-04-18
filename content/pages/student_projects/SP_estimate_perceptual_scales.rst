*********************************************************************
Testing the validity of a new method for estimating perceptual scales
*********************************************************************


:save_as: SP_estimate_perceptual_scales.html
:url: SP_estimate_perceptual_scales.html


Project Description
######################################################################

Perceptual scales are mathematical functions that describe the relationship between a physical and a perceptual variable, such as weight in kilogram and perceived weight, or reflectance of a
surface and perceived lightness. There are some standard routines to measure perceptual scales but all of them require the observer to judge the stimuli many times.
`Radonjic, Cottaris and Brainard (2019) <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006950>`_ studied how two perceptual variables, color and material, depended on their respective physical variables. They proposed a novel modeling
procedure and claimed to be able to estimate scales for two perceptual dimensions at the same time (for example by a weighted sum).

The goal of this project is to critically evaluate their claims. We think that the problem as they phrase it is underdetermined, and that is impossible to disentangle the two perceptual
dimensions with their type of psychophysical experiment without making further assumptions.

To check their claims requires the following:

1. implement their model and fitting procedures in python
2. run simulations to check if the problem is indeed underconstrained
3. collect data in a replication attempt

There are two possible outcomes to the experiment and both of them are interesting. If the results can be replicated that is good. Then the code will be wrapped in a user-friendly python
package and be published online (in github) so that other research groups can use it. If it does not succeed, that is also interesting because it would invalidate the prior work and would
deserve further research. 


Requirements

- interest in visual perception and psychophysics
- scientific curiosity and being critical about models and their assumptions
- good programming skills in python
- good English skills to read the relevant literature

If you are interested, please contact Guillermo Aguilar (guillermo.aguilar@mail.tu-berlin.de)

