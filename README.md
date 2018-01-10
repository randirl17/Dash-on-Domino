# Dash-on-Domino

Examples of files needed to publish a [Dash](https://plot.ly/products/dash/) app on [Domino Data Labs](https://www.dominodatalab.com/).  

**app.sh** is the call to the app script.  This needs to be in your Domino project in order to publish the app.  
**app.py** is the app script itself, including the necessary configuration for Domino.  
**local_app.py** is another version of the app script without the Domino requirements to highlight the differences.  This could be run from the command line on your local machine.

In order to run these files, Dash and its dependencies must also be installed in your Domino environment.  For more information, see my [blog post](templink).
