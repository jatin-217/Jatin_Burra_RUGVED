def coleman_liau_index(text: str) -> str:
    letters=sum(c.isalpha()for c in text)
    words=len(text.split())
    sentences=sum(text.count(end) for end in ".!?")
    L=(letters/words)*100
    S=(sentences/words)*100

    index =round(0.0588*L-0.296*S-15.8)
    if index<1:
        return "Before Grade 1"
    elif index>=16:
        return "Grade 16+"
    else:
        return f"Grade {index}"
text = input("Enter the text:")
print("Grade Level:",coleman_liau_index(text))

 
                    