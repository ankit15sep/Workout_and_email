from PIL import Image, ImageDraw, ImageFont, ImageSequence
from PIL import GifImagePlugin
import io
import os
import numpy as np
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random
import datetime
import pytz

def prep_attachment(i):
    attachment = open(GIFFiles[i],'rb')

    #encode attachment as base 64
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)

    #add header to attachment
    part.add_header('Content-Disposition',"attachment; filename= "+HeaderName[i])
    part.add_header('X-Attachment-Id', f'{i}')
    part.add_header('Content-ID', f'<{i}>')

    ##print(part.get('X-Attachment-Id'))
    msg.attach(part)

    msg.attach(MIMEText(('<html><body><h1>{name}</h1>').format(name=HeaderName[i]) +
    '<p><img src="cid:{i}"></p>'.format(i=i) +
    '</body></html>', 'html', 'utf-8'))

    text = msg.as_string()

    return text

def HeaderandGIF(csv_name,NoOfExe,path):
    ExerciseList = np.genfromtxt(csv_name,dtype=None,delimiter = ',')
    row = random.sample(range(0,len(ExerciseList)),NoOfExe)
    selectedExercises = ExerciseList[row]
    Ex_dict = {'Group':selectedExercises}
    Header =[]
    GIF =[]
    for j in range(0,len(selectedExercises)):
        header = (str((Ex_dict.get('Group'))[j,0])+str((Ex_dict.get('Group'))[j,1])).replace("b'",' ').replace("'","")
        gif = str((Ex_dict.get('Group'))[j,2]).replace("b'",'').replace("'","").strip()
        gif = os.path.join(path,gif)
        Header.append(header)
        GIF.append(gif)
        
    return Header,GIF

home_path = os.getcwd()
upperbody_path = os.path.join(home_path,"UpperBody")
lowerbody_path = os.path.join(home_path,"LowerBody")
correctives_path = os.path.join(home_path,"Correctives")
fullbody_path = os.path.join(home_path,"FullBody")

#### UPPERBODY #####
back_path = os.path.join(upperbody_path,"Back")
csv = os.path.join(back_path,"backexercises.csv")
Back_exrcse_name,Back_exrcse_gif  = HeaderandGIF(csv,1,back_path)

bicep_path = os.path.join(upperbody_path,"Biceps")
csv = os.path.join(bicep_path,"bicepexercises.csv")
Bicep_exrcse_name,Bicep_exrcse_gif  = HeaderandGIF(csv,1,bicep_path)

chest_path = os.path.join(upperbody_path,"Chest")
csv = os.path.join(chest_path,"Chestexercises.csv")
Chest_exrcse_name,Chest_exrcse_gif  = HeaderandGIF(csv,1,chest_path)

shoulder_path = os.path.join(upperbody_path,"Shoulders")
csv = os.path.join(shoulder_path,"Shoulderexercises.csv")
Shoulder_exrcse_name,Shoulder_exrcse_gif  = HeaderandGIF(csv,1,shoulder_path)

Triceps_path = os.path.join(upperbody_path,"Triceps")
csv = os.path.join(Triceps_path,"Tricepexercises.csv")
Triceps_exrcse_name,Triceps_exrcse_gif  = HeaderandGIF(csv,1,Triceps_path)

cardio_path = os.path.join(upperbody_path,"Cardio")
csv = os.path.join(cardio_path,"Cardio.csv")
Cardio_exrcse_name,Cardio_exrcse_gif  = HeaderandGIF(csv,2,cardio_path)

#### LOWERBODY #####
AddAbd_path = os.path.join(lowerbody_path,"Abductor_adductor")
csv = os.path.join(AddAbd_path,"AbdAddexercises.csv")
AddAbd_exrcse_name,AddAbd_exrcse_gif  = HeaderandGIF(csv,1,AddAbd_path)

Calves_path = os.path.join(lowerbody_path,"Calves")
csv = os.path.join(Calves_path,"Calvesexercises.csv")
Calves_exrcse_name,Calves_exrcse_gif  = HeaderandGIF(csv,1,Calves_path)

hamstring_path = os.path.join(lowerbody_path,"Hamstring")
csv = os.path.join(hamstring_path,"Hamstringexercises.csv")
Hamstring_exrcse_name,Hamstring_exrcse_gif  = HeaderandGIF(csv,1,hamstring_path)

LwrBack_path = os.path.join(lowerbody_path,"LowerBack")
csv = os.path.join(LwrBack_path,"lowerBackexercises.csv")
LwrBack_exrcse_name,LwrBack_exrcse_gif  = HeaderandGIF(csv,1,LwrBack_path)

Quads_path = os.path.join(lowerbody_path,"Quads")
csv = os.path.join(Quads_path,"Quadexercises.csv")
Quads_exrcse_name,Quads_exrcse_gif  = HeaderandGIF(csv,1,Quads_path)

cardio_path = os.path.join(lowerbody_path,"Cardio")
csv = os.path.join(cardio_path,"Cardio.csv")
Cardio_exrcse_name,Cardio_exrcse_gif  = HeaderandGIF(csv,2,cardio_path)

#### FULLBODY #####
hi_int_path = os.path.join(fullbody_path,"HI")
csv = os.path.join(hi_int_path,"FullBody_HIInt.csv")
hi_int_exrcse_name,hi_int_exrcse_gif  = HeaderandGIF(csv,2,hi_int_path)

low_int_path = os.path.join(fullbody_path,"LI")
csv = os.path.join(low_int_path,"FullBody_LIInt.csv")
low_int_exrcse_name,low_int_exrcse_gif  = HeaderandGIF(csv,3,low_int_path)

#### CORRECTIVES #####
Correctives_path = os.path.join(home_path,"Correctives")
csv = os.path.join(Correctives_path,"Correctivexercises.csv")
Correctives_exrcse_name,Correctives_exrcse_gif  = HeaderandGIF(csv,1,Correctives_path)

#### BREATHING #####
Breathe_path = os.path.join(home_path,"Breathing")
csv = os.path.join(Breathe_path,"Breathingexercise.csv")
Breathe_exrcse_name,Breathe_exrcse_gif  = HeaderandGIF(csv,1,Breathe_path)

##identify the day in India
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_ind = dt_utcnow.astimezone(pytz.timezone('Asia/Calcutta'))
## 0-Monday->BREAK, 1-Tuesday_>LWR, 2-Wednesday->UPR, 3-Thursday->Full, 4-Friday->BREAK, 5-Saturday->LWR, 6-Sunday->Full
day = dt_ind.weekday()

if day == 0 or day == 4:
    flag = 2  ##break
if day == 1 or day ==5:
    flag = 1  ##lower body
if day == 2:
    flag = 0  ##upper body
if day == 3 or day == 6:
    flag = 3  ##full body

if flag == 0:
    HeaderName = Bicep_exrcse_name+Back_exrcse_name+[Cardio_exrcse_name[0]]+Chest_exrcse_name+Shoulder_exrcse_name+Triceps_exrcse_name+[Cardio_exrcse_name[1]]+Correctives_exrcse_name+Breathe_exrcse_name
    GIFFiles = Bicep_exrcse_gif+Back_exrcse_gif+[Cardio_exrcse_gif[0]]+Chest_exrcse_gif+Shoulder_exrcse_gif+Triceps_exrcse_gif+[Cardio_exrcse_gif[1]]+Correctives_exrcse_gif+Breathe_exrcse_gif
elif flag == 1:
    HeaderName = Quads_exrcse_name+LwrBack_exrcse_name+AddAbd_exrcse_name+[Cardio_exrcse_name[0]]+Calves_exrcse_name+[Cardio_exrcse_name[1]]+Hamstring_exrcse_name+Correctives_exrcse_name+Breathe_exrcse_name
    GIFFiles = Quads_exrcse_gif+LwrBack_exrcse_gif+AddAbd_exrcse_gif+[Cardio_exrcse_gif[0]]+Calves_exrcse_gif+[Cardio_exrcse_gif[1]]+Hamstring_exrcse_gif+Correctives_exrcse_gif+Breathe_exrcse_gif
elif flag == 3:
    HeaderName = [low_int_exrcse_name[0]]+[hi_int_exrcse_name[0]]+[low_int_exrcse_name[1]]+[hi_int_exrcse_name[1]]+[low_int_exrcse_name[2]]+Correctives_exrcse_name+Breathe_exrcse_name
    GIFFiles = [low_int_exrcse_gif[0]]+[hi_int_exrcse_gif[0]]+[low_int_exrcse_gif[1]]+[hi_int_exrcse_gif[1]]+[low_int_exrcse_gif[2]]+Correctives_exrcse_gif+Breathe_exrcse_gif
    
#get email address and password stored in environment variable
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
#add email
EMAIL_to = "example@gmail.com"
if flag == 0 or flag ==1 or flag ==3:
    subject = "Goodmorning! Workout for today - 20mins."
else:
    subject = "Goodmorning! Take a Break but be active"
    
#Set MIMEMultipart message
msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_to
msg["Subject"] = subject
if flag == 0:
    body = "Upper body centered workout plan - finish 2 rounds of circuit in 20minutes. Warmup by doing some jump ropes :)"
if flag == 1:
    body = "Lower body centered workout plan - finish 2 rounds of circuit in 20minutes. Warmup by doing some jump ropes :)"
if flag == 3:
    body = "Full body centered workout plan - finish 2 rounds of circuit in 20minutes. Warmup by doing some jump ropes :)"
if flag == 2:
    body = "Take a break from strength training. Be active and eat healthy :) !!"
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()

if flag == 0 or flag ==1 or flag ==3 :
    for i in range(0,len(GIFFiles)):
        text = prep_attachment(i)


#open gmail server
with smtplib.SMTP('smtp.gmail.com',587) as smtpObj:
    smtpObj.ehlo()              #ping server
    smtpObj.starttls()          #start encryption
    smtpObj.ehlo()
    smtpObj.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtpObj.sendmail(EMAIL_ADDRESS,EMAIL_to,text)
print("Email sent to" +  EMAIL_to)
