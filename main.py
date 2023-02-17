import csv

attributes_expand= {
  "hard-working":
  "You faithfully complete the nightly homework and are fully engaged in class discussions.",
  "curious":
  "You come to see me outside of class for extra help and ask additional questions that demonstrate your strong curiosity towards computer science.",
  "perseverant":
  "When faced with challenges, you persevere and work your way through even the knottiest of problems through using your peers, teachers, or even google.",
  "engaging":
  "You bring a interesting and relevent questions to class and stay on topic during class. You are active in your learning process and love to engage in the material.",
  "humorous":
  "You add a layer of humour to our material that is appreciated by all.",
  "collaborative":
  "You are really comfortable asking questions during the larger class discussion and you work well in small groups with your peers."
}
#a dict of attributes and their corresponding pregenerated praise


learning_outcome = [
  "Identify/characterize/define a programming problem.",
  "Understand and be able to use a variety of data types, control structures, and algorithmic problem-solving techniques in their programming.",
  "Design, document, implement and test solutions to programming problems.",
  "Express creativity using coding and technology in a variety of contexts.",
  "Identify and repair coding errors in a program.",
  "Effectively communicate programming solutions to others.",
  "work collaboratively to write modular code on larger projects."
]
#list of learning outcomes

class_desc = "This semester in Advanced Programming in Python, we covered the topics of the usage of string, list, tuple, dictionary. We have also practiced how to define and apply functions to code. In addition to daily homework and problem sets, we had an in-class test, a cumulative final exam, and three partner projects to demonstrate learning. A successful student will be able to develop efficient, readable code when necessary as well as clearly communicate their understanding of programming concepts."
#class description to make it callable and easy to print


def score_maker(score:int):
  #creates a automatic grade based on how well the student performed for their final
  if int(score) >= 90:
    grade = 'A'
  elif 90 > int(score) >= 80:
    grade = 'B'
  elif 80 > int(score) >= 70:
    grade = 'C'
  else:
    grade = 'D'
  return (grade)



with open('teacher_comment.csv') as csvfile:
  data = csv.reader(csvfile, delimiter=',')
  header = next(data)
  for row in data:
    attendence = row[2]
    #attendance marker
    attribute = row[3].strip().split(',')
    #attribute marker
   
    enrichments = row[4]
    #enrichment marker
    if len(attribute) == 3:
      compliment = "You are stellar " + attribute[0] + ', ' + attribute[1] + ', and ' + attribute[2] + ' student during class. You showed up to ' + attendence + '% of class! '
    elif len(attribute) ==2:
      compliment = "You are " + attribute[0] + ' and ' + attribute[1] + ' during class. You showed up to ' + attendence + '% of class! '
    else:
      compliment = "You are a "+ attribute[0] + ' student. You showed up to ' + attendence + '% of class! '
    #creates a sentence based on how many attributes the teacher has given the student
  
    para3 = ''
    name = row[0]
    para3 += f"{name}, "
    score = row[1]
    if score_maker(score) == 'A':
      para3 += "your performance in the course this semester has been phenomenal. "
    elif score_maker(score) == 'B':
      para3 += "you occasionally run into coding errors in exams. "
    elif score_maker(score) == 'C':
      para3 += "some of the questions may be difficult to you, but you manage to explore and try out solutions. "
    else:
      print(score)
      para3 += "you have room to improve on your learning. "
    para3 += f"You have received {score_maker(score)}’s on all tests, including a {score}% of your cumulative final exam. "
    strengths = row[4].strip().split(',')
    para3 += "You have demonstrated strong performace in the following learning outcomes: "
    #depending on score through the score maker, a sentence is generated. 
    
    for strength in strengths:
      para3 += f" {learning_outcome[int(strength)]}"
    enrichments = row[5].strip().split(',')
    para3 += " In the following semester, you can improve on the following learning outcome(s):"
    for enrichment in enrichments:
      para3 += f" {learning_outcome[int(enrichment)]}"
    #Creates a sentence for learning outcomes that could be improved
    
  
    compliment_expanded = ''
    for attri in attribute:
      attri.strip()
      description = attributes_expand.get(attri)
      compliment_expanded += str(description)
    #creates a sentence that expands on a compliment based on the attributes_expand dict
    para4 = ''
    para4 += f"{name}, you have earned an {score_maker(score)} for the semester and I look forward to working with you for the remainder of the year."
    
    word = '    ' + class_desc + '\n' + '    ' + compliment + compliment_expanded + '\n' + '    ' + para3 + '\n' + '    ' + para4
    word = str(word)
    with open(f'{name}_comments.txt', 'w') as f:
      f.write(word)
    #creates the text file based off the name of the student that it's writing for 
