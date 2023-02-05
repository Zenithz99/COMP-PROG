import math as m
def mosteller(w, h):
 # return the body surface area of a person
 # based on body weight (w) and height (h)
 # using Mosteller formula
 return (w*h)**(1/2) / 60
def du_bois(w, h):
 # return the body surface area of a person
 # based on body weight (w) and height (h)
 # using Du Bois formula
 return 0.007184 * w**0.425 * h**0.725

def fujimoto(w, h):
 # return the body surface area of a person
 # based on body weight (w) and height (h)
 # using Fujimoto formula
 return 0.008883 * w**0.444 * h**0.663
def main():
 weight = float(input())
 height = float(input())
 x1 = mosteller(weight,height)
 x2 = du_bois(weight, height)
 x3 = fujimoto(weight, height)
 print("Mosteller =", round(x1, 5))
 print("Du Bois =", round(x2, 5))
 print("Fujimoto =", round(x3,5))


exec(input()) # DON'T remove this line