from fabric.api import local, env, run
import os
import marshal
# Local path configuration (can be absolute or relative to fabfile)
#
PYQ = 'root@192.168.200.159'
PY_BIN = '/data/data/com.hipipal.qpyplus/files/bin/python'
QPY_ROOT = '/storage/sdcard0/com.hipipal.qpyplus/projects'
PROJ = 'chaos'
MAIN = 'main.py'
TMODS = '3party'
CFG = {'proj':PROJ}
CFG_DUMP = 'fab.dump'
if os.path.exists(CFG_DUMP): pass
else:
    print "init.", CFG_DUMP
    marshal.dump(CFG, open(CFG_DUMP, "wb"))
CFG = marshal.load(open(CFG_DUMP, "rb"))
# Remote server configuration
env.hosts= [PYQ]
env.user = "root"
env.shell = "/system/bin/sh -c"
#
#CRT_PROJ = "%(PYQ_ROOT)s/%(PROJ)s"% locals()
SCP_UP = "scp *.py {pyq}:{qpy_root}/{proj_name}/ "
SCP_R = "scp -r {locmod} {pyq}:{qpy_root}/{proj_name}/ "
SCP_VIEWS = "scp -r views {pyq}:{qpy_root}/{proj_name}/ "
SCP_STATIC = "scp -r static {pyq}:{qpy_root}/{proj_name}/ "

QPY_CALL = "source {qpy_root}/qpy_profile && {qpy_bin} {qpy_root}/{proj_name}/{main_scrip}"
# Actions define.
#def pushproj(ports='22', name='chaos'):
def push(proj=PROJ):
    '''push:proj=chaos \tscp all *.py up QPy projects/(default "chaos")
    '''
    print SCP_UP.format(pyq = PYQ
            , qpy_root = QPY_ROOT
            , proj_name = proj
            )
    CFG['proj'] = proj
    marshal.dump(CFG, open(CFG_DUMP, "wb"))
    local(SCP_VIEWS.format(pyq = PYQ
            , qpy_root = QPY_ROOT
            , proj_name = proj
            )
        )
    local(SCP_STATIC.format(pyq = PYQ
            , qpy_root = QPY_ROOT
            , proj_name = proj
            )
        )
    local(SCP_UP.format(pyq = PYQ
            , qpy_root = QPY_ROOT
            , proj_name = proj
            )
        )

def pumod():
    '''pumod \t\tscp -r mod up QPy projects/(foucs "3party")
    '''
    print "CFG", CFG
    print SCP_R.format(locmod = TMODS
            , pyq = PYQ
            , qpy_root = QPY_ROOT
            , proj_name = CFG['proj']
            )
    local(SCP_R.format(locmod = TMODS
            , pyq = PYQ
            , qpy_root = QPY_ROOT
            , proj_name = CFG['proj']
            )
        )

def qpy_call(main=MAIN):
    '''qpy_call:main=MY.py \t(default is "main.py")
    '''
    run('pwd')
    run('ls -la ./')
    #run('export PYTHONHOME=/data/data/com.hipipal.qpyplus/files')
    #print '%s %s/%s'% (PY, CRT_PROJ, script)
    #run('%s %s/%s'% (PY, CRT_PROJ, script))
    print QPY_CALL.format(qpy_root = QPY_ROOT
            , qpy_bin = PY_BIN
            , proj_name = CFG['proj']
            , main_scrip = main
            )
    run(QPY_CALL.format(qpy_root = QPY_ROOT
            , qpy_bin = PY_BIN
            , proj_name = CFG['proj']
            , main_scrip = main
            )
        )
    #run('source %s/qpy_profile && %s %s/%s'% (PYQ_ROOT
    #    , PY
    #    , CRT_PROJ
    #    , main
    #    ))
    #run('%s %s/%s'% (PY, CRT_PROJ, script))

'''main develop loop usage :
$ fab qpy:main=MY.py
so fab will auto:
    - scp all local .py up into mobile QPython projects fold
    - and source right sys. env
    - and call the 'MY_developing.py'
    - so wiil see the script running in mobile desktop ;-) 
'''
def qpy(main=MAIN):
    '''qpy:main=main.py develop main loop:auto do all for QPy(default proj. as "chaos", change by `fab push:proj=*`)
    '''
    #pushproj()
    push(proj=CFG['proj'])
    qpy_call(main)
    env()

def uname():
    '''echo Android sys. info.
    '''
    run('uname -a')

def env():
    '''echo Android sys. env
    '''
    print 'source %s/qpy_profile'% PYQ_ROOT
    run('env')
    #run('source %s/qpy_profile && env'% PYQ_ROOT)

def envgen(script="gen_env.py"):
    '''gen. into: /storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profile (must link as /etc/profile at first)
    '''
    qpy_call(main=script)
    #run('ls -la %s'% CRT_PROJ)

