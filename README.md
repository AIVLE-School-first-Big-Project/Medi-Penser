# ![logo1](https://user-images.githubusercontent.com/90889155/163949077-046b55ab-af67-492c-8f95-049dd1aa39a3.png)

๐์๊ฐ ์ง๋ฅ์ ํ์ฉํ ์๋ฉด์ธ์ Medi-Penser
## ์กฐ์
> ์๋ํ ์ค์ง์ฐ ์ ๊ฑดํฌ ์ ๊ฒฝ์ ์ฒ์ ์ง
## ์คํ๋ฐฉ๋ฒ
```
> git clone https://github.com/AIVLE-School-first-Big-Project/Medi-Penser.git
> cd Medi-Penser
> pip install -r requirements.txt
> python manage.py makemigrations(์ต์ด์คํ์)
> python manage.py migrate(์ต์ด์คํ์)
> python manage.py runserver
```
### ์ฑ๋ด์ด ๋๋ต์ด ์์๋
```
> python train.py
> python manage.py runserver
```
#### CNN_FaceRecog.ipynb
  ์น ์บ ์ ์ฌ์ฉํ ์ง์  ๋ฐ์ดํฐ ์์ง์ด ๊ฐ๋ฅํ CNN ๋ชจ๋ธ๋ง์ ์ํ ์ฃผํผํฐ ๋ธํธ๋ถ ํ์ผ
  ํ๋์จ์ด์ ์ ์ฉํ๊ธฐ ์ํ ๋ชจ๋ธ์ ๋ง๋ค๊ธฐ ์ํด ์ฌ์ฉํฉ๋๋ค.


# ๋ชฉ์ฐจ 

- [์ ์ ๋ฐฐ๊ฒฝ ๋ฐ ๊ธฐ๋ํจ๊ณผ](#์ ์ ๋ฐฐ๊ฒฝ-๋ฐ-๊ธฐ๋ํจ๊ณผ)

- [์๋น์ค FLOW](#์๋น์ค-flow)

- [๊ธฐ๋ฅ FLOW](#๊ธฐ๋ฅ-flow)

- [์์ํ๊ฒฝ](#์์ํ๊ฒฝ)

- [ERD](#erd)

- [Architecture](#architecture)

- [UI/UX](#ui-ux)
- [์ผ๊ตด์ธ์ ๋ฐ์ดํฐ์](#์ธ์ํ -์ผ๊ตด์-data-set-๋ง๋ค๊ธฐ)
- [์ผ๊ตด ๊ฒ์ถ](#์ผ๊ตด-๊ฒ์ถํ๊ธฐ)
- [ํ๋์จ์ด ์ค๊ณ](#ํ๋์จ์ด-์ค๊ณ)



## ์ ์ ๋ฐฐ๊ฒฝ ๋ฐ ๊ธฐ๋ํจ๊ณผ

> **์ ์ ๋ฐฐ๊ฒฝ**
>>์น๋งค ํ์, ์ง์ ์ฅ์ ์ธ๋ค์ ๋ณต์ฉํด์ผ ํ๋ ์ฝ์ ํท๊ฐ๋ฆด ์ ์๋ค.  
>>๋๊ตฐ๊ฐ๊ฐ ๋์์ค๋ค๋ฉด ๋ง๋ ์ฝ์ ๋ณต์ฉํ  ์ ์์ง๋ง
>>๋ณดํธ์๊ฐ ํ๋ฃจ ์ข์ผ ๋ถ์ด์๊ธฐ๋ ์ฝ์ง ์๋ค.  
>>์ฝ์ ์ค๋จ์ฉ์ ๋ฐฉ์งํ๊ณ  ๋ณดํธ์์๊ฒ ์ฌ์ ๋ฅผ ์ ๊ณตํ  ์ ์๋ ๋ฐฉ๋ฒ์ด ๋ฌด์์ผ์ง ์๊ฐํด๋ณด์๊ณ ,    
>>์ผ๊ตด์ธ์์ ํตํด ์ฌ๋ฐ๋ฅธ ์ฝ์ ๊ณต๊ธํ๋ ์๋น์ค์ ๋ํ ์์ด๋์ด๋ฅผ ๋์ถ ํ  ์ ์์๋ค.



> **๊ธฐ๋ํจ๊ณผ**
>> 1. ์น๋งคํ์, ์ง์ ์ฅ์ ์ธ(๋ณดํธ๊ฐ ํ์ํ ๋ถ๋ค)์ ์ฌ๋ฐ๋ฅธ ์ฝ ๋ณต์ฉ ์ง๋
>> 2. ๊ฐ๋ณ์ธ/์์๋ณดํธ์ฌ ๋ฑ์๊ฒ ์๋ฌดํจ์จํ ์ง์
>> 3. KT B2B+DIGICO ์ฌ์ ๋น์ค ํ๋์ ์ด๋ฐ์ง

## ์๋น์ค FLOW
![big project service flow](https://user-images.githubusercontent.com/42240751/167738730-690cfd87-d268-491a-9928-5c3d28a6b223.png)

## ๊ธฐ๋ฅ Flow
![๊ธฐ๋ฅ](https://user-images.githubusercontent.com/90889155/167329955-8ea883ee-bc1c-4ef6-90c4-1f1bce145fc7.PNG)

## ์์ํ๊ฒฝ
![์์](https://user-images.githubusercontent.com/90889155/167336536-2bead010-65c2-472b-b64b-674f88359d07.PNG)

## ERD
![erd](https://user-images.githubusercontent.com/90889155/167431283-8bb696ce-35d3-4a9b-88fb-9f9b1a5057ca.PNG)

## Architecture
![arc](https://user-images.githubusercontent.com/90889155/167430614-82109d19-9e90-4874-9df8-8f0c082301ba.PNG)
## UI UX
- ๋ฉ์ธ ํ์ด์ง
![127 0 0 1_8000_ (1)](https://user-images.githubusercontent.com/90889155/167337450-3ef8d319-29ff-4e6d-ac95-b7ae33461a74.png)

- ๋ก๊ทธ์ธ,ํ์๊ฐ์
![login](https://user-images.githubusercontent.com/90889155/167346333-155600de-c606-42eb-974f-266557446a96.png)

- ๊ฒ์ํ
![๊ฒ์ํ2](https://user-images.githubusercontent.com/90889155/167348425-f80547c1-22fa-46b6-a654-2992e8dba927.PNG)

- ๊ฒ์๊ธ
![๊ฒ์ํ](https://user-images.githubusercontent.com/90889155/167348335-834af48a-0127-4123-a3eb-323f08605d59.PNG)


## ์ธ์ํ  ์ผ๊ตด์ data set ๋ง๋ค๊ธฐ
![OpenCV - Webcam Capture](https://user-images.githubusercontent.com/85106442/165012056-c7a9ad83-9ffe-43cf-88ca-be2a3c083576.jpg)   
   
cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # ํ๋ฐฑ์ผ๋ก   
minSize=(20,20) # ์ผ๊ตด ์ต์ ํฌ๊ธฐ


## ์ผ๊ตด ๊ฒ์ถํ๊ธฐ
![Face Detecting](https://user-images.githubusercontent.com/42240751/167565215-081b5eef-5211-49af-9e4c-fefca8251c28.png)

## ํ๋์จ์ด ์ค๊ณ
![hardware](https://user-images.githubusercontent.com/42240751/167565955-97236825-ba37-4370-b277-b85fbaae94e2.png)
