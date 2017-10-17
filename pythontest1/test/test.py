import sys


def Fuc(x):
    print ('hello')
    print (x)
    print (x)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print ('Usage: python input_name output_name')
        exit(1)
    f_input = sys.argv[0]
    f_output = sys.argv[0]
    Fuc(f_output)

