*********************
Project descriptions
*********************


:save_as: projects.html
:url: projects.html




Thesis Projects
******************

Learning about human edge perception through noise masking experiments
######################################################################

It is widely known that edges (e.g. object boundaries) serve as a major source of information to the human visual system. We define an edge as a luminance discontinuity in an image which is localized in space and extends along one axis. To test human edge perception experimentally, different tasks have been proposed such as edge localization `[1] <https://doi.org/10.1016/j.visres.2018.09.007>`__ and edge polarity judgments in noise `[2] <https://doi.org/10.1016/j.visres.2003.11.021>`__. However, it is still debated to which extent human edge perception relies on processing in a wide range of so-called spatial-frequency-selective channels. To better answer this question, we want to probe human edge perception in noise masking experiments in which we specifically interfere with the presumed underlying mechanisms. The aim of this project will be to implement and conduct a psychophysical experiments in our laboratory, and to analyze and interpret the resulting data with statistical methods.

Students will have to

- scan and read papers from the edge perception literature
- write code to conduct and evaluate a psychophysical experiments

Students will learn

- about fundamental mechanisms of visual processing
- how to implement and evaluate psychophysical experiments with statistical methods

Requirements

- Good programming skills in Python
- Good English proficiency

If you are interested, please contact Lynn Schmittwilken (L.Schmittwilken@tu-berlin.de)

----

Can Convolutional Neural Networks benefit from fixational eye movements?
########################################################################

Human vision is mediated by neural responses to luminance discontinuities, i.e edges, in space and time (e.g. object boundaries or flashing lights, e.g. `[1] <https://doi.org/10.1167/13.2.25>`__, `[2] <https://doi.org/10.1523/JNEUROSCI.0848-14.2014>`__). These spatiotemporal edge signals are the basis for higher-level visual processes such as object perception and object recognition. Convolutional Neural Networks (CNNs) are a powerful tool to model human object recognition. However, current CNNs mostly ignore the relevance of temporal transients for visual processing. 
Different than for CNNs, the input to the visual system is always moving. Even when the eyes are still, tiny eye jitters (i.e. fixational eye movements, FEMs) occur. These FEMs seem to be important for encoding edges in space and time (e.g. `[3] <https://dx.doi.org/10.1016%2Fj.tins.2015.01.005>`__), because they introduce visual transients over time that naturally emphasize edge signals in the visual input. Here, we want to explore whether CNNs could benefit from a more dynamic strategy to recognize objects in natural images. The aim of the project will be to set up a dynamic-processing pipeline inspired by FEMs and spatiotemporal characteristics of the human eye, and to compare the object recognition performance of this dynamic CNN with a classical CNN.

Students will have to

- Scan the literature for existing implementations of CNNs that use videos as inputs
- Train at least two CNNs on object recognition with a static and dynamic-processing pipeline

Students will learn

- about fundamental mechanisms of visual processing
- how to implement a dynamic-processing pipeline inspired by spatiotemporal characteristics of the human eye

Requirements

- Good programming skills in Python
- Good English proficiency
- Experience with deep learning and deep learning software (TensorFlow or Keras)

If you are interested, please contact Lynn Schmittwilken (L.Schmittwilken@tu-berlin.de)

----

Investigating brightness perception in psychophysical experiments or computational models
#########################################################################################

The perceived brightness of a surface is affected by its local luminance as well as the visual context in which it is viewed `[1] <https://doi.org/10.1016/j.visres.2010.09.012>`__. To probe this relationship, many visual stimuli (also known as visual brightness illusion) have been developed. Typically, brightness perception is tested with a small selection of these stimuli in a highly controlled laboratory settings. Since collecting empirical data is resourceful, there are many open questions with respect to how certain variations of these visual stimuli (e.g. luminance profiles, size, spatial frequency, noise, presentation times, etc) affect human brightness perception and how robust these findings are among a larger group of participants. The aim of this project will be to come up with a research question in the realm of human brightness perception, and then implement and conduct a psychophysical experiment, and to analyze and interpret the resulting data with statistical methods. The alternative aim of this project would be to come up with a research question in the realm of human brightness perception, which we can answer theoretically with the help of computational models of human brightness perception.

Students will have to

- scan and read papers from the brightness perception literature
- write code to conduct and analyze a psychophysical experiment or a simulated experiment with the help of computational models of human brightness perception

Students will learn

- how to conduct psychophysical experiments
- how to implement and test mechanistic models of human brightness perception

Requirements

- Good programming skills in Python
- Good English proficiency

If you are interested, please contact Lynn Schmittwilken (L.Schmittwilken@tu-berlin.de)

----

Testing the validity of a new method for estimating perceptual scales
#####################################################################

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


----

Vergleich von verschieden Helligkeitsphänomene 
###############################################

Es geht darum, verschiedene Wahrnehmungsphänomene (optische Täuschungen)  aus dem Bereich der Helligkeitswahrnehmung miteinander zu vergleichen. Die Fragestellung ist, inwiefern diese verschiedenen Effekte auf denselben oder unterschiedlichen perzeptuellen Mechanismen beruhen. Dazu würde eine große Anzahl von solchen Effekten von Versuchspersonen beurteilt werden. Es müßten viele Versuchspersonen gemessen werden bei uns im Labor. In Abhängigkeit vom Interesse der Kandidat*in könnten diese Effekte auch mit einem computationalen Modell vorhergesagt werden.


Vorteile  des Projekts
-----------------------
- konkrete Fragestellung bereits vorhanden
- beim Implementieren der Versuchsreize bekommt ihr Hilfe
- selbständiges wissenschaftliches Arbeiten
- der Datensatz kann veröffentlicht werden, da viele Arbeitsgruppen für ihre Modellierung Interesse an so einem Datensatz haben
- nette Arbeitsgruppe ;-)


Anforderungen
-------------------
- Interesse an visueller Wahrnehmung
- wissenschaftliche Neugier
- gute Programmierfähigkeiten in Python
- gute Englischkenntnisse um die relevanten Arbeiten zu lesen


Bei Interesse bitte `Prof. Maertens <https://www.psyco.tu-berlin.de/maertens.html>`_ kontaktieren.


.. figure:: img/stim_robinson07.png
   :figwidth: 477
   :alt: Helligskeit Täuschungen

   Helligskeit Täuschungen im Robinson, Hammond and De Sa (2007).



