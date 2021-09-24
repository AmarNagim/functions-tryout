import time

answer = int(input('Van welk getal wilt u de tafel zien?: '))

print('')

def tafel(answer):
    een = 1*answer
    twee = 2*answer
    drie = 3*answer
    vier = 4*answer
    vijf = 5*answer
    zes = 6*answer
    zeven = 7*answer
    acht = 8*answer
    negen = 9*answer
    tien = 10*answer
    tafel = str(answer)
    tafels = print(f"""De tafel van {tafel} is: 
1x{tafel}={een}
2x{tafel}={twee}
3x{tafel}={drie}
4x{tafel}={vier}
5x{tafel}={vijf}
6x{tafel}={zes}
7x{tafel}={zeven}
8x{tafel}={acht}
9x{tafel}={negen}
10x{tafel}={tien}

""")
    
tafel(answer)
