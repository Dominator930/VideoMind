model = "medium" 
#change the model to "base" or "tiny" for lower end systems but note that this will drastically degrade the performance of the project. if you want higher performance use "large-v3" but this is for very high end systems as the processing could take hours depending upon the video and system configuration. also if the video you are passing is not in english the "medium" model will perform significantly worse in situations like this you have to use "large-v3" model.
output_model = "llama3.2"
#this model gives the output. the better model you choose more precise result you will see but the output may delay based on the system. also make sure whatever model you choose that model is downloaded or the project is going to throw an error, if not downloaded open command prompt or terminal and write - 
#                                                               ollama pull model_name
# if you are not sure about this part i suggest you to do some research on the subject.
