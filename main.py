"""
Author: Ander Cejudo
Github: https://github.com/anderct105/va-questionnaire-3d
"""

from utils.CargarCuestionario import CargarCuestionario
from utils.CargarEmbedding import CargarEmbedding
from utils.Preprocesar import Preprocesar
from utils.RepresentarEmbedding import RepresentarEmbedding

def menu():
	with open('banner.txt','r') as f:
		text = f.read()
		f.close()
	print(text)
	print("Which questions do you want to load?")
	print("\t1. All the questions in the questionnaire")
	print("\t2. All the questions present in Adult")
	print("\t3. All the questions present in Child")
	print("\t4. All the questions present in Neonate")
	print("\t0. Finish")
	try: 
		option = int(input("Select one between 0-4: "))
		if option < 0 or option > 4:
			raise Exception
	except:
		print("Not a valid value!")
		exit(1)
	return option

def load_questions(option):
	try:
		if option == 0:
			print("Bye!")
			exit(0)
		elif option == 1:
			questions = CargarCuestionario('./data/FullInstrument4-3-13.xls', hoja='Master', columna='question')()[2:]
		elif option == 2:
			questions = CargarCuestionario('./data/AdultQuestions.txt')(formato='txt')
		elif option == 3:
			questions = CargarCuestionario('./data/ChildQuestions.txt')(formato='txt')
		else:
			questions = CargarCuestionario('./data/NeonateQuestions.txt')(formato='txt')
	except IOError as exc:
		print(exc)
		print("The data could not be found, make sure that you downloaded the data folder from the repo.")
		exit(1)
	return questions


# Load questions
option = menu()
questions = load_questions(option)
# Preprocess the questions (lower, tokenize...)
questions_pre, _ = Preprocesar(questions)()
# Get doc embedding of each question, the Glove in the repo is 50 dimensional
glove = CargarEmbedding('./glove.txt').loadGloveModel()
questions_pre = RepresentarEmbedding(questions_pre)(glove)
# Save the questions and the embeddings in the corresponding format to load them in projector.tensorflow.org
print("Saving the results in questions_emb.tsv and questions_meta.tsv")
out_questions_emb = open('./out/questions_emb.tsv', 'w', encoding='utf-8')
out_questions_meta = open('./out/questions_meta.tsv', 'w', encoding='utf-8')
for i, emb in enumerate(questions_pre):
	out_questions_meta.write(questions[i] + '\n')
	out_questions_emb.write('\t'.join([str(x) for x in emb]) + '\n')
out_questions_meta.flush(); out_questions_emb.flush()
out_questions_meta.close(); out_questions_emb.close()
