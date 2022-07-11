# ExternalTools
This is a collection of External Tools for JetBrain's IDEs. You can set add an External Tool in your IDE by going to File > Settings > Tools > External Tools > +.

The binaries in the `dist` folder are compiled on Linux `x86_64`. You can recompile them on your own specific architecture using this command:
```console
pyinstaller --onefile toolFile.py
```
