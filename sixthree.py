import math



def main():

    def sphereArea(radius):
        return 4 * math.pi * (int(radius)) * (int(radius))

    def sphereVolume(radius):
        return (4/3) * math.pi * (int(radius)) * (int(radius)) * (int(radius))

    print(sphereArea(5))
    print(sphereVolume(5))










main()
