from .base import *

if base.DEBUG:
	try:
		from .local import *
	except:
		pass
elif not base.DEBUG:
	try:
		from .production import *
	except:
		pass
else:
	pass
