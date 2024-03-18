Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

1.0.0a3 (2024-03-18)
--------------------

Bug fixes:


- Fix an error with event config on Urban Classic
  [mpeeters] (URB-3006)


1.0.0a2 (2024-03-14)
--------------------

Bug fixes:


- Fix enum dependency
  [jchandelle] (URB-3006)


1.0.0a1 (2024-03-13)
--------------------

New features:


- Add function to import event config and create
  new CODT reform events at profile import.
  Split configuration files between urban classic and liege.
  [jchandelle, daggelpop, mpeeters] (URB-3006)


Bug fixes:


- Avoid an error between liege and main urban branch
  Fix existing content handling
  [mpeeters, jchandelle] (URB-3006)
