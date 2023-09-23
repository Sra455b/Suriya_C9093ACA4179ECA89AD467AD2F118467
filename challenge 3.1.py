def linearsearchproduct(productlist, targetproduct):
  indicates=[]

  for index, product in enumerate(productlist):
    if product==targetproduct:
      indicates.append(index)
  return indicates

#example 
products=["shoes","boot","loafer", "shoes","sandal","shoes"]
target="shoes"
target2='apple'
result=linearsearchproduct(products, target)
print(result)