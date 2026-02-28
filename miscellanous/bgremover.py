from withoutbg import WithoutBG as wbg
img = wbg.opensource()
result = img.remove_background("ronaldo.jpg")
result.save("out.png")