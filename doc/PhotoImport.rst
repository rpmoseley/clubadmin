Photo Import
============
Overview
--------
This document describes the process of importing the existing photos of members in order to be usable by the ClubAdmin package.

Assumptions
-----------
The process assumes that the resultant photos are not intended to be used in their original form but instead are used to provide
a proof of membership in the shape of a card that carries the image of the member to avoid possible impersonation by another party.

Notes
-----
This section describes the initial investigations into migrating the existing photos to the new format, it consists of loading
each photo then re-scaling them to the size expected by the ClubAdmin package which can then be either saved as BLOBs within the
database or incorporated into a separate ZIP file which is then loaded as required.

Script
------
The following sequence produces an image that is one of the expected output format and size, run within a Python session:

>>> import wx
>>> app = wx.App()      #  Required to enable the use of Image to work
>>> img = wx.Image('/rpiwork/USC/photo/database/Photo_1111.jpg')
>>> print(img.Width, img.Height)
1600 1200
>>> img2 = img.Rescale(320, 240)
>>> print(img2.Width, img2.Height)
320 240
>>> img2.SaveFile('/tmp/photo1111.jpg')
