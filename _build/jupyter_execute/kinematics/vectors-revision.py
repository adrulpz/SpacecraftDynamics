#!/usr/bin/env python
# coding: utf-8

# ## Vectors Fundamentals

# - **scalar**: A quantity described purely by a number. <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. $1.1, 2, 3\ldots$; one tree; 3 spacecraft; 7 robot arms.<br>
# In dynamics, you will also see scalars in the context of quantifying masses (e.g., the mass of a professional football is  $430$ g, which is a scalar unit of measure) or geometric dimensions (e.g., the circumference of a professional football is $63.5$ mm, which is also a scalar).
# - **vector**: a quantity characterised by both magnitude and direction.
# 
# ### Notation of Vectors: handwritten and typewritten
# 
# Vectors are commonly denoted using letters from the English and Greek alphabets. When typed, you will typically see a general vector typed in boldface. For example, $\bf a$ is a vector. When written by hand, you will see instructors use two common notifications. Below, we show how the vectors $\boldsymbol\alpha$ and $\bf a$ are commonly written by hand.
# 
# ```{figure} ./images/3.png
# ---
# name: 3
# ---
# ```
# In live lectures by Angadh, you will commonly see the highlighted notation in his handwriting. However, both notations are equally valid.
# 
# ### Graphical Representation of Vectors
# > Vectors are drawn as a directed line segment (i.e., a line segment with an arrow at one end). 
# 
# They are typically represented for two cases:
#   
# ```{figure} ./images/4.png
# ---
# name: 4
# ---
# ```
# 
# Conversely, by the same rule, a clockwise vector will have a negative direction and points into the plane of the paper.
# 
# <!-- The convention is shown below for a vector $\boldsymbol\alpha$:
# 
# ```{figure} ./images/5.png
# ---
# name: 5
# ---
# ```
#  -->
# ```{attention}
# The inclination of clockwise and counterclockwise vectors is $90^{\circ{}}$ with respect to the plane of the paper or the computer screen.
# ```
# 
# ### Unit vector
# >A vector of unit magnitude (i.e., its magnitude is $1$). 
# 
# Unit vectors are commonly written with a caret $(\hat{\ })$; this is typically seen over a letter in the alphabet. For example, $\hat{\bf i}$ is a unit vector and $\left|\hat{\bf i}\right|=1$ says that magnitude of $\hat{\bf i}$ is $1$.
# 
# ### Reference frames 
# 
# > A set of three right-handed unit vectors (i.e., obeying the 'right-hand rule') that are mutually orthogonal.
# 
# In {numref}`RefR` below, $X-Y-Z$ form a Cartesian coordinate system. $\hat{\bf i},\;\hat{\bf j}\;\& \;\hat{\bf k}$ (drawn in pink) are a set of unit vectors that are mutually orthogonal and directed along $X$,$Y$, and $Z$, respectively.
# 
# ```{figure} ./images/6.png
# :name: RefR
# 
# Reference Frame R and its unit vectors.
# ```
# 
# The set of unit vectors are right-handed (also known as a “dextral set”), which means the following relationships hold true:
# 
# $$
# \hat{\bf i} \times \hat{\bf j} = \hat{\bf k}  \\
# \hat{\bf j} \times \hat{\bf k} = \hat{\bf i}  \\
# \hat{\bf k} \times \hat{\bf i} = \hat{\bf j}  \\
# $$
# 
# In reference to {numref}`RefR` above, this set of unit vectors forms a reference frame $R$. Reference frames are useful for studying moving objects. This is discussed in further detail much further on in this book.
# 
# :::{admonition}Other notations of unit vectors
# An alternate notation for unit vectors that make up a reference frame commonly used for dynamics is shown in the figure below; it makes use of subscripts in $x$, $y$, and $z$ to make explicit along which coordinate axis the unit vectors are aligned. We will (almost always) see (and use) this alternative subscript-based notations in dynamics for sake of clarity.
# 
# ```{figure} ./images/7.png
# :name: 7
# 
# Reference Frame A and its unit vectors.
# ```
# 
# * $\hat{\bf a}_x$ is the unit vector along the $X$-direction
# * $\hat{\bf a}_y$ is the unit vector along the $Y$-direction
# * $\hat{\bf a}_z$ is the unit vector along the $Z$-direction
# 
# This is a right-handed set of unit vectors. In the {numref}`7` above, this set forms the reference frame $A$.
# 
# $$
# \begin{align}
# \hat{\bf a}_x \times \hat{\bf a}_y =& \hat{\bf a}_z  \\
# \hat{\bf a}_y \times \hat{\bf a}_z =& \hat{\bf a}_x  \\
# \hat{\bf a}_z \times \hat{\bf a}_x =& \hat{\bf a}_y  \\
# \hat{\bf a}_x \times \hat{\bf a}_z =& -\hat{\bf a}_y  \\
# \hat{\bf a}_z \times \hat{\bf a}_y =& -\hat{\bf a}_x  \\
# \hat{\bf a}_y \times \hat{\bf a}_x =& -\hat{\bf a}_z  \\
# \end{align}
# $$
# :::
# 
# ### Component form
# Let $a,\;b,\;c$ be three scalar coordinates that describe the location of an arbitrary point in space in the $X-Y-Z$ coordinate system as shown in {numref}`8`. We can locate this point from the origin of the  using a position vector, denoted as $\bf{r}$. From our earlier review on vectors form the videos, we can see (in {numref}`8`) that the tail of the vector is at the origin while its head is at the point of interest.
# 
# ```{figure} ./images/8.png
# :name: 8
# 
# The scalar components of ${\bf r}$.
# ```
# 
# ```{note}
# $a,\;b,\;c$ are scalars and ${\bf r}$ is a vector.
# ```
# 
# The component form of this position vector, $\bf{r}$, can be written as:
# 
# $$
# {\bf r} = a\hat{\bf i} + b\hat{\bf j} + c\hat{\bf k}
# $$
# 
# The above “component form” of expressing vectors makes use of scalar coordinates and their corresponding directions through the use of the unit vectors. In other words, the equation above says that we can march
# $a$ units along $X$, $b$ units along $Y$, and $c$ units along $Z$ to get to the head of the vector $\bf r$.

# ### Vector algebra using a CAS (Computer Algebra Systems)

# ```{attention}
# If you haven't already done so, it would benefit the reader to review addition and multiplication of vectors from the video links on the preceding page [on fundamentals](vector.ipynb).
# ```
# In this book, we exploit a computer algebra system (CAS, for short) to perform vector algebra operations. A CAS is a software that allows manipulation of non-numerical as well as numerical mathematical expressions in a manner similar to that preformed manually (on a piece of paper by humans).
# 
# `SymPy` is an [open-source](https://en.wikipedia.org/wiki/Open-source_software) and free CAS that we will use in our studies on dynamics in this textbook. It has many advanced features that are particularly useful in studying dynamics of rigid bodies.
