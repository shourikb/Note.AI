from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import openai
import json

openai.api_key = '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'

# Create your views here.
def index(request):
	return HttpResponse("Hello world, youre at polls index")

def get_completion(prompt): 
	print("Prompt:")
	print(prompt)
    # Step 1: send the conversation and available functions to GPT
    # messages = [{"role": "user", "content": prompt}]
    # functions = [
    #     {
    #         "name": "get_current_weather",
    #         "description": "Get the current weather in a given location",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "location": {
    #                     "type": "string",
    #                     "description": "The city and state, e.g. San Francisco, CA",
    #                 },
    #                 "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
    #             },
    #             "required": ["location"],
    #         },
    #     }
    # ]
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-0613",
    #     messages=messages,
    #     functions=functions,
    #     function_call="auto",  # auto is default, but we'll be explicit
    # )
    # response_message = response["choices"][0]["message"]

    # # Step 2: check if GPT wanted to call a function
    # if response_message.get("function_call"):
    #     # Step 3: call the function
    #     # Note: the JSON response may not always be valid; be sure to handle errors
    #     available_functions = {
    #         "get_current_weather": get_current_weather,
    #     }  # only one function in this example, but you can have multiple
    #     function_name = response_message["function_call"]["name"]
    #     function_to_call = available_functions[function_name]
    #     function_args = json.loads(response_message["function_call"]["arguments"])
    #     function_response = function_to_call(
    #         location=function_args.get("location"),
    #         unit=function_args.get("unit"),
    #     )

    #     # Step 4: send the info on the function call and function response to GPT
    #     messages.append(response_message)  # extend conversation with assistant's reply
    #     messages.append(
    #         {
    #             "role": "function",
    #             "name": function_name,
    #             "content": function_response,
    #         }
    #     )  # extend conversation with function response
    #     second_response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo-0613",
    #         messages=messages,
    #     )  # get a new response from GPT where it can see the function response
    #     return second_response

	query = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0.5, 
    ) 
	# print("Response:")
	# print(response)
	response = query.choices[0].text
	return response
  
  
def query_view(request): 
    if request.method == 'POST':

        print(request)

        prompt = request.POST.get('prompt') 

        response = get_completion(prompt) 
        print(response)
        return JsonResponse({'response': response})
    return render(request, 'index.html') 