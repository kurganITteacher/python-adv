BASE_DIR = './'
environ = {
    'KPK_DATA': '/home/kpk/data',
    'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

KPK_DATA = environ.get('KPK_DATA')
# print(KPK_DATA)

# _KPK_DATA = environ['KPK_DATA']
# print(_KPK_DATA)

# os.environ.get('KPK_DATA') or BASE_DIR
#
# os.environ.get('KPK_DATA') if os.environ.get('KPK_DATA') else BASE_DIR

# ROOT = os.environ.get('KPK_DATA') if os.environ.get('KPK_DATA') else BASE_DIR
pass

if KPK_DATA:
    ROOT = KPK_DATA
else:
    ROOT = BASE_DIR
print(ROOT)

pass

ROOT = KPK_DATA if KPK_DATA else BASE_DIR
print(ROOT)

pass

ROOT = KPK_DATA or BASE_DIR
print(ROOT)

