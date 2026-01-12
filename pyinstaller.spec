# pyinstaller.spec
# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

# Collect QtWebEngine data
qt_webengine_datas = collect_data_files(
    'PyQt6.QtWebEngineCore',
    include_py_files=False
)

hidden_imports = (
    collect_submodules('PyQt6.QtWebEngineWidgets') +
    collect_submodules('PyQt6.QtWebEngineCore')
)

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        *qt_webengine_datas
    ],
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MyApp',
    windowed=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MyApp'
)