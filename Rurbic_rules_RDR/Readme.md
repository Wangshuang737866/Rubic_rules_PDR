# Pre-trained models
#Run in python
1 Run cd pSCRDRtagger
# Generate Rules Rubric.RDR
2 Run python RDRPOSTagger.py train ../data/Rubric 
# Tag students Answer
3 Run  python RDRPOSTagger.py tag ../data/Rubric.RDR ../data/Rubric.DICT ../data/student_answer