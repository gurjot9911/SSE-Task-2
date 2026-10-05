marks = {

}

p = float(input("Enter physics marks here: "))
c = float(input("Enter chem marks here: "))
m = float(input("Enter maths marks here: "))

marks.update(physics=p)
marks.update(chemistry=c)
marks.update(maths=m)

print(marks)
