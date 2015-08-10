@ECHO OFF
SET curdir=%cd%
CD %~dp0 && (
  CALL python setup.py clean --all
  CALL python setup.py install
  CALL python setup.py cleanpyc
  CALL python setup.py test
) || ( GOTO Return )

:Return
CD %curdir%
