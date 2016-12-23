Colorinche
=================================
Colorinche is a Python package to create beautiful CLIs with Blessings from Jinja templates.

How does it works?
==================

First you create a jinja environment and render a template, and print it.

.. code-block:: python

    from colorinche import print_template, set_env


    options = [
        [1, "First", "the first option"],
        [2, "Second", "the middle option"],
        [3, "Third", "the final option"]
    ]

    data = {
        "title": "Awesome Example",
        "options": options,
    }

    set_env("templates_dir")
    print_template(template, data)


Then you create a Jinja template

.. code-block::
    
    {% bless 'white_bold' %}{{title}}{% end %}                                                                 
                                                                                                               
    {% for option in options %}                                                                                
    {% bless 'red' %}{{option.0}}) {% end %}                                                                   
    {% bless 'bold_underline_blue' %}{{option.1}}{% end %} - {% bless 'yellow_on_white' %}{{option.2}}{% end %}
                                                                                                               
    {% endfor %}                                                                                               

And that's it. You get your pretty Terminal with Blessings charm and your code will be clean.

.. image:: ./screenshots/screenshot.png

Installation
============
With pip

.. code-block:: bash

    sudo pip install colorinche

From source

.. code-block:: bash

    git clone https://github.com/felipelerena/colorinche.git
    sudo python setup.py install

Dependencies
=====================
* Jinja2
* Blessings
