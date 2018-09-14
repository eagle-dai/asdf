# -*- mode: python -*-

block_cipher = None


a = Analysis(['ops.py'],
             pathex=['C:\\Users\\win 10\\PycharmProjects\\asdf'],
             binaries=[],
             datas=[('C:\\Users\\win 10\\PycharmProjects\\asdf\\characters\\*.png','characters'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\clear\\*.png','clear'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\direction\\*.png','direction'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\home\\*.png','home'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\item\\*.png','item'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\screen\\*.png','screen'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\task\\*.png','task'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\conf\\*.conf','conf'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\city\\*.png','city'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\mission\\*.png','mission'),('C:\\Users\\win 10\\PycharmProjects\\asdf\\door\\*.png','door')],
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
