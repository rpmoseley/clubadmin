# clubadmin
Python club administration system written using the wxPython package.

This package is an implementation of a Club Administration system written using Python and wxPython or PyQt
(commercial licenses permitting) which provides a free (as in beer) system to maintain a database of members
whom may be in a number of states: Newly joined, Paying members and Life members.

The package provides the ability to maintain a database of Members including their Photo and associated
information such as address, and date-of-birth (DOB), and enables those Members to become Life-members after
they match (and maintain) certain criteria that includes the number of years they have paid and also their
age in order to receive the privilege of a Life-Member status.

The package has been written using Python 3.6 and the so called Phoenix version of wxPython which uses gtk3
as the underlying toolkit on Linux. It will use the appropriate underlying toolkit on Microsoft Windows.

The reason for the creation of this system is to provide a freely available package that provides Clubs 
(this meaning those establishments that operate in a manner a kin to "Working Mens Club" in the UK), providing a
more reasonable system for the administration of Members, those being people who pay a fixed subscription
cost. This includes associating a photo with their details, amongst other information.

The underlying database is, by default, providing by the libsqlite embedded database library, that provides an
ACID approach to the data updates.
