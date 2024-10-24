# menggunakan posisi default
default_order = "{}, {} dan {}".format("ANTON", "ALDI", "VARO")
print('\n-----Urutan default-----')
print(default_order)

# menggunakan argumen posisi
positional_order = "{1}, {2} dan {0}".format("ANTON", "ALDI", "VARO")
print('\n-----Urutan berdasarkan posisi-----')
print(positional_order)