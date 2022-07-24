# Book-Bot

```
S. Datta, M. Kundu, R.D. Choudhury, Sriramalakshmi P. and Sreedevi VT, “IoT Book Bot”, 
IEEE India Council International Subsections Conference (INDISCON). Bhubaneswar July, 2022. [Accepted]
```

### Steps to run livestream with Code Scanner
1) Start livestream
2) Go to the folder of live_Stream_qr_merged
3) Open command prompt in above location
4) Type this exactly in cmd - *python server.py*
5) Now go back to livestream webpage and click on QR / BARCODE Scanner
6) Click on the followup button
7) Scan QR or BARCODE and see the result on the webpage itself. 

### Steps to run QR code & Barcode scanner and insert the data in database:

1) Do everything according the steps mentioned above for running livestream with code scanner
2) Make sure that you have MongoDB compass configured in your computer. If you don't have compass then you have to change the mongo URI with the mongo atlas one which you can create by going to their website and following their steps.
3) Then scan the Student unique QR code and Book's Barcode seperately.
4) After scan each you one of then you will be shown a scanned value for your verification. After that just click the back button of your browser.
5) If you aren't satisfied with the shown value then you can scan it again
6) After scanning both of then, you can submit your scanned values to the database. Remember you can only submit when you have scanned both the values.
7) If you see *submitted successfully*, then you can click the back button of the browser and scan more books by repeating the same process or you can again click the the back button to navigate yourself to the home page.

## Hardware Setup - 

<img src="https://github.com/souvik0306/Book-Bot/blob/master/Media/Image (2).jpeg" width="550" height="350">
<img src="https://github.com/souvik0306/Book-Bot/blob/master/Media/Image (3).jpeg" width="550" height="350">
<!-- <img src="https://github.com/souvik0306/Book-Bot/blob/master/Media/Image (1).jpeg" width="550" height="350"> -->
<!-- <img src="https://github.com/souvik0306/Book-Bot/blob/master/Photos/d.jpeg" width="550" height="350">
 -->
 <image src="https://github.com/souvik0306/Book-Bot/blob/master/Media/Test_Run_1.gif" width="550" height="350">

  <image src="https://github.com/souvik0306/Book-Bot/blob/master/Media/Video_2.gif" width="550" height="350">

### *References* - 
1. Saral Tayal's Self-Drive Repository - [GitHub](https://github.com/SaralTayal123/SelfDrive)
2. AiPhile's Speed & Distance Estimation - [YouTube](https://www.youtube.com/watch?v=DIxcLghsQ4Q&ab_channel=AiPhile)
3. Eben Kouao's Live Stream Repository - [GitHub](https://github.com/EbenKouao/pi-camera-stream-flask)
4. Murtaza's Workshop - [YouTube](https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A)

