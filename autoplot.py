import argparse

parser = argparse.ArgumentParser(description='Generate Windows user-land agent with a interface recovery output')

parser.add_argument('-num', help='number of print Fuzzing Results (default : 1)', default=1, type=str)

args = parser.parse_args()
indata = ''
plot1_data = ''
plot2_data = ''
plot3_data = ''

for i in range (1, int(args.num)+1):
        indata += 'indata'+str(i)+' = ARG'+str(i)+'\n'
        #PLOT1 - Total execs
        plot1_data += 'indata' + str(i) + ' using '
        plot1_data += '1:12' #data
        plot1_data += ' title '
        plot1_data += '\'Total execs ' + str(i) + '\' ' #Title
        plot1_data += 'with line linecolor rgb '
        plot1_data += '\'#0090ff\' ' #color
        plot1_data += 'linewidth 4, \\\n' #linewidth

        #PLOT2
        plot2_data += 'indata' + str(i) + ' using '
        plot2_data += '1:3' #data
        plot2_data += ' title '
        plot2_data += '\'Paths Total ' + str(i) + '\' ' #Title
        plot2_data += 'with line linecolor rgb '
        plot2_data += '\'#7d00d6\' ' #color
        plot2_data += 'linewidth 2, \\\n' #linewidth

        plot2_data += 'indata' + str(i) + ' using '
        plot2_data += '1:5' #data
        plot2_data += ' title '
        plot2_data += '\'favs Total ' + str(i) + '\' ' #Title
        plot2_data += 'with line linecolor rgb '
        plot2_data += '\'#8d4fff\' ' #color
        plot2_data += 'linewidth 2 ' #linewidth

        #PLOT3
        plot3_data += 'indata' + str(i) + ' using '
        plot3_data += '1:6' #data
        plot3_data += ' title '
        plot3_data += '\'Unique Crashes ' + str(i) + '\' ' #Title
        plot3_data += 'with line linecolor rgb '
        plot3_data += '\'#db006a\' ' #color
        plot3_data += 'linewidth 2, \\\n' #linewidth

        #PLOT3 - Bytes in Bitmap
        plot3_data += 'indata' + str(i) + ' using '
        plot3_data += '1:13' #data
        plot3_data += ' title '
        plot3_data += '\'Bytes in Bitmap ' + str(i) + '\' ' #Title
        plot3_data += 'with line linecolor rgb '
        plot3_data += '\'#f4fa46\' ' #color
        plot3_data += 'linewidth 4 ' #linewidth

        if i == int(args.num): #is it fin?
            plot1_data += ' \n' #linestyle, fin.
            plot2_data += '\n'
            plot3_data += '\n'
        else:
            plot1_data += ', \\\n' #linestyle
            plot2_data += ', \\\n'
            plot3_data += ', \\\n'
            
f = open('./stats_template.plot', 'r')
code = f.read()
f.close()

code = code.replace('__INDATA__', indata)
code = code.replace('__PLOT1__', plot1_data)
code = code.replace('__PLOT2__', plot2_data)
code = code.replace('__PLOT3__', plot3_data)

f = open('./test.plot', 'w')
f.write(code)
f.close()

print(indata)
print(plot1_data)
print(plot2_data)
print(plot3_data)