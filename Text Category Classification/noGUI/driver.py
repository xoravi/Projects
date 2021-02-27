from model import myinput
text = input("Enter sample text: ")
predicted_result, prob_list = myinput(text)
print("Predicted Category: "+predicted_result)