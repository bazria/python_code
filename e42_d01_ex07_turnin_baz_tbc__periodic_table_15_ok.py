#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def open_in_browser(absolute_filename):
    """
    Open argument file in browser.
    """
    from webbrowser import open_new_tab
    open_new_tab('file://' + absolute_filename)

def generate_periodic_table_html(in_filename, out_filename):
    """
    Write periodic table in html format from text file. 
    """
    # define 2-dimension list of tuple as structure to hold periodic table elements. group is horizontal, period is vertical.
    groups = 18
    periods = 7
    periodic_table = [[(None, None, None, None, None, None,) for y in range(periods)] for x in range(groups)]

    # process text file containing periodic table element data
    with open(in_filename, 'r') as in_file:
        write_period = 0
        raw_periodic_table = in_file.read().splitlines()
        for line in raw_periodic_table:
            # extract elemet data and convert to proper type
            raw_name_long, raw_atomic_number, raw_name_short, raw_molar_weight, raw_electron_configuration = line.split(sep = ',')
            name_long, raw_position = raw_name_long.replace(' ', '').split(sep = '=')
            not_used, position_str = raw_position.split(sep = ':')
            position = int(position_str)
            not_used, atomic_number_str = raw_atomic_number.replace(' ', '').split(sep = ':')
            atomic_number = int(atomic_number_str)
            not_used, name_short = raw_name_short.replace(' ', '').split(sep = ':')
            not_used, molar_weight_str = raw_molar_weight.replace(' ', '').split(sep = ':')
            molar_weight = float(molar_weight_str)
            not_used, electron_configuration = raw_electron_configuration.split(sep = ':')
            # enter element data in tuple
            periodic_table [position] [write_period] = position, name_long, name_short, atomic_number, molar_weight, electron_configuration
            # increment write period when reaching end of group
            if position == (groups - 1):
                write_period += 1

    # generate html file
    with open(out_filename, 'w') as out_file:
        # write html head and beginning of body
        out_file.write("""<!doctype html>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <title>Periodic table</title>
        <style type="text/css">
            body
            {
                background-color: lightblue;
                text-align: center;
            }
            h1  {color: white;}
            h4  {font-size: 15px;}
            img {width: 20%;}
            li
            {
                padding-left: 0px;
                text-align: left;
            }
            table
            {
                border-collapse: collapse;
                text-align: center;
                width: 100%;
            }
            th, td
            {
                border: 1px solid black;
                border-collapse: collapse;
                padding: 1px;
                text-align: center;
                vertical-align: top;
            }
            ul
            {
                text-align: left;
            }
            td.empty_cell
            {
               border: 0;
            }
        </style>
    </head>
    <body>
        <br><br />
        <h1>Mendeleiev periodic table</h1>
        <br><br />
    	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/DIMendeleevCab.jpg/220px-DIMendeleevCab.jpg"
             alt="Picture of Dimitri Mendeleiev">
        <br><br />
        <br><br />
        <table>
            <tr>""")
        for y in range(periods):
            for x in range(groups):
                position, name_long, name_short, atomic_number, molar_weight, electron_configuration = periodic_table [x] [y] 
                if name_long != None:
                    molar_weight_rounded = round(molar_weight, 1)
                    out_file.write("""
                <td>
                    <h4>%s</h4>
                    <ul>
                        <li>%s</li>
                        <li>%s</li>
                        <li>%s</li>
                    </ul>
                </td>""" % (name_long, name_short, atomic_number, molar_weight_rounded))
                else:
                    out_file.write("""
                <td class="empty_cell"></td>""")
            if position == (groups - 1) and y != (periods - 1):
                out_file.write("""
            </tr>
            <tr>""")

        # write end of html body
        out_file.write("""
            </tr>
        </table>
        <br><br />
    </body>
</html>""")

if __name__ == '__main__':
    """
    Créez un programme qui utilise ce fichier pour écrire une page HTML représentant le tableau périodique des éléments correctement formaté.
    """

    in_filename  = 'e42_d01_ex07_resource__periodic_table.txt'
    out_filename = 'e42_d01_ex07_turnin_baz_tbc__periodic_table.html'
    pathname = '/Users/bazria/Google Drive/gdrive_bruno/python_code/'
    generate_periodic_table_html(in_filename, out_filename)
    open_in_browser(pathname + out_filename)
