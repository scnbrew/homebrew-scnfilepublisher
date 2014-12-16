homebrew-scnfilepublisher
=========================
Renames files based on templates.  
Copies them to target folder.

Building from source
--
create setup.py using the following command   
replace src/helloworld.py with the source of the actual program once we get that far  

<code>
py2applet `--`make-setup src/helloworld.py
</code>

build a development version of the app using the following command  

<code>
python setup.py py2app -A
</code>

This creates the app using live links from the source.  
This means that as long as you don't add any new files any changes you make to  
the source are reflected in the app

When you are ready to build the actual app, run the following  

<code>
python setup.py py2app
</code>



