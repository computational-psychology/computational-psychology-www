Research
*********

:save_as: research.html
:url: research.html

.. role:: highlight


.. _student_projects:

:highlight:`Research projects for students`
--------------------------------------------

- Comparison of various lightness illusions and analysing to what extent these different phenomena are based on the same or different perceptual mechanisms. See our `Theses page <https://www.psyco.tu-berlin.de/theses.html>`_ for more details.

- Contrast as a cue for image segmentation in transparency conditions

- Perceived transparency and perceived contrast using real world stimuli (episcotisters)

- Crispening in real world stimuli

- Learning about human edge perception through noise masking experiments (See `Theses project page <https://www.psyco.tu-berlin.de/projects.html>`__)

- Can Convolutional Neural Networks benefit from fixational eye movements? (See `Theses project page <https://www.psyco.tu-berlin.de/projects.html>`__)

- Investigating brightness perception in psychophysical experiments or computational models (See `Theses project page <https://www.psyco.tu-berlin.de/projects.html>`__)



.. _lightness:


----


Easy evaluation and comparison of brightness perception models
---------------------------------------------------------------

There exist various models of human brightness perception that can account for human brightness perception on specific sets of input stimuli (e.g. specific brightness illusions). However, there is no structured overview of how each of these models performs on a larger test battery that contains input stimuli and tasks that the model was not specifically designed for. This makes both the qualitative as well as the quantitative comparison of existing brightness perception models difficult. Our goal is to develop an open-source framework which enables easy evaluation and comparison of different brightness perception models on different input stimuli. For this, we will develop a user-friendly pipeline where users can select multiple brightness perception models and input stimuli and receive an easily interpretable output about the model performance.



.. _evaluating_brightness_models:


----


Experimental characterization of lightness constancy
-----------------------------------------------------

The perceptual domain in which we currently study the above question is lightness. Human observers  perceive the lightness of surfaces relatively stable despite tremendous fluctuation in the sensory signal due to changes in viewing conditions. The luminance that is reflected to the eye from one and the same surface might vary substantially depending on whether the surface is seen under direct illumination or might be obscured by a shadow.



.. _methods:


----


Evaluation of experimental techniques to measure appearance
------------------------------------------------------------

The appearance of visual stimuli is commonly measured with matching procedures. 
In such an experiment the observer is asked to adjust an external reference stimulus until it looks the same as the target, and usually the target is presented in a different context or viewing condition, e.g. a different illumination. Although prevalent in the literature, matching tasks are usually difficult for the observer, do not guarantee subjective equality (as observers could be doing a 'minimal' difference match), and provide data which are an indirect measure of the underlying perceptual dimension. 
As an alternative we have explored the use of scaling methods for the measurement of appearance of visual stimuli presented across different viewing contexts. Specifically, we have evaluated Maximum Likelihood Difference Scaling (MLDS) and Maximum Likelihood Conjoint Measurement (MLCM).  `Here our recent poster about this topic <files/Aguilar_Maertens_VSS2019.pdf>`_.

.. figure:: img/matching_logic.png
   :figwidth: 600
   :align: center
   :alt: Matching logic in variegated checkerboards seen through a transparency.

   Matching procedures and underlying perceptual processes. After `Wiebel et al. (2017) <https://dx.doi.org/10.1167/17.4.1>`_.



.. _early_vision_model:


----


An early vision model of lightness perception
-----------------------------------------------

Our goal is to develop a mechanistic account of the computational principles and mechanisms that transform retinal sensations into meaningful percepts. We address this goal in the domain of lightness perception and want to understand how surface lightness is determined from the luminance signal in the retina. A computational model of lightness should receive a 2d matrix of gray values as input and compute the perceived lightness at all image positions as output.


.. figure:: img/white_illusion_odog.png
   :figwidth: 650
   :alt: White's illusion and ODOG model

   Response of ODOG model to White's illusion stimulus from `Betz et al. (2015) <https://dx.doi.org/10.1167/15.14.1>`_.



.. _inc_dec:

----


Increments and decrements in naturalistic stimuli
--------------------------------------------------

In this project we study the question under which conditions increments and decrements are matched with targets of opposite polarity.


.. _depth_3d:

----



Depth perception in 3d scenes
-------------------------------

The perception of surface lightness is influenced by the depth arrangement of a scene. To study depth perception under naturalistic conditions we collaborate with the Computer Graphics lab. We use objects that are created by means of 3d printing on the basis of mesh models. The availability of these models
means that for each 3d object a corresponding image of the object can be rendered on the computer. We test perceptual responses to 3d objects and their 2d counterparts.



.. _manual_dexterity:


----


Manual dexterity in humans and robots
---------------------------------------

Human grasping skills are far superior to those of robots. In collaboration with the Robotics lab we investigate the principles that lead to this superior performance in human grasping and work towards transferring these principles to robotic systems. Our key hypothesis is that human  grasping performance crucially depens on the purposeful exploitation of contact with the environment.
