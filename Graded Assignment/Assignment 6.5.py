text = "X-DSPAM-Confidence:    0.8475";
sp = text.find('0')
val = float(text[sp:])
print(val)