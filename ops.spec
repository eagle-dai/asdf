# -*- mode: python -*-

block_cipher = None


a = Analysis(['ops.py'],
             pathex=['C:\\Users\\pig\\PycharmProjects\\dnf'],
             binaries=[],
             datas=[('C:\\Users\\pig\\PycharmProjects\\dnf\\characters\\*.png','characters'),('C:\\Users\\pig\\PycharmProjects\\dnf\\clear\\*.png','clear'),('C:\\Users\\pig\\PycharmProjects\\dnf\\direction\\*.png','direction'),('C:\\Users\\pig\\PycharmProjects\\dnf\\home\\*.png','home'),('C:\\Users\\pig\\PycharmProjects\\dnf\\item\\*.png','item'),('C:\\Users\\pig\\PycharmProjects\\dnf\\screen\\*.png','screen'),('C:\\Users\\pig\\PycharmProjects\\dnf\\task\\*.png','task'),('C:\\Users\\pig\\PycharmProjects\\dnf\\conf\\*.conf','conf'),('C:\\Users\\pig\\PycharmProjects\\dnf\\city\\*.png','city'),('C:\\Users\\pig\\PycharmProjects\\dnf\\mission\\*.png','mission')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ops',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='dnf.ico')
