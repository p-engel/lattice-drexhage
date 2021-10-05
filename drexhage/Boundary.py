#! /usr/bin/env python
  
def main():
    """\
    A program to convert shape.dat file to shape.xyz file.
    """
    from argparse import ArgumentParser, RawDescriptionHelpFormatter
    from textwrap import dedent
    parser = ArgumentParser(description=dedent(main.__doc__),
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('file', help='The shape.dat file to convert.')
    args = parser.parse_args()

    # Get the coordinates 
    x = []
    y = []
    z = []
    with open(args.file) as file:
         data = file.readlines ()
    for line in data:
        line = line.split()
        if len(line) == 7 and '=' not in line:
           x.append(int(line[1]))
           y.append(int(line[2]))
           z.append(int(line[3]))

    print min(x), max(x)
    print min(y), max(y)
    print min(z), max(z)

    str =  ("%r \n\n" % len(x))
    for i in range(len(x)):
        str += ("Au %r %r %r\n" % (x[i], y[i], z[i]))

    with open('shape.xyz', 'w') as file:
         file.writelines(str)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
