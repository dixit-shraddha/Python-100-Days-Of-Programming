letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))


school = "KIT college of engineering"
name = "Shraddha"
sentence = "My name is {0} and I am studying in {1} \n"
print(sentence.format(name, school))
# print(sentence.format(0,1))
name = "Smith"
school = "ABC"

sentence1 = f"My name is {{name}} and I am studying in {{school}} \n"

sentence = f"My name is {name} and I am studying in {school} \n"

print(sentence1)
print(sentence)
print(type(sentence))
print(f"{2*60}")
print(type(f"{2*60}"))
