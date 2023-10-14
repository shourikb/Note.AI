from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import UploadFileForm
import openai
import json
import docx

openai.api_key = "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"


# Create your views here.
def index(request):
    return HttpResponse("Hello world, youre at polls index")


def get_completion(prompt):
    print("Prompt:")
    print(prompt)

    # query = openai.Completion.create(
    # 	 engine="text-davinci-003",
    # 	 prompt=prompt,
    # 	 max_tokens=1024,
    # 	 n=1,
    # 	 stop=None,
    # 	 temperature=0.5,
    # )
    #
    # response = query.choices[0].text
    return "asdf"


# def upload_file(request):
# 	print(request)
# 	print('asdfdsf')
# 	if request.method == "POST":
# 		print("im a apost")
# 		print(request.POST)
# 		print(request.FILES)
# 		form = UploadFileForm(request.POST, request.FILES)
# 		print(form)
# 		if form.is_valid():
# 			f = request.FILES["file"]

# 			return JsonResponse({'response': "asdf"})
# 	else:
# 		form = UploadFileForm()
# 	return render(request, 'index.html')


def query_view(request):
    if request.method == "POST":
        print(request)

        url = request.POST.get("prompt")

        doc = docx.Document(url)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)

        prompt = (
            "\n".join(fullText)
            + " Based on the above notes, generate 2 multiple choice question with 4 answer choices."
        )

        response = get_completion(prompt)
        print(response)
        return JsonResponse({"response": response})
    return render(request, "index.html")
